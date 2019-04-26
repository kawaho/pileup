#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"


class PileupAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit PileupAnalyzer(const edm::ParameterSet&);
      ~PileupAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------

  edm::EDGetTokenT<std::vector<PileupSummaryInfo> > pileUpToken_;

  TH1F *h_pu;
};

PileupAnalyzer::PileupAnalyzer(const edm::ParameterSet& iConfig)

{
   //usesResource("TFileService");

   pileUpToken_ = consumes<std::vector<PileupSummaryInfo> >
     (iConfig.getParameter <edm::InputTag>
      ("pileUp"));

   edm::Service<TFileService> fs;
   h_pu = fs->make<TH1F>("pileup", "pileup", 100, 0, 100);
}


PileupAnalyzer::~PileupAnalyzer()
{
}

// ------------ method called for each event  ------------
void
PileupAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   edm::Handle<std::vector<PileupSummaryInfo> > puInfo;
   iEvent.getByToken(pileUpToken_, puInfo);

   if (puInfo.isValid()) {
     std::vector<PileupSummaryInfo>::const_iterator pvi;   
     float npv = -1;
     for(pvi = puInfo->begin(); pvi != puInfo->end(); ++pvi) {
       npv = pvi->getTrueNumInteractions();
       h_pu -> Fill(npv);
     }
   }
}

// ------------ method called once each job just before starting event loop  ------------
void 
PileupAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PileupAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PileupAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PileupAnalyzer);
