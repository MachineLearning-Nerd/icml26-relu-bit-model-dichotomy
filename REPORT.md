# ReLU bit-model audit report

## Result

This repository has one **TOY_FINITE_SLP_GADGET** result and four
**UNVERIFIED_NOT_STARTED** claims.

Claim 1 exercises the source's quadratic multiplication identity with four
exact-rational straight-line-program fixtures. All 16 queried low-order bits
match direct arithmetic. A corrupted gadget that omits the negative square
disagrees on every fixture.

## Claim status

| Claim | Status | Evidence |
| --- | --- | --- |
| 1 | TOY_FINITE_SLP_GADGET | Four exact-rational fixtures, 16 queried bits, and a corrupted-gadget control |
| 2 | UNVERIFIED_NOT_STARTED | No polynomial-hierarchy conditional reduction |
| 3 | UNVERIFIED_NOT_STARTED | No gradient-bit or sign reduction |
| 4 | UNVERIFIED_NOT_STARTED | No ReLU witness or backpropagation bit audit |
| 5 | UNVERIFIED_NOT_STARTED | No end-to-end SLP-to-ERM reduction |

## What this does not claim

The toy does not reproduce the paper's #P-hardness, NP-completeness,
polynomial-hierarchy consequence, BPP sign lower bound, auxiliary-sample ERM
construction, or universal SLP reduction. No external judge score or author
endorsement is claimed.

The five-claim, ten-point contract remains untouched. Exact finite arithmetic
conformance is recorded as a scoped mechanism audit, not promoted to a
complexity-theorem verdict.
