#coding:utf-8
import simplejson as json


if __name__ == "__main__":
	svg = ''
	# now all the data is in the first and second dictionaries, time to find them and plot them!
	svg += ('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve">')
	
	# get all the houses on the streets
	landsnr = json.loads(open("houses.json").readline())
	output = []
	for nr in landsnr:
		lat = ((nr['lat']*1000)*2)-128000;
		lon = (nr['lon']*1000)+22000;
    
		svg += '<circle r=".1" cy="'+str(lat)+'" cx="'+str(lon)+'" stroke-width="0" fill="#ccccc"/>'
		
	
	svg += ('</svg>')

	print svg
	
