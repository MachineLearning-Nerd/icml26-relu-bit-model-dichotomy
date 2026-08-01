# Claim 1 protocol — ERM_bit #P-hardness for non-linear polynomial activations

**Exact live claim:** Theorem 1.1 proves that deciding ERM_bit for deep networks with any non-linear polynomial activation of degree at least 2 is #P-hard (Section 1.1, Theorem 1.1).

## Pinned-source audit

The source defines exact rational bit-model ERM in `evidence/source/arxiv.tex` and states its polynomial-activation reduction in Sections 1 and 3. No author repository, executable, input fixtures, or generated reduction instances appear in the pinned source archive (only `arxiv.tex`, bibliography, and one PDF figure). This audit cannot establish #P-hardness and is therefore inconclusive.

## Next local protocol

Implement a clean-room exact-rational small straight-line-program-to-polynomial-network construction, validate loss/value identities against independently evaluated SLP outputs over a bounded enumerated fixture, and add a malformed-gate/destructive control. This will be labeled toy unless it independently validates the universal reduction proof.
