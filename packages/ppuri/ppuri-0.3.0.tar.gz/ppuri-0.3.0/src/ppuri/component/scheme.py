import pyparsing as pp
from ppuri import colon

scheme_characters_start = pp.alphas
scheme_characters_next = pp.alphanums + "+.-"


scheme_name = pp.Word(scheme_characters_start, scheme_characters_next)
Scheme = pp.Combine(
    scheme_name + colon + ~pp.FollowedBy(pp.Word(pp.nums))
).set_results_name("scheme")


def parse(text: str) -> str:
    """Gets the scheme if present"""
    res = Scheme.parse_string(text)
    return res.as_dict()["scheme"]  # type: ignore
