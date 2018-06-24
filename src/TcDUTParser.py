
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

    # check if C++ line-end comments are used:
    s0 = re.finditer(r'(?m)^.*?//(?P<comment>.*?)$', attributes['type_text'])
    s1 = re.split(r'(?m)^.*?//(?P<comment>.*?)$', attributes['type_text'])
    print(s1)
    for match in s0:
        comment_span = match.span('comment')
        print(repr(attributes['type_text'][match.start('comment'):match.end('comment')]))
        #print(repr(match.group('comment')))

    #m0 = re.search(r'(?s)TYPE\s+?(?P<name>\S+?)\s*?:(?P<body>.*?)END_TYPE', attributes['type_text'])
    #type_body = m0.group('body')

    # find STRUCT ... END_STRUCT body:
    #m1 = re.search(r'(?s).*?STRUCT(?P<struct_body>.*?)END_STRUCT', type_body)
    #struct_body = m1.group('struct_body')

    #print(repr(struct_body))

    #m2 = re.search(r'(?m)\s*?(\S+?)\s*?:\s*?;', type_body)

if __name__ == '__main__':
    main()
