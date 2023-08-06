import pyparsing as pp

from ppuri.component.ipv4 import IPv4Address
from ppuri.component.ipv6 import IPv6Address
from ppuri.exception import ParseError

ipv4_hostname = IPv4Address

ipv6_hostname = pp.And(
    [pp.Literal("[").suppress(), IPv6Address, pp.Literal("]").suppress()]
)

period = pp.Literal(".")
hostname_part = pp.Word(pp.alphas, pp.alphanums + "-")
hostname_string = pp.Combine(hostname_part + pp.ZeroOrMore(period + hostname_part))


def check_hostname(toks: pp.ParseResults):
    d: dict[str, str] = toks.as_dict()  # type: ignore
    if isinstance(d["address"], list) and len(d["address"]) == 1:
        toks["address"] = d["address"][0]


Hostname = (
    pp.Or([ipv4_hostname, ipv6_hostname, hostname_string])
    .set_results_name("address")
    .set_parse_action(check_hostname)  # type: ignore
)


def hostname_parse(text: str) -> str:
    try:
        res = Hostname.parse_string(text, parse_all=True)
        hostname: str = res.as_list()[0]  # type: ignore
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid hostname") from exc
    return hostname


def hostname_scan(text: str) -> list[str]:
    """Scan text for URI schemes"""
    results = Hostname.scan_string(text)
    schemes: list[str] = []

    for result in results:
        s: str = result[0].as_dict()["address"]  # type: ignore
        schemes.append(s)

    return schemes
