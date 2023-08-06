from ppuri.scheme.aaa import AAA
from ppuri.scheme.coap import COAP
from ppuri.scheme.crid import Crid
from ppuri.scheme.data import Data
from ppuri.scheme.file import File
from ppuri.scheme.http import Http
from ppuri.scheme.mailto import MailTo
from ppuri.scheme.urn import Urn

Uri = Http ^ MailTo ^ File ^ AAA ^ COAP ^ Crid ^ Urn ^ Data
