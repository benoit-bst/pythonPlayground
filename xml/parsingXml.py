#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET
# from lxml import etree

#---------------------------------------
# Parsing xml file
#---------------------------------------
tree = ET.ElementTree(file='input.xml')

tree.write(sys.stdout)

# root
root = tree.getroot()
print("root : %s" %root.tag)

# parse data
for child_of_root in root:

  if child_of_root.tag == 'filename':
    print ("filename %s" %child_of_root.text)

  # modules
  if child_of_root.tag == 'modules':

    for child_modules in child_of_root:

      if child_modules.tag == 'module':
        print ("module %s" %child_modules.text)

      if child_modules.tag == 'test':
        for child_test in child_modules:
          print ("val %s" %child_test.text)


  if child_of_root.tag == 'level':
    print ("level %d" %int(child_of_root.text))

for elem in tree.iter(tag='modules'):
  print elem.tag

for elem in tree.iterfind('modules/test/val1'):
  print elem.tag

for elem in tree.iterfind('modules/module'):
  print elem.tag

#---------------------------------------
# Write xml file
#---------------------------------------
rootNode = ET.Element('debug')

filenameNode = ET.SubElement(rootNode, 'filename')
filenameNode.text = 'debug.log'

modulesNode = ET.SubElement(rootNode, 'modules')
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'Finance'
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'Admin'
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'HR'

modulesNode = ET.SubElement(rootNode, 'modules')
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'Finance 2'
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'Admin 2'
moduleNode = ET.SubElement(modulesNode, 'module')
moduleNode.text = 'HR 2'

testNode = ET.SubElement(modulesNode, 'test')
valNode = ET.SubElement(testNode, 'val1')
valNode.text = 'val 1'
valNode = ET.SubElement(testNode, 'val2')
valNode.text = 'val 2'
valNode = ET.SubElement(testNode, 'val3')
valNode.text = '2.36541'

levelNode = ET.SubElement(rootNode, 'level')
levelNode.text = '2'

tree = ET.ElementTree(rootNode)
tree.write('ouput.xml')

#---------------------------------------
# Write xml file
#---------------------------------------
f = open("output1.xml", "w")
f.write("<?xml version='1.0' encoding='utf'?>\n")
f.write("<debug>\n")
f.write("    <filename>debug.log</filename>\n")
f.write("    <modules>\n")
strtmp = "Finance"
f.write("        <module>%s</module>\n" %strtmp)
f.write("        <module>Adin</module>\n")
f.write("        <module>HR</module>\n")
f.write("    </modules>\n")
f.write("</debug>\n")
f.close()