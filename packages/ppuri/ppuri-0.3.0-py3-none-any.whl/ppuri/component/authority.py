"""URL authority

Optional(UserInfo) + Hostname + Optional(Port)
"""
from typing import Any

import pyparsing as pp
from ppuri.component.address import Address
from ppuri.component.userinfo import UserInfo
from ppuri.exception import ParseError


def check_port_number(tokens: pp.ParseResults) -> Any:
    try:
        port = int(tokens[0])  # type: ignore
        if port <= 0 or port > 65535:
            raise pp.ParseException("Invalid port number > 65535")
    except ValueError:
        raise pp.ParseException("Port is not a number")


port_part = pp.Word(pp.nums).set_parse_action(check_port_number).set_results_name("port")  # type: ignore
port = pp.Literal(":").suppress() + port_part

Authority = pp.Group(
    pp.Optional(UserInfo) + Address + pp.Optional(port)
).set_results_name("authority")


def parse(text: str) -> dict[str, Any]:
    try:
        res = Authority.parse_string(text, parse_all=True)
        authority: dict[str, Any] = res.as_dict()["authority"]  # type: ignore
        return authority
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid authority") from exc
