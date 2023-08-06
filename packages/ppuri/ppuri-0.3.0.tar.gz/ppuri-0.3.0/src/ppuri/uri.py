from typing import Any

from pyparsing import ParseException

from ppuri.exception import ParseError
from ppuri.scheme.aaa import AAA
from ppuri.scheme.coap import COAP
from ppuri.scheme.crid import Crid
from ppuri.scheme.data import Data
from ppuri.scheme.file import File
from ppuri.scheme.http import Http
from ppuri.scheme.mailto import MailTo
from ppuri.scheme.url import Url
from ppuri.scheme.urn import Urn

Uri = Http ^ MailTo ^ File ^ AAA ^ COAP ^ Crid ^ Urn ^ Data | Url


def parse(text: str) -> dict[str, Any]:
    try:
        parse_result = Uri.parse_string(text, parse_all=True)
        parse_result = parse_result.as_dict()  # type: ignore
        parse_result["uri"] = text
        return parse_result  # type: ignore
    except ParseException as exc:
        raise ParseError(f"{text} is not a valid URI") from exc


def scan(text: str) -> list[dict[str, str]]:
    uris: list[dict[str, str]] = []

    for tokens, start, end in Uri.scan_string(text):
        scan_result: dict[str, str] = tokens.as_dict()  # type: ignore
        scan_result["uri"] = text[start:end]
        uris.append(scan_result)

    return uris
