import simplejson
import re
from pprint import pprint

case1 = re.compile("comp", re.IGNORECASE)
case2 = re.compile("shortname?(.+)", re.IGNORECASE)
with open("resultsf.txt", "a+") as resultsf:
	with open("resultsw.txt", "a+") as resultsw:
		with open("f13.json", "r") as f13:
			with open("w14.json", "r") as w14:
		 		semesters = [f13, w14]
		 		
	 			for lines in f13:
	 			 	if re.search(case1, str(lines)):
	 					if re.search(case2, str(lines)):
	 						#results.write(simplejson.dumps({"name": name}) + "/n")
							#results.write(str(lines))
							resultsf.write(lines + ",")
				
				
				for lines in w14:
	 				if re.search(case1, str(lines)):
	 					if re.search(case2, str(lines)):
	 						#results.write(simplejson.dumps({"name": name}) + "/n")
							#results.write(str(lines))
							resultsw.write(lines + ",")
				