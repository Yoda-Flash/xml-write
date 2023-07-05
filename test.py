import xml.etree.ElementTree as ET

#Creates element called "annotations"
annotations = ET.Element('annotations')

#Creates a new line with \n, indents with \t
annotations.tail = '\n'
annotations.text = '\n\t'

#Creates subelement within "annotations" called "image"
image = ET.SubElement(annotations, 'image')

image.tail = '\n'
image.text = '\n\t\t'

#Sets attributes within the tag "image"
image.set('id', '2')
image.set('name', 'NENT_Landfill_20230303_low.tif')
image.set('width', '7223')
image.set('height', '6522')

#Converts XML to bye object so it can be flushed to file stream
b_xml = ET.tostring(annotations)

with open('test.xml', "wb") as f:
    f.write(b_xml)

#Creates subelement within "image" called "polygon"
polygon = ET.SubElement(image, 'polygon')

polygon.tail = '\n'
polygon.text = '\n\t\t'

label_counter = 0
label_list = ["1, 3", 2, 3]

for x in annotations[0]:
    label = annotations[0][label_counter].get('width', default=None)
    label_list.append(label)
    
list = [x for x in label_list]
string = ''

zero = 0
string += str(label_list[0])

for x in label_list[1:]:
    string += ";" + str(x)

#Sets attributes within the tag "polygon"
polygon.set('label', string)
polygon.set('points', string)

polygon = ET.SubElement(image, 'polygon')
polygon.set('label', string)
polygon.set('points', string)

#Indents the closing image tag as well
image[-1].tail = '\n\t'

# image.append(polygon)

b_xml = ET.tostring(annotations)

with open('test.xml', "wb") as f:
    f.write(b_xml)