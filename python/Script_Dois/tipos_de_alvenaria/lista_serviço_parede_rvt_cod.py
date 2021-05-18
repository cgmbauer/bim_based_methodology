# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfService = IN[0]

# Custom variables
PAREDE_RVT_COD = []

# Place your code below this line
for i in listOfService:
	for j in i:
		if j == "ALVENARIA_BLC_CERAMICO_9X19X19cm" or j == "ALVENARIA_BLC_CONCETO_9X19X39cm" or j == "ALVENARIA_BLC_CONCETO_14X19X39cm":
			PAREDE_RVT_COD.append("PAREDE_RVT_COD")

# Assign your output to the OUT variable.
OUT = PAREDE_RVT_COD