# MadGraph5_aMCatNLO_Grid

Packages for generating gridpacks.

## Installation

Log into lxplus machine, clone a copy of the package in a clean directory

```
git clone -b cmslpc-branch git@github.com:SiewYan/MadGraph5_aMCatNLO_Grid.git
```

## Produce gridpack

To produce gridpack, do

```
./install.py --carddir Cards/psdcalar_darkphoton_13TeV-madgraph --proc 702 --dm 10 --med 50
```

Examples are show (here)[https://github.com/SiewYan/MadGraph5_aMCatNLO_Grid/blob/cmslpc-branch/submit.sh]

## Ported model

Model description

| Process code| Models | Cards |
| -- | --- | --- |
| 400 | pscalar_darkphoton_UFO | psdcalar_LO_darkphoton_13TeV-madgraph |
| 401 | HAHM_darkphoton_iDM_UFO | iDM_LO_darkphoton_13TeV-madgraph |
| 402 | Fermion_Portal_Complex_UFO | fPort_Comp_LO_lu1_Mphi_Mchi_13TeV-madgraph |
| 403 | Fermion_Portal_Dirac_UFO | fPort_Dir_LO_lu1_Mphi_Mchi_13TeV-madgraph |
| 404 | Fermion_Portal_Majorana_UFO | fPort_Maj_LO_ld1_Mphi_Mchi_13TeV-madgraph |
| 405 | ZpHiggs_UFO | darkHiggs_Monohs_LO_MZprime_Mhs_Mchi_13TeV-madgraph |
| 406 | ZpHiggs_UFO | darkHiggs_MonoZp_LO_MZprime_Mhs_Mchi_13TeV-madgraph |
| 407 | STripletBaryogen_X2N1_UFO | NonthDM_MonoJet_Mx_l1_l2_13TeV-madgraph |

| Models | order | jet-matching | madspin | SysCal | Reweighting |
| --- | --- | --- | --- | --- | --- | 
| pscalar_darkphoton_UFO | LO  | No | No | 1.1.0 | No |  
| HAHM_darkphoton_iDM_UFO | LO  | No | No | 1.1.0 | No | 
| Fermion_Portal_Complex_UFO | LO | No | No | 1.1.0 | No |	
| Fermion_Portal_Dirac_UFO | LO | No | No | 1.1.0 | No | 
| Fermion_Portal_Majorana_UFO | LO | No | No | 1.1.0 | No |	
| ZpHiggs_UFO | LO | No | No | 1.1.0 | No |  
| ZpHiggs_UFO | LO | No | No | 1.1.0 | No |  
| STripletBaryogen_X2N1_UFO | LO | No | No | 1.1.0 | No |
