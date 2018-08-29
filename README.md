# MadGraph5_aMCatNLO_Grid@DM-LPC

Clone the repo in lxplus@CERN in a clean environment.

```
git clone 
```

## Prepare Generation configuration
Generate Gridpack of your favourite processes by placing all necessary ```run_card.dat``` etc in the ```Cards``` folders. 
To generate gridpack, for example, for Monojet process under dark higgs models. Do

```
./install.py --carddir Cards/MonojetDM_LO_MZprime_Mhs_Mchi_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph --gq 0.25 --gdm 1.001 --hdm 90 --med 3000 --dm 100 
```
The text is self-explanatory, the corresponding mass grid is defined as mass_jet.txt in each process ```Cards``` folder. Please refer to
```run.sh``` for more example. The following command resulted in a series of job submission, you may find your gridpack in your EOS space.
