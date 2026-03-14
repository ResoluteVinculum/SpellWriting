#
from os.path import abspath, dirname, join
from pathlib import Path

from SpellWriting.spell import SpellData


SpellData_5e = SpellData.from_yaml(
    join(dirname(abspath(__file__)),
         'fifth_edition.yaml'))

Library = {file.stem: SpellData_5e.yaml_spell(file)
           for file in (Path(__file__).parent / 'library').glob('*.yaml')}