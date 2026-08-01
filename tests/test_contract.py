import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_contract():
 d=json.loads((ROOT/'contract/live_claims.json').read_text())
 assert d['openreview_id']=='nMS1YTjHMH'
 assert d['claim_count']==5 and d['max_points']==10 and len(d['claims'])==5
def test_source_manifest():
 for line in (ROOT/'evidence/source/SHA256SUMS').read_text().splitlines():
  h,name=line.split(maxsplit=1)
  assert hashlib.sha256((ROOT/'evidence/source'/name.strip()).read_bytes()).hexdigest()==h
