import json
import click
import pyparsing as pp
import sys

from ppuri.component import scheme
from ppuri import uri as _uri


DEFAULT_SCHEME = "https://"


@click.command()
@click.argument(
    "uri", default="https://www.example.com:443/long/path?q=where%20am%20i#here"
)
def parse(uri: str) -> None:
    colon_pos = uri.find(":")
    if colon_pos == -1:
        print(f"{uri} is not a valid URI")
        sys.exit(1)

    try:
        result = _uri.parse(uri)
        print(json.dumps(result))  # type: ignore
    except pp.ParseException as exc:
        if exc.loc > colon_pos + 1:
            print(f"Unable to parse uri error at position {exc.loc}")
            print(uri)
            print(" " * exc.loc + "^")
        else:
            uri_scheme = scheme.parse(uri)
            print(f"Don't know how to parse scheme {uri_scheme}")
            sys.exit(1)


parse()
