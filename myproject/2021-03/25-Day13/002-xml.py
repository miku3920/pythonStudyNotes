from xml.etree import ElementTree

xmlstr = """<?xml version="1.0" encoding="utf-8"?>
<root>
 <person age="16">
    <name>miku3920</name>
    <sex>female</sex>
 </person>
 <person age="19" des="hello">
    <name>Alex</name>
    <sex>male</sex>
 </person>
</root>"""

root = ElementTree.fromstring(xmlstr)
print(root.findall("person/name")[0].text)
print(root.findall("person")[1].attrib["age"])
