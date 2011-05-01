# coding=utf-8
from string import * 
import sys, os, codecs

def reader(infile):
	"""docstring for reader"""
	pass
	try:
		csv = open(infile,"r")	
	except IOError:
		print 'cannot open', infile
	else:
		lines = csv.readlines()
		return lines

def elementcatch(liste):
	identifier = []
	try:
		x = sys.argv[2]
	except IndexError:
		print "please pass a column that will be extracted:"
		print "e.g. python csvexport.py filename.csv 15 8"
	else:
		for element in liste:
			if element != "\n":
				temp = element.split(";")
				temptwo = temp[-1]
				temp.pop()
				temptwo = temptwo.rstrip()
				temp.append(temptwo)
				identifier.append(temp)
		return identifier


def comparer(identifier):
	header = identifier[0]
	header.append("old identifier")
	header.append("new identifier")
	header.append("# errors")
	header.append("\r\n")
	identifier.pop(0)
	counter = 0
	outlist = []
	outlist.append(header)
	shorties = []
	temphit = []
	
	try: 
		x = sys.argv[3]
	except IndexError:
		print "please pass length of the column that will be extracted:"
		print "e.g. python csvexport.py filename.csv 43 10"
	else: 
			
		for current in identifier:
			if len(current[int(sys.argv[2])-1]) != int(sys.argv[3]):
				temphit = list(current)
				temphit.append(current[int(sys.argv[2])-1])
				temphit.append("none")
				temphit.append("none")
				temphit.append("\r\n")
				outlist.append(list(temphit))
			else: 
				besthit = ["null", float("inf")]
				counteridentifier = list(identifier)
				counteridentifier.pop(counter)
				for candidate in counteridentifier:
					if len(candidate[int(sys.argv[2])-1]) == int(sys.argv[3]):
						errorcounter = 0
						lettercounter = 0
						for letter in current[int(sys.argv[2])-1]:
							if letter.upper() != candidate[int(sys.argv[2])-1][lettercounter].upper():
								errorcounter += 1
							lettercounter += 1
						if errorcounter < besthit[1]:
							besthit = [candidate[int(sys.argv[2])-1],errorcounter]
					else:
						errorcounter = 0
						lettercounter = 0
				temphit = list(current)
				temphit.append(current[int(sys.argv[2])-1])
				temphit.append(besthit[0])
				temphit.append(str(besthit[1]))
				temphit.append("\r\n")
				outlist.append(temphit)
			counter += 1
		return outlist
		
def writer(infile):
	out = ""
	for x in infile:
		temp = ";".join(x)
		out = out + temp
	print out
						
		

def main():
	try: 
		x = sys.argv[1]
		x = sys.argv[2]
		x = sys.argv[3]
	except IndexError:
		print "\nplease pass the following arguments:"
		print "a) the filename" 
		print "b) which column you want to extract" 
		print "c) length of correct identifiers\n"
		print "e.g. python csvexport.py filename.csv 43 10"
	else:
		lines = reader(sys.argv[1])
		if lines != None:
			identifier = elementcatch(lines)
		if identifier != None:	
			tofile = comparer(identifier)
		if tofile != None:
			writer(tofile)
					

main()
