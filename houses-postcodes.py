import requests
import json
import glob
import os
import time

# skra.is geoserver
url = 'http://geo.skra.is/geoserver/wfs'

def postcode_jsondump(postnr):
    time.sleep(10)
	
    params = {'service':'wfs', 'version':'1.1.0','request':'GetFeature','typename':'fasteignaskra:VSTADF','outputformat':'json','filter':'<Filter><PropertyIsLike wildCard="*" singleChar="#" escapeChar="!"><PropertyName>fasteignaskra:POSTNR</PropertyName><Literal>%s</Literal></PropertyIsLike></Filter>' % (postnr)}
    r = requests.post(url,data=params)
    jsonstring = r.content
    return jsonstring

if __name__ == "__main__":
	# get the json dump of every house in the postcodes from streets.py
	postcodes = glob.glob('data/streets/*')
	if not os.path.exists('data/houses'):
		os.makedirs('data/houses')
    
	postcodes = [101,103,104,105,107,108,109,110,111,112,113,116,121,123,124,125,127,128,129,130,132,150,155,170,172,190,200,201,202,203,210,212,220,221,222,225,230,232,233,235,240,245,250,260,270,271,276,300,301,302,310,311,320,340,345,350,355,356,360,370,371,380,400,401,410,415,420,425,430,450,451,460,465,470,471,500,510,512,520,524,530,531,540,541,545,550,551,560,565,566,570,580,600,601,602,603,610,611,620,621,625,630,640,641,645,650,660,670,671,675,680,681,685,690,700,701,710,715,720,730,735,740,750,755,760,765,780,781,785,800,801,802,810,815,816,820,825,840,845,850,851,860,861,870,871,880,900,902]
	postcodes = [500]
	for pc in postcodes:	
		print "Getting json dump in postcode %s" % pc
		try:
			output = postcode_jsondump(pc)
		except Exception,e:
			print 'Something went wrong with postcode ', pc, e
		fh = open("data/landsnr/%s_houses" % pc, "w+")
		fh.write(output)
		fh.close()