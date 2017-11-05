#!/usr/bin/env python
# coding=utf-8

import time
import pp

ppservers = ()
ncpus = 4
nbTick = 100000000
nbLoopTick = 10

def privateLoop(nbTick, nbLoopTick):
	a = 0
	b = nbTick
	for x in xrange(0, nbLoopTick):
		for i in xrange(0, nbTick):
	  		a = b + 2
  	
  	return 10

job_server = pp.Server(ncpus, ppservers=ppservers, secret="password")

for i in xrange(0,job_server.get_ncpus()):
	f1 = job_server.submit(privateLoop, (nbTick, nbLoopTick))


# Wait for jobs in all groups to finish
job_server.wait()

job_server.print_stats()
