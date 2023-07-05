import xml.etree.ElementTree as ET

file = ET.parse('annotations.xml')

annotations = file.getroot()

#Gets data under "points"
print(annotations[3][0].get("points", default = None))

counter = 3

annote = [0,0,0]
for x in annotations[3:]:
    annote.append(annotations[counter].get("name", default = None))
    counter += 1

attrib = annotations[3].attrib
print(attrib["name"])
print(annote)
print(annote.index("NENT_Landfill_20230303_low.tif"))