# Why ReLU? A Bit-Model Dichotomy for Deep Network Training — reproduction

Independent reproduction workspace for ICML 2026 submission 15471 (`nMS1YTjHMH`).

**Compute policy:** local CPU/local GPU only. No Hugging Face cpu-upgrade, Jobs, paid compute, or remote GPU services.

## Current evidence

Claim 1 has a source-pinned finite exact-rational clean-room SLP-to-quadratic-network gadget reproduction. Four independent small SLP fixtures and sixteen queried-bit checks match exactly; a malformed multiplication gadget fails all fixtures. This is explicitly a **toy** conformance check, not a #P-hardness proof or a complete ERM reduction.

## Reproduce contract checks

```bash
python3 -m pytest -q
(cd evidence/source && sha256sum -c SHA256SUMS)
python3 src/claim1_quadratic_slp_toy.py --out outputs/claim1_quadratic_slp_toy
(cd outputs/claim1_quadratic_slp_toy && sha256sum -c SHA256SUMS)
```
