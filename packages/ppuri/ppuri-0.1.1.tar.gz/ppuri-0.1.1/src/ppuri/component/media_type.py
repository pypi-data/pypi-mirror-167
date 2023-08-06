import pyparsing as pp

t_specials = '()<>@,;:\\<"/[]?='
ascii_chars = (chr(x) for x in range(33, 128))
token_chars = "".join(set(ascii_chars) - set(t_specials))

x_token = pp.CaselessLiteral("x-") + pp.Word(token_chars)

discrete_types = (
    pp.Literal("application")
    | pp.Literal("audio")
    | pp.Literal("image")
    | pp.Literal("text")
    | pp.Literal("video")
)
composite_types = pp.Literal("message") | pp.Literal("multipart")

iana_types = pp.Literal("font") | pp.Literal("example") | pp.Literal("model")
types = pp.Combine(discrete_types | composite_types | iana_types | x_token)

iana_subtypes = (
    # RFC 4026
    pp.Literal("octet-stream")
)
general_subtype = pp.Word(pp.alphanums, token_chars)

subtypes = pp.Combine(iana_subtypes | x_token | general_subtype)

MediaType = pp.Combine(
    types.set_results_name("type")
    + pp.Literal("/")
    + subtypes.set_results_name("subtype")
)
