#!/usr/bin/env python
##Spin 1
#2=>gDMV
#3=>gDMA
# 4, 5, 6, 7, 8, 9=>gV
#10,11,12,13,14,15=>gA


def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])

def printsetVA(gDMV,gDMA,gV,gA):
    print 'launch'
    #Vector
    print 'set dminputs 2  %s' % str(gDMV)
    print 'set dminputs 4  %s' % str(gV)
    print 'set dminputs 5  %s' % str(gV)
    print 'set dminputs 6  %s' % str(gV)
    print 'set dminputs 7  %s' % str(gV)
    print 'set dminputs 8  %s' % str(gV)
    print 'set dminputs 9  %s' % str(gV)
    #Axial
    print 'set dminputs 3  %s' % str(gDMA)
    print 'set dminputs 10 %s' % str(gA)
    print 'set dminputs 11 %s' % str(gA)
    print 'set dminputs 12 %s' % str(gA)
    print 'set dminputs 13 %s' % str(gA)
    print 'set dminputs 14 %s' % str(gA)
    print 'set dminputs 15 %s' % str(gA)
    #Width
    print 'set DECAY 55 AUTO'

def printsetSP(gDMS,gDMP,gS,gP):
    print 'launch'
    #Scalar
    print 'set dminputs 3  %s' % str(gDMS)
    print 'set dminputs 5  %s' % str(gS)
    print 'set dminputs 6  %s' % str(gS)
    print 'set dminputs 7  %s' % str(gS)
    print 'set dminputs 8  %s' % str(gS)
    print 'set dminputs 9  %s' % str(gS)
    print 'set dminputs 10 %s' % str(gS)
    #Pseudo
    print 'set dminputs 4  %s' % str(gDMP)
    print 'set dminputs 11 %s' % str(gP)
    print 'set dminputs 12 %s' % str(gP)
    print 'set dminputs 13 %s' % str(gP)
    print 'set dminputs 14 %s' % str(gP)
    print 'set dminputs 15 %s' % str(gP)
    print 'set dminputs 16 %s' % str(gP)
    #Width
    print 'set DECAY 55 AUTO'

def printsetSPSMM(gDMS,gS,gH):
    print 'launch'
    #Scalar
    print 'set dminputs 1  %s' % str(gDMS)
    print 'set dminputs 2  %s' % str(gS)
    print 'set dminputs 3  %s' % str(gH)
    #Width
    print 'set DECAY 55 AUTO'

#print 'change mode NLO'
print 'change rwgt_dir rwgt'

weight_counter = 0

print '#' + str(weight_counter) + ' start of scalar'

#pure vector
for yDM in [0.001,0.005,0.025,0.1,0.2,0.4,0.6,0.8,1.0]:
    for gS in [0.01,0.05,0.1,0.15,0.2,0.3,0.4]:
        for gH in [1]:
            printsetSPSMM(yDM,gS,gH)
            weight_counter += 1

print '#' + str(weight_counter) + ' start of pseudo'
