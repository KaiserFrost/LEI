import xml.etree.ElementTree as ET
tree = ET.parse('official-cpe-dictionary_v2.3.xml')
root = tree.getroot()
for child in root.findall("cpe-23:cpe23-item"):
    print(child)