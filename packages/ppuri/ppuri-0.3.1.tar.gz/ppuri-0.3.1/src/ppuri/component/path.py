import pyparsing as pp

from ppuri import path_characters, path_start
from ppuri.exception import ParseError

Path = pp.Combine(path_start + pp.Word(pp.alphanums, path_characters)).set_results_name(
    "path"
)


def parse(text: str) -> str:
    try:
        res = Path.parse_string(text, parse_all=True)
        path: str = res.as_dict()["path"]  # type: ignore
        return path
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid path") from exc
