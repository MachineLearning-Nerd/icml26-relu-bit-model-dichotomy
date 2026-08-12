# Why ReLU? A Bit-Model Dichotomy for Deep Network Training

Independent reproduction workspace for:

> Ilan Doron-Arad and Elchanan Mossel, “Why ReLU? A Bit-Model Dichotomy for Deep Network Training.”

Paper: [arXiv:2602.19017](https://arxiv.org/abs/2602.19017) · [HTML paper](https://arxiv.org/html/2602.19017) · [OpenReview submission nMS1YTjHMH](https://openreview.net/forum?id=nMS1YTjHMH) · ICML 2026 submission 15471.

This is an independent audit, not an author-maintained implementation. The
current repository contains one finite exact-rational SLP-to-quadratic-network
toy. It does not yet construct the paper’s auxiliary-sample ERM reduction or
verify the paper’s complexity theorems.

## Current status

| Claim | Paper target | Repository evidence | Verdict |
| --- | --- | --- | --- |
| 1 | Theorem 1.1: `ERM_bit` for deep non-linear polynomial activations of degree at least 2 is `#P`-hard | Four exact-rational SLP fixtures and 16 queried-bit checks match; a malformed multiplication gadget fails all fixtures | **TOY ONLY** |
| 2 | Corollary 1.2: an NP algorithm for the polynomial-activation problem would collapse the polynomial hierarchy to level two | No complexity reduction or conditional argument independently reproduced | **UNVERIFIED** |
| 3 | Theorem 1.3: a gradient bit is `#P`-hard and gradient sign is not in BPP under the stated assumptions | No gradient construction or sign experiment | **UNVERIFIED** |
| 4 | Theorem 1.4: ReLU/piecewise-linear `ERM_bit` is NP-complete and exact backpropagation is polynomial-time | No ReLU witness verifier or bit-complexity audit | **UNVERIFIED** |
| 5 | The polynomial-activation hardness is obtained through straight-line-program reductions | The toy exercises the quadratic multiplication identity only; the full reduction is not implemented | **UNVERIFIED** |

The narrow Claim 1 fixture uses the source identity for the quadratic activation
`sigma(z)=z^2`:

```text
xy = 1/2 * ((x + y)^2 - x^2 - y^2)
```

Four small straight-line programs are evaluated with exact `Fraction` arithmetic.
All 16 queried low-order bits match direct arithmetic, while omitting the `-y^2`
term makes every fixture disagree. This demonstrates local gadget conformance,
not `#P`-hardness, an ERM instance, or a universal theorem.

## How the current claim evidence is produced

| Claim | Evidence path | What is and is not established |
| --- | --- | --- |
| 1 | `contract/live_claims.json` defines the live wording; `CLAIM_1_PROTOCOL.md` records the source contract; `src/claim1_quadratic_slp_toy.py` evaluates exact rational SLPs; `outputs/claim1_quadratic_slp_toy/{results.csv,summary.json,run.log,SHA256SUMS}` stores the result | Four fixtures × four queried bits pass and the corrupted gadget fails. The auxiliary-sample forcing construction and full ERM reduction are absent. |
| 2 | Planned conditional-complexity audit from Theorem 1.1 to Corollary 1.2 | No evidence has been produced. |
| 3 | Planned exact gradient-bit/sign reduction audit | No evidence has been produced. |
| 4 | Planned bit-bounded ReLU witness and backpropagation audit | No evidence has been produced. |
| 5 | Planned end-to-end SLP-to-ERM reduction audit | No evidence has been produced. |

The pinned paper source is under `evidence/source/`. Its inventory reports no
author executable, dataset, seed list, or release artifact, so future work must
remain clean-room and record every construction explicitly.

## Reproduce

```bash
python3 -m pytest -q
(cd evidence/source && sha256sum -c SHA256SUMS)
python3 src/claim1_quadratic_slp_toy.py --out outputs/claim1_quadratic_slp_toy
(cd outputs/claim1_quadratic_slp_toy && sha256sum -c SHA256SUMS)
```

The compute policy is local CPU/local GPU only. No Hugging Face, Jobs, paid, or
remote GPU compute is used.

## Repository map

- `contract/` — immutable challenge metadata and five live claim texts.
- `evidence/source/` — pinned arXiv TeX/PDF source and checksums.
- `src/claim1_quadratic_slp_toy.py` — exact-rational clean-room gadget test.
- `outputs/claim1_quadratic_slp_toy/` — raw toy outputs and hashes.
- `logbook/claim-1.md` — detailed protocol, result, and scope limitation.
- `tests/` — contract and Claim 1 checks.

## Branch state

Only `main` exists. There are no hidden experiment branches or `orx/*` branches
to interpret. If later complexity claims are implemented, each branch should
state its theorem target, reduction construction, exact arithmetic assumptions,
checker/control, and whether it is a proof-oriented audit or a finite toy.

## Citation

```bibtex
@article{doronarad2026why,
  title         = {Why ReLU? A Bit-Model Dichotomy for Deep Network Training},
  author        = {Doron-Arad, Ilan and Mossel, Elchanan},
  journal       = {arXiv preprint arXiv:2602.19017},
  year          = {2026},
  eprint        = {2602.19017},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  doi           = {10.48550/arXiv.2602.19017}
}
```

## Thank you

Thank you to Ilan Doron-Arad and Elchanan Mossel for presenting the bit-model
complexity dichotomy clearly and for publishing the source record behind the
results. The explicit straight-line-program identity and theorem structure make
it possible to audit the local gadget independently while keeping the stronger
complexity claims clearly marked as work still to be reproduced.

This repository is intended as a transparent companion audit: it separates exact
finite arithmetic evidence from claims that require a full complexity reduction.

## Attribution

Approved repository commits are attributed to:

```text
MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>
```
