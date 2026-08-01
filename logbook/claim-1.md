# Claim 1 — ERM_bit hardness

**Status: toy.** Exact live wording: “Theorem 1.1 proves that deciding ERM_bit for deep networks with any non-linear polynomial activation of degree at least 2 is #P-hard.”

## Local clean-room finite conformance evidence

Using the source's special quadratic activation identity, `xy = 1/2[(x+y)^2-x^2-y^2]`, `src/claim1_quadratic_slp_toy.py` evaluates four exact-rational small SLP fixtures through a three-square-node multiplication gadget. All 16 independently queried BitSLP bits agree with direct `Fraction` arithmetic. The destructive control omits the `-y^2` gadget term and disagrees on every fixture. Raw results/configuration and checksums are in `outputs/claim1_quadratic_slp_toy/`; run `python3 src/claim1_quadratic_slp_toy.py --out outputs/claim1_quadratic_slp_toy` then `(cd outputs/claim1_quadratic_slp_toy && sha256sum -c SHA256SUMS)`.

**Scope limitation:** this finite clean-room gadget test does not construct the source's auxiliary-sample forcing ERM instance and cannot prove the universal #P-hardness theorem. It is labeled toy, not verified/falsified.
