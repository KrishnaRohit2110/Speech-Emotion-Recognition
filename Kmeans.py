def km(fea):
    #from pandas import DataFrame
    #import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    
    kmeans=KMeans(n_clusters=8).fit(fea)
    
    return kmeans
    

