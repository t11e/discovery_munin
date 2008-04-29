#!/usr/bin/python

import sys, os, commands, urllib
from xml.dom import minidom

url = "http://localhost:8080/ws/info/runtime"

if len(sys.argv) == 2 and sys.argv[1] == 'config' : 
	print "graph_title engine memory stats"
	print "graph_vlabel size (bytes)"
	print "graph_args --base 1024 -l 0"
	print "graph_category engine"
	print "freememory.label free memory"
	print "totalmemory.label total memory"
	print "maxmemory.label max memory"
	print "graph.info Amount of free, total, and max memory reported as reported by the engine, sampled every 5 minutes."
else:
	try:
		sock = urllib.urlopen(url)
	except (IOError, OSError):
		exit(1)
	doc = minidom.parse(sock).documentElement
	sock.close()
	print "freememory.value %s" % doc.getElementsByTagName("freeMemory")[0].firstChild.data
	print "totalmemory.value %s" % doc.getElementsByTagName("totalMemory")[0].firstChild.data
	print "maxmemory.value %s" % doc.getElementsByTagName("maxMemory")[0].firstChild.data
