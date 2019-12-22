#coding:utf-8
from xml.dom import minidom

def read_xml_test(filename):
    xml=minidom.parse(filename)
    root=xml.documentElement
    elements=root.getElementsByTagName('element')
#    print(elements)
    
    for element in elements:
#        print(element)
        if element.hasAttribute('id'):
            print("id:",element.getAttribute('id'))
            
        for node in element.childNodes:
            if node.nodeName=='#text':
                text=node.data.replace('\n','')
                print('\t文本：',text)
            else:
                print('\t'+node.nodeName)
                for attr,attr_val in node.attributes.items():
                    print('\t\t',attr,':',attr_val)
        print('')
        
if __name__=="__main__":
    read_xml_test('1.xml')