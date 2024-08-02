# -----------------------------------------------------------
# Nombre      :: IOTools
# Autor       :: Shigueru Nagata
# Descripcion :: Funciones para input o output de informacion
# -----------------------------------------------------------

# colores

COLORS = {
        "BLACKFG":"\033[30m",
        "BLACKBG":"\033[40m",
        "REDFG":"\033[31m",
        "REDBG":"\033[41m",
        "GREENFG":"\033[32m",
        "GREENBG":"\033[42m",
        "YELLOWFG":"\033[33m",
        "YELLOWBG":"\033[43m",
        "BLUEFG":"\033[34m",
        "BLUEBG":"\033[44m",
        "MAGENTAFG":"\033[35m",
        "MAGENTABG":"\033[45m",
        "CYANFG":"\033[36m",
        "CYANBG":"\033[46m",
        "GRAYFG":"\033[90m",
        "GRAYBG":"\033[100m",
        "WHITEFG":"\033[97m",
        "WHITEBG":"\033[107m",
        "LIGHTREDFG":"\033[91m",
        "LIGHTREDBG":"\033[101m",
        "LIGHTGREENFG":"\033[92m",
        "LIGHTGREENBG":"\033[102m",
        "LIGHTYELLOWFG":"\033[93m",
        "LIGHTYELLOWBG":"\033[103m",
        "LIGHTBLUEFG":"\033[94m",
        "LIGHTBLUEBG":"\033[104m",
        "LIGHTMAGENTAFG":"\033[95m",
        "LIGHTMAGENTABG":"\033[105m",
        "LIGHTCYANFG":"\033[96m",
        "LIGHTCYANBG":"\033[106m",
        "ENDCOLOR":"\033[0m"
}

def IOText(IOTColor,IOTText,IOTWidth):
    if (IOTWidth == 0):
        IOTS = COLORS[IOTColor] + IOTText + COLORS["ENDCOLOR"]
    
    if (IOTWidth != 0):
        IOTTextCenter = IOTText.center(IOTWidth)
        IOTS =  COLORS[IOTColor] + IOTTextCenter + COLORS["ENDCOLOR"]
    #print(COLORS[IOTColor] + IOTText + COLORS["ENDCOLOR"])
    return IOTS
