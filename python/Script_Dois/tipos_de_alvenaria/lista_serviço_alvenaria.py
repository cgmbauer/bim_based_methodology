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

ALVENARIA_BLC_CERAMICO_9X19X19cm = {"ALVENARIA_BLC_CERAMICO_9X19X19cm": [], "title": []}
ALVENARIA_BLC_CONCETO_9X19X39cm = {"ALVENARIA_BLC_CONCETO_9X19X39cm": [], "title": []}
ALVENARIA_BLC_CONCETO_14X19X39cm = {"ALVENARIA_BLC_CONCETO_14X19X39cm": [], "title": []}

# Place your code below this line
for i in listOfService:
	for j in i:
		if j == "ALVENARIA_BLC_CERAMICO_9X19X19cm":
			ALVENARIA_BLC_CERAMICO_9X19X19cm[j].append(listOfElementsCategory[listLoop])
			ALVENARIA_BLC_CERAMICO_9X19X19cm["title"].insert(0, "ALVENARIA_BLC_CERAMICO_9X19X19cm")
		elif j == "ALVENARIA_BLC_CONCETO_9X19X39cm":
			ALVENARIA_BLC_CONCETO_9X19X39cm[j].append(listOfElementsCategory[listLoop])
			ALVENARIA_BLC_CONCETO_9X19X39cm["title"].insert(0, "ALVENARIA_BLC_CONCETO_9X19X39cm")
		elif j == "ALVENARIA_BLC_CONCETO_14X19X39cm":
			ALVENARIA_BLC_CONCETO_14X19X39cm[j].append(listOfElementsCategory[listLoop])
			ALVENARIA_BLC_CONCETO_14X19X39cm["title"].insert(0, "ALVENARIA_BLC_CONCETO_14X19X39cm")
	listLoop = listLoop + 1

# Assign your output to the OUT variable.
OUT = ALVENARIA_BLC_CERAMICO_9X19X19cm["title"] + ALVENARIA_BLC_CONCETO_9X19X39cm["title"] + ALVENARIA_BLC_CONCETO_14X19X39cm["title"], ALVENARIA_BLC_CERAMICO_9X19X19cm["ALVENARIA_BLC_CERAMICO_9X19X19cm"], ALVENARIA_BLC_CONCETO_9X19X39cm["ALVENARIA_BLC_CONCETO_9X19X39cm"], ALVENARIA_BLC_CONCETO_14X19X39cm["ALVENARIA_BLC_CONCETO_14X19X39cm"]