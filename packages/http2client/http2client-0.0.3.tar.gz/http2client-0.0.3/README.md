# http2client
A simple HTTP/2 client for Cyber Security

Useage:
```python

body = b'0\r\n\r\nGET /404 HTTP/1.1\r\nx: x'

headers = [
    (':method', 'GET'),
    (':path', "/"),
    (':authority', "example.com"),
    (':scheme', 'https'),
    ('User-Agent', 'testet\r\nTransfer-Encoding: chunked'),
    ('content-length', str(len(body))),
]
```