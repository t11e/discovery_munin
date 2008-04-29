#!/usr/bin/python

import sys, os, commands

db_path = "/home/demo/demos/marketlinx/engine/db"

if len(sys.argv) == 2 and sys.argv[1] == 'config' : 
	print "graph_title db size"
	print "graph_vlabel size (bytes)"
	print "items.label db/items"
	print "lucene.label db/lucene"
	print "graph_args --base 1024 -l 0"
	print "graph_category engine"
	print "graph.info Disk usage for the db/items and db/lucene directories taken every 5 minutes."
	print "items.label Disk usage for db/items"
	print "lucene.label Disk usage for db/lucene"
else:
	if os.path.isdir(db_path + "/items"):
		print "items.value %s" % commands.getoutput("du -s " + db_path + "/items | cut -f1")
	else:
		print "items.value 0"
	if os.path.isdir(db_path + "/lucene"):
		print "lucene.value %s" % commands.getoutput("du -s " + db_path + "/lucene | cut -f1")
	else:
		print "lucene.value 0"
