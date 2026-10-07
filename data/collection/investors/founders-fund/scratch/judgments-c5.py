"""Fixes after the first in-flight verify."""
from jl import *
C("sword-health", flags=["cite_pending"])
for s in ("lava", "navia", "top-fans"):
    C(s, seed_to_a_graduation="undetermined")
write("c5-fixes")
