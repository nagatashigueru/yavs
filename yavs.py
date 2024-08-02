# -------------------------------------------
# autor       :: Shigueru Nagata
# Descripcion :: Funciones de ayuda para vasp
# -------------------------------------------

from modules import IOTools
from modules import VaspTools


def Welcome():

    # Mensajes

    Msg1 = "WELCOME TO"
    Msg2 = "YET ANOTHER VASP SCRIPTS"
    Msg3 = "YAVS"
    Separator = "-"

    Width = 80

    print()
    print(Width * Separator)
    print(IOTools.IOText(IOTColor="GREENFG",IOTText=Msg1,IOTWidth=Width))
    print(IOTools.IOText(IOTColor="YELLOWFG",IOTText=Msg2,IOTWidth=Width))
    print(IOTools.IOText(IOTColor="YELLOWFG",IOTText=Msg3,IOTWidth=Width))
    print(Width * Separator)
    print()

Welcome()

VaspTools.VTBandsDos("borrame")
