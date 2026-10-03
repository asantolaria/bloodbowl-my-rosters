"""Datos de las listas EuroBowl 2026 FINAL. Cada grupo vive en `_final_data_gN.py` (lista TEAMS)."""
import glob
import importlib
import os

TEAMS = []
for _f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_final_data_g*.py"))):
    TEAMS += importlib.import_module(os.path.basename(_f)[:-3]).TEAMS
