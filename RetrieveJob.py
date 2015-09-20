#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
# Workaround to fix threadlock issues with GUI
ROOT.PyConfig.StartGuiThread = False
# suppress ROOT command line, use python optparse
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
import shutil
import logging
logging.basicConfig(level=logging.DEBUG)


shutil.copyfile(ROOT.gSystem.ExpandPathName('$ROOTCOREDIR/scripts/load_packages.C'), 'load_packages.C')
ROOT.gROOT.ProcessLine(".x load_packages.C")

ROOT.EL.Driver.retrieve("mc-test");

