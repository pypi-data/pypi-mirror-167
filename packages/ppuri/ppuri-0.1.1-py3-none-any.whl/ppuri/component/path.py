import pyparsing as pp

from ppuri import path_characters, path_start

Path = pp.Combine(path_start + pp.Word(pp.alphanums, path_characters)).set_results_name(
    "path"
)
