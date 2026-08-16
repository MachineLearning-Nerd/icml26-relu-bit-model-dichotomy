# Claim-to-evidence ledger

## Reading this ledger

The five live claims are defined by
<code>contract/live_claims.json</code>. The status
**TOY_FINITE_SLP_GADGET** means that a finite exact-rational local gadget
conformed to the named arithmetic identity; it is not a #P-hardness proof, an
ERM reduction, or a complexity-class result. **UNVERIFIED_NOT_STARTED** means
that no independent theorem-level evidence has been produced here.

## Claims and production paths

| Claim | Paper target | Evidence producer | Independent check or control | Status |
| --- | --- | --- | --- | --- |
| 1 | Theorem 1.1: polynomial-activation ERM_bit is #P-hard | <code>src/claim1_quadratic_slp_toy.py</code> replaces multiplication in four exact-rational SLP fixtures with the three-square quadratic gadget | 16 queried bits match direct Fraction arithmetic; omitting the -y^2 term disagrees on every fixture; <code>tests/test_claim1_quadratic_slp_toy.py</code> checks the identity and bit convention | TOY_FINITE_SLP_GADGET |
| 2 | Corollary 1.2: an NP algorithm would collapse the polynomial hierarchy | No producer has been implemented | No conditional complexity reduction or checker exists | UNVERIFIED_NOT_STARTED |
| 3 | Theorem 1.3: gradient-bit #P-hardness and sign not in BPP | No producer has been implemented | No gradient construction, bit audit, or sign experiment exists | UNVERIFIED_NOT_STARTED |
| 4 | Theorem 1.4: ReLU ERM_bit is NP-complete and exact backpropagation is polynomial | No producer has been implemented | No ReLU witness verifier or bit-complexity audit exists | UNVERIFIED_NOT_STARTED |
| 5 | Section 3: hardness reductions from straight-line programs | The toy uses the local multiplication identity only | The auxiliary-sample forcing ERM construction and end-to-end reduction are absent | UNVERIFIED_NOT_STARTED |

## Claim 1 evidence

The source identity is:

<code>xy = 1/2 * ((x + y)^2 - x^2 - y^2)</code>

Four exact-rational SLP fixtures are evaluated through a three-square-node
quadratic gadget. Each fixture has four queried low-order bits, for 16 exact
comparisons total. The expected and network rational values match for all rows.
The corrupted gadget omits the <code>-y^2</code> term and disagrees for all 16
rows.

The fixtures are:

| Instance | Expected/network value | Quadratic gadget nodes |
| --- | ---: | ---: |
| square_plus | 7 | 3 |
| signed_product | -7 | 3 |
| nested | 100 | 6 |
| rational | 1 | 3 |

The exact bit convention is the absolute numerator divided by the denominator
before selecting the j-th low-order bit. The retained outputs are:

- <code>outputs/claim1_quadratic_slp_toy/results.csv</code>
- <code>outputs/claim1_quadratic_slp_toy/summary.json</code>
- <code>outputs/claim1_quadratic_slp_toy/command.stdout</code>
- <code>outputs/claim1_quadratic_slp_toy/run.log</code>
- <code>outputs/claim1_quadratic_slp_toy/SHA256SUMS</code>

## Evidence boundary

This finite gadget test does not construct the paper's auxiliary-sample forcing
ERM instance and cannot establish #P-hardness, NP-completeness, a polynomial
hierarchy collapse, a BPP lower bound, or the universal SLP reduction. Claims
2–5 remain unverified until theorem-level clean-room protocols and decisive
controls are produced.
