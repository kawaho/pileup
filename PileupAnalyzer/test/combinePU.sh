declare -a arr=('2016preVFP' '2016postVFP' '2017' '2018')
for i in "${arr[@]}"
do
  echo $i
  hadd $CMSSW_BASE/src/FinalStateAnalysis/TagAndProbe/data/$i/Pileup.root /nfs_scratch/kaho/PU_$i-runAnalyzer/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/submit/*/*root
done
