# ----------------------------------------------
# Nombre      :: VaspTools
# Autior      :: Shigueru Nagata
# Descripcion :: Funciones relacionadas a Vasp
# ----------------------------------------------

import os

# ------------------------------------------------------------------------------
# Funciones para generar cada archivo
# INCAR - POSCAR - KPOINTS - POTCAR
# ------------------------------------------------------------------------------

def INCARCreate(ICName):
    INCAR = open(ICName, "x")
    INCAR.close()

def KPOINTSCreate(KCName):
    KPOINTS = open(KCName, "x")
    KPOINTS.close()

def POSCARCreate(PSCName):
    POSCAR = open(PSCName, "x")
    POSCAR.close()

def POTCARCreate(PTCName):
    POTCAR = open(PTCName, "x")
    POTCAR.close()


# ------------------------------------------------------------------------------
# Funciones para generar la estructura basica de la carpeta
# INCAR - POSCAR - KPOINTS - POTCAR
# correspondiente a cada caso de simulacion
# ------------------------------------------------------------------------------

def VTBasic(VTBPath):

    PathDir = "./" + VTBPath
    
    os.mkdir(PathDir)
    os.chdir(PathDir)

    INCARCreate("INCAR")
    KPOINTSCreate("KPOINTS")
    POSCARCreate("POSCAR")
    POTCARCreate("POTCAR")
    
def VTBandsDos(VTBDPath):
    
    PathDir = "./" + VTBDPath
    
    os.mkdir(PathDir)
    os.chdir(PathDir)

    POSCARCreate("POSCAR")
    POTCARCreate("POTCAR")

    INCARCreate("INCAR-1")
    INCARCreate("INCAR-2")

    KPOINTSCreate("KPOINTS-1")
    KPOINTSCreate("KPOINTS-2")
    
