import json
import click
import pyparsing as pp
import sys

from ppuri.component.scheme import Scheme
from ppuri.uri import Uri


DEFAULT_SCHEME = "https://"


@click.command()
@click.argument(
    "uri", default="https://www.example.com:443/long/path?q=where%20am%20i#here"
)
def parse(uri: str) -> None:
    uri = uri.strip("'\"")
    try:
        result = Scheme.parse_string(uri)
    except pp.ParseException as exc:
        uri = f"{DEFAULT_SCHEME}{uri}"

    colon_pos = uri.find(":")
    if colon_pos == -1:
        print(f"{uri} is not a valid URI")
        sys.exit(1)

    try:
        result = Uri.parse_string(uri, parse_all=True)
        print(json.dumps(result.as_dict()))  # type: ignore
    except pp.ParseException as exc:
        if exc.loc > colon_pos + 1:
            print(f"Unable to parse uri error at position {exc.loc}")
            print(uri)
            print(" " * exc.loc + "^")
        else:
            uri_scheme = Scheme.parse_string(uri)["scheme"]  # type: ignore
            print(f"Don't know how to parse scheme {uri_scheme}")
            sys.exit(1)


parse()
