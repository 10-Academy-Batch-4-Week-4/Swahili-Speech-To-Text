import librosa
import numpy as np
import pandas as pd
import glob
from pathlib import Path
import unittest
import sys

import warnings
warnings.filterwarnings("ignore")


sys.path.append("../scripts/")

from scripts.channel import channels_check
from scripts.Feature_extraction import mel_scale
from scripts.data_augmentation import time_shift
from scripts.load_text import loading
from scripts.resize import resize_

files = []
for path in Path('./SWH-05-20101106').glob('*.wav'):
    files.append('./SWH-05-20101106/'+path.name)
    
audio, fs = librosa.load(files[0])

#meta_df = pd.read_csv('../metadata.csv')
import unittest

class testSwahlli(unittest.TestCase):

    def Feature_extraction_(self):
        s = mel_scale(audio, 1600)
        assert type(s) == np.ndarray, \
        f"Function should return the value {np.ndarray}, it is returning the value {type(s)}"

    def channel_(self):
        ch = channels_check(files)
        assert {list(ch)} in [[1],[1,2], [2]],\
        f"Function should return the an element of  {[[1],[1,2], [2]]}, it is returning {list(ch)}"

    def data_augimentation_(self):
            sh = time_shift(audio, 1)
            assert len(sh) == (len(audio)), \
            f"Function should return the value {len(audio)}, it is returning the value {len(sh)}"

    # def load_text_(self):
    #     txt = 'rais wa tanzania jakaya mrisho kikwete'
    #     t = loading(text_path)
    #     assert t.iloc[0] == txt, f"Function should return the value {txt}, it is returning the value {t}"

    def resize_(self):
        re = resize_(audio, 100000)
        print('yeah')
        assert len(re) == (100000), \
        f"Function should return the value {100000}, it is returning the value {len(re)}"

if __name__ == '__main__':
    unittest.main()