# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
elements_COMP_COD = IN[0]
all_COMP_CODS = IN[1]
costs = IN[2]

outCosts = []
# Place your code below this line

for i in range(len(elements_COMP_COD)):
  for j in range(len(all_COMP_CODS)):
    if elements_COMP_COD[i] == all_COMP_CODS[j]:
      outCosts.append(costs[j])

# Assign your output to the OUT variable.
OUT = outCosts