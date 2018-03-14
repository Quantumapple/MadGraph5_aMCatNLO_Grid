# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Mon 10 Oct 2016 08:07:13


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_h1 = Decay(name = 'Decay_h1',
                 particle = P.h1,
                 partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*TH1x1**2*yb**2 + 3*mh1**2*TH1x1**2*yb**2)*cmath.sqrt(-4*MB**2*mh1**2 + mh1**4))/(16.*cmath.pi*abs(mh1)**3)',
                                   (P.g,P.g):'0.',
                                   (P.h2,P.h2):'((muS**2*TH1x2**4*TH2x1**2 + 2*muS**2*TH1x1*TH1x2**3*TH2x1*TH2x2 + muS**2*TH1x1**2*TH1x2**2*TH2x2**2 + 12*lam*muS*TH1x1*TH1x2**4*TH2x1*vev + 12*lam*muS*TH1x1**2*TH1x2**3*TH2x2*vev + 4*laS*muS*TH1x2**3*TH2x1**2*TH2x2*vev + 8*laS*muS*TH1x1*TH1x2**2*TH2x1*TH2x2**2*vev + 4*laS*muS*TH1x1**2*TH1x2*TH2x2**3*vev + 36*lam**2*TH1x1**2*TH1x2**4*vev**2 + 24*lam*laS*TH1x1*TH1x2**3*TH2x1*TH2x2*vev**2 + 24*lam*laS*TH1x1**2*TH1x2**2*TH2x2**2*vev**2 + 4*laS**2*TH1x2**2*TH2x1**2*TH2x2**2*vev**2 + 8*laS**2*TH1x1*TH1x2*TH2x1*TH2x2**3*vev**2 + 4*laS**2*TH1x1**2*TH2x2**4*vev**2)*cmath.sqrt(mh1**4 - 4*mh1**2*mh2**2))/(32.*cmath.pi*abs(mh1)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((mh1**2*TH1x1**2*ytau**2 - 4*MTA**2*TH1x1**2*ytau**2)*cmath.sqrt(mh1**4 - 4*mh1**2*MTA**2))/(16.*cmath.pi*abs(mh1)**3)',
                                   (P.t,P.t__tilde__):'((3*mh1**2*TH1x1**2*yt**2 - 12*MT**2*TH1x1**2*yt**2)*cmath.sqrt(mh1**4 - 4*mh1**2*MT**2))/(16.*cmath.pi*abs(mh1)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ee**4*TH1x1**2*vev**2)/(4.*sw**4) + (ee**4*mh1**4*TH1x1**2*vev**2)/(16.*MW**4*sw**4) - (ee**4*mh1**2*TH1x1**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(mh1**4 - 4*mh1**2*MW**2))/(16.*cmath.pi*abs(mh1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((2*mh1**2*TH2x1**2*yS**2 - 8*MXd**2*TH2x1**2*yS**2)*cmath.sqrt(mh1**4 - 4*mh1**2*MXd**2))/(16.*cmath.pi*abs(mh1)**3)',
                                   (P.Z,P.Z):'(((9*ee**4*TH1x1**2*vev**2)/2. + (3*ee**4*mh1**4*TH1x1**2*vev**2)/(8.*MZ**4) - (3*ee**4*mh1**2*TH1x1**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*TH1x1**2*vev**2)/(4.*sw**4) + (cw**4*ee**4*mh1**4*TH1x1**2*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*mh1**2*TH1x1**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*TH1x1**2*vev**2)/sw**2 + (cw**2*ee**4*mh1**4*TH1x1**2*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*mh1**2*TH1x1**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*TH1x1**2*vev**2)/cw**2 + (ee**4*mh1**4*sw**2*TH1x1**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*mh1**2*sw**2*TH1x1**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*TH1x1**2*vev**2)/(4.*cw**4) + (ee**4*mh1**4*sw**4*TH1x1**2*vev**2)/(16.*cw**4*MZ**4) - (ee**4*mh1**2*sw**4*TH1x1**2*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(mh1**4 - 4*mh1**2*MZ**2))/(32.*cmath.pi*abs(mh1)**3)'})

Decay_h2 = Decay(name = 'Decay_h2',
                 particle = P.h2,
                 partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*TH1x2**2*yb**2 + 3*mh2**2*TH1x2**2*yb**2)*cmath.sqrt(-4*MB**2*mh2**2 + mh2**4))/(16.*cmath.pi*abs(mh2)**3)',
                                   (P.g,P.g):'0.',
                                   (P.h1,P.h1):'((muS**2*TH1x1**2*TH1x2**2*TH2x1**2 + 2*muS**2*TH1x1**3*TH1x2*TH2x1*TH2x2 + muS**2*TH1x1**4*TH2x2**2 + 12*lam*muS*TH1x1**3*TH1x2**2*TH2x1*vev + 4*laS*muS*TH1x1*TH1x2**2*TH2x1**3*vev + 12*lam*muS*TH1x1**4*TH1x2*TH2x2*vev + 8*laS*muS*TH1x1**2*TH1x2*TH2x1**2*TH2x2*vev + 4*laS*muS*TH1x1**3*TH2x1*TH2x2**2*vev + 36*lam**2*TH1x1**4*TH1x2**2*vev**2 + 24*lam*laS*TH1x1**2*TH1x2**2*TH2x1**2*vev**2 + 4*laS**2*TH1x2**2*TH2x1**4*vev**2 + 24*lam*laS*TH1x1**3*TH1x2*TH2x1*TH2x2*vev**2 + 8*laS**2*TH1x1*TH1x2*TH2x1**3*TH2x2*vev**2 + 4*laS**2*TH1x1**2*TH2x1**2*TH2x2**2*vev**2)*cmath.sqrt(-4*mh1**2*mh2**2 + mh2**4))/(32.*cmath.pi*abs(mh2)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((mh2**2*TH1x2**2*ytau**2 - 4*MTA**2*TH1x2**2*ytau**2)*cmath.sqrt(mh2**4 - 4*mh2**2*MTA**2))/(16.*cmath.pi*abs(mh2)**3)',
                                   (P.t,P.t__tilde__):'((3*mh2**2*TH1x2**2*yt**2 - 12*MT**2*TH1x2**2*yt**2)*cmath.sqrt(mh2**4 - 4*mh2**2*MT**2))/(16.*cmath.pi*abs(mh2)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ee**4*TH1x2**2*vev**2)/(4.*sw**4) + (ee**4*mh2**4*TH1x2**2*vev**2)/(16.*MW**4*sw**4) - (ee**4*mh2**2*TH1x2**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(mh2**4 - 4*mh2**2*MW**2))/(16.*cmath.pi*abs(mh2)**3)',
                                   (P.Xd,P.Xd__tilde__):'((2*mh2**2*TH2x2**2*yS**2 - 8*MXd**2*TH2x2**2*yS**2)*cmath.sqrt(mh2**4 - 4*mh2**2*MXd**2))/(16.*cmath.pi*abs(mh2)**3)',
                                   (P.Z,P.Z):'(((9*ee**4*TH1x2**2*vev**2)/2. + (3*ee**4*mh2**4*TH1x2**2*vev**2)/(8.*MZ**4) - (3*ee**4*mh2**2*TH1x2**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*TH1x2**2*vev**2)/(4.*sw**4) + (cw**4*ee**4*mh2**4*TH1x2**2*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*mh2**2*TH1x2**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*TH1x2**2*vev**2)/sw**2 + (cw**2*ee**4*mh2**4*TH1x2**2*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*mh2**2*TH1x2**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*TH1x2**2*vev**2)/cw**2 + (ee**4*mh2**4*sw**2*TH1x2**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*mh2**2*sw**2*TH1x2**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*TH1x2**2*vev**2)/(4.*cw**4) + (ee**4*mh2**4*sw**4*TH1x2**2*vev**2)/(16.*cw**4*MZ**4) - (ee**4*mh2**2*sw**4*TH1x2**2*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(mh2**4 - 4*mh2**2*MZ**2))/(32.*cmath.pi*abs(mh2)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

