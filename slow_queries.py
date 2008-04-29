#!/usr/bin/python

import sys, os, commands

log_path = "/home/demo/demos/marketlinx/engine/log/discovery.log"
grep_str = "' Aggregating query.* \[done\]'"

if len(sys.argv) == 2 and sys.argv[1] == 'config' : 
	print "graph_title Slow queries"
	print "graph_vlabel # queries"
	print "num.label # queries"
	print "num.type DERIVE"
	print "num.min 0"
	print "graph_args -l 0"
	print "graph_category engine"
	print "graph.info Count of queries slow enough to be logged to the aggregator's log file. Collected every 5 minutes."
	print "num.label # slow queries since last collection"
else:
	if os.path.exists(log_path):
		print "num.value %s" % commands.getoutput("cat " + log_path + " | grep " + grep_str + " | wc -l")
	else:
		sys.exit(-1)
