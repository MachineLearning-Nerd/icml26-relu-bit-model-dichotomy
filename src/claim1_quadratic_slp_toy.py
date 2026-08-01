#!/usr/bin/env python3
"""Clean-room finite SLP-to-quadratic-network gadget audit.

Implements the pinned source identity for sigma(z)=z^2:
  xy = 1/2[(x+y)^2-x^2-y^2].
It evaluates small exact-rational SLPs by replacing multiplication gates with
that network gadget, then checks queried output bits.  This is finite toy
conformance evidence, not a #P-hardness proof or a constructed ERM instance.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, platform, sys
from fractions import Fraction
from pathlib import Path


def bit_lsb(q: Fraction, j: int) -> int:
    """Pinned BitSLP convention: j-th LSB of |numerator|/denominator."""
    return (abs(q.numerator) // (q.denominator * (2 ** j))) % 2


def quadratic_multiply(x: Fraction, y: Fraction, corrupt: bool = False) -> Fraction:
    # Lemma 3.1 source special case: lambda_0=1/2 for sigma(z)=z^2.
    value = ((x + y) ** 2 - x ** 2 - y ** 2) / 2
    return value if not corrupt else ((x + y) ** 2 - x ** 2) / 2


def eval_slp(program: list[dict], corrupt: bool = False) -> tuple[Fraction, int]:
    values: list[Fraction] = []
    gadget_nodes = 0
    for gate in program:
        if gate["op"] == "const":
            values.append(Fraction(gate["value"]))
        else:
            x, y = values[gate["left"]], values[gate["right"]]
            if gate["op"] == "+": values.append(x + y)
            elif gate["op"] == "-": values.append(x - y)
            elif gate["op"] == "*":
                values.append(quadratic_multiply(x, y, corrupt))
                gadget_nodes += 3 # three sigma nodes in Figure 1
            else: raise ValueError(gate["op"])
    return values[-1], gadget_nodes

# Each instance uses only earlier gate references and admits an independent
# expected exact result computed from the displayed arithmetic expression.
INSTANCES = [
    ("square_plus", [{"op":"const","value":"2"},{"op":"*","left":0,"right":0},{"op":"const","value":"3"},{"op":"+","left":1,"right":2}], Fraction(7)),
    ("signed_product", [{"op":"const","value":"-3"},{"op":"const","value":"5/2"},{"op":"*","left":0,"right":1},{"op":"const","value":"1/2"},{"op":"+","left":2,"right":3}], Fraction(-7)),
    ("nested", [{"op":"const","value":"2"},{"op":"const","value":"3"},{"op":"*","left":0,"right":1},{"op":"const","value":"4"},{"op":"+","left":2,"right":3},{"op":"*","left":4,"right":4}], Fraction(100)),
    ("rational", [{"op":"const","value":"3/2"},{"op":"const","value":"4/3"},{"op":"*","left":0,"right":1},{"op":"const","value":"1"},{"op":"-","left":2,"right":3}], Fraction(1)),
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--out", required=True); args=ap.parse_args()
    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    rows=[]
    for name, program, expected in INSTANCES:
        actual, nodes=eval_slp(program)
        broken,_=eval_slp(program, corrupt=True)
        for j in range(4):
            rows.append({"instance":name,"bit":j,"expected":"%s/%s"%(expected.numerator,expected.denominator),"network":"%s/%s"%(actual.numerator,actual.denominator),"expected_bit":bit_lsb(expected,j),"network_bit":bit_lsb(actual,j),"gadget_sigma_nodes":nodes,"broken_network":"%s/%s"%(broken.numerator,broken.denominator),"broken_matches":broken==expected})
    with (out/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    result={"scope":"finite exact-rational clean-room quadratic SLP gadget toy; not #P-hardness proof or full ERM reduction","instances":len(INSTANCES),"bit_queries":len(rows),"all_exact":all(r['expected']==r['network'] and r['expected_bit']==r['network_bit'] for r in rows),"negative_control_detected":any(not r['broken_matches'] for r in rows),"python":sys.version,"platform":platform.platform()}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+"\n")
    (out/'run.log').write_text("command: "+" ".join(sys.argv)+"\n"+json.dumps(result)+"\n")
    files=['results.csv','summary.json','run.log']
    (out/'SHA256SUMS').write_text(''.join(f'{sha256(out/f)}  {f}\n' for f in files))
if __name__=='__main__': main()
