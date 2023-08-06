import pyparsing as pp


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


def userinfo_parse(text: str) -> dict[str, str]:
    res = user_info_part.parse_string(text)
    return res.as_dict()  # type: ignore


def userinfo_scan(text: str) -> list[dict[str, str]]:
    userinfos: list[dict[str, str]] = []

    for tokens, _start, _end in UserInfo.scan_string(text):
        parse_result: dict[str, str] = tokens.as_dict()  # type: ignore
        userinfos.append(parse_result)

    return userinfos
