# This file was automatically created by FeynRules $Revision: 915 $
# Mathematica version: 8.0 for Linux x86 (64-bit) (October 10, 2011)
# Date: Sun 6 Oct 2013 19:56:46



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

lam1 = Parameter(name = 'lam1',
                 nature = 'external',
                 type = 'real',
                 value = X_LAM1_X,
                 texname = '\\lambda _1',
                 lhablock = 'NP',
                 lhacode = [ 1 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = X_LAM2_X,
                 texname = '\\lambda _2',
                 lhablock = 'NP',
                 lhacode = [ 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mn = Parameter(name = 'Mn',
               nature = 'external',
               type = 'real',
               value = X_MDM_X,
               texname = '\\text{Mn}',
               lhablock = 'MASS',
               lhacode = [ 5000001 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX1 = Parameter(name = 'MX1',
                nature = 'external',
                type = 'real',
                value = X_MX1_X,
                texname = '\\text{MX1}',
                lhablock = 'MASS',
                lhacode = [ 6000001 ])

MX2 = Parameter(name = 'MX2',
                nature = 'external',
                type = 'real',
                value = X_MX2_X,
                texname = '\\text{MX2}',
                lhablock = 'MASS',
                lhacode = [ 6000002 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WX1 = Parameter(name = 'WX1',
                nature = 'external',
                type = 'real',
                value = 1.79,
                texname = '\\text{WX1}',
                lhablock = 'DECAY',
                lhacode = [ 6000001 ])

WX2 = Parameter(name = 'WX2',
                nature = 'external',
                type = 'real',
                value = 7.16,
                texname = '\\text{WX2}',
                lhablock = 'DECAY',
                lhacode = [ 6000002 ])

CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM11}')

CKM12 = Parameter(name = 'CKM12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.sin(cabi)',
                  texname = '\\text{CKM12}')

CKM21 = Parameter(name = 'CKM21',
                  nature = 'internal',
                  type = 'complex',
                  value = '-cmath.sin(cabi)',
                  texname = '\\text{CKM21}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM22}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_w')

Lam1I11 = Parameter(name = 'Lam1I11',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I11}')

Lam1I12 = Parameter(name = 'Lam1I12',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I12}')

Lam1I13 = Parameter(name = 'Lam1I13',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I13}')

Lam1I21 = Parameter(name = 'Lam1I21',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I21}')

Lam1I22 = Parameter(name = 'Lam1I22',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I22}')

Lam1I23 = Parameter(name = 'Lam1I23',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I23}')

Lam1I31 = Parameter(name = 'Lam1I31',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I31}')

Lam1I32 = Parameter(name = 'Lam1I32',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I32}')

Lam1I33 = Parameter(name = 'Lam1I33',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1I33}')

Lam1R11 = Parameter(name = 'Lam1R11',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R11}')

Lam1R12 = Parameter(name = 'Lam1R12',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{Lam1R12}')

Lam1R13 = Parameter(name = 'Lam1R13',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{Lam1R13}')

Lam1R21 = Parameter(name = 'Lam1R21',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R21}')

Lam1R22 = Parameter(name = 'Lam1R22',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R22}')

Lam1R23 = Parameter(name = 'Lam1R23',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{Lam1R23}')

Lam1R31 = Parameter(name = 'Lam1R31',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R31}')

Lam1R32 = Parameter(name = 'Lam1R32',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R32}')

Lam1R33 = Parameter(name = 'Lam1R33',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Lam1R33}')

lam1X1 = Parameter(name = 'lam1X1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{lam1X1}')

lam1X2 = Parameter(name = 'lam1X2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{lam1X2}')

Lam2R1 = Parameter(name = 'Lam2R1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{Lam2R1}')

Lam2R2 = Parameter(name = 'Lam2R2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{Lam2R2}')

Lam2R3 = Parameter(name = 'Lam2R3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{Lam2R3}')

lam2X1 = Parameter(name = 'lam2X1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{lam2X1}')

lam2X2 = Parameter(name = 'lam2X2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{lam2X2}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

