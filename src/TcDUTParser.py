
from xml.etree import ElementTree
import re

dut_filename = r'../data/TestTypeB.TcDUT'

elementName_object = 'TcPlcObject'
elementName_dut = 'DUT'
elementName_declaration = 'Declaration'

def main():

    tree = ElementTree.parse(dut_filename)
    elem_root = tree.getroot()

    attributes = dict()
    attributes['object_version'] = elem_root.get('Version')
    attributes['prod_version'] = elem_root.get('ProductVersion')
    attributes['type_name'] = None
    attributes['type_id'] = None
    attributes['type_text'] = None

    elem_dut = elem_root.find('DUT')
    elem_decl = None

    if elem_dut is not None:
        elem_decl = elem_dut.find('Declaration')
        attributes['type_name'] = elem_dut.get('Name')
        attributes['type_id'] = elem_dut.get('Id')

    if elem_decl is not None:
        attributes['type_text'] = elem_decl.text

    print(attributes)

    m0 = re.search(r'(?s)TYPE\s+?(?P<name>\S+?)\s*?:(?P<body>.*?)END_TYPE', attributes['type_text'])
    type_name = m0.group('name')
    type_body = m0.group('body')
    #print(type_body)
    m1 = re.search(r'(?s)STRUCT(.*?)END_STRUCT', type_body)
    print(m1.group(1))

if __name__ == '__main__':
    main()
