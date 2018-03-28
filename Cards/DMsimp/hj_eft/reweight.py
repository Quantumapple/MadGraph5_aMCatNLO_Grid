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

def printsetg(cyr,cyi,cg,cgt,mtp):
    weight_id = 'cyr_%s_cyi_%s_cg_%s_cgt_%s_mtp_%s' % (str(cyr), str(cyi), str(cg), str(cgt),str(mtp))
    print 'launch --rwgt_name=%s' % (weight_id.replace('.','p'))
    #Scalar
    print 'set param_card DIM6  1  %s' % str(cyr)
    print 'set param_card DIM6  2  %s' % str(cyi)
    print 'set param_card DIM6  3  %s' % str(cg)
    print 'set param_card DIM6  4  %s' % str(cgt)
    print 'set param_card mass  6000006 %s' % str(mtp)
    print 'set param_card decay 25 AUTO'
    print 'set param_card decay 6000006 AUTO'

print 'change mode LO'
print 'change helicity False'
print 'change rwgt_dir rwgt'
weight_counter = 0

print '#' + str(weight_counter) + ' start of scalar'

#pure scalar
for mtp in [10000]:
    for cmean in [0.0,0.2,0.4,0.6,0.8,1.0]:
        for cdiff in [-0.3,-0.15,0.0,0.15,0.3]:
            for cyi in [0]:
                for cgt in [0.]:
                    cg=cmean+cdiff/2
                    cyr=cmean-cdiff/2
                    printsetg(cyr,cyi,cg,cgt,mtp)
                    weight_counter += 1

