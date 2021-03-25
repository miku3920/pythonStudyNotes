import urllib.request as httplib
import xml.etree.ElementTree as ET
import ssl

tree = ET.parse('RealPrice.xml')
root = tree.getroot()

# context = ssl._create_unverified_context()
# url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=a9a97996-3a55-46c8-9076-e5ebdefad6dc&rid=2979c431-7a32-4067-9af2-e716cd825c4b"
# req = httplib.Request(url)
# res = httplib.urlopen(req, context=context)
# contents = res.read()
# root = ET.fromstring(contents)

namespaces = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'a': 'http://tempuri.org/',
}

items = root.findall('soap:Body/a:RPWeekDataResponse/a:RPWeekDataResult/a:Rows/a:Row/a:Col1',namespaces)
print(items[0].attrib["CASE_T"])

