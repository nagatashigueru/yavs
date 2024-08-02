# ----------------------------------------------
# Nombre      :: VaspTools
# Autior      :: Shigueru Nagata
# Descripcion :: Funciones relacionadas a Vasp
# ----------------------------------------------

import os

def VTBasic(VTBPath):

    PathDir = "./" + VTBPath
    
    os.mkdir(PathDir)
    os.chdir(PathDir)
    
    INCAR = open("INCAR","x")
    KPOINTS = open("KPOINTS","x")
    POSCAR = open("POSCAR","x")
    POTCAR = open("POTCAR","x")

    INCAR.close()
    KPOINTS.close()
    POSCAR.close()
    POTCAR.close()

def VTBandsDos(VTBDPath):
    
    PathDir = "./" + VTBDPath
    
    os.mkdir(PathDir)
    os.chdir(PathDir)
    
    INCAR_1 = open("INCAR-1","x")
    KPOINTS_1 = open("KPOINTS-1","x")
    INCAR_2 = open("INCAR-2","x")
    KPOINTS_2 = open("KPOINTS-2","x")
    POSCAR = open("POSCAR","x")
    POTCAR = open("POTCAR","x")

    INCAR_1.close()
    KPOINTS_1.close()
    INCAR_2.close()
    KPOINTS_2.close()
    POSCAR.close()
    POTCAR.close()

