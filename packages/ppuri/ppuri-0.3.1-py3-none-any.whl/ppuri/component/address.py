import pyparsing as pp

from ppuri.component.ipv4 import IPv4Address
from ppuri.component.ipv6 import IPv6Address
from ppuri.exception import ParseError

ipv4_address = IPv4Address

ipv6_address = pp.And(
    [pp.Literal("[").suppress(), IPv6Address, pp.Literal("]").suppress()]
)

period = pp.Literal(".")
hostname_part = pp.Word(pp.alphas, pp.alphanums + "-")
hostname_string = pp.Combine(hostname_part + pp.ZeroOrMore(period + hostname_part))


def check_hostname(toks: pp.ParseResults):
    d: dict[str, str] = toks.as_dict()  # type: ignore
    if isinstance(d["address"], list) and len(d["address"]) == 1:
        toks["address"] = d["address"][0]


Address = (
    pp.Or([ipv4_address, ipv6_address, hostname_string])
    .set_results_name("address")
    .set_parse_action(check_hostname)  # type: ignore
)


def parse(text: str) -> str:
    try:
        res = Address.parse_string(text, parse_all=True)
        hostname: str = res.as_list()[0]  # type: ignore
        return hostname
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid address") from exc
