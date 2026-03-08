# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:26:28 2026

@author: trent
"""

from enum import Enum, EnumType

class IterEnum(Enum):
    
    def __iter__(self):
        return iter(self.value)
    
    def __call__(self, item: str|int) -> int|str:
        assert isinstance(item, (str, int)), 'Must call with a str or int!'
        
        if isinstance(item, str):
            return self.value.index(item)
        return self.value[item]
    
    def __getitem__(self, item: str|int):
        assert isinstance(item, (str, int)), 'Must index with a str or int!'
        
        if isinstance(item, str):
            item = self.value.index(item)
        return self.value[item]
    

class FunctionalEnum(Enum):
    
    def __getitem__(self, item: str):
        return getattr(self, item)