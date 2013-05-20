#coding:utf-8
import urllib2
from BeautifulSoup import BeautifulSoup
import simplejson as json
from isn93 import *
import time

def get_street_coords_isn93(box):
	# pass in a street name and it returns all the houses on that street
	url = "http://arcgis.reykjavik.is/bvsAddressFind/?Addr=%s&top=200&type=3" % urllib2.quote(box)
	u = urllib2.urlopen(url)
	
	print url
	# wait a bit so the requests don't slam the server
	time.sleep(1)

	box = json.loads("".join(u.readlines()).decode("iso-8859-1"))
	return box


def get_street_coords_wgs84(box):
	# go fetch all the streets
	box = get_street_coords_isn93(box)
	
	# convert from Icelandic spacial coordinates to regular lat/lon
	for s in box:
		if not s.has_key("x") or not s.has_key("y"):
			continue
		if s["x"] == 0 and s["y"] == 0:
			box.remove(s)
		s["lat"], s["lon"] = isn93_to_wgs84(s["x"], s["y"])

	return box


if __name__ == "__main__":
	# get all the houses on the streets
	post_boxes = [
	"Aðalstæti 2, 101",
	"Bankastræti 2, 101",
	"Bergstaðastræti 37, 101",
	"Grandagarður 11, 101",
	"Hringbraut, 101",
	"Hverfisgata 39, 101",
	"Ingólfsstræti /Sölvhólsgata 7, 101",
	"Laugavegur 43, 101",
	"Pósthússtræti 5, 101",
	"Reykjavíkurflugvöllur, 101",
	"Skólavörðustígur 19, 101",
	"Tryggvagata 11, 101",
	"Vatnsmýrarvegur 10, 101",
	"Vesturgata 51, 101",
	"Háaleitisbraut 68, 103",
	"Kringlan 8, 103",
	"Álfheimar 74, 104",
	"Langholtsvegur 128, 104",
	"Langholtsvegur 43, 104",
	"Skútuvogur 13, 104",
	"Hamrahlíð 17, 105",
	"Hátún 10b, 105",
	"Hlemmur, 105",
	"Lauganesvegur 74a, 105",
	"Nóatún 17, 105",
	"Skipholt 50, 105",
	"Sundlaugavegur 34, 105",
	"Hagamelur 39, 107",
	"Hjarðarhagi 45-47, 107",
	"Hringbraut 121, 107",
	"Hringbraut 50, 107",
	"Ármúli 34, 108",
	"Efstaland 26, 108",
	"Háleitisbraut 58, 108",
	"Landspítali Fossvogi , 108",
	"Síðumúli 3, 108",
	"Skeifan 11, 108",
	"Suðurlandsbraut 2, 108",
	"Seljabraut 54, 109",
	"Þönglabakki 4, 109",
	"Höfðabakki 9, 110",
	"Hraunbær 119, 110",
	"Rofabær 39, 110",
	"Stórhöfði 32, 110",
	"Lóuhólar 2-6, 111",
	"Fjallkonuvegur 1, 112",
	"Gagnvegur 2, 112",
	"Hverafold 1-3, 112",
	"Spöngin 23, 112",
	"Þjóðhildarstígur 2, 113",
	"Esjugrund, 116",
	"Eiðistorg, 170",
	"Vogar Iðndalur 2, 190",
	"Borgarholtsbraut 19, 200",
	"Dalvegur 2, 200",
	"Hamraborg 1, 200",
	"Smiðjuvegur 4, 200",
	"Bæjarlind 14, 201",
	"Hlíðasmári 8, 201",
	"Smáralind 2, 201",
	"Smáralind Hagkaup, 201",
	"Salavegur 2, 203",
	"Garðatorg 5, 210",
	"Litlatún 3, 210",
	"Lyngás 18, 210",
	"Bæjarhraun 26, 220",
	"Fjarðargata 13, 220",
	"Lækjargata 46, 220",
	"Melabraut 11, 220",
	"Reykjavíkurvegur 50, 220",
	"Reykjavíkurvegur 66, 220",
	"Álftanes, 225",
	"Reykjanesbær Hafnargata 40, 230",
	"Reykjanesbær Hafnargata 89, 230",
	"Reykjanesbær Sólvallagata 2, 230",
	"Reykjanesbær Leifsstöð, 235",
	"Grindavík Svartsengi, 240",
	"Grindavík Víkurbraut 25, 240",
	"Sandgerði Suðurgata 2, 245",
	"Garður Garðbraut 69, 250",
	"Reykjanesbær Grundarvegur 23, 260",
	"Háholt 14, 270"
]

	output = []
	for box in post_boxes:
		print "Getting %s" % box
		f = get_street_coords_wgs84(box)

		output.append(f)
			
		#fh = open("data/houses/%d_houses" %pc, "w+")
		#fh.write(json.dumps(output))
		#fh.close()
	print output