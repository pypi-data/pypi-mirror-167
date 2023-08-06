import pyparsing as pp
from ppuri import colon

scheme_characters_start = pp.alphas
scheme_characters_next = pp.alphanums + "+.-"

Scheme = (
    pp.WordStart()
    + pp.Word(scheme_characters_start, scheme_characters_next).set_results_name(
        "scheme"
    )
    + colon
    + ~pp.FollowedBy(pp.Word(pp.nums))
)


def parse_scheme(text: str, default: str = "") -> str:
    """Gets the scheme if present"""
    try:
        res = Scheme.parse_string(text)
        return res.as_dict()["scheme"]  # type: ignore
    except pp.ParseException:
        return default


def scan_scheme(text: str) -> list[str]:
    """Scan text for URI schemes"""
    results = Scheme.scan_string(text)
    schemes: list[str] = []

    for result in results:
        s: str = result[0].as_dict()["scheme"]  # type: ignore
        schemes.append(s)

    return schemes
