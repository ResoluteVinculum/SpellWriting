# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:01:51 2026

@author: trent
"""
from dataclasses import dataclass
from typing import Literal

from SpellWriting.attributes import SpellAttributes
from SpellWriting.generation import bases

@dataclass
class SpellData:
    """
    Data container for Spell information
    
    """
    
    name: str = ''
    
    level: Literal[*SpellAttributes.Level] | int = None
    school: Literal[*SpellAttributes.School] | int = None
    damage_type: Literal[*SpellAttributes.DamageType] | int = None
    area_of_effect: Literal[*SpellAttributes.AreaOfEffect] | int = None
    range: Literal[*SpellAttributes.Range] | int = None
    duration: Literal[*SpellAttributes.Duration] | int = None
    concentration: bool = False
    ritual: bool = False
    
    def __str__(self):
        return f'<SpellData: {self.name}>'


class SpellNotation:
    
    