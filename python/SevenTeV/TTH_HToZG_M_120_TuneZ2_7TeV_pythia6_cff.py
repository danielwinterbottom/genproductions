import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

source = cms.Source("EmptySource")
generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(7000.0),
	crossSection = cms.untracked.double(1.0),
	filterEfficiency = cms.untracked.double(1.0),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

        PythiaParameters = cms.PSet(
            pythiaUESettingsBlock,
            processParameters = cms.vstring('PMAS(25,1)=120.0        !mass of Higgs', 
            'MSEL=0                  ! user selection for process', 
            'MSUB(102)=0             !ggH', 
            'MSUB(123)=0             !ZZ fusion to H', 
            'MSUB(124)=0             !WW fusion to H', 
            'MSUB(24)=0              !ZH production', 
            'MSUB(26)=0              !WH production', 
            'MSUB(121)=1             !gg to ttH', 
            'MSUB(122)=1             !qq to ttH', 
            'MDME(210,1)=0           !Higgs decay into dd', 
            'MDME(211,1)=0           !Higgs decay into uu', 
            'MDME(212,1)=0           !Higgs decay into ss', 
            'MDME(213,1)=0           !Higgs decay into cc', 
            'MDME(214,1)=0           !Higgs decay into bb', 
            'MDME(215,1)=0           !Higgs decay into tt', 
            'MDME(216,1)=0           !Higgs decay into', 
            'MDME(217,1)=0           !Higgs decay into Higgs decay', 
            'MDME(218,1)=0           !Higgs decay into e nu e', 
            'MDME(219,1)=0           !Higgs decay into mu nu mu', 
            'MDME(220,1)=0           !Higgs decay into tau nu tau', 
            'MDME(221,1)=0           !Higgs decay into Higgs decay', 
            'MDME(222,1)=0           !Higgs decay into g g', 
            'MDME(223,1)=0           !Higgs decay into gam gam', 
            'MDME(224,1)=1           !Higgs decay into gam Z', 
            'MDME(225,1)=0           !Higgs decay into Z Z', 
            'MDME(226,1)=0           !Higgs decay into W W',
                                            
            'MDME(174,1)=0           !Z decay into d dbar',
            'MDME(175,1)=0           !Z decay into u ubar',
            'MDME(176,1)=0           !Z decay into s sbar',
            'MDME(177,1)=0           !Z decay into c cbar',
            'MDME(178,1)=0           !Z decay into b bbar',
            'MDME(179,1)=0           !Z decay into t tbar',
            'MDME(182,1)=1           !Z decay into e- e+',
            'MDME(183,1)=0           !Z decay into nu_e nu_ebar',
            'MDME(184,1)=1           !Z decay into mu- mu+',
            'MDME(185,1)=0           !Z decay into nu_mu nu_mubar',
            'MDME(186,1)=1           !Z decay into tau- tau+',
            'MDME(187,1)=0           !Z decay into nu_tau nu_taubar'
            ),
            # This is a vector of ParameterSet names to be read, in this order
            parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )

)
