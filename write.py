import xml.etree.ElementTree as ET
import json

#Parse file
file = ET.parse('annotations.xml')

#Load json as a dictionary, named "data"
f = open('random.json', 'r')
data = json.loads(f.read())
print(data)
print(type(data[0]))

#Parent tag of the file
root = file.getroot()

#4th subtag of the parent tag
# image = root[4]

#Initialize counters
counter = 0

#Array for image names, in terms of tags (start from the third tag)
name_list = []

#Array for image counters (whether that image has appeared before, if it has then it will append, if it hasn't then it will create a new thing)
image_counter = []

#Array for actual image annotations
image_list = []

#Configure required lists based on json 
for x in data:
    # name_list.append(data[counter].get("name"))
    image_counter.append(0)
    image_list.append([])
    counter += 1

print(name_list)
print(image_counter)
print(image_list)

#Reset counter for next loop (in terms of images)
counter = 0
#Counter for the arrays within arrays (in terms of labels/annotations)
small_counter = 0

string = ''

#Loop through data
for x in data:
    #If the name is new
    if name_list.count(data[counter].get("name")) == 0:
        #Add into name list
        name_list.append(data[counter].get("name"))
        #Create image tag
        image = ET.SubElement(root, 'image')
        image.tail = '\n'
        image.text = '\n\t\t'
        image.set('name', data[counter].get("name"))
        #Loops through each annotation within each image
        for y in data[counter]["polygon"]:
            #If the image has never been edited before, it will create a new list
            if image_counter[counter] == 0:
                #Adds annotation to the list within the image list
                image_list[counter] = [data[counter]["polygon"][small_counter].get("annotations")]
                #Increases counter so that it will move on to next label/annotation
                    
                print("image list:" + str(image_list))
                #Signals that the image has been added and when it appears later on it will be appended
                image_counter[counter] = 1
                print(image_counter)

            else:
                #Adds annotations to the list within the image list if the list has been edited before
                image_list[counter].append(data[counter]["polygon"][small_counter].get("annotations"))
                image_counter[counter] += 1
                print("image list:" + str(image_list))
                print(image_counter)

            polygon = ET.SubElement(image, 'polygon')
            polygon.tail = '\n'
            polygon.text = '\n\t\t'
            polygon.set('label', str(data[counter]["polygon"][small_counter].get("label")))
            polygon.set('source', 'manual')
            polygon.set('occluded', '0')
            polygon.set('points', str(data[counter]["polygon"][small_counter].get("annotations")))
            image[-1].tail = '\n\t\t'

            b_xml = ET.tostring(root)

            with open('thing.xml', "wb") as f:
                f.write(b_xml)
            small_counter += 1
            print("Hi")

            
        #Resets everything for the new image
        small_counter = 0
        counter += 1
        print(counter)
        print(image_list)
    else: #If the image has appeared before
        small_counter = 0
        name_index = name_list.index(data[counter].get("name"))
        print("name index:" + str(name_index))
        print(counter)
        for z in data[counter]["polygon"]:
            print_index = name_index + 5
            print("small_counter" + str(small_counter))
            print("counter" + str(counter))
            image_list[name_index].append(data[counter]["polygon"][small_counter].get("annotations"))
            polygon = ET.SubElement(root[print_index], 'polygon')
            polygon.tail = '\n'
            polygon.text = '\n\t\t'
            polygon.set('label', str(data[counter]["polygon"][small_counter].get("label")))
            polygon.set('source', 'manual')
            polygon.set('occluded', '0')
            polygon.set('points', str(data[counter]["polygon"][small_counter].get("annotations")))
            small_counter += 1

            # root[print_index].append(polygon)

            image[-1].tail = '\n\t\t'

            b_xml = ET.tostring(root)

            with open('thing.xml', "wb") as f:
                f.write(b_xml)

            print("Bye")

# #Creates subelement polygon within 4th subtag
# polygon = ET.SubElement(image, 'polygon')

# polygon.tail = '\n'
# polygon.text = '\n\t\t'

# image[1].text = '\n\t\t'

# polygon.set('label', 'Hi')

# b_xml = ET.tostring(root)

# with open('thing.xml', "wb") as f:
#     f.write(b_xml)