import xml.etree.ElementTree as ET
import xmlschema
import os

xsd_file = 'Validate/OpenSCENARIO-new.xsd'

def validate_file(filename):
    xml_tree = ET.parse(filename)
    xsd = xmlschema.XMLSchema(xsd_file)
    xsd.validate(xml_tree)

def walk_files(directory_name):
    for root, dirs, files in os.walk(directory_name):
        for filename in files:
            print(os.path.join(root, filename))
            validate_file(os.path.join(root, filename))
        for dir in dirs:
            walk_files(dir)

if __name__ == '__main__':
    validate_file('ParseXOSC/resources/xosc/controller_test.xosc')