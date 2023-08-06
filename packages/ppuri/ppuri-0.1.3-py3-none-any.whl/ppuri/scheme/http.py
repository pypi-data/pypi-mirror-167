import pyparsing as pp
from ppuri import colon, authority_start
from ppuri.component.authority import Authority
from ppuri.component.fragment import Fragment
from ppuri.component.path import Path
from ppuri.component.query import Query

Http = (
    (pp.CaselessLiteral("https") | pp.CaselessLiteral("http")).set_results_name(
        "scheme"
    )
    + colon
    + authority_start
    + Authority
    + pp.Optional(Path)
    + pp.Optional(Query)
    + pp.Optional(Fragment)
)
