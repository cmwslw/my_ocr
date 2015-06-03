import sys
from matplotlib.image import imread
import numpy as np
from scipy.cluster.vq import kmeans, whiten

CHARSIZE = 28

def draw(data):
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            val = data[y,x]
            if val > 0.5:
                c = '0'
            else:
                c = '.'
            print c,
        print ''

phrase = imread(sys.argv[1])
phrase = phrase[:,:,0:2]
phrase = np.mean(phrase, axis=2)
phrase = phrase * -1 + 1
draw(phrase[:,1:28])
phrasetemp = np.zeros((phrase.shape[0]+CHARSIZE, phrase.shape[1]+CHARSIZE))
phrasetemp[CHARSIZE/2:-CHARSIZE/2,CHARSIZE/2:-CHARSIZE/2] = phrase
phrase = phrasetemp
#s = np.sum(phrase, axis=0)
#print phrase
#print phrase.shape
nzy, nzx = np.nonzero(phrase)
nz = np.zeros((nzy.size, 2))
nz[:,0] = nzy
nz[:,1] = nzx
#print nz
#whitened = whiten(nz)
#print whitened
centroids = kmeans(nz, 5)
print centroids

cents = []
for i in range(centroids[0].shape[0]):
    pos = list(centroids[0][i,:])
    pos = [int(round(x)) for x in pos]
    cents.append(pos)

cents = sorted(cents, key=lambda c: c[1])
print cents
for y, x in cents:
    draw(phrase[y-CHARSIZE/2:y+CHARSIZE/2,x-CHARSIZE/2:x+CHARSIZE/2])
