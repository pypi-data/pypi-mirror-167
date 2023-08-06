"""A generic URL"""

from typing import Any

import pyparsing as pp
from ppuri import (
    authority_start,
    scheme_characters_start,
    scheme_characters_next,
    colon,
)
from ppuri.component.authority import Authority
from ppuri.component.fragment import Fragment
from ppuri.component.path import Path
from ppuri.component.query import Query
from ppuri.exception import ParseError


scheme_name = pp.Word(scheme_characters_start, scheme_characters_next)
UrlScheme = pp.Combine(scheme_name + colon)


Url = (
    UrlScheme.set_results_name("scheme")
    + authority_start
    + Authority
    + pp.Optional(Path)
    + pp.Optional(Query)
    + pp.Optional(Fragment)
)


def parse(text: str) -> dict[str, Any]:
    try:
        parse_result = Url.parse_string(text)
        parse_result = parse_result.as_dict()  # type: ignore
        parse_result["uri"] = text.strip("\n")
        return parse_result  # type: ignore
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid URL") from exc


def scan(text: str) -> list[dict[str, str]]:
    uris: list[dict[str, str]] = []

    for tokens, start, end in Url.scan_string(text):
        scan_result: dict[str, str] = tokens.as_dict()  # type: ignore
        scan_result["uri"] = text[start:end].strip("\n")
        uris.append(scan_result)

    return uris
