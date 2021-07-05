import os
from os.path import join
save_dir                    = join(os.getcwd(), 'result')
data_dir = {}
data_dir['CUB']             = './filelists/CUB/' 
data_dir['miniImagenet']    = './filelists/miniImagenet/' 
data_dir['omniglot']        = './filelists/omniglot/' 
data_dir['emnist']          = './filelists/emnist/' 
data_dir['plant']           = './filelists/plant/'
