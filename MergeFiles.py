#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" small executable to merge and download output of eventloop job
"""


import os

import shutil
import logging
logging.basicConfig(level=logging.DEBUG)
import ROOT
import FileHelper

def main(argv):
	from optparse import OptionParser
	parser = OptionParser(usage="usage: %prog sample",description="script to merge root files." )
	# parser.add_option('-v','--verbose',default=None, action='store_true', help='verbose output.')
	parser.add_option("-o","--outfile",default='output.root',help="output directory (default: \"VaryEcm.pdf\")")

	(options,args) = parser.parse_args()

	FileHelper.MergeFiles(files = args, output = options.outfile)




if __name__ == '__main__':

	main(os.sys.argv[1:])