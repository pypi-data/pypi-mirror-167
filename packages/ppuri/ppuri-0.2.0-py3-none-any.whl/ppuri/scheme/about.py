"""About scheme RFC6694

https://www.rfc-editor.org/rfc/rfc6694.html
"""

import pyparsing as pp
from ppuri.component.query import Query
from ppuri.component.fragment import Fragment

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

tokens = pp.Literal("blank")

About = pp.Combine(
    pp.CaselessLiteral("about").set_results_name("scheme")
    + colon
    + tokens
    + pp.Optional(Query)
    + pp.Optional(Fragment)
)
