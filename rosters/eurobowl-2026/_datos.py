"""Datos de las listas EuroBowl 2026. Cada grupo vive en `_datos_gN.py` (lista TEAMS)."""
import glob
import importlib
import os

TEAMS = []
for _f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_datos_g*.py"))):
    TEAMS += importlib.import_module(os.path.basename(_f)[:-3]).TEAMS
