import pyparsing as pp

colon = pp.Literal(":").suppress()
nid = pp.Word(pp.alphanums, pp.alphanums + "-", min=1, max=31).set_results_name("nid")

reserved = "%/?#"
other = "()+,-.:=@;$_!*'"
trans = pp.alphanums + other + reserved

nss = pp.Word(trans).set_results_name("nss")

Urn = pp.CaselessLiteral("urn").set_results_name("scheme") + colon + nid + colon + nss
