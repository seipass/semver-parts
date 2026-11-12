from __future__ import annotations
def run(version):
 core=version.split("-",1)[0].split("+",1)[0]; parts=core.split(".")
 if len(parts)!=3 or not all(p.isdigit() for p in parts): raise ValueError("expected MAJOR.MINOR.PATCH")
 return tuple(map(int,parts))
