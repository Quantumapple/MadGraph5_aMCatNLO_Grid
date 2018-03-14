# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 11.1.0 for Linux x86 (64-bit) (March 13, 2017)
# Date: Mon 1 May 2017 00:27:54


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_180_51,(0,1,1):C.R2GC_90_61})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_129_26,(2,0,1):C.R2GC_129_27,(0,0,0):C.R2GC_129_26,(0,0,1):C.R2GC_129_27,(4,0,0):C.R2GC_127_22,(4,0,1):C.R2GC_127_23,(3,0,0):C.R2GC_127_22,(3,0,1):C.R2GC_127_23,(8,0,0):C.R2GC_128_24,(8,0,1):C.R2GC_128_25,(7,0,0):C.R2GC_133_32,(7,0,1):C.R2GC_184_56,(6,0,0):C.R2GC_132_31,(6,0,1):C.R2GC_185_57,(5,0,0):C.R2GC_127_22,(5,0,1):C.R2GC_127_23,(1,0,0):C.R2GC_127_22,(1,0,1):C.R2GC_127_23,(11,3,0):C.R2GC_131_29,(11,3,1):C.R2GC_131_30,(10,3,0):C.R2GC_131_29,(10,3,1):C.R2GC_131_30,(9,3,1):C.R2GC_130_28,(2,1,0):C.R2GC_129_26,(2,1,1):C.R2GC_129_27,(0,1,0):C.R2GC_129_26,(0,1,1):C.R2GC_129_27,(6,1,0):C.R2GC_181_52,(6,1,1):C.R2GC_181_53,(4,1,0):C.R2GC_127_22,(4,1,1):C.R2GC_127_23,(3,1,0):C.R2GC_127_22,(3,1,1):C.R2GC_127_23,(8,1,0):C.R2GC_128_24,(8,1,1):C.R2GC_184_56,(7,1,0):C.R2GC_133_32,(7,1,1):C.R2GC_128_25,(5,1,0):C.R2GC_127_22,(5,1,1):C.R2GC_127_23,(1,1,0):C.R2GC_127_22,(1,1,1):C.R2GC_127_23,(0,2,0):C.R2GC_129_26,(0,2,1):C.R2GC_129_27,(2,2,0):C.R2GC_129_26,(2,2,1):C.R2GC_129_27,(5,2,0):C.R2GC_127_22,(5,2,1):C.R2GC_127_23,(1,2,0):C.R2GC_127_22,(1,2,1):C.R2GC_127_23,(7,2,0):C.R2GC_182_54,(7,2,1):C.R2GC_182_55,(4,2,0):C.R2GC_127_22,(4,2,1):C.R2GC_127_23,(3,2,0):C.R2GC_127_22,(3,2,1):C.R2GC_127_23,(8,2,0):C.R2GC_128_24,(8,2,1):C.R2GC_182_55,(6,2,0):C.R2GC_132_31})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_172_42})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_175_45})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,1,0):C.R2GC_170_40,(0,0,0):C.R2GC_177_47,(0,2,0):C.R2GC_173_43})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,2,0):C.R2GC_171_41,(0,0,0):C.R2GC_176_46,(0,1,0):C.R2GC_174_44})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,1,0):C.R2GC_190_59,(0,0,0):C.R2GC_191_60})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_137_35})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_139_36})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_139_36})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_36})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_34})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_135_34})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_34})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_35})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_37})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_109_18,(0,1,0):C.R2GC_168_39})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_109_18,(0,1,0):C.R2GC_168_39})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_109_18,(0,1,0):C.R2GC_168_39})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_17,(0,1,0):C.R2GC_91_62})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_108_17,(0,1,0):C.R2GC_91_62})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_17,(0,1,0):C.R2GC_91_62})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_134_33})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_33})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_165_38,(0,2,0):C.R2GC_165_38,(0,3,0):C.R2GC_134_33,(0,1,0):C.R2GC_134_33})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_33})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_134_33})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_33})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_189_58,(0,2,0):C.R2GC_189_58,(0,1,0):C.R2GC_134_33,(0,3,0):C.R2GC_134_33})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,1):C.R2GC_179_50,(0,1,2):C.R2GC_99_66,(0,1,3):C.R2GC_99_67,(0,2,0):C.R2GC_178_48,(0,2,1):C.R2GC_178_49})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_101_3,(0,0,1):C.R2GC_101_4})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.g, P.g, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_96_63})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_113_21,(0,1,0):C.R2GC_113_21,(0,2,0):C.R2GC_113_21})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_104_9,(0,0,1):C.R2GC_104_10,(0,1,0):C.R2GC_104_9,(0,1,1):C.R2GC_104_10,(0,2,0):C.R2GC_104_9,(0,2,1):C.R2GC_104_10})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_107_15,(0,0,1):C.R2GC_107_16,(0,1,0):C.R2GC_107_15,(0,1,1):C.R2GC_107_16,(0,2,0):C.R2GC_107_15,(0,2,1):C.R2GC_107_16})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,0,1):C.R2GC_102_6,(0,1,0):C.R2GC_102_5,(0,1,1):C.R2GC_102_6,(0,2,0):C.R2GC_102_5,(0,2,1):C.R2GC_102_6})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_106_13,(1,0,1):C.R2GC_106_14,(0,1,0):C.R2GC_105_11,(0,1,1):C.R2GC_105_12,(0,2,0):C.R2GC_105_11,(0,2,1):C.R2GC_105_12,(0,3,0):C.R2GC_105_11,(0,3,1):C.R2GC_105_12})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_7,(0,0,1):C.R2GC_103_8,(0,1,0):C.R2GC_103_7,(0,1,1):C.R2GC_103_8,(0,2,0):C.R2GC_103_7,(0,2,1):C.R2GC_103_8})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,0,1):C.R2GC_100_2})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_97_64})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_98_65})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_112_19,(0,0,0):C.R2GC_112_20})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,0):C.UVGC_180_57,(0,0,3):C.UVGC_180_58,(0,0,4):C.UVGC_180_59,(0,1,1):C.UVGC_115_1,(0,2,2):C.UVGC_116_2})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(2,0,2):C.UVGC_128_9,(2,0,3):C.UVGC_128_8,(0,0,2):C.UVGC_128_9,(0,0,3):C.UVGC_128_8,(4,0,2):C.UVGC_127_6,(4,0,3):C.UVGC_127_7,(3,0,2):C.UVGC_127_6,(3,0,3):C.UVGC_127_7,(8,0,2):C.UVGC_128_8,(8,0,3):C.UVGC_128_9,(7,0,1):C.UVGC_184_70,(7,0,2):C.UVGC_184_71,(7,0,3):C.UVGC_184_72,(7,0,4):C.UVGC_184_73,(7,0,5):C.UVGC_184_74,(6,0,1):C.UVGC_184_70,(6,0,2):C.UVGC_185_75,(6,0,3):C.UVGC_185_76,(6,0,4):C.UVGC_184_73,(6,0,5):C.UVGC_184_74,(5,0,2):C.UVGC_127_6,(5,0,3):C.UVGC_127_7,(1,0,2):C.UVGC_127_6,(1,0,3):C.UVGC_127_7,(11,3,2):C.UVGC_131_12,(11,3,3):C.UVGC_131_13,(10,3,2):C.UVGC_131_12,(10,3,3):C.UVGC_131_13,(9,3,2):C.UVGC_130_10,(9,3,3):C.UVGC_130_11,(2,1,2):C.UVGC_128_9,(2,1,3):C.UVGC_128_8,(0,1,2):C.UVGC_128_9,(0,1,3):C.UVGC_128_8,(6,1,2):C.UVGC_181_60,(6,1,3):C.UVGC_181_61,(6,1,4):C.UVGC_181_62,(6,1,5):C.UVGC_181_63,(4,1,2):C.UVGC_127_6,(4,1,3):C.UVGC_127_7,(3,1,2):C.UVGC_127_6,(3,1,3):C.UVGC_127_7,(8,1,1):C.UVGC_186_77,(8,1,2):C.UVGC_184_71,(8,1,3):C.UVGC_186_78,(8,1,4):C.UVGC_186_79,(8,1,5):C.UVGC_186_80,(7,1,0):C.UVGC_132_14,(7,1,2):C.UVGC_128_8,(7,1,3):C.UVGC_133_15,(5,1,2):C.UVGC_127_6,(5,1,3):C.UVGC_127_7,(1,1,2):C.UVGC_127_6,(1,1,3):C.UVGC_127_7,(0,2,2):C.UVGC_128_9,(0,2,3):C.UVGC_128_8,(2,2,2):C.UVGC_128_9,(2,2,3):C.UVGC_128_8,(5,2,2):C.UVGC_127_6,(5,2,3):C.UVGC_127_7,(1,2,2):C.UVGC_127_6,(1,2,3):C.UVGC_127_7,(7,2,2):C.UVGC_182_64,(7,2,3):C.UVGC_182_65,(7,2,4):C.UVGC_181_62,(7,2,5):C.UVGC_181_63,(4,2,2):C.UVGC_127_6,(4,2,3):C.UVGC_127_7,(3,2,2):C.UVGC_127_6,(3,2,3):C.UVGC_127_7,(8,2,1):C.UVGC_183_66,(8,2,2):C.UVGC_182_64,(8,2,3):C.UVGC_183_67,(8,2,4):C.UVGC_183_68,(8,2,5):C.UVGC_183_69,(6,2,0):C.UVGC_132_14,(6,2,3):C.UVGC_130_10})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_172_41,(0,0,2):C.UVGC_172_42,(0,0,1):C.UVGC_172_43})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_175_46,(0,0,2):C.UVGC_175_47,(0,0,1):C.UVGC_175_48})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,1,0):C.UVGC_170_39,(0,0,0):C.UVGC_177_50,(0,2,0):C.UVGC_173_44})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,2,0):C.UVGC_171_40,(0,0,0):C.UVGC_176_49,(0,1,0):C.UVGC_174_45})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.tp__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2, L.FFS4 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,1,0):C.UVGC_190_84,(0,0,0):C.UVGC_191_85})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,3):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,1):C.UVGC_136_19,(0,1,2):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,3):C.UVGC_188_82})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_139_25,(0,1,0):C.UVGC_120_5,(0,2,0):C.UVGC_120_5})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_25,(0,1,0):C.UVGC_120_5,(0,2,0):C.UVGC_120_5})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_139_25,(0,1,0):C.UVGC_162_31,(0,2,0):C.UVGC_161_30})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_135_17,(0,1,0):C.UVGC_118_4,(0,2,0):C.UVGC_118_4})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_135_17,(0,1,0):C.UVGC_118_4,(0,2,0):C.UVGC_118_4})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_135_17,(0,1,0):C.UVGC_118_4,(0,2,0):C.UVGC_118_4})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,3):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,1):C.UVGC_136_19,(0,1,2):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,3):C.UVGC_136_23,(0,2,0):C.UVGC_136_18,(0,2,1):C.UVGC_136_19,(0,2,2):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,3):C.UVGC_136_23})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,1):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,2):C.UVGC_136_19,(0,1,3):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,1):C.UVGC_136_23,(0,2,0):C.UVGC_136_18,(0,2,2):C.UVGC_136_19,(0,2,3):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,1):C.UVGC_136_23})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,3):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,1):C.UVGC_136_19,(0,1,2):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,3):C.UVGC_164_33,(0,2,0):C.UVGC_136_18,(0,2,1):C.UVGC_136_19,(0,2,2):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,3):C.UVGC_163_32})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,1):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,2):C.UVGC_136_19,(0,1,3):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,1):C.UVGC_136_23,(0,2,0):C.UVGC_136_18,(0,2,2):C.UVGC_136_19,(0,2,3):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,1):C.UVGC_136_23})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,3):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,1):C.UVGC_136_19,(0,1,2):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,3):C.UVGC_136_23,(0,2,0):C.UVGC_136_18,(0,2,1):C.UVGC_136_19,(0,2,2):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,3):C.UVGC_136_23})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,1):C.UVGC_137_24,(0,1,0):C.UVGC_136_18,(0,1,2):C.UVGC_136_19,(0,1,3):C.UVGC_136_20,(0,1,4):C.UVGC_136_21,(0,1,5):C.UVGC_136_22,(0,1,1):C.UVGC_136_23,(0,2,0):C.UVGC_136_18,(0,2,2):C.UVGC_136_19,(0,2,3):C.UVGC_136_20,(0,2,4):C.UVGC_136_21,(0,2,5):C.UVGC_136_22,(0,2,1):C.UVGC_136_23})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,1):C.UVGC_157_27})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,1):C.UVGC_157_27})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,2):C.UVGC_167_36,(0,0,1):C.UVGC_157_27})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,1):C.UVGC_157_27})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,1):C.UVGC_157_27})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_157_26,(0,0,2):C.UVGC_167_36,(0,0,1):C.UVGC_157_27})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_169_38,(0,1,0):C.UVGC_168_37})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_134_16,(0,1,0):C.UVGC_117_3,(0,2,0):C.UVGC_117_3})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_134_16,(0,1,0):C.UVGC_117_3,(0,2,0):C.UVGC_117_3})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_165_34,(0,2,0):C.UVGC_166_35,(0,3,0):C.UVGC_159_28,(0,1,0):C.UVGC_160_29})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_134_16,(0,1,0):C.UVGC_117_3,(0,2,0):C.UVGC_117_3})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_134_16,(0,1,0):C.UVGC_117_3,(0,2,0):C.UVGC_117_3})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_134_16,(0,1,0):C.UVGC_117_3,(0,2,0):C.UVGC_117_3})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.tp__tilde__, P.tp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.UVGC_189_83,(0,2,0):C.UVGC_189_83,(0,1,0):C.UVGC_187_81,(0,3,0):C.UVGC_187_81})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ] ],
                couplings = {(0,0,0):C.UVGC_179_53,(0,0,1):C.UVGC_179_54,(0,0,2):C.UVGC_179_55,(0,0,3):C.UVGC_179_56,(0,1,2):C.UVGC_178_51,(0,1,3):C.UVGC_178_52})

