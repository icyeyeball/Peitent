# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
import requests
from lxml import etree
from io import BytesIO

r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=xml", verify=False)
xml_bytes = r.content
f = BytesIO(xml_bytes)
tree = etree.parse(f)
print (tree)
counties = [t.text for t in tree.xpath("/AQI/Data/County")]
site_names = [t.text for t in tree.xpath("/AQI/Data/SiteName")]
pm25 = [t.text for t in tree.xpath("/AQI/Data/PM2.5")]
print(type(xml_bytes))
for c, s, p in zip(counties, site_names, pm25):
    print(c, s, p)