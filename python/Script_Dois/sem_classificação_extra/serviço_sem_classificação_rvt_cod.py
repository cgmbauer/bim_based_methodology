# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfService = IN[0]

# Custom variables
PAREDE_RVT_COD = []
CHAPISCO_INT_F1_RVT_COD = []
CHAPISCO_INT_F2_RVT_COD = []
DIVISORIA_RVT_COD = []
SELADOR_INT_F1_RVT_COD = []
SELADOR_INT_F2_RVT_COD = []
SELADOR_EXT_RVT_COD = []
MASSA_UNICA_INT_F1_RVT_COD = []
MASSA_UNICA_INT_F2_RVT_COD = []
MASSA_CORRIDA_INT_F1_RVT_COD = []
MASSA_CORRIDA_INT_F2_RVT_COD = []
MASSA_CORRIDA_EXT_RVT_COD = []
PINTURA_INT_F1_RVT_COD = []
PINTURA_INT_F2_RVT_COD = [] 
PINTURA_EXT_RVT_COD = []
TEXTURA_INT_F1_RVT_COD = []
TEXTURA_INT_F2_RVT_COD = []
TEXTURA_EXT_RVT_COD = []
ENCUNHAMENTO_RVT_COD = []
ISOLAMENTO_DRYWALL_RVT_COD = []
DEMOLICAO_CERAMICA_RVT_COD = []
APICOAMENTO_RVT_COD = []

# Place your code below this line
for i in listOfService:
	for j in i:
		if j == "PAREDE_BLC_GESSO_10cm":
			PAREDE_RVT_COD.append("PAREDE_RVT_COD")
		elif j == "CHAPISCO_INT_F1_SERV":
			CHAPISCO_INT_F1_RVT_COD.append("CHAPISCO_INT_F1_RVT_COD")
		elif j == "CHAPISCO_INT_F2_SERV":
			CHAPISCO_INT_F2_RVT_COD.append("CHAPISCO_INT_F2_RVT_COD")
		elif j == "DIVISORIA_EUCATEX_PAINEL" or j == "DIVISORIA_EUCATEX_PAINEL_VIDRO" or j == "DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL" or j == "DIVISORIA_PISO_TETO_PAINEL" or j == "DIVISORIA_PISO_TETO_VIDRO" or j == "DIVISORIA_PVC_PAINEL" or j == "DIVISORIA_PVC_PAINEL_VIDRO" or j == "DIVISORIA_PVC_PAINEL_VIDRO_PAINEL" or j == "DIVISORIA_GRANITO":
			DIVISORIA_RVT_COD.append("DIVISORIA_RVT_COD")
		elif j == "SELADOR_ACRILICO_INT_F1_SERV" or j == "SELADOR_PVA_INT_F1_SERV":
			SELADOR_INT_F1_RVT_COD.append("SELADOR_INT_F1_RVT_COD")
		elif j == "SELADOR_ACRILICO_INT_F2_SERV" or j == "SELADOR_PVA_INT_F2_SERV":
			SELADOR_INT_F2_RVT_COD.append("SELADOR_INT_F2_RVT_COD")
		elif j == "SELADOR_ACRILICO_EXT_TERREO_SERV":
			SELADOR_EXT_RVT_COD.append("SELADOR_EXT_RVT_COD")
		elif j == "MASSA_UNICA_INT_F1_SERV_10mm" or j == "MASSA_UNICA_INT_F1_SERV_20mm":
			MASSA_UNICA_INT_F1_RVT_COD.append("MASSA_UNICA_INT_F1_RVT_COD")
		elif j == "MASSA_UNICA_INT_F2_SERV_10mm" or j == "MASSA_UNICA_INT_F2_SERV_20mm":
			MASSA_UNICA_INT_F2_RVT_COD.append("MASSA_UNICA_INT_F2_RVT_COD")
		elif j == "MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV" or j == "MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV":
			MASSA_CORRIDA_INT_F1_RVT_COD.append("MASSA_CORRIDA_INT_F1_RVT_COD")
		elif j == "MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV" or j == "MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV":
			MASSA_CORRIDA_INT_F2_RVT_COD.append("MASSA_CORRIDA_INT_F2_RVT_COD")
		elif j == "MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV" or j == "MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV":
			MASSA_CORRIDA_EXT_RVT_COD.append("MASSA_CORRIDA_EXT_RVT_COD")
		elif j == "PINTURA_PVA_INT_F1_SERV" or j == "PINTURA_ACRILICA_INT_F1_SERV":
			PINTURA_INT_F1_RVT_COD.append("PINTURA_INT_F1_RVT_COD")
		elif j == "PINTURA_PVA_INT_F2_SERV" or j == "PINTURA_ACRILICA_INT_F2_SERV":
			PINTURA_INT_F2_RVT_COD.append("PINTURA_INT_F2_RVT_COD")
		elif j == "PINTURA_ACRILICA_EXT_TERREO_SERV":
			PINTURA_EXT_RVT_COD.append("PINTURA_EXT_RVT_COD")
		elif j == "TEXTURA_ACRILICA_INT_F1_SERV":
			TEXTURA_INT_F1_RVT_COD.append("TEXTURA_INT_F1_RVT_COD")
		elif j == "TEXTURA_ACRILICA_INT_F2_SERV":
			TEXTURA_INT_F2_RVT_COD.append("TEXTURA_INT_F2_RVT_COD")
		elif j == "TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV" or j == "TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV":
			TEXTURA_EXT_RVT_COD.append("TEXTURA_EXT_RVT_COD")
		elif j == "ENCUNHAMENTO_SERV":
			ENCUNHAMENTO_RVT_COD.append("ENCUNHAMENTO_RVT_COD")
		elif j == "ISOLAMENTO_DRYWALL_SERV":
			ISOLAMENTO_DRYWALL_RVT_COD.append("ISOLAMENTO_DRYWALL_RVT_COD")
		elif j == "DEMOLIÇÃO_CERÂMICA_SERV":
			DEMOLICAO_CERAMICA_RVT_COD.append("DEMOLICAO_CERAMICA_RVT_COD")
		elif j == "APICOAMENTO_SERV":
			APICOAMENTO_RVT_COD.append("APICOAMENTO_RVT_COD")
# Assign your output to the OUT variable.
OUT = PAREDE_RVT_COD + CHAPISCO_INT_F1_RVT_COD + CHAPISCO_INT_F2_RVT_COD + DIVISORIA_RVT_COD + SELADOR_INT_F1_RVT_COD + SELADOR_INT_F2_RVT_COD + SELADOR_EXT_RVT_COD + MASSA_UNICA_INT_F1_RVT_COD + MASSA_UNICA_INT_F2_RVT_COD + MASSA_CORRIDA_INT_F1_RVT_COD + MASSA_CORRIDA_INT_F2_RVT_COD + MASSA_CORRIDA_EXT_RVT_COD + PINTURA_INT_F1_RVT_COD + PINTURA_INT_F2_RVT_COD +  PINTURA_EXT_RVT_COD + TEXTURA_INT_F1_RVT_COD + TEXTURA_INT_F2_RVT_COD + TEXTURA_EXT_RVT_COD + ENCUNHAMENTO_RVT_COD + ISOLAMENTO_DRYWALL_RVT_COD + DEMOLICAO_CERAMICA_RVT_COD + APICOAMENTO_RVT_COD