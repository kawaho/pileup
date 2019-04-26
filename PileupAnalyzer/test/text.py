filein = ['crab_DY3v1.py', 'crab_GGH.py', 'crab_TT2h.py', 'crab_W1.py', 'crab_WZ.py', 'crab_ZH.py', 'crab_DY1.py', 'crab_DY4.py', 'crab_STtWat.py', 'crab_TT2l.py', 'crab_W2.py', 'crab_Wext1v2.py', 'crab_ZZ.py', 'crab_DY2ext1v1.py', 'crab_DYext1v1.py', 'crab_STtWt.py', 'crab_TT2s.py', 'crab_W3.py', 'crab_Wm.py', 'crab_DY2v1.py', 'crab_DYv1.py', 'crab_STtat.py', 'crab_VBF.py', 'crab_W4.py', 'crab_Wp.py', 'crab_ttH.py', 'crab_DY3ext1v1.py', 'crab_GG.py', 'crab_STtt.py', 'crab_VBFH.py', 'crab_WW.py', 'crab_Wv2.py']

for fi in filein:
    f = open(fi, 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace('Automatic', 'FileBased')

    f = open(fi, 'w')
    f.write(newdata)
    f.close()
