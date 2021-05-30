from FinalStateAnalysis.Utilities.dbsinterface import get_das_info
import argparse
import os

parser = argparse.ArgumentParser()

def getFilesName(dataset):
  dbs_datasets = get_das_info('file dataset=%s  status=*'%dataset)
  return dbs_datasets

def run(cmd, dr):
  print "%s\n"%cmd
  if not dr: os.system(cmd)

parser = argparse.ArgumentParser()
parser.add_argument("--era", type=str, default='2017')
parser.add_argument("--dryRun", action="store_true")
args = parser.parse_args()
era = args.era

if era=='2016preVFP':
  samples = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v1/MINIAODSIM'
elif era=='2016postVFP':
  samples = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM'
elif era=='2017':
  samples = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
elif era=='2018':
  samples = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM'

files = getFilesName(samples)

with open('inputlist'+era+'.txt', 'w') as txt:
  txt.write('\n'.join(files))

itest = 'farmoutAnalysisJobs PU_'+era+' --vsize-limit 8000 --memory-requirements=3000 --infer-cmssw-path runAnalyzer.py era='+era+' \'inputFiles=$inputFileNames\' \'outputFile=$outputFileNames\' --input-dir=/ --output-dir=. --assume-input-files-exist --input-file-list=./inputlist'+era+'.txt'

run(itest, args.dryRun)
