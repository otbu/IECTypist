
from xml.parsers import expat

elements = dict(
    root=dict(name='TcPlcObject',isFound=False),
    dut=dict(name='DUT',isFound=False),
    decl=dict(name='Declaration',isFound=False))

dut_filename = r'../data/OperatorAlertData.TcDUT'

elementName_object = 'TcPlcObject'
elementName_dut = 'DUT'
elementName_declaration = 'Declaration'

elementIsFound_object = False
elementIsFound_dut = False
elementIsFound_declaration = False
cached_cdata = ''

def start_element(name, attributes):

    global \
        elements, \
        elementIsFound_object, \
        elementIsFound_dut, \
        elementIsFound_declaration

    if name == elements['root']['name']:
        print('-- Found', elements['root']['name'])
        elements['root']['isFound'] = True

    if name == elements['dut']['name']:
        print('-- Found', elements['dut']['name'])
        elements['dut']['isFound'] = True

    if name == elements['decl']['name']:
        print('-- Found', elements['decl']['name'])
        elements['decl']['isFound'] = True


def char_data(data):
    global cached_cdata
    if elements['root']['isFound'] and elements['dut']['isFound'] and elements['decl']['isFound']:
        cached_cdata += data

def main():
    #p = expat.ParserCreate()
    #p.StartElementHandler = start_element
    #p.CharacterDataHandler = char_data
    #with open(r'../../OperatorAlertData.TcDUT', 'rb') as file:
    #    p.ParseFile(file)
    #print('-- Found DUT CharacterData:\n', repr(cached_cdata))

    import xml.etree.ElementTree as ET
    tree = ET.parse(dut_filename)
    root = tree.getroot()
    print(root[0][0].text)

if __name__ == '__main__':
    main()
