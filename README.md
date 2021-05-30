# pileup
Generate PU distributions of MC samples.
## Prerequisite
The package is designed to submit jobs via condor on wisc hep computing account. You will also need the FSA package here: https://github.com/uwcms/FinalStateAnalysis/tree/miniAOD_10_2_22/NtupleTools/test to generate sample file lists.
## Usage
Submit jobs (using 2018 as an example) with
```console
cd PileupAnalyzer/test
python submit_job.py --era "2018"
```
and get the final output by
```console
source combinePU.sh 
```
Change the sample names in submit_job.py if you intend to use samples other than DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.
Change "kaho" to your user name in combinePU.sh.
