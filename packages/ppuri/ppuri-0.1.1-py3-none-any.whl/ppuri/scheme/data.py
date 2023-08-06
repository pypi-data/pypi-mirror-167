import pyparsing as pp

from ppuri.component.media_type import MediaType
from ppuri import semicolon


colon = pp.Literal(":").suppress()

data_value = pp.Literal(",").suppress() + pp.Word(
    pp.alphas, pp.alphanums
).set_results_name("data")

Data = (
    pp.Literal(f"data").set_results_name("scheme")
    + colon
    + pp.Optional(MediaType)
    + pp.Optional(semicolon + pp.Literal("base64").set_results_name("encoding"))
    + data_value
)
