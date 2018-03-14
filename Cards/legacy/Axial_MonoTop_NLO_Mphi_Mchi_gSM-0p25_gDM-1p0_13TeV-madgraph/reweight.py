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
    print 'set dminputs 16 %s' % str(gV)
    print 'set dminputs 18 %s' % str(gV)
    #Axial
    print 'set dminputs 3  %s' % str(gDMA)
    print 'set dminputs 17 %s' % str(gA)
    print 'set dminputs 19 %s' % str(gA)
    #Width
    print 'set DECAY 55 AUTO'


print 'change mode NLO'
print 'change helicity False'


weight_counter = 0

print '#' + str(weight_counter) + 'scales'
print 'launch'
print 'set run_card mur_over_ref 1.000001'
print 'set run_card muf_over_ref 1.000001'
print 'launch'
print 'set run_card mur_over_ref 2'
print 'launch'
print 'set run_card mur_over_ref 0.5'
print 'launch'
print 'set run_card muf_over_ref 2'
print 'launch'
print 'set run_card muf_over_ref 2'
print 'set run_card mur_over_ref 2'
print 'launch'
print 'set run_card muf_over_ref 2'
print 'set run_card mur_over_ref 0.5'
print 'launch'
print 'set run_card muf_over_ref 0.5'
print 'launch'
print 'set run_card muf_over_ref 0.5'
print 'set run_card mur_over_ref 2'
print 'launch'
print 'set run_card muf_over_ref 0.5'
print 'set run_card mur_over_ref 0.5'


print '#' + str(weight_counter) + ' start of vector'

#pure vector
for gDM in [0.01,0.05,0.1,0.2,0.25,0.3,0.5,0.7,0.9,1.1,1.3,1.6,2.0]:
    for gV in [0.01,0.05,0.1,0.2,0.3,0.5,0.75,1]:
        printsetVA(gDM,0,gV,0)
        weight_counter += 1

print '#' + str(weight_counter) + ' start of axial'

#pure axial
for gDM in [0.01,0.05,0.1,0.2,0.25,0.3,0.5,0.7,0.9,1.0,1.1,1.3,1.6,2.0]:
    for gA in [0.01,0.05,0.1,0.2,0.3,0.5,0.75,1]:
        printsetVA(0,gDM,0,gA)
        weight_counter += 1

print '#' + str(weight_counter) + ' start of vector+axial'

#V+A
for gDM in [0.01,0.05,0.1,0.2,0.25,0.3,0.5,0.7,0.9,1.0,1.1,1.3,1.6,2.0]:
    for gVgA in [0.01,0.05,0.1,0.2,0.3,0.5,0.75,1,2]:
        printsetVA(gDM*0.5,gDM*0.5,gVgA*0.5,gVgA*0.5)
        weight_counter += 1

