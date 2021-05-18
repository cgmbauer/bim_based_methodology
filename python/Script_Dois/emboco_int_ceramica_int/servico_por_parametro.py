# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfService = IN[0]
listOfElementsCategory = IN[1]

# Custom variables
listLoop = 0

output = {"element": [], "rvt_serv": []}


# Place your code below this line
for i in listOfService:
	for j in i:
		if j == 'EMBOCO_INT_F1_SERV_10mm' or j == 'EMBOCO_INT_F2_SERV_10mm' or j == 'EMBOCO_INT_F1_SERV_20mm' or j == 'EMBOCO_INT_F2_SERV_20mm' or j == 'CERAMICA_INT_F1_SERV_33x45cm' or j == 'CERAMICA_INT_F2_SERV_33x45cm' or j == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm' or j == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm' or j == 'CERAMICA_INT_F1_SERV_30x60cm' or j == 'CERAMICA_INT_F2_SERV_30x60cm' or j == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm' or j == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm' or j == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm' or j == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm':
			output["element"].append(listOfElementsCategory[listLoop])
			output["rvt_serv"].append(j)
	listLoop = listLoop + 1

# Assign your output to the OUT variable.
OUT = output["rvt_serv"], output["element"]