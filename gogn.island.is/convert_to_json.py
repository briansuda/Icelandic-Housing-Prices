#coding:utf-8
import os
import sys
import csv
import simplejson as json
from isn93 import *

if __name__ == "__main__":
    output = []
    # This file comes from gogn.islands.is under a sort of creative commons attribution license
    with open('Stadfangaskra_20130326.dsv', 'rb') as csvfile:
        creader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in creader:
            item = {}
            item['municipality_number'] = row[1]
            item['land_number']         = row[3]
            item['postal_code']         = row[7]
            item['street']              = row[8].decode("iso-8859-1")
            item['street_declined']     = row[9].decode("iso-8859-1")
            item['house_number']        = row[10]
            if row[22] != '' and row[23] != '':
                item['x'] = float(row[22].replace(',','.'))
                item['y'] = float(row[23].replace(',','.'))
                item["lat"], item["lon"] = isn93_to_wgs84(item["x"], item["y"])
            output.append(item)
    
    print json.dumps(output)