import numpy as np
import matplotlib.pyplot as plt
import sys
import warnings
import librosa
import Emotions as em
import FeatureExtraction as fe
import Kmeans


warnings.filterwarnings("ignore")
#Taking the supervised audio data and getting the emotion through file names
emotions,entries=em.speechEm() 


'''if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)'''

features=fe.FE(entries)
features=np.array(features)

kmeans = Kmeans.km(features)
centroids = kmeans.cluster_centers_
labels=kmeans.labels_

#print(features,np.array(features).shape)
