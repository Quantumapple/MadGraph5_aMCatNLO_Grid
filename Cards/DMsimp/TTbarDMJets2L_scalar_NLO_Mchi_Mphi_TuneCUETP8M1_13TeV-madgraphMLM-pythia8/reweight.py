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
    weight_id = 'gdmv_%s_gdma_%s_gv_%s_ga_%s' % (str(gDMV), str(gDMA), str(gV), str(gA))
    print 'launch --rwgt_name=%s' % (weight_id.replace('.','p'))
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
    weight_id = 'gdms_%s_gdmp_%s_gs_%s_gp_%s' % (str(gDMS), str(gDMP), str(gS), str(gP))
    print 'launch --rwgt_name=%s' % (weight_id.replace('.','p'))
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

print 'change mode NLO'
print 'change helicity False'
#print 'change rwgt_dir rwgt'
weight_counter = 0

print '#' + str(weight_counter) + ' start of scalar'

#pure scalar
#for gDM in [0.1,0.5,1,2.0,3.5]:
#    for gS in [0.1,0.5,1,2.0,3.5]:
for gDM in [1,2.0]:
    for gS in [0.1,0.5,1,2.0,3.5]:
        printsetSP(gDM,0,gS,0)
        weight_counter += 1

#print '#' + str(weight_counter) + ' start of pseudo'

#pure pseudo
#for gDM in [0.1,0.5,1,1.5,2.25,3.5]:
#    for gP in [0.1,0.5,1,1.5,2.25,3.5]:
#        printsetSP(0,gDM,0,gP)
#        weight_counter += 1

#print '#' + str(weight_counter) + ' start of scalar+pseudo'

#P+S
#for gDM in [0.1,0.5,1,1.5,2.25,3.5]:
#    for gSgP in [0.1,0.5,1,1.5,2.25,3.5]:
#        printsetSP(gDM*0.5,gDM*0.5,gSgP*0.5,gSgP*0.5)
#        weight_counter += 1

