# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfService = IN[0]

# Custom variables
RVT_COD = []

# Place your code below this line
for i in listOfService:
	for j in i:
		if j == 'EMBOCO_INT_F1_SERV_10mm' or j == 'EMBOCO_INT_F1_SERV_20mm':
			RVT_COD.append("EMBOCO_INT_F1_RVT_COD")
    elif j == 'CERAMICA_INT_F1_SERV_33x45cm' or j == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm' or j == 'CERAMICA_INT_F1_SERV_30x60cm' or j == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm' or j == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm':
      RVT_COD.append("CERAMICA_INT_F1_RVT_COD")
		elif j == 'EMBOCO_INT_F2_SERV_10mm' or j == 'EMBOCO_INT_F2_SERV_20mm':
			RVT_COD.append("EMBOCO_INT_F2_RVT_COD")
    elif j == 'CERAMICA_INT_F2_SERV_33x45cm' or j == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm' or j == 'CERAMICA_INT_F2_SERV_30x60cm' or j == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm' or j == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm' or j == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm' or j == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm':
      RVT_COD.append("CERAMICA_INT_F1_RVT_COD")

# Assign your output to the OUT variable.
OUT = RVT_COD