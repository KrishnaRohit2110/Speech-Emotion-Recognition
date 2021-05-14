def speechEm():
    import os
    import numpy as np  
    
    addr='D:\OneDrive - Amrita Vishwa Vidyapeetham\Machine Learning\Project\All'
    os.chdir(addr)
    entries = os.listdir(addr)
    
    emotion={0:'male_angry',1:'male_disgust',2:'male_error',3:'male_fear',
                        4:'male_happy',5:'male_neutral',6:'male_sad',7:'male_surprise'}
    '''for i in entries:
        if i[-8:-6]=='_a':
            emotion.append('male_angry')
        elif i[-8:-6]=='_d':
            emotion.append('male_disgust')
        elif i[-8:-6]=='_f':
            emotion.append('male_fear')
        elif i[-8:-6]=='_h':
            emotion.append('male_happy')
        elif i[-8:-6]=='_n':
            emotion.append('male_neutral')
        elif i[-8:-6]=='sa':
            emotion.append('male_sad')
        elif i[-8:-6]=='su':
            emotion.append('male_surprise')
        else:
            emotion.append('male_error') '''
    return emotion,np.array(entries)
