from pymatgen import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
import os

JINNYAPI = os.environ['materials_project']

a = MPRester(JINNYAPI)

#Entries are the basic unit for thermodynamic and other analyses in pymatgen.
#This gets all entries belonging to the Ca-C-O system.
entries = a.get_entries_in_chemsys(['Ca', 'C', 'O'])

#With entries, you can do many sophisticated analyses, 
#like creating phase diagrams.
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show() 