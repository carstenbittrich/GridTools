#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" small executable to merge and download output of eventloop job
"""


import os

import shutil
import logging
logging.basicConfig(level=logging.DEBUG)
import ROOT

def SetupEventLoopEnvironment():
	# Workaround to fix threadlock issues with GUI
	ROOT.PyConfig.StartGuiThread = False
	# suppress ROOT command line, use python optparse
	ROOT.PyConfig.IgnoreCommandLineOptions = True
	shutil.copyfile(ROOT.gSystem.ExpandPathName('$ROOTCOREDIR/scripts/load_packages.C'), 'load_packages.C')
	ROOT.gROOT.ProcessLine(".x load_packages.C")

def main(argv):
	from optparse import OptionParser
	parser = OptionParser(usage="usage: %prog sample",description="small executable to merge and download output of eventloop job." )
	# parser.add_option('-v','--verbose',default=None, action='store_true', help='verbose output.')
	# parser.add_option("-o","--outfile",default='VaryEcm.pdf',help="output directory (default: \"VaryEcm.pdf\")")

	(options,args) = parser.parse_args()

	SetupEventLoopEnvironment()

	for job in args:
		print "Downloading job: ", job
		ROOT.EL.Driver.retrieve(job);



if __name__ == '__main__':

	main(os.sys.argv[1:])