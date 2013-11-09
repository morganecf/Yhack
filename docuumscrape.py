from bs4 import BeautifulSoup
import requests
from pprint import pprint
import urllib2
import simplejson
import re
import csv
case1 = re.compile("\n", re.IGNORECASE)

tags = ["exam","syllabus","midterm","assignment","solution","notes"]


#spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#spamwriter.writerow(['shortcourse', 'longcourse', 'description', 'tag', 'docname','url'])

courses = open('course.csv').read().splitlines()

#i = 0
for x in xrange(1357, 1369):
	for line in courses:
		info = line.split(',')
		shortcourse = info[0]
		longcourse = info[1]
		description = info[2]
		#pprint(shortcourse)
		for tag in tags:
			r = requests.get("http://www.docuum.com/McGill/document/filter/" + str(x) + "?tag=" + tag)
			soup = BeautifulSoup(r.text)	 
			
			for link in soup.find_all("a", {"class":"doc_download"}):
				doclink = (link.get('href'))
				doctitle = str(link.text)
				
				if re.search(case1, doctitle):
						doctitle2 = re.sub(case1, "", doctitle)
				x = [shortcourse, tag, doclink, doctitle2]
				pprint(x)



"""
			i+=1
			
			for line in open("course.csv").read().splitlines():
				info = line.split(',')
				shortcourse = info[0]
				longcourse = info[1]
				description = info[2]
				for tag in tags:
					r = requests.get("http://www.docuum.com/McGill/document/filter/" + str(x) + "?tag=" + tag)
					soup = BeautifulSoup(r.text)
							 
					for link in soup.find_all("a", {"class":"doc_download"}):
					
						doclink = str(link.get('href'))
						#pprint(doclink)
						doctitle = str(link.text)
						if re.search(case1, doctitle):
							doctitle2 = re.sub(case1, "", doctitle)
			pprint(i)
			pprint(shortcourse) 
			pprint(longcourse)
			pprint(description)
			pprint(tag)
			pprint(doctitle2)
			pprint(doclink)
					#pprint(doctitle2)
				#docs.append(doctitle)
				
					"""