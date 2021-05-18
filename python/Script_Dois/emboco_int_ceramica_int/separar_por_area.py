# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
wallElements = IN[0]  ##  L2 -len igual a areaValue
areaValues = IN[1] ## L2 - len igual a wallElements
servParams = IN[2]   # L3
rvtCod =  IN[3] # escolher o L2

walls = []
paramsValue = []
outRvtCod = []

# Place your code below this line
for i in range(len(areaValues)):
  if areaValues[i] < 5:
    if servParams[0][i] == 'EMBOCO_INT_F1_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F1_SERV_20mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_20mm' or servParams[0][i] == 'CERAMICA_INT_F1_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm':
      walls.append(wallElements[i])
      paramsValue.append(servParams[0][i]+'_<5m2')
      outRvtCod.append(rvtCod[i])
  elif areaValues[i] >= 5 and areaValues[i] <= 10:
    if servParams[0][i] == 'EMBOCO_INT_F1_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F1_SERV_20mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_20mm':
      walls.append(wallElements[i])
      paramsValue.append(servParams[0][i]+'_>=5m2_E_<=10m2')
      outRvtCod.append(rvtCod[i])
    elif servParams[0][i] == 'CERAMICA_INT_F1_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm':
      walls.append(wallElements[i])
      paramsValue.append(servParams[0][i]+'_>=5m2')
      outRvtCod.append(rvtCod[i])
  elif areaValues[i] > 10:
    if servParams[0][i] == 'EMBOCO_INT_F1_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_10mm' or servParams[0][i] == 'EMBOCO_INT_F1_SERV_20mm' or servParams[0][i] == 'EMBOCO_INT_F2_SERV_20mm':
      walls.append(wallElements[i])
      paramsValue.append(servParams[0][i]+'_>10m2')
      outRvtCod.append(rvtCod[i])
    elif servParams[0][i] == 'CERAMICA_INT_F1_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm' or servParams[0][i] == 'CERAMICA_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm' or servParams[0][i] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm':
      walls.append(wallElements[i])
      paramsValue.append(servParams[0][i]+'_>=5m2')
      outRvtCod.append(rvtCod[i])

# Assign your output to the OUT variable.
OUT = walls, paramsValue, outRvtCod # paredes, valor para rvtCode, rvtCode