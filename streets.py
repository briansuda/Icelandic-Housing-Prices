#coding:utf-8
import urllib2
import simplejson as json

if __name__ == "__main__":	
	post_codes = {}
	
	print "Getting streets"	

	# fetch the cvs data from online
	url = 'http://www.postur.is/gogn/Gotuskra/gotuskra.txt'
	u = urllib2.urlopen(url)
	data = u.readlines()
	
	# loop through the data and create a dict, POST_CODE -> [street,street,...,street]
	for d in data:
		parts = d.decode("iso-8859-1").strip().split(';')
		if not parts[1] in post_codes:
			post_codes[parts[1]] = []
		post_codes[parts[1]].append(parts[2])
	

	# write it to file so we can pass it through the next stage.
	# keep it as json for portability
	for k,v in post_codes.iteritems():
		fh = open("data/streets/%s_streets" %k, "w+")
		fh.write(json.dumps(v))
		fh.close()