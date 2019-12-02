# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191001
############################
#
# Connect MySQL

import json
test_l = []

ratio_l = [0.3, 0.1,0.2,0.3,0.15]
for i in range(0,5):
    appDict = {'applNo': '012120000','ratio': ratio_l[i]}
    test_l.append(appDict)
app_json = json.dumps(test_l)
print(test_l[4]['ratio'])