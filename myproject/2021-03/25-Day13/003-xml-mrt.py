import xml.etree.ElementTree as ET

tree = ET.parse('StationTimeTable.xml')

root = tree.getroot()
print(root.findall("StationTimeTable/StationName/Zh_tw")[0].text)
