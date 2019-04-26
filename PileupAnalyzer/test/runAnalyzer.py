import FWCore.ParameterSet.Config as cms

process = cms.Process('Demo')

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v17', '')

inputFilesData = cms.untracked.vstring(
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/FAF5C76A-EA85-E811-A3D4-FA163E69288A.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/F0DB6FF1-8486-E811-843A-0CC47AFB7D60.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/D2E64914-5586-E811-8AD4-B8CA3A709028.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/CE10E06D-EA85-E811-8600-FA163E41CC90.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/C8ABAF8B-7186-E811-A52A-003048CB8610.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/C0683AA8-1586-E811-8066-FA163E781D28.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/B6A1737F-EA85-E811-ACA0-FA163E4BEFFB.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/B0F13701-B986-E811-9B65-001CC4A60CF8.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/B094B346-4686-E811-B6C3-FA163E95DFD6.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/A6DBE1B1-8D86-E811-97B8-AC1F6B56762A.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/A2488E3F-B985-E811-933D-008CFA1974E4.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/8E436AAD-AF86-E811-BB06-0017A4770458.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/8C901753-E585-E811-99D0-00145EDD79D9.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/80D94D92-CD86-E811-B02B-A0369F83630C.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/7A2B2CBC-7D87-E811-87F6-A4BF0112BD90.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/749F4C9E-1287-E811-B7D4-FA163E11D44C.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/72AE896E-EA85-E811-953E-FA163E41CC90.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/725D8094-F185-E811-8FE2-FA163E44EC3B.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/7090D675-7D87-E811-8BB9-FA163E1ABE52.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/681D3029-1586-E811-85C3-FA163E7EFBB1.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/666F09AF-3886-E811-94C4-FA163E2148D2.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/64382055-F185-E811-9934-FA163E41CC90.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/621EF0F8-7086-E811-88E0-20CF3019DF02.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/5A50833D-1586-E811-AE2D-FA163E898C76.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/481CF2F7-A986-E811-BDBA-002590D8C68A.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/461FDC6D-EA85-E811-9811-FA163E41CC90.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/426323AB-D585-E811-BDBC-0242AC130002.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/40C4DD86-7186-E811-B476-0CC47AA98F96.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/3E34E54F-1586-E811-BD2B-FA163E2491DF.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/30E2C4E3-B185-E811-902C-001517FB25E4.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/283DE774-F086-E811-B439-A0369FD0B2AA.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/20C7D880-EA85-E811-98E0-FA163E285B61.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/1ECBFD99-3186-E811-8185-FA163E5B9804.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/0C536046-A385-E811-8B2E-0CC47A13D3B2.root',
'/store/mc/RunIIFall17MiniAODv2/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/08192B9B-BB86-E811-930C-002590E7D7D0.root',
)

inputFiles = inputFilesData

outputFile = "pileupGGHMTNew.root"
process.source = cms.Source ("PoolSource", fileNames = inputFiles )
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())

process.pileup = cms.EDAnalyzer(
    'PileupAnalyzer',
    pileUp = cms.InputTag('slimmedAddPileupInfo'),
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

process.p = cms.Path(process.pileup)
