# This file was automatically created by FeynRules $Revision: 915 $
# Mathematica version: 8.0 for Linux x86 (64-bit) (October 10, 2011)
# Date: Sun 6 Oct 2013 19:56:46


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*lam1*Lam1R12*lam1X1) + complex(0,1)*lam1*Lam1R21*lam1X1',
                 order = {'NP':3})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*lam1*Lam1R13*lam1X1 - complex(0,1)*lam1*Lam1R31*lam1X1',
                 order = {'NP':3})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*lam1*Lam1R23*lam1X1 - complex(0,1)*lam1*Lam1R32*lam1X1',
                 order = {'NP':3})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*lam1*Lam1R12*lam1X2) + complex(0,1)*lam1*Lam1R21*lam1X2',
                 order = {'NP':3})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*lam1*Lam1R13*lam1X2 - complex(0,1)*lam1*Lam1R31*lam1X2',
                 order = {'NP':3})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*lam1*Lam1R23*lam1X2 - complex(0,1)*lam1*Lam1R32*lam1X2',
                 order = {'NP':3})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*lam2*Lam2R1*lam2X1',
                 order = {'NP':3})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*lam2*Lam2R2*lam2X1',
                 order = {'NP':3})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*lam2*Lam2R3*lam2X1',
                 order = {'NP':3})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*lam2*Lam2R1*lam2X2',
                 order = {'NP':3})

GC_21 = Coupling(name = 'GC_21',
                 value = 'complex(0,1)*lam2*Lam2R2*lam2X2',
                 order = {'NP':3})

GC_22 = Coupling(name = 'GC_22',
                 value = 'complex(0,1)*lam2*Lam2R3*lam2X2',
                 order = {'NP':3})

GC_23 = Coupling(name = 'GC_23',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKM11*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKM12*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(CKM21*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM22*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1)*complexconjugate(CKM11))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*complexconjugate(CKM12))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ee*complex(0,1)*complexconjugate(CKM21))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ee*complex(0,1)*complexconjugate(CKM22))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

