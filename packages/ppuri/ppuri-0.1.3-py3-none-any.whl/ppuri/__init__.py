"""Copyright 2022 Simon Kenendy

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import pyparsing as pp

__version__ = "0.1.3"

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
