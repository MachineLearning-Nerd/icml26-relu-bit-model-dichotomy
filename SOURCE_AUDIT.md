# Source and provenance audit

## Paper identity

- Title: **Why ReLU? A Bit-Model Dichotomy for Deep Network Training**
- Authors: Ilan Doron-Arad and Elchanan Mossel
- Stable source: [arXiv:2602.19017](https://arxiv.org/abs/2602.19017)
- HTML source: [arXiv HTML](https://arxiv.org/html/2602.19017)
- OpenReview: [nMS1YTjHMH](https://openreview.net/forum?id=nMS1YTjHMH)
- ICML submission: 15471

The challenge snapshot was retrieved at 2026-08-01T12:30:34Z. The pinned
source archive is retained under <code>evidence/source/</code>.

## Immutable source hashes

- <code>evidence/source/paper.pdf</code>:
  <code>5f8d8f7a9e905541f7724601c31ee7c0986f8b84ee4384e5a4d6255ecfb29496</code>
- <code>evidence/source/arxiv_source.tar</code>:
  <code>0884358e1014ea14cba64c83cdc57a40521d82a219dabdebc01b5af6a3b87f28</code>
- <code>evidence/source/SHA256SUMS</code>:
  <code>afde2971896c84dc5df369e21318fdf7793b9f076da3a30a15d58d548139da19</code>
- <code>evidence/source/source_inventory.txt</code>:
  <code>93dc51c0ca1483939d85990f96f3174fcb94a4c228bdbd0bc8d67c5964d2bad3</code>

The inventory contains arXiv TeX, bibliography, one illustrative PDF figure,
and metadata. It reports no author GitHub URL, executable code, dataset,
configuration, seed list, or release artifact.

## Source locations used by the toy

The source defines exact-rational bit-model ERM in <code>evidence/source/arxiv.tex</code>
and presents the polynomial-activation reduction in Sections 1 and 3. Claim 1's
local protocol uses the special quadratic identity
<code>xy = 1/2[(x+y)^2-x^2-y^2]</code>. It validates that identity in finite
SLP fixtures but does not claim to reproduce the source's auxiliary-sample
forcing construction.

## Repository identity

- Former name:
  <code>icml26-repro-nMS1YTjHMH-relu-bit-model-dichotomy</code>
- Current name:
  <code>icml26-relu-bit-model-dichotomy</code>
- Current URL:
  https://github.com/MachineLearning-Nerd/icml26-relu-bit-model-dichotomy

No author review or endorsement is inferred.
