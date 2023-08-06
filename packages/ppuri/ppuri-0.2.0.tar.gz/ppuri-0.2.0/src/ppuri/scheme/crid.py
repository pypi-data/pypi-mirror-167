import pyparsing as pp

from ppuri.component.authority import Authority
from ppuri.component.path import Path
from ppuri import authority_start


colon = pp.Literal(":").suppress()

Crid = (
    pp.Literal(f"crid").set_results_name("scheme")
    + colon
    + authority_start
    + Authority
    + Path
)
