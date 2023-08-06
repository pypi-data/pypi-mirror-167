"""A generic URL"""

import pyparsing as pp
from ppuri import authority_start
from ppuri.component.authority import Authority
from ppuri.component.fragment import Fragment
from ppuri.component.path import Path
from ppuri.component.scheme import Scheme
from ppuri.component.query import Query

Url = (
    Scheme.set_results_name("scheme")
    + authority_start
    + Authority
    + pp.Optional(Path)
    + pp.Optional(Query)
    + pp.Optional(Fragment)
)
