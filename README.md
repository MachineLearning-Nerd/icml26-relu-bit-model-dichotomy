# Why ReLU? A Bit-Model Dichotomy for Deep Network Training — reproduction

Independent reproduction workspace for ICML 2026 submission 15471 (`nMS1YTjHMH`).

**Compute policy:** local CPU/local GPU only. No Hugging Face cpu-upgrade, Jobs, paid compute, or remote GPU services.

## Current evidence

Claim 1 has a source-pinned local feasibility/protocol audit only. It is **inconclusive**, not a verification. The next milestone is an independent constructive small-SLP/ERM reduction implementation with exact rational arithmetic and destructive controls.

## Reproduce contract checks

```bash
python3 -m pytest -q
sha256sum -c evidence/source/SHA256SUMS
```
