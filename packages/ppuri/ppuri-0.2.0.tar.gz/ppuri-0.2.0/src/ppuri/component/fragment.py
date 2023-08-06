import pyparsing as pp
from ppuri import fragment_characters

hash = pp.Literal("#").suppress()
Fragment = pp.And([hash, pp.Word(fragment_characters).set_results_name("fragment")])


def parse(text: str) -> dict[str, str]:
    res = Fragment.parse_string(text)
    return res.as_dict()["fragment"]  # type: ignore
