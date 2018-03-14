#bin/bash

#./install.py --carddir Cards/DarkHiggsDiJetsDMJets_axial_LO_MZprime_Mhs_Mchi-10_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001

#BBbarDM
#./install.py --carddir Cards/BBbarDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 50
./install.py --carddir Cards/BBbarDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 50
./install.py --carddir Cards/BBbarDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 70
./install.py --carddir Cards/BBbarDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 90

#DijetDM, 50,100,300
#./install.py --carddir Cards/DiJetsDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 150 --dm 10 --med 50
#./install.py --carddir Cards/DiJetsDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001

#DijetDM left out.
#for i in 50 150
#do
#    for j in 50 100 300
#    do
#	echo "./install.py --carddir Cards/DiJetsDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm $i --dm 10 --med $j"
#	./install.py --carddir Cards/DiJetsDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm $i --dm 10 --med $j
#    done
#done
