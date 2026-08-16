#!/usr/bin/env python3
"""Verify the published ReLU bit-model dossier without theorem-scale work."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_ORIGIN = (
    "https://github.com/MachineLearning-Nerd/"
    "icml26-relu-bit-model-dichotomy"
)
EXPECTED_BRANCHES = {"main"}
EXPECTED_IDENTITY = (
    "MachineLearning-Nerd",
    "37579156+MachineLearning-Nerd@users.noreply.github.com",
)
ERRORS: list[str] = []


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        ERRORS.append(f"{relative}: cannot parse JSON: {exc}")
        return {}


def verify_hash_manifest(relative: str, base: Path) -> None:
    for line in (ROOT / relative).read_text().splitlines():
        fields = line.split()
        require(len(fields) == 2, f"malformed hash row in {relative}: {line}")
        if len(fields) == 2:
            digest, name = fields
            path = base / name
            require(path.is_file(), f"missing hash input: {path}")
            if path.is_file():
                require(sha256(path) == digest, f"hash mismatch: {path}")


def main() -> int:
    origin_result = run("git", "remote", "get-url", "origin")
    origin = origin_result.stdout.strip().removesuffix(".git").rstrip("/")
    require(origin == EXPECTED_ORIGIN, f"unexpected origin: {origin!r}")

    symref = run("git", "ls-remote", "--symref", "origin", "HEAD")
    require(
        "ref: refs/heads/main\tHEAD" in symref.stdout,
        "origin HEAD does not point to main",
    )

    heads = run("git", "ls-remote", "--heads", "origin")
    remote_branches = set()
    for line in heads.stdout.splitlines():
        fields = line.split("\t", 1)
        if len(fields) == 2 and fields[1].startswith("refs/heads/"):
            remote_branches.add(fields[1].removeprefix("refs/heads/"))
    require(remote_branches == EXPECTED_BRANCHES, f"remote branches: {sorted(remote_branches)}")
    require(
        not any(branch.startswith("orx/") for branch in remote_branches),
        "old orx branch remains on the remote",
    )

    local_heads = run(
        "git",
        "for-each-ref",
        "--format=%(refname:strip=2)",
        "refs/heads",
    )
    local_branches = set(filter(None, local_heads.stdout.splitlines()))
    require(
        local_branches <= EXPECTED_BRANCHES,
        f"unexpected local branches: {sorted(local_branches - EXPECTED_BRANCHES)}",
    )
    old_refs = run("git", "for-each-ref", "refs/original")
    require(not old_refs.stdout.strip(), "refs/original exists")

    count_result = run("git", "rev-list", "--count", "--all")
    try:
        commit_count = int(count_result.stdout.strip())
    except ValueError:
        commit_count = 0
    require(commit_count >= 5, f"reachable commit count is only {commit_count}")

    identity_output = run(
        "git",
        "log",
        "--all",
        "--format=%an%x09%ae%x09%cn%x09%ce",
    ).stdout
    for line in filter(None, identity_output.splitlines()):
        fields = line.split("\t")
        require(len(fields) == 4, f"malformed identity row: {line}")
        if len(fields) == 4:
            author_name, author_email, committer_name, committer_email = fields
            require(
                (author_name, author_email) == EXPECTED_IDENTITY,
                f"non-canonical author identity: {line}",
            )
            require(
                (committer_name, committer_email) == EXPECTED_IDENTITY,
                f"non-canonical committer identity: {line}",
            )
    messages = run("git", "log", "--all", "--format=%B").stdout
    require(
        "Co-authored-by:" not in messages and "Co-Authored-By:" not in messages,
        "co-author trailer found in commit messages",
    )

    required_files = [
        "README.md",
        "STATUS.md",
        "BRANCH_AUDIT.md",
        "AUTHOR_THANK_YOU.md",
        "CITATION.cff",
        "CLAIM_EVIDENCE.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "SOURCE_AUDIT.md",
        "claims.json",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
        "contract/live_claims.json",
        "evidence/source/SHA256SUMS",
        "evidence/source/source_inventory.txt",
        "outputs/claim1_quadratic_slp_toy/SHA256SUMS",
        "outputs/claim1_quadratic_slp_toy/summary.json",
        "outputs/claim1_quadratic_slp_toy/results.csv",
        "outputs/claim1_quadratic_slp_toy/run.log",
        "outputs/claim1_quadratic_slp_toy/command.stdout",
    ]
    for relative in required_files:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    manifest = load_json("EVIDENCE_MANIFEST.json")
    require(manifest.get("branch_contract") == {
        "default": "main",
        "total": 1,
        "descriptive": 0,
        "old_prefix_absent": "orx/",
    }, "branch contract mismatch")
    for relative, expected in manifest.get("aggregates", {}).items():
        path = ROOT / relative
        require(path.is_file(), f"missing aggregate input: {relative}")
        if path.is_file():
            require(sha256(path) == expected, f"aggregate hash mismatch: {relative}")
    for row in manifest.get("files", []):
        relative = row.get("path", "")
        path = ROOT / relative
        expected = row.get("sha256")
        require(path.is_file(), f"manifest file missing: {relative}")
        require(expected not in (None, "", "PENDING"), f"manifest hash pending: {relative}")
        if path.is_file() and expected not in (None, "", "PENDING"):
            require(sha256(path) == expected, f"manifest hash mismatch: {relative}")

    claims = load_json("claims.json")
    expected_statuses = {
        1: "TOY_FINITE_SLP_GADGET",
        2: "UNVERIFIED_NOT_STARTED",
        3: "UNVERIFIED_NOT_STARTED",
        4: "UNVERIFIED_NOT_STARTED",
        5: "UNVERIFIED_NOT_STARTED",
    }
    actual_claims = {item.get("id"): item for item in claims.get("claims", [])}
    require(set(actual_claims) == set(expected_statuses), "claims.json IDs mismatch")
    for claim_id, status in expected_statuses.items():
        require(
            actual_claims.get(claim_id, {}).get("status") == status,
            f"claims.json status mismatch for Claim {claim_id}",
        )

    verify_hash_manifest("evidence/source/SHA256SUMS", ROOT / "evidence/source")
    verify_hash_manifest(
        "outputs/claim1_quadratic_slp_toy/SHA256SUMS",
        ROOT / "outputs/claim1_quadratic_slp_toy",
    )

    summary = load_json("outputs/claim1_quadratic_slp_toy/summary.json")
    require(summary.get("instances") == 4, "Claim 1 instance count mismatch")
    require(summary.get("bit_queries") == 16, "Claim 1 bit count mismatch")
    require(summary.get("all_exact") is True, "Claim 1 exact result failed")
    require(
        summary.get("negative_control_detected") is True,
        "Claim 1 negative control missing",
    )

    rows = []
    with (ROOT / "outputs/claim1_quadratic_slp_toy/results.csv").open(newline="") as stream:
        import csv

        rows = list(csv.DictReader(stream))
    require(len(rows) == 16, "Claim 1 CSV row count mismatch")
    require(
        all(
            row["expected"] == row["network"]
            and row["expected_bit"] == row["network_bit"]
            and row["broken_matches"] == "False"
            for row in rows
        ),
        "Claim 1 CSV evidence mismatch",
    )

    try:
        sys.path.insert(0, str(ROOT))
        from src.claim1_quadratic_slp_toy import (
            INSTANCES,
            bit_lsb,
            eval_slp,
        )

        require(len(INSTANCES) == 4, "recomputed fixture count mismatch")
        for _, program, expected in INSTANCES:
            actual, _ = eval_slp(program)
            broken, _ = eval_slp(program, corrupt=True)
            require(actual == expected, "recomputed exact rational value mismatch")
            require(broken != expected, "recomputed corrupted control did not fail")
            require(
                [bit_lsb(actual, j) for j in range(4)]
                == [bit_lsb(expected, j) for j in range(4)],
                "recomputed bit mismatch",
            )
    except Exception as exc:
        ERRORS.append(f"Claim 1 recomputation failed: {exc}")

    if ERRORS:
        print("FINAL_AUDIT=FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(
        f"FINAL_AUDIT=VERIFIED branches={len(remote_branches)} "
        f"commits={commit_count} claim1=toy claims2-5=unverified"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
