## Herwig++ job option file for Susy 2-parton -> 2-sparticle processes

## Get a handle on the top level algorithms' sequence
from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.SMModeCDG')

if not 'evgenConfig' in dir():
    raise RuntimeError('These jobOptions should be run through Generate_trf.py')

## Setup Herwig++
include ( 'MC12JobOptions/Herwigpp_UEEE3_CTEQ6L1_Common.py' )

# define spectrum file name
include ( 'Susy_simplifiedModel_wA_slep_noWcascade_mc12points.py' )
print 'run number: %d' % runArgs.runNumber
try:
    (mc1,mn1) = pointdict[runArgs.runNumber]
except:
    raise RuntimeError('DSID %d not found in grid point dictionary. Aborting!' % runArgs.runNumber)
slha_file = 'susy_simplified_model_wA_sl_noWcascade.c1n2_%s.n1_%s.xslep_0.95.slha' % (mc1, mn1)
print 'mc1: %s' % mc1
print 'mn1: %s' % mn1
print 'slha_file: %s' % slha_file

# Add Herwig++ parameters for this process
include ( 'MC12JobOptions/Herwigpp_SUSYConfig.py' )
cmds = buildHerwigppCommands(['~chi_1+','~chi_20'],slha_file,'Exclusive')

## Define metadata
evgenConfig.description = 'Simplified Model Mode A grid generation for direct gaugino search...'
evgenConfig.keywords    = ['SUSY','Direct Gaugino','Simplified Models','chargino','neutralino']
evgenConfig.contact     = ['alaettin.serhan.mete@cern.ch']

## Print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')

## Set the command vector
topAlg.Herwigpp.Commands += cmds.splitlines()

# Set up filter
from GeneratorFilters.GeneratorFiltersConf import MultiElecMuTauFilter
topAlg += MultiElecMuTauFilter()
MultiElecMuTauFilter = topAlg.MultiElecMuTauFilter
MultiElecMuTauFilter.NLeptons  = 2
MultiElecMuTauFilter.MinPt = 7000.
MultiElecMuTauFilter.MaxEta = 2.7
MultiElecMuTauFilter.IncludeHadTaus = 0

StreamEVGEN.RequireAlgs = [ "MultiElecMuTauFilter" ]

## Clean up
del cmds
