#coding:utf-8
import urllib2
from BeautifulSoup import BeautifulSoup
import simplejson as json
from isn93 import *
import time

def get_street_coords_isn93(street):
	# pass in a street name and it returns all the houses on that street
	url = "http://arcgis.reykjavik.is/bvsAddressFind/?Addr=%s&top=200&type=3" % urllib2.quote(street.encode("iso-8859-1"))
	u = urllib2.urlopen(url)
	print url
	# wait a bit so the requests don't slam the server
	time.sleep(1)

	street = json.loads("".join(u.readlines()).decode("iso-8859-1"))
	return street


def get_street_coords_wgs84(street):
	# go fetch all the streets
	street = get_street_coords_isn93(street)
	
	# convert from Icelandic spacial coordinates to regular lat/lon
	for s in street:
		if not s.has_key("x") or not s.has_key("y"):
			continue
		if s["x"] == 0 and s["y"] == 0:
			street.remove(s)
		s["lat"], s["lon"] = isn93_to_wgs84(s["x"], s["y"])

	return street


if __name__ == "__main__":
	# get all the houses on the streets
	#for pc in [101,103,104,105,107,108,109,110,111,112,113,116,121,123,124,125,127,128,129,130,132,150,155,170,172,190,200,201,202,203,210,212,220,221,222,225,230,232,233,235,240,245,250,260,270,271,276,300,301,302,310,311,320,340,345,350,355,356,360,370,371,380,400,401,410,415,420,425,430,450,451,460,465,470,471,500,510,512,520,524,530,531,540,541,545,550,551,560,565,566,570,580,600,601,602,603,610,611,620,621,625,630,640,641,645,650,660,670,671,675,680,681,685,690,700,701,710,715,720,730,735,740,750,755,760,765,780,781,785,800,801,802,810,815,816,820,825,840,845,850,851,860,861,870,871,880,900,902]:
	#for pc in [300,301,310,311,320,340,345,350,355,356,360,370,371,380,400,401,410,415,420,425,430,450,451,460,465,470,471,500,510,512,520,524,530,531,540,541,545,550,551,560,565,566,570,580,600,601,602,603,610,611,620,621,625,630,640,641,645,650,660,670,671,675,680,681,685,690,700,701,710,715,720,730,735,740,750,755,760,765,780,781,785,800,801,802,810,815,816,820,825,840,845,850,851,860,861,870,871,880,900,902,101,203,210,220,221,222,225,230,233,235,240,245,250,260,270,271,276]:
	for pc in [671]:
		print "Getting %d" % pc
		streets = json.loads(open("data/streets/%d_streets" % pc).readline())
		output = []
		for street in streets:
			print("Getting street coords for '%s'" % street)
			f = get_street_coords_wgs84(street)
			output.append(f)
			
		fh = open("data/houses/%d_houses" %pc, "w+")
		fh.write(json.dumps(output))
		fh.close()
