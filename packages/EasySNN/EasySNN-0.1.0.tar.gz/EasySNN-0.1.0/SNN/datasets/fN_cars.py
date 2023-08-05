from .. import event as ev
from .fEventBase import n_carsBase
import torch
import numpy as np
import time

class NCARS(n_carsBase):
    def __init__(self, 
        root: str, 
        represent:str='timesteps',
        step:int = 100,
        folders_names: list=["oriDownload", "extract", "convert"], 
        download: bool = False, 
        subSet: str = "Train", 
        extention: str = ".npy", 
        transform=None, 
        target_transform=None) -> None:

        self.represent = represent.lower()
        self.step = step
        super().__init__(root, folders_names, download, subSet, extention, transform, target_transform)
        

    def __getitem__(self, index):
        path, target = self.samples[index]
        sample:ev.event = self.loader(path)
        if self.transform:
            sample = self.transform(sample)
        if self.target_transform:
            target = self.target_transform(target)
        if self.represent == 'timesteps':
            img = sample.toTimeStep((2, 100, 120, self.step), 'count')
            img = torch.from_numpy(img)
            target = torch.tensor(target)
        elif self.represent in ['est', 'eventcount', 'eventframe', 'voxgrid']:
            img = sample.toArray('xytp')
        return img, target