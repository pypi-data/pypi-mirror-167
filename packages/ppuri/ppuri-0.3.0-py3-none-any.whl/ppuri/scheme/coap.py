import pyparsing as pp

from ppuri.component.authority import Authority
from ppuri.component.path import Path
from ppuri import colon, authority_start


def _COAPf(suffix: str = "") -> pp.ParserElement:
    return (
        pp.Literal(f"coap{suffix}").set_results_name("scheme")
        + colon
        + authority_start
        + Authority
        + Path
    )


COAP = (
    _COAPf()
    ^ _COAPf("+tcp")
    ^ _COAPf("+ws")
    ^ _COAPf("s")
    ^ _COAPf("s+tcp")
    ^ _COAPf("s+ws")
)
