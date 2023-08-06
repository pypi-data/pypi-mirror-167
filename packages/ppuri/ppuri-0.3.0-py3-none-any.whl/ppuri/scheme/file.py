import pyparsing as pp
from ppuri import authority_start, colon, path_start, path_characters

FilePath = pp.Combine(
    pp.Optional(path_start) + pp.Word(pp.alphanums, path_characters)
).set_results_name("path")

File = (
    pp.CaselessLiteral("file").set_results_name("scheme")
    + colon
    + authority_start
    + FilePath
)
