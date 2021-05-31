import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process('Demo')

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

options = VarParsing.VarParsing ('analysis')
options.register ('era',
                  "2017", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "which era")

options.outputFile = "Pileup.root"
options.parseArguments()

if options.era=="2018":
  GT = '106X_upgrade2018_realistic_v15_L1v1'
elif options.era=="2017":
  GT = '106X_mc2017_realistic_v8'
elif options.era=="2016postVFP":
  GT = '106X_mcRun2_asymptotic_v15'
elif options.era=="2016preVFP":
  GT = '106X_mcRun2_asymptotic_preVFP_v9'

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.GlobalTag = GlobalTag(process.GlobalTag, GT, '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v17', '')

process.source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring( options.inputFiles ) )

process.pileup = cms.EDAnalyzer(
    'PileupAnalyzer',
    pileUp = cms.InputTag('slimmedAddPileupInfo'),
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( options.outputFile )
                                   )

process.p = cms.Path(process.pileup)
