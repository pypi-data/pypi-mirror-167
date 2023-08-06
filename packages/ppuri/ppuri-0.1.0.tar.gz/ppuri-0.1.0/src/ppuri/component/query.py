import pyparsing as pp

question = pp.Literal("?").suppress()
equals = pp.Literal("=").suppress()
ampersand = pp.Literal("&").suppress()


def query_param_default_value(toks: pp.ParseResults):
    tok_dict: dict[str, str | None] = toks.as_dict()  # type: ignore
    if "value" not in tok_dict:
        tok_dict["value"] = None
        res = pp.ParseResults.from_dict(tok_dict)  # type: ignore
        return res


value_chars = "".join(set(pp.printables) - set("=&/#")) + " "

name = pp.Word(pp.alphas, pp.alphanums).set_results_name("name")
value = pp.Optional(equals + pp.Word(value_chars).set_results_name("value"))
value.set_parse_action(query_param_default_value)  # type: ignore

param = pp.Group(name + value)

QueryParams = pp.ZeroOrMore(pp.Optional(ampersand) + param).set_results_name(
    "parameters"
)
Query = question + QueryParams
