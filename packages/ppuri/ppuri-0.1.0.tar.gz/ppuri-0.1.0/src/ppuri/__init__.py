import pyparsing as pp

__version__ = "0.1.0"

# TODO: Use these variables
general_delimeter_set = set(":/?#[]@")
sub_delimeter_set = set("!$&'()*+,;=")

reserved_set = general_delimeter_set | sub_delimeter_set
reserved_characters = "".join(reserved_set)

unreserved_set = set(pp.alphanums + "-._~")
unreserved_characters = "".join(unreserved_set)

pchar_set = unreserved_set | sub_delimeter_set | set("%" + pp.alphanums)

path_set = set(pp.alphanums + "/@.:%_-=")
path_characters = "".join(path_set)

query_set = path_set | set("/?")
query_characters = "".join(query_set)

fragment_characters = query_characters

colon = pp.Literal(":").suppress()
dot = pp.Literal(".").suppress()
semicolon = pp.Literal(";").suppress()
slash = pp.Literal("/").suppress()
authority_start = pp.Literal("//").suppress()
path_start = pp.Literal("/")
