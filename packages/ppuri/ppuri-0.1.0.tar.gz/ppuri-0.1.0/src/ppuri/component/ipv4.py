import pyparsing as pp


ipv4_segment = (
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

IPv4Address = pp.Combine(ipv4_segment + (dot + ipv4_segment) * 3).set_results_name(
    "address"
)


def ipv4_parse(text: str) -> str:
    """Parse an IPv4 address

    Returns:
        The IP address passed in if a valid address.

    Raises:
        `pyparsing.ParseException` for an invalid IPv4 address"""
    ip = IPv4Address.parse_string(text)
    return ip.as_list()[0]  # type: ignore


def ipv4_search(text: str) -> list[str]:
    """Search text for IPv4 addresses

    Returns:
        A list of IPv4 valid addresses"""
    res = IPv4Address.search_string(text)
    if res:
        return [i[0] for i in res.as_list()]  # type: ignore
    else:
        return []
