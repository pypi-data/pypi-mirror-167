import pyparsing as pp
from ppuri.exception import ParseError


segment = (
    pp.MatchFirst(
        [
            # 250 - 255
            pp.Combine(pp.Literal("25") + pp.Word("012345", max=1)),
            # 200 - 249
            pp.Combine(
                pp.Literal("2")
                + pp.Optional(pp.Word("01234", max=1))
                + pp.Word(pp.nums, max=1)
            ),
            # 10 - 199
            pp.Combine(pp.Optional(pp.Literal("1")) + pp.Word(pp.nums, max=2)),
            # 0 - 9
            pp.Word(pp.nums, max=1),
        ]
    )
    + ~pp.FollowedBy(pp.Word(pp.nums))
)

dot = pp.Literal(".")

IPv4Address = pp.Combine(segment + (dot + segment) * 3).set_results_name("address")


def parse(text: str) -> str:
    """Parse an IPv4 address

    Returns:
        The IP address passed in if a valid address.

    Raises:
        `ParseError` for an invalid IPv4 address
    """
    try:
        ip = IPv4Address.parse_string(text)
        return ip.as_dict()["address"]  # type: ignore
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid IPv4 address") from exc


def scan(text: str) -> list[str]:
    """Scan text for IPv4 addresses

    Returns:
        A list of IPv4 valid addresses
    """
    res = IPv4Address.scan_string(text)
    addresses: list[str] = []
    for result, _start, _end in res:
        addresses.append(result[0])  # type: ignore
    return addresses
