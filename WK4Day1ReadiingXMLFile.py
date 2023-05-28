import xml.etree.ElementTree as ET
mytree = ET.parse('property.xml') #call parser
myroot = mytree.getroot() # get the root


for x in myroot.findall('bathrooms'):
    name = x.find('name').text
    price = x.find('price').text
    print(name,price)