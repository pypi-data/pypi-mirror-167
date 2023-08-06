# ppURI

A [pyparsing](https://pyparsing-docs.readthedocs.io/en/latest/) based URI parser/scanner library.

Install using pip or your tool of choice e.g.

```
pip install ppuri
poetry add ppuri
```

## Usage

### Parsing

Either import `ppuri.uri` and use the `parse` function to match and parse against all URI schemes e.g.

```python
from ppuri import uri
info = uri.parse("https://www.example.com:443/a.path?q=aparam#afragment")
print(info)
```

prints

```json
{
  "authority": { "address": "www.example.com", "port": "443" },
  "fragment": "afragment",
  "parameters": [{ "name": "q", "value": "aparam" }],
  "path": "/a.path",
  "scheme": "https",
  "uri": "https://www.example.com:443/a.path?q=aparam#afragment"
}
```

Or import a specific scheme's parse function.

```python
from ppuri.scheme import http
info = http.parse()
```

and use that to parse

### Scanning

To scan text for URIs use the `scan` method

## Supported schemes

Currently supports the following schemes

- http(s)
- urn
- data
- file
- mailto
- about
- aaa
- coap
- crid

### Http(s)

`parse_string` returns a dictionary of the form

```json
{
  "scheme": "http or https",
  "authority": {
    "address": "hostname or ipv4 address or ipv6 address",
    "port": "port number",
    "username": "user name if provided",
    "password": "pasword if provided"
  },
  "path": "path if provided",
  "parameters": [
    // list of parameters if provided
    {
      "name": "parameter name",
      "value": "parameter value or None if not provided"
    }
  ],
  "fragment": "fragment if provided",
  "uri": "The full URI"
}
```

### Urn

`parse_string` returns a dictionary of the form

```json
{
  "scheme": "urn",
  "nid": "Namespace Identifier",
  "nss": "Namespace Specific String",
  "uri": "The full URI"
}
```

### MailTo

`parse_string` returns a dictionary of the form

```json
{
  "scheme": "mailto",
  "addresses": [
    "List of email addresses",
  ]
  "parameters": [
    "list of parameters if provided",
    {
        "name": "bcc",
        "value": "dave@example.com"
    }
  ],
  "uri": "The full URI"
}
```

### Data

`parse_string` returns a dictionary of the form

```json
{
  "scheme": "data",
  "type": "Mime type",
  "subtype": "Mime Subtype",
  "encoding": "base64 if specified",
  "data": "The actual data",
  "uri": "The full URI"
}
```

### File

`parse_string` returns a dictionary of the form

```json
{
  "scheme": "file",
  "path": "The /file/path",
  "uri": "The full URI"
}
```

## Package Status

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/sffjunkie/ppuri/ppuri-test) ![PyPI - Downloads](https://img.shields.io/pypi/dm/ppuri)
