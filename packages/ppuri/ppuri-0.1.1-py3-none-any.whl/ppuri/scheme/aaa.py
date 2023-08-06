"""Diameter Base Protocol RFC6733

https://www.rfc-editor.org/rfc/rfc6733.html
"""

import pyparsing as pp
from ppuri import authority_start
from ppuri.component.authority import Authority

colon = pp.Literal(":").suppress()
semicolon = pp.Literal(";").suppress()

transports = pp.Literal("tcp") | pp.Literal("udp") | pp.Literal("utcp")
protocols = pp.Literal("diameter") | pp.Literal("radius") | pp.Literal("tacacs+")

transport = pp.Combine(
    semicolon + pp.Literal("transport=") + transports.set_results_name("transport")
)
protocol = pp.Combine(
    semicolon + pp.Literal("protocol=") + protocols.set_results_name("protocol")
)


def AAAf(suffix: str = "") -> pp.ParserElement:
    return pp.Combine(
        pp.CaselessLiteral(f"aaa{suffix}").set_results_name("scheme")
        + colon
        + authority_start
        + Authority
        + pp.Optional(transport)
        + pp.Optional(protocol)
    )


AAA = AAAf() ^ AAAf("s")
