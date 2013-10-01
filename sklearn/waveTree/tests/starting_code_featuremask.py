__author__ = 'beau'
__author__ = 'beau'

import pywt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

x = np.random.randint(100,size=16)
print x

# haar = pywt.Wavelet('haar')
# dwt_x = pywt.wavedec(x,haar)
# print dwt_x

import math
c = 1/2.0#math.sqrt(2)/2 #'real' haar
dec_lo, dec_hi, rec_lo, rec_hi = [c, c], [-c, c], [c, c], [c, -c]
filter_bank = [dec_lo, dec_hi, rec_lo, rec_hi]
wl = pywt.Wavelet(name="", filter_bank=filter_bank)

dwt_x = pywt.wavedec(x,wl)

print dwt_x
dwt_x = np.concatenate(dwt_x)
#Left child:  2i
#Right child: 2i+1

class featureMask:
    def __init__(self,n_features=None,mask_arr=None):
        if mask_arr is None:
            self.mask = np.array([0]*n_features)
        else:
            self.mask = mask_arr


        assert ((n_features & (n_features - 1)) == 0) and n_features > 0
        self.selection_count = [0]*n_features


    def update(self,selected_feature_idx):

        assert self.mask[selected_feature_idx]==1 #check if update allowed by mask
        self.selection_count[selected_feature_idx]+=1

        if selected_feature_idx*2+1<len(self.mask):#check for not leaf
            self.mask[selected_feature_idx*2]=1#LC
            self.mask[selected_feature_idx*2+1]=1#RC

    def print_tree(self):
        pass

    def validIdxs(self):
        return np.where(self.mask == 1)[0]

    def pickRandomFeat(self):
        """Selects a random feature, allowed by the current mask"""


fm = featureMask(n_features=32)
print fm.mask
fm.mask[0]=1
print fm.mask
fm.update(0)
fm.update(1)
fm.update(3)
fm.update(7)
fm.update(14)
print fm.mask
print fm.validIdxs()