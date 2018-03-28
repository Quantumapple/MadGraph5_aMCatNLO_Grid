#!/bin/bash 

#400 -> pseudoscalar dark photon 
./install.py --carddir Cards/psdcalar_LO_darkphoton_13TeV-madgraph --proc 400 --med 50 --dm 3 --runcms runcmsgrid_LO.sh

#401 -> iDM dark photon
./install.py --carddir Cards/iDM_LO_darkphoton_13TeV-madgraph --proc 401 --med 500 --dm 50 --hdm 50 --runcms runcmsgrid_LO.sh

#402 -> fermionDarkPortal complex
./install.py --carddir Cards/fPort_Comp_LO_lu1_Mphi_Mchi_13TeV-madgraph --proc 402 --med 500 --dm 400 --glu 1 --gld 0 --runcms runcmsgrid_LO.sh

#403 -> fermionDarkPortal dirac
./install.py --carddir Cards/fPort_Dir_LO_lu1_Mphi_Mchi_13TeV-madgraph --proc 403 --med 500 --dm 400 --glu 1 --gld 0 --runcms runcmsgrid_LO.sh

#404 -> fermionDarkPortal Majora
./install.py --carddir Cards/fPort_Maj_LO_ld1_Mphi_Mchi_13TeV-madgraph --proc 404 --med 500 --dm 400 --glu 1 --gld 0 --runcms runcmsgrid_LO.sh
./install.py --carddir Cards/fPort_Maj_LO_ld1_Mphi_Mchi_13TeV-madgraph --proc 404 --med 500 --dm 400 --glu 0.5 --gld 0 --runcms runcmsgrid_LO.sh
./install.py --carddir Cards/fPort_Maj_LO_ld1_Mphi_Mchi_13TeV-madgraph --proc 404 --med 500 --dm 400 --glu 0 --gld 1 --runcms runcmsgrid_LO.sh

#405 -> darkHiggs Mono-hs
./install.py --carddir Cards/darkHiggs_Monohs_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --proc 405 --gq 0.25 --gdm 1.001 --hdm 50 --med 2000 --dm 100 --runcms runcmsgrid_LO.sh 

#406 -> darkHiggs Mono-Z'
./install.py --carddir Cards/darkHiggs_MonoZp_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --proc 406 --gq 0.25 --gdm 1.001 --hdm 150 --med 2000 --dm 50 --runcms runcmsgrid_LO.sh

#407 -> Non Thermal Dark Matter
./install.py --carddir Cards/NonthDM_MonoJet_Mx_l1_l2_13TeV-madgraph --proc 407 --glam1 0.25 --glam2 1.001 --med 2000 -runcms runcmsgrid_LO.sh 
