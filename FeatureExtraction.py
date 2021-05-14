def FE(entries):
    from python_speech_features import mfcc
    import os
    import scipy.io.wavfile as wav
    import numpy as np
    import statistics as st


    features=[]
        
    for i in entries:
        (rate,data) = wav.read(i)
        mf=mfcc(data,rate)
        mf=np.transpose(np.array(mf))
        mf=[st.mean(j) for j in mf]
        #fea=[item for sublist in mf for item in sublist]
        features.append(mf)
    return features