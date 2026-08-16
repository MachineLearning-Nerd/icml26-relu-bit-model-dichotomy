# Environment and reproduction record

## Fixed local entrypoint

The committed Claim 1 command is:

~~~bash
python3 src/claim1_quadratic_slp_toy.py --out outputs/claim1_quadratic_slp_toy
(cd outputs/claim1_quadratic_slp_toy && sha256sum -c SHA256SUMS)
~~~

The retained artifact was generated with Python 3.14.5 on a Linux x86_64
machine. The implementation uses Python's standard-library
<code>fractions.Fraction</code>; no external model, dataset, or remote service
is used.

## What ran

| Workload | Scale | Result |
| --- | --- | --- |
| Exact quadratic SLP gadget | Four fixtures | 16/16 queried bits match direct rational arithmetic |
| Corrupted multiplication gadget | Four fixtures | 16/16 rows disagree, as intended |
| Source checksums | Pinned PDF and source archive | All entries in <code>evidence/source/SHA256SUMS</code> match |

The raw CSV, summary, stdout, log, and checksum manifest are committed under
<code>outputs/claim1_quadratic_slp_toy/</code>. This dossier does not rerun or
rewrite them.

The repository's broader reproduction command mentions pytest, but the dossier
verifier intentionally performs only the lightweight exact-arithmetic Claim 1
check and checksum validation. It never launches a theorem reduction, ERM
construction, or remote workload.

## Source and implementation pins

- Paper PDF SHA-256:
  <code>5f8d8f7a9e905541f7724601c31ee7c0986f8b84ee4384e5a4d6255ecfb29496</code>
- Paper source archive SHA-256:
  <code>0884358e1014ea14cba64c83cdc57a40521d82a219dabdebc01b5af6a3b87f28</code>
- Source inventory SHA-256:
  <code>93dc51c0ca1483939d85990f96f3174fcb94a4c228bdbd0bc8d67c5964d2bad3</code>

The pinned source inventory reports no author executable, dataset, seed list, or
release artifact. Future evidence must therefore be independently constructed
and must state any reduction or implementation substitution explicitly.
