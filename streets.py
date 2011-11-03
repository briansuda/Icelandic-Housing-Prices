#coding:utf-8
import urllib2
from BeautifulSoup import BeautifulSoup
import simplejson as json

def get_streets_in_postcode(code):
	""" 
	Retrieves all street names in a given post code.
	"""
	print "Getting streets in postcode %d" % code	
	# First we need to receive a state. We can store it for the session, but that's TODO.
	u = urllib2.urlopen("http://www.postur.is/cgi-bin/hsrun.exe/Distributed/gamli/StateId/Qa4JXyRn7-JB2wlCuEf_Oiqx3r6Wm-GFH2/HAHTpage/HS_gotuskra?Postnumer=%s"%code)
	soup = BeautifulSoup("\n".join(u.readlines()).decode("iso-8859-1"))
	rows = soup.findAll("table")[1].findAll("tr")
	streets = []
	for row in rows:
		if len(row.findAll("td")) > 0:
			streets.append(row.findAll("td")[1].contents[0])

	return streets


if __name__ == "__main__":
	# Get all the streets in a given postcode
	for pc in [101,102,103,104,105,107,108,109,110,111,112,113,116,121,123,124,125,127,128,129,130,132,150,155,170,172,190,200,201,202,203,210,212,220,221,222,225,230,232,233,235,240,245,250,260,270,271,276,300,301,302,310,311,320,340,345,350,355,356,360,370,371,380,400,401,410,415,420,425,430,450,451,460,465,470,471,500,510,512,520,524,530,531,540,541,545,550,551,560,565,566,570,580,600,601,602,603,610,611,620,621,625,630,640,641,645,650,660,670,671,675,680,681,685,690,700,701,710,715,720,730,735,740,750,755,760,765,780,781,785,800,801,802,810,815,816,820,825,840,845,850,851,860,861,870,871,880,900,902]:
		print "Getting %d" % pc
		f = get_streets_in_postcode(pc)
		fh = open("data/streets/%d_streets" % pc, "w+")
		fh.write(json.dumps(f))
		fh.close()
