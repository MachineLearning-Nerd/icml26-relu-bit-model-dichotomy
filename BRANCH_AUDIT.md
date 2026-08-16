# Branch and attribution audit

## Repository identity

- Current repository:
  <https://github.com/MachineLearning-Nerd/icml26-relu-bit-model-dichotomy>
- Former repository:
  <code>icml26-repro-nMS1YTjHMH-relu-bit-model-dichotomy</code>
- Default branch: <code>main</code>
- Expected remote branches: exactly one
- Former prefix: <code>orx/</code>; no former-prefixed branch exists

The pre-dossier main checkpoint was
<code>50e9755409231e1ddc714662b4bdd2181a148793</code>. A recovery bundle made
before dossier edits has SHA-256
<code>78824e2d46f910246a079938bd204f62fb3591499558cf65af2fcfe0f8e2b376</code>.
It contains the complete five-commit history.

## Branch contract

Only <code>main</code> is published. There are no experiment-lineage branches
to rename or interpret. Future theorem or reduction work should use a
descriptive branch only after its exact assumptions, construction, checker,
control, and status are documented.

## Attribution contract

Every reachable commit must use:

<code>MachineLearning-Nerd &lt;37579156+MachineLearning-Nerd@users.noreply.github.com&gt;</code>

Commit messages must not contain a <code>Co-authored-by:</code> trailer. The
repository verifier checks author and committer identities across all reachable
refs.

## Verification contract

The publication verifier checks the canonical origin, main default branch,
one-branch topology, commit attribution, dossier hashes, source/toy-output
hashes, exact-rational Claim 1 values, and the corrupted-gadget control.

Run it with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~
