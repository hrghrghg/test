#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")

name1 = ET.SubElement(new_xml, "info", attrib={"enrolled": "yes"})
name = ET.SubElement(name1, "name")
name.text = '22'
age = ET.SubElement(name1, "age", attrib={"checked": "no"})
sex = ET.SubElement(name1, "sex")
sex.text = '33'

name2 = ET.SubElement(new_xml, "info", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'


et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式