#!/bin/bash
##########################################################################################
# \project:     ATLAS Experiment at CERN's LHC
# \package:     N/A
# \class:       N/A
# \file:        $Id$
# \author:      Alaettin.Serhan.Mete@cern.ch
# \history:     N/A 
# \description: Shell Script for running Generate_trf.py locally
#
# Copyright (C) 2012 University of California, Irvine
###########################################################################################

# Assumes DS number is provided as argument, i.e. ./RunEvgenLocal.sh DSID
# There is a folder w/ the DSID in the current directory that has the 
# jOptions and SLHA file

datasets=( "${1}" )

for folder in "${datasets[@]}"
do
  cd $folder
  runNumber=$(echo $folder | sed 's/\([0-9]*\).*/\1/g')
  # config=( `ls | grep "MC12.*.py" ` )
  config=../MC12.Herwigpp_UEEE3_CTEQ6L1_simplifiedModel_wA_slep_noWcascade.xslep_0.95.py
  echo $config
  Generate_trf.py ecmEnergy=8000 \
        runNumber=1 \
        firstEvent=1 \
        maxEvents=10 \
        randomSeed=1 \
        jobConfig=$config \
        outputEVNTFile=test.pool.root \
        evgenJobOpts=MC12JobOpts-00-09-46_v4.tar.gz \
        --omitvalidation=testEventMinMax > generationLog 2>&1;
  cd ..
done

echo "All done!"
