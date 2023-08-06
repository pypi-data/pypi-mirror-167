import pyparsing as pp
from ppuri.exception import ParseError


def set_default_password(toks: pp.ParseResults):
    if len(toks) == 0:
        toks["password"] = ""


username = pp.Word(pp.alphas, pp.alphanums).set_results_name("username")
password = pp.Word(pp.alphanums).set_results_name("password")
user_info_part = (
    username
    + pp.Literal(":").suppress()
    + pp.Optional(password).set_parse_action(set_default_password)  # type: ignore
)
UserInfo = user_info_part + pp.Optional(pp.Literal("@")).suppress()


def parse(text: str) -> dict[str, str]:
    try:
        res = UserInfo.parse_string(text, parse_all=True)
        return res.as_dict()  # type: ignore
    except pp.ParseException as exc:
        raise ParseError(f"{text} is not a valid authority") from exc
