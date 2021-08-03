import io
import os
import glob

import torch
from torch import tensor
from torch import Tensor
import torchaudio
import numpy as np

from random import randrange

from pathlib import Path
from typing import List, Tuple, Union

import torchaudio.functional as F
import torchaudio.transforms as T

import matplotlib.pyplot as plt
from torch.utils.data import Dataset
from IPython.display import Audio, display
from torchaudio.datasets.utils import (download_url, extract_archive, )

_RELEASE_CONFIGS = {
    "release1": {
        "folder_in_archive": "data/",
        "url": "doit@prince:~/Pictures/10Academy/Week4/cloned/Swahili-Speech-To-Text",
        # "checksum": "30301975fd8c5cac4040c261c0852f57cfa8adbbad2ce78e77e4986957445f27",
    }
}


class Dataloader(Dataset):

    def __init__(
        self,
        root: Union[str, Path],
        url: str = _RELEASE_CONFIGS["release1"]["url"],
        folder_in_archive: str = _RELEASE_CONFIGS["release1"]["folder_in_archive"],
        download: bool = False,
        test: bool = False
    ) -> None:
        self._walker = ''
        self.test = test
        self._parse_filesystem(root, url, folder_in_archive, download)

        n_fft = 1024
        hop_length = 512
        n_mels = 128
        sample_rate = 22050

        self.mel_spectrogram = T.MelSpectrogram(
            sample_rate=sample_rate,
            n_fft=n_fft,
            hop_length=hop_length,
            #center = True,
            #pad_mode = "reflect",
            power=2.0,
            #norm= 'slaney',
            #onesided = True,
            n_mels=n_mels,
        )

        #self.Labels = Path(url+'/'+folder_in_archive).glob('*.wav').split['/'][-1].split('-')[-2]
    def _parse_filesystem(self, root: str, url: str, folder_in_archive: str, download: bool) -> None:
        self._walker = [i for i in Path(root).glob('*.wav')]
        return self._walker

    def _load_item(self, fileid: str):
        waveform, _ = torchaudio.load(fileid)
        waveform = torch.mean(waveform, 0, True)
        # Perform transformation
        spec = self.mel_spectrogram(waveform)
        spec = torchaudio.transforms.AmplitudeToDB()(spec)
        # To be checked..................
        padd = torch.zeros(1,128,128)
        if padd.shape[-1] < spec.shape[-1]:
            indices = torch.arange(0, 128)
            padd = torch.index_select(spec, 2, indices)
        else:
            indices = torch.arange(0, spec.shape[-1])
            padd.index_copy_(2, indices,spec)

        return padd, 1

        return spec, int('1')

    def __getitem__(self, n: int) -> Tuple[Tensor, int, List[int]]:
        fileid = self._walker[n]
        item = self._load_item(fileid)
        return item

    def __len__(self) -> int:
        return len(self._walker)

# dataset_train = Dataloader('data/train/SWH-05-20101106/')
# dataset_test = Dataloader('data/test/SWH-05-20101124/')
# print(f'length of train data: {dataset_train.__len__()}')
# print(f'length of train data: {dataset_test.__len__()}')
# f = dataset_train._walker
# # for i in f:
# #     print(i)
