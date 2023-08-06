import pyparsing as pp
from ppuri import fragment_characters

hash = pp.Literal("#").suppress()
Fragment = pp.And([hash, pp.Word(fragment_characters).set_results_name("fragment")])
