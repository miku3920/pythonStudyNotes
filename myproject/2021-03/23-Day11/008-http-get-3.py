import urllib.request
url="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0002-001?Authorization=rdec-key-123-45678-011121314&format=XML"
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
