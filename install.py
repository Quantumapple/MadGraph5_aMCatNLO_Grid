#! /usr/bin/env python
import commands,sys,os,subprocess,stat,math,pwd
import datetime
import time 
from os import listdir
from os.path import isfile, join
from optparse import OptionParser
import argparse
import random

#eos='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'
#MGrelease="2_5_2"
MGrelease="2_5_1"
#MGrelease="2_4_3"

def completed(name,medrange,dmrange,basedir,carddir):
    completed = True
    for med in medrange:
        for dm in dmrange:
            if med < dm: 
                continue
            fileExists=os.path.isfile('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/process/run.sh' % (basedir,name,name,med,dm)) 
            if fileExists:
                madgraph='%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/mgbasedir' % (basedir,name,name,med,dm)
                process ='%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/process'   % (basedir,name,name,med,dm)
                runcms  ='%s/runcmsgrid.sh'                           % (basedir)
                output  ='%s_%s_%s_tarball.tar.xz'                    % (name,med,dm)
                os.system('XZ_OPT="--lzma2=preset=9,dict=512MiB" tar -cJpsf '+output+' '+madgraph+' '+process+' '+runcms)
            else:
                if not os.path.isfile('MG_%s_%s_%s.tgz' % (name,med,dm)):
                    completed = False
    return completed

def replace(name,med,dm,gdm,gq,proc,rand,directory):
    print "proc = ", proc
    #Avoid restrict cards
    if gq == 1:
        gq=9.999999e-1
    if gdm == 1:
        gdm=9.999999e-1
    if dm==1:
        dm=9.999999e-1
    gqS=gq
    gqP=gq
    gdmS=gdm
    gdmP=gdm
    gqV=gq
    gqA=gq
    #Diagonals for monotop (set it to 0 for now)
    gqVii=0
    gqAii=0
    gdmV=gdm
    gdmA=gdm
    gSw=gq*(80.19)*math.sqrt(3.1419265/132.5/0.233)
    gPw=gq*(80.19)*math.sqrt(3.1419265/132.5/0.233)
    gSb=gq*(80.19)*math.sqrt(3.1419265/132.5/(1-0.233))
    gPb=gq*(80.19)*math.sqrt(3.1419265/132.5/(1-0.233))
    gSinTheta=gq
    gH=1

    if proc > 800 and proc < 807:
        print "!!!!!!!!!!!!!!!!",gdm,med,dm,gq,gdmS,gdmP
        
    if proc == 805:
        gqP=0#1e-99
        gdmP=0#1e-99
        gqV=0
        gqA=0
        gdmV=0
        gdmA=0
        gPw=0
        gPb=0
    elif proc == 806:
        gqS=0#1e-99
        gdmS=0#1e-99
        gqV=0
        gqA=0
        gdmV=0
        gdmA=0
        gSw=0
        gSb=0
        gSinTheta=0
    elif proc == 801:
        gqS=0
        gdmS=0
        gqP=0
        gdmP=0
        gqV=1e-99
        gdmV=1e-99
        gSw=0
        gSb=0
        gPw=0
        gPb=0
        gSinTheta=0
    else: # turn off all unrelated parameter for non-DMSimp
        gqS=0
        gdmS=0
        gqP=0
        gdmP=0
        gqA=1e-99
        gdmA=1e-99
        gSw=0
        gSb=0
        gPw=0
        gPb=0
        gSinTheta=0
        
    if proc > 800 and proc < 807: #DMsimp
        print "!!!!!!!!!!!!!!!!",gdm,med,dm,gq,gdmS,gdmP
    elif proc == 400: #pseudoscalar dark photon
        print 'Process code : %s ; med = %s ; dm = %s' %(proc,med,dm)
    elif proc == 401: #iDM dark photon
        hdm = 50
        print 'Process code : %s ; med = %s ; dm = %s ; hdm = %s' %(proc,med,dm,hdm)
    elif proc > 401 and proc < 405: #Fermion portal
        lu=gdm
        ld=gq
        ls=0
        lc=0
        lt=0
        lb=0
        print 'Process code : %s ; med = %s ; dm = %s ; lu = %s ; ld = %s ; ls = %s ; lc = %s ; lt = %s ; lb = %s' %(proc,med,dm,lu,ld,ls,lc,lt,lb)
    elif proc == 405 or proc == 406: #dark Higgs
        hdm = 50
        theta = 0.01
        print 'Process code : %s ; med = %s ; dm = %s ; hdm = %s' %(proc,med,dm,hdm)
    elif proc == 407: #non-thermal dark matter
        hdm = 8000
        lam1 = gdm
        lam2 = gq
        print 'Process code : %s ; med = %s ; dm = %s ; hdm = %s ; lam1 = %s ; lam2 = %s' %(proc,med,dm,hdm,lam1,lam2)

    parameterfiles = [ f for f in listdir(directory) if isfile(join(directory,f)) ]    
    for f in parameterfiles:
         with open('%s/%s_tmp' % (directory,f),"wt") as fout: 
            with open(directory+'/'+f        ,"rt") as fin: 
                for line in fin:
                    if proc > 800 and proc < 807: #DMSImp
                        tmpline =    line.replace('X_MMED_X' ,str(med))
                        tmpline = tmpline.replace('X_MMED2_X',str(max(med,400.)))
                        tmpline = tmpline.replace('X_MDM_X' ,str(float(dm)))
                        tmpline = tmpline.replace('X_gS_X'  ,str(gqS))
                        tmpline = tmpline.replace('X_gP_X'  ,str(gqP))
                        tmpline = tmpline.replace('X_gDMS_X',str(gdmS))
                        tmpline = tmpline.replace('X_gDMP_X',str(gdmP))
                        tmpline = tmpline.replace('X_gV_X'  ,str(gqV))
                        tmpline = tmpline.replace('X_gA_X'  ,str(gqA))
                        tmpline = tmpline.replace('X_gVii_X',str(gqVii))
                        tmpline = tmpline.replace('X_gAii_X',str(gqAii))
                        tmpline = tmpline.replace('X_gDMV_X',str(gdmV))
                        tmpline = tmpline.replace('X_gDMA_X',str(gdmA))
                        tmpline = tmpline.replace('X_gSw_X' ,str(gSw))
                        tmpline = tmpline.replace('X_gPw_X' ,str(gPw))
                        tmpline = tmpline.replace('X_gSb_X' ,str(gSb))
                        tmpline = tmpline.replace('X_gPb_X' ,str(gPb))
                        tmpline = tmpline.replace('X_gDMA_X',str(gdmA))
                        tmpline = tmpline.replace('X_sintheta_X',str(gSinTheta))
                        tmpline = tmpline.replace('X_gH_X',str(gH))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC'    ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 400: #psdcalar_darkphoton
                        tmpline =    line.replace('X_MZP_X'  , str(dm))
                        tmpline = tmpline.replace('X_MPS_X'   , str(med))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 401: #iDM
                        tmpline =    line.replace('X_MZDINPUT_X'  , str(med))
                        tmpline = tmpline.replace('X_DMCHI_X'  , str(hdm))
                        tmpline = tmpline.replace('X_MCHI_X'   , str(dm))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XHS'     ,str(hdm))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 402: #Fermion_Portal_Complex
                        tmpline =    line.replace('X_COMPLEX_X'  , str(med))
                        tmpline = tmpline.replace('X_MDM_X'   , str(dm))
                        tmpline = tmpline.replace('X_LU_X'   , str(lu))
                        tmpline = tmpline.replace('X_LD_X'   , str(ld))
                        tmpline = tmpline.replace('X_LS_X'   , str(ls))
                        tmpline = tmpline.replace('X_LC_X'   , str(lc))
                        tmpline = tmpline.replace('X_LT_X'   , str(lt))
                        tmpline = tmpline.replace('X_LB_X'   , str(lb))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 403: #Fermion_Portal_Dirac
                        tmpline =    line.replace('X_DIRAC_X'  , str(med))
                        tmpline = tmpline.replace('X_MDM_X'   , str(dm))
                        tmpline = tmpline.replace('X_LU_X'   , str(lu))
                        tmpline = tmpline.replace('X_LD_X'   , str(ld))
                        tmpline = tmpline.replace('X_LS_X'   , str(ls))
                        tmpline = tmpline.replace('X_LC_X'   , str(lc))
                        tmpline = tmpline.replace('X_LT_X'   , str(lt))
                        tmpline = tmpline.replace('X_LB_X'   , str(lb))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 404: #Fermion_Portal_Majorana
                        tmpline =    line.replace('X_MAJORANA_X'  , str(med))
                        tmpline = tmpline.replace('X_MDM_X'   , str(dm))
                        tmpline = tmpline.replace('X_LU_X'   , str(lu))
                        tmpline = tmpline.replace('X_LD_X'   , str(ld))
                        tmpline = tmpline.replace('X_LS_X'   , str(ls))
                        tmpline = tmpline.replace('X_LC_X'   , str(lc))
                        tmpline = tmpline.replace('X_LT_X'   , str(lt))
                        tmpline = tmpline.replace('X_LB_X'   , str(lb))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                        tmpline = tmpline.replace('RAND'    ,str(rand))
                    elif proc == 405 or proc == 406: #dark Higgs 
                        tmpline = line.replace('X_gQ_X'   , str(gq))
                        tmpline = tmpline.replace('X_gX_X'   , str(gdm))
                        tmpline = tmpline.replace('X_tH_X'   , str(theta))
                        tmpline = tmpline.replace('X_MZP_X'  , str(med))
                        tmpline = tmpline.replace('X_MHS_X'  , str(hdm))
                        tmpline = tmpline.replace('X_MX_X'   , str(dm))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XHS'     ,str(hdm))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                    elif proc == 407: #non-thermal dark matter
                        tmpline = line.replace('X_LAM1_X'   , str(lam1))
                        tmpline = tmpline.replace('X_LAM2_X'   , str(lam2))
                        tmpline = tmpline.replace('X_MX1_X'  , str(med))
                        tmpline = tmpline.replace('X_MX2_X'  , str(hdm))
                        tmpline = tmpline.replace('X_MDM_X'   , str(dm))
                        tmpline = tmpline.replace('MED'     ,str(med))
                        tmpline = tmpline.replace('XHS'     ,str(hdm))
                        tmpline = tmpline.replace('XMASS'   ,str(dm))
                        tmpline = tmpline.replace('PROC' ,str(proc))
                    
                    fout.write(tmpline)
         os.system('mv %s/%s_tmp %s/%s'%(directory,f,directory,f))
 
def fileExists(user,filename):
   sc=None
   #print '%s ls eos/cms/store/user/%s/gridpack/%s | wc -l' %(eos,user,filename)
   exists = commands.getoutput('ls /eos/user/%s/%s/gridpacks/%s | wc -l' %(user[0],user,filename)  )
   if len(exists.splitlines()) > 1: 
      exists = exists.splitlines()[1]
   else:
      exists = exists.splitlines()[0]
   #print exists
   return int(exists) == 1

def loadRestrict(iFile,proc):
    #print iFile
    inputfile =  open(iFile)
    pairs=[]
    for line in inputfile:
        if line.find("#") > -1:
            continue
        tmpline=line.replace("\n","").replace(" ","").replace("\t","")
        lX = tmpline.split(":")[0] 
        if lX=='null':
            lX=0
        lY = tmpline.split(":")[1].split(",")
        for pY in lY:
            pairs.append([int(pY),int(lX)])
    return pairs
 
def checkRestrict(iRestrict,iMMED,iMDM):
    for pair in iRestrict:
        if pair[0] == 0:
            if iMDM == pair[1]:
                return True
        elif iMMED == pair[0] and iMDM == pair[1]:
            return True
    return False

aparser = argparse.ArgumentParser(description='Process benchmarks.')
aparser.add_argument('-carddir','--carddir'   ,action='store',dest='carddir',default=''   ,help='carddir')
aparser.add_argument('-q'      ,'--queue'      ,action='store',dest='queue'  ,default='2nw'                   ,help='queue')
aparser.add_argument('-dm'      ,'--dmrange'   ,dest='dmrange' ,nargs='+',type=int,default=[0],help='mass range')
aparser.add_argument('-med'     ,'--medrange'  ,dest='medrange',nargs='+',type=int,default=[],help='mediator range')
aparser.add_argument('-proc'    ,'--proc'      ,dest='procrange',nargs='+',type=int,     default=[],help='proc')
aparser.add_argument('-gq'      ,'--gq'        ,dest='gq',nargs='+',type=float,      default=[1.0],help='gq')
aparser.add_argument('-gdm'     ,'--gdm'       ,dest='gdm',nargs='+',type=float,     default=[1.0],help='gdm')
aparser.add_argument('-resubmit','--resubmit'  ,type=bool      ,dest='resubmit',default=False,help='resubmit')
aparser.add_argument('-install' ,'--install'   ,type=bool      ,dest='install' ,default=True ,help='install MG')
aparser.add_argument('-runcms'  ,'--runcms'    ,action='store' ,dest='runcms'  ,default='runcmsgrid_NLO.sh',help='runcms')
aparser.add_argument('-release' ,'--release'    ,action='store' ,dest='release'  ,default='2_6_0',help='MG version')
#Reserve for fermion Portal
aparser.add_argument('-glu'      ,'--glu'        ,dest='glu',nargs='+',type=float,      default=[1.0],help='glu')
aparser.add_argument('-gld'     ,'--gld'       ,dest='gld',nargs='+',type=float,     default=[0.0],help='gld')
#Reserve for iDM dark Photon and dark Higgs
aparser.add_argument('-hdm' ,'--hdmrange' ,dest='hdmrange' ,nargs='+',type=int,default=[50],help='dark higgs mass range')
#Reserve for Nonthermal dark matter 
aparser.add_argument('-glam1'      ,'--glam1'        ,dest='glam1',nargs='+',type=float,      default=[1.0],help='glam1')
aparser.add_argument('-glam2'     ,'--glam2'       ,dest='glam2',nargs='+',type=float,     default=[1.0],help='glam2')

args1 = aparser.parse_args()
MGrelease=args1.release

user=pwd.getpwuid( os.getuid() ).pw_name
basedir=os.getcwd()
os.system('rm %s/%s/*~' % (basedir,args1.carddir))

##Get the base files
parameterdir   = [ f for f in listdir(basedir+'/'+args1.carddir) if not isfile(join(basedir+'/'+args1.carddir,f)) ]
parameterfiles = [ f for f in listdir(basedir+'/'+args1.carddir) if     isfile(join(basedir+'/'+args1.carddir,f)) ]
#print parameterfiles,' -',basedir+'/'+args1.carddir,parameterdir,parameterfiles

mgcf = [f for f in parameterfiles if f.find('madconfig') > -1]
proc = [f for f in parameterfiles if f.find('proc')      > -1]
cust = [f for f in parameterfiles if f.find('custom')    > -1]
spin = [f for f in parameterfiles if f.find('madspin')   > -1]
rwgt = [f for f in parameterfiles if f.find('reweight')  > -1]
rtct = [f for f in parameterfiles if f.find('mass')      > -1]

testproc = args1.procrange[0]

#Redundant
#if testproc > 401 and testproc < 405: #Fermion Portal model
#    procnamebase = commands.getoutput('cat %s | grep fPort | awk \'{print $2}\' ' % (basedir+'/'+args1.carddir+'/'+proc[0]))
#else:
procnamebase = commands.getoutput('cat %s | grep output | awk \'{print $2}\' ' % (basedir+'/'+args1.carddir+'/'+proc[0]))

print "Procnamebase =  %s"  % procnamebase

##Start with the basics download Madgraph and add the options we care  :
if not args1.resubmit and args1.install:
    #os.system('rm -rf /tmp/%s/CMSSW_7_1_25_patch5' % user)
    #os.system('rm -rf /tmp/%s/CMSSW_7_1_20' % user)
    #os.system('rm -rf /tmp/%s/CMSSW_9_0_0_pre2' % user)
    os.system('rm -rf /tmp/%s/CMSSW_9_3_0_pre1' % user)
    os.system('rm -rf /tmp/%s/MG5_aMC_v%s'  % (user,MGrelease))
    os.system('cp  patches/install.sh .')
    os.system('./install.sh %s' % args1.release)
    os.system(('mv MG5_aMC_v'+MGrelease+' %s_MG5_aMC_v'+MGrelease) % procnamebase)

os.chdir (('%s_MG5_aMC_v'+MGrelease) % procnamebase)

if not args1.resubmit and args1.install:
    os.system("cp "+basedir+"/"+args1.carddir+"/%s ." % mgcf[0])
    #os.system("cp /afs/cern.ch/work/b/bmaier/public/xMadGraph243/lhe_parser.py ./madgraph/various/")
    #os.system("cp /afs/cern.ch/user/p/pharris/pharris/public/amcatnlo_run_interface.py ./madgraph/interface/amcatnlo_run_interface.py")
    os.system("./bin/mg5_aMC %s" % mgcf[0])

##Now build the directories iterating over options

random.seed(1)
#This is expected not to pass
for f in parameterdir:
    if f.find('model') == -1:
        continue
    os.system('echo cp -r %s/%s/%s models/%s' % (basedir,args1.carddir,f,f))
    os.system('cp -r %s/%s/%s models/%s' % (basedir,args1.carddir,f,f))
    os.chdir('models/%s' % (f))
    os.system('python write_param_card.py')
    os.system('cp param_card.dat restrict_test.dat')
    os.chdir(('%s/%s_MG5_aMC_v'+MGrelease) % (basedir,procnamebase))

restrict = loadRestrict(basedir+"/"+args1.carddir+"/"+rtct[0],testproc)

print "****************************************************"
print "Model : %s" %parameterdir[0]
print "****************************************************"

#Loop
for med    in args1.medrange:
    for dm in args1.dmrange:
        #print 'restrict= %s ; med = %s ; dm = %s' %(restrict,med,dm)
        if not checkRestrict(restrict,med,dm):
            print "Restricted phase space, abort!"
            continue
        tmpMed = med
        tmpDM  = dm 
        if med == 2*dm: #avoid generator instability
            tmpDM = dm-10
        for pProc in args1.procrange:
            rand=random.randrange(1000,9999,1)
            procname=procnamebase.replace("PROC",str(pProc)).replace("MED",str(tmpMed)).replace("XMASS",str(tmpDM))
            if not args1.resubmit:
                for f in parameterdir:
                    os.system('cp -r %s/%s/%s models/%s_%s_%s_%s' % (basedir,args1.carddir,f,f,tmpMed,tmpDM,pProc))
                    os.system('echo cp -r %s/%s/%s models/%s_%s_%s' % (basedir,args1.carddir,f,f,tmpMed,tmpDM))
                    #overriding gdm,gq
                    if pProc > 401 and pProc < 405:
                        print "Coupling choice set at glu = %s ; gld = %s" %(args1.glu[0],args1.gld[0])
                        replace(procnamebase,tmpMed,tmpDM,args1.glu[0],args1.gld[0],pProc,rand,'models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))
                    elif pProc == 407:
                        print "Coupling choice set at glam1 = %s ; glam2 = %s" %(args1.glam1[0],args1.glam2[0])
                        replace(procnamebase,tmpMed,tmpDM,args1.glam1[0],args1.glam2[0],pProc,rand,'models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))
                    else:
                        print "Coupling choice set at gdm = %s ; gq = %s" %(args1.gdm[0],args1.gq[0])
                        replace(procnamebase,tmpMed,tmpDM,args1.gdm[0],args1.gq[0],pProc,rand,'models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))


                    os.chdir('models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))
                    
                    os.system('python write_param_card.py')
                    os.system('cp param_card.dat restrict_test.dat')
                    os.chdir(('%s/%s_MG5_aMC_v'+MGrelease) % (basedir,procnamebase))
                    os.system('mkdir MG_%s' % (procname))
                
                for f in parameterfiles:
                    with open('MG_%s/%s' % (procname,f), "wt") as fout: 
                        with open(basedir+'/'+args1.carddir+'/'+f        ,"rt") as fin: 
                            for line in fin:
                                tmpline =    line.replace('MED'  ,str(tmpMed))
                                tmpline = tmpline.replace('XMASS',str(tmpDM))
                                if pProc == 401 or pProc == 405 or pProc == 406:
                                    tmpline = tmpline.replace('XHS' ,str(args1.hdmrange[0]))
                                tmpline = tmpline.replace('PROC' ,str(pProc))
                                tmpline = tmpline.replace('RAND' ,str(random.randrange(1000,9999,1)))
                                fout.write(tmpline)
            
                job_file = open(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (basedir,procnamebase,procname), "wt")
                job_file.write('#!/bin/bash\n')
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/  .     \n') % (basedir,procnamebase,procname))
                job_file.write('export SCRAM_ARCH=slc6_amd64_gcc530 \n')
                #job_file.write('export SCRAM_ARCH=slc6_amd64_gcc481 \n')
                #job_file.write('cd /afs/cern.ch/user/p/pharris/pharris/public/bacon/prod/CMSSW_7_1_20/src \n')
                #job_file.write('scramv1 project CMSSW CMSSW_7_1_25_patch5 \n')
                #job_file.write('cd CMSSW_7_1_25_patch5/src \n')
                #job_file.write('scramv1 project CMSSW CMSSW_7_1_20 \n')
                #job_file.write('cd CMSSW_7_1_20/src \n')
                job_file.write('scramv1 project CMSSW CMSSW_9_3_0_pre1 \n')
                job_file.write('cd CMSSW_9_3_0_pre1/src \n')
                job_file.write('eval `scramv1 runtime -sh` \n')
                job_file.write('LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml \n')
                job_file.write('if [ -e $LHAPDF6TOOLFILE ]; then \n')
                job_file.write('  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\\"LHAPDF6_BASE\\"" | cut -d \\" -f 4`/bin/lhapdf-config \n')
                job_file.write('else \n')
                job_file.write('  LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"` \n')
                job_file.write('fi \n')
                job_file.write('export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir` \n')
                job_file.write('LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir` \n')
                job_file.write('LHAPDFLIBS=`$LHAPDFCONFIG --libdir` \n')
                job_file.write('cd - \n')
                job_file.write('cd MG_%s/                       \n' % (procname) )
                job_file.write(('%s/%s_MG5_aMC_v'+MGrelease+'/bin/mg5_aMC  %s  \n') % (basedir,procnamebase,proc[0]) )
                if len(cust) > 0:
                    job_file.write('cp %s %s/                   \n' % (cust[0],procname))
                if args1.runcms.find("NLO") > -1:
                    job_file.write('mv %s process  \n' % (procname))
                    job_file.write('cd process     \n' )
                else:
                    job_file.write('cd  %s                      \n' % (procname) )
                pReweight=False
                for f in parameterfiles:
                    if f.find('dat') > -1:
                        job_file.write('mv ../%s Cards \n' % f)
                    if f.find('.f')  > -1:
                        job_file.write('mv ../%s SubProcesses \n' % f)
                    if f.find('reweight') > -1:
                        job_file.write('cp Cards/%s . \n' % f)
                        pReweight=True
                if args1.runcms.find("NLO") > -1:
                    job_file.write('echo "shower=OFF" > makegrid.dat  \n')
                    #if pReweight:
                    #    job_file.write('echo "reweight=OFF" >> makegrid.dat  \n')
                job_file.write('echo "done"              >>  makegrid.dat  \n')
                if len(cust) > 0:
                    job_file.write('cat %s >> makegrid.dat \n' % (cust[0]))
                if args1.runcms.find("NLO") == -1:
                    job_file.write('echo "set gridpack true" >> makegrid.dat \n')
                job_file.write('echo "" >> makegrid.dat \n')
                job_file.write('echo "done">> makegrid.dat  \n')
                if args1.runcms.find("NLO") > -1:
                    job_file.write('cat makegrid.dat | ./bin/generate_events -n pilotrun \n')
                else:
                    job_file.write('cat makegrid.dat | ./bin/generate_events pilotrun \n')
                job_file.write('cd ..      \n')
                if args1.runcms.find("NLO") > -1:
                    job_file.write('echo "mg5_path = ../mgbasedir"  >> process/Cards/amcatnlo_configuration.txt \n')
                    job_file.write('echo "cluster_temp_path = None" >> process/Cards/amcatnlo_configuration.txt \n')  
                    job_file.write('cd process  \n')
                else:
                    job_file.write('mkdir process \n')
                    job_file.write('mv %s/pilotrun_gridpack.tar.gz                 process  \n' % (procname))
                    job_file.write('mv %s/Events/pilotrun/unweighted_events.lhe.gz process  \n' % (procname))
                    job_file.write('cd process  \n')
                    job_file.write('tar xzf pilotrun_gridpack.tar.gz  \n')
                    job_file.write('rm pilotrun_gridpack.tar.gz  \n')
                    job_file.write('echo "mg5_path = ../../mgbasedir" >> ./madevent/Cards/me5_configuration.txt \n')
                    job_file.write('echo "run_mode = 0" >> ./madevent/Cards/me5_configuration.txt \n')  
                    if len(spin) > 0: 
                        job_file.write('echo "import unweighted_events.lhe.gz"          >  madspinrun.dat \n')
                        job_file.write('cat %s                                          >> madspinrun.dat \n' % spin[0])
                        job_file.write('cat madspinrun.dat | MadSpin/madspin \n')
                        job_file.write('rm madspinrun.dat \n')
                        job_file.write('rm unweighted_events.lhe.gz \n')
                        job_file.write('rm -rf tmp* \n')
                        job_file.write('cp %s/%s/%s process/madspin_card.dat \n' % (basedir,args1.carddir,spin[0]))
                    if pReweight > 0: 
                        job_file.write('mkdir -p madevent/Events/pilotrun \n')
                        job_file.write('cp unweighted_events.lhe.gz madevent/Events/pilotrun \n')
                        #if args1.runcms.find("NLO") > -1:
                        #    job_file.write('echo "f2py_compiler=" `which gfortran` >> ./madevent/Cards/me5_configuration.txt \n')
                        job_file.write('export LIBRARY_PATH=$LD_LIBRARY_PATH \n')
                        job_file.write('cd madevent;./bin/madevent reweight pilotrun;cd .. \n')
                                   
                job_file.write('cd .. \n')
                job_file.write('cp    %s/cleangridmore.sh .      \n'  % (basedir))
                job_file.write('cp    %s/%s               runcmsgrid.sh      \n'  % (basedir,args1.runcms))
                job_file.write('./cleangridmore.sh               \n')
                job_file.write('mkdir  mgbasedir     \n')
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/MadSpin  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/SysCalc  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/input    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/HELAS    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/HEPTools mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/README   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/Template mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/VERSION  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/aloha    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/bin      mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/madconfig  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/madgraph   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/mg5decay   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/models     mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/tests      mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/vendor     mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/PLUGINS    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/PLUGIN     mgbasedir \n') % (basedir,procnamebase))
                output  ='%s_tarball.tar.xz'                    % (procname)
                job_file.write('XZ_OPT="--lzma2=preset=9,dict=512MiB" tar -cJpsf '+output+' mgbasedir process runcmsgrid.sh \n')
                #job_file.write(('cp -r %s  %s/%s_MG5_aMC_v'+MGrelease+'/         \n') % (output,basedir,procnamebase))

                job_file.write(('mkdir -p /eos/user/%s/%s/gridpacks \n') % (user[0],user))
                job_file.write(('rm  /eos/user/%s/%s/gridpacks/%s  \n') % (user[0],user,output))
                job_file.write(('cp %s   /eos/user/%s/%s/gridpacks/%s  \n') % (output,user[0],user,output))
                job_file.close()
                os.chmod(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')             % (basedir,procnamebase,procname),0777)
                print '%s' %basedir
                print '%s' %procnamebase
                print '%s' %procname
            if os.path.isfile(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')        % (basedir,procnamebase,procname)):
                #print "Looking",('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')      % (basedir,procnamebase,procname)
                #print "Loooking More",('%s/%s_MG5_aMC_v'+MGrelease+'/%s_tarball.tar.xz') % (basedir,procnamebase,procname)
                #if not os.path.isfile(('%s/%s_MG5_aMC_v'+MGrelease+'/%s_tarball.tar.xz') % (basedir,procnamebase,procname)):
                output     ='%s_tarball.tar.xz'                    % (procname)
                if not fileExists(user,output):
                    os.system(('echo bsub -q  %s -R "rusage[mem=12000]" %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (args1.queue,basedir,procnamebase,procname))
                    os.system(('bsub -q  %s -R "rusage[mem=12000]" %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (args1.queue,basedir,procnamebase,procname))

print "Gridpack will be generated here once the job is finished :"
print "/eos/user/%s/%s/gridpacks/%s" % (user[0],user,output)
           
#while not completed(args1.name,args1.medrange,args1.dmrange,basedir,args1.carddir):
#    print "Waiting ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#    time.sleep(60)
