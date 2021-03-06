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

PAREDE_BLC_GESSO_10cm = {"PAREDE_BLC_GESSO_10cm": [], "title": []}
CHAPISCO_INT_F1_SERV = {"CHAPISCO_INT_F1_SERV": [], "title": []}
CHAPISCO_INT_F2_SERV = {"CHAPISCO_INT_F2_SERV": [], "title": []}
DIVISORIA_EUCATEX_PAINEL = {"DIVISORIA_EUCATEX_PAINEL": [], "title": []}
DIVISORIA_EUCATEX_PAINEL_VIDRO = {"DIVISORIA_EUCATEX_PAINEL_VIDRO": [], "title": []}
DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL = {"DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL": [], "title": []}
DIVISORIA_PISO_TETO_PAINEL = {"DIVISORIA_PISO_TETO_PAINEL": [], "title": []}
DIVISORIA_PISO_TETO_VIDRO = {"DIVISORIA_PISO_TETO_VIDRO": [], "title": []}
DIVISORIA_PVC_PAINEL = {"DIVISORIA_PVC_PAINEL": [], "title": []}
DIVISORIA_PVC_PAINEL_VIDRO = {"DIVISORIA_PVC_PAINEL_VIDRO": [], "title": []}
DIVISORIA_PVC_PAINEL_VIDRO_PAINEL = {"DIVISORIA_PVC_PAINEL_VIDRO_PAINEL": [], "title": []}
DIVISORIA_GRANITO = {"DIVISORIA_GRANITO": [], "title": []}
SELADOR_ACRILICO_INT_F1_SERV = {"SELADOR_ACRILICO_INT_F1_SERV": [], "title": []}
SELADOR_ACRILICO_INT_F2_SERV = {"SELADOR_ACRILICO_INT_F2_SERV": [], "title": []}
SELADOR_PVA_INT_F1_SERV = {"SELADOR_PVA_INT_F1_SERV": [], "title": []}
SELADOR_PVA_INT_F2_SERV = {"SELADOR_PVA_INT_F2_SERV": [], "title": []}
SELADOR_ACRILICO_EXT_TERREO_SERV = {"SELADOR_ACRILICO_EXT_TERREO_SERV": [], "title": []}
MASSA_UNICA_INT_F1_SERV_10mm = {"MASSA_UNICA_INT_F1_SERV_10mm": [], "title": []}
MASSA_UNICA_INT_F2_SERV_10mm = {"MASSA_UNICA_INT_F2_SERV_10mm": [], "title": []}
MASSA_UNICA_INT_F1_SERV_20mm = {"MASSA_UNICA_INT_F1_SERV_20mm": [], "title": []}
MASSA_UNICA_INT_F2_SERV_20mm = {"MASSA_UNICA_INT_F2_SERV_20mm": [], "title": []}
MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV = {"MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV": [], "title": []}
MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV = {"MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV": [], "title": []}
MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV = {"MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV": [], "title": []}
MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV = {"MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV": [], "title": []}
MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV = {"MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV": [], "title": []}
MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV = {"MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV": [], "title": []}
PINTURA_PVA_INT_F1_SERV = {"PINTURA_PVA_INT_F1_SERV": [], "title": []}
PINTURA_PVA_INT_F2_SERV = {"PINTURA_PVA_INT_F2_SERV": [], "title": []}
PINTURA_ACRILICA_INT_F1_SERV = {"PINTURA_ACRILICA_INT_F1_SERV": [], "title": []}
PINTURA_ACRILICA_INT_F2_SERV = {"PINTURA_ACRILICA_INT_F2_SERV": [], "title": []}
PINTURA_ACRILICA_EXT_TERREO_SERV = {"PINTURA_ACRILICA_EXT_TERREO_SERV": [], "title": []}
TEXTURA_ACRILICA_INT_F1_SERV = {"TEXTURA_ACRILICA_INT_F1_SERV": [], "title": []}
TEXTURA_ACRILICA_INT_F2_SERV = {"TEXTURA_ACRILICA_INT_F2_SERV": [], "title": []}
TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV = {"TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV": [], "title": []}
TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV = {"TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV": [], "title": []}
ENCUNHAMENTO_SERV = {"ENCUNHAMENTO_SERV": [], "title": []}
ISOLAMENTO_DRYWALL_SERV = {"ISOLAMENTO_DRYWALL_SERV": [], "title": []}
DEMOLI????O_CER??MICA_SERV = {"DEMOLI????O_CER??MICA_SERV": [], "title": []}
APICOAMENTO_SERV = {"APICOAMENTO_SERV": [], "title": []}

# Place your code below this line
for i in listOfService:
	for j in i:
		if j == "PAREDE_BLC_GESSO_10cm":
			PAREDE_BLC_GESSO_10cm[j].append(listOfElementsCategory[listLoop])
			PAREDE_BLC_GESSO_10cm["title"].insert(0, "PAREDE_BLC_GESSO_10cm")
		elif j == "CHAPISCO_INT_F1_SERV":
			CHAPISCO_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			CHAPISCO_INT_F1_SERV["title"].insert(0, "CHAPISCO_INT_F1_SERV")
		elif j == "CHAPISCO_INT_F2_SERV":
			CHAPISCO_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			CHAPISCO_INT_F2_SERV["title"].insert(0, "CHAPISCO_INT_F2_SERV")
		elif j == "DIVISORIA_EUCATEX_PAINEL":
			DIVISORIA_EUCATEX_PAINEL[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_EUCATEX_PAINEL["title"].insert(0, "DIVISORIA_EUCATEX_PAINEL")
		elif j == "DIVISORIA_EUCATEX_PAINEL_VIDRO":
			DIVISORIA_EUCATEX_PAINEL_VIDRO[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_EUCATEX_PAINEL_VIDRO["title"].insert(0, "DIVISORIA_EUCATEX_PAINEL_VIDRO")
		elif j == "DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL":
			DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL["title"].insert(0, "DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL")
		elif j == "DIVISORIA_PISO_TETO_PAINEL":
			DIVISORIA_PISO_TETO_PAINEL[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_PISO_TETO_PAINEL["title"].insert(0, "DIVISORIA_PISO_TETO_PAINEL")
		elif j == "DIVISORIA_PISO_TETO_VIDRO":
			DIVISORIA_PISO_TETO_VIDRO[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_PISO_TETO_VIDRO["title"].insert(0, "DIVISORIA_PISO_TETO_VIDRO")
		elif j == "DIVISORIA_PVC_PAINEL":
			DIVISORIA_PVC_PAINEL[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_PVC_PAINEL["title"].insert(0, "DIVISORIA_PVC_PAINEL")
		elif j == "DIVISORIA_PVC_PAINEL_VIDRO":
			DIVISORIA_PVC_PAINEL_VIDRO[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_PVC_PAINEL_VIDRO["title"].insert(0, "DIVISORIA_PVC_PAINEL_VIDRO")
		elif j == "DIVISORIA_PVC_PAINEL_VIDRO_PAINEL":
			DIVISORIA_PVC_PAINEL_VIDRO_PAINEL[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_PVC_PAINEL_VIDRO_PAINEL["title"].insert(0, "DIVISORIA_PVC_PAINEL_VIDRO_PAINEL")
		elif j == "DIVISORIA_GRANITO":
			DIVISORIA_GRANITO[j].append(listOfElementsCategory[listLoop])
			DIVISORIA_GRANITO["title"].insert(0, "DIVISORIA_GRANITO")
		elif j == "SELADOR_ACRILICO_INT_F1_SERV":
			SELADOR_ACRILICO_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			SELADOR_ACRILICO_INT_F1_SERV["title"].insert(0, "SELADOR_ACRILICO_INT_F1_SERV")
		elif j == "SELADOR_ACRILICO_INT_F2_SERV":
			SELADOR_ACRILICO_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			SELADOR_ACRILICO_INT_F2_SERV["title"].insert(0, "SELADOR_ACRILICO_INT_F2_SERV")
		elif j == "SELADOR_PVA_INT_F1_SERV":
			SELADOR_PVA_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			SELADOR_PVA_INT_F1_SERV["title"].insert(0, "SELADOR_PVA_INT_F1_SERV")
		elif j == "SELADOR_PVA_INT_F2_SERV":
			SELADOR_PVA_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			SELADOR_PVA_INT_F2_SERV["title"].insert(0, "SELADOR_PVA_INT_F2_SERV")
		elif j == "SELADOR_ACRILICO_EXT_TERREO_SERV":
			SELADOR_ACRILICO_EXT_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			SELADOR_ACRILICO_EXT_TERREO_SERV["title"].insert(0, "SELADOR_ACRILICO_EXT_TERREO_SERV")
		elif j == "MASSA_UNICA_INT_F1_SERV_10mm":
			MASSA_UNICA_INT_F1_SERV_10mm[j].append(listOfElementsCategory[listLoop])
			MASSA_UNICA_INT_F1_SERV_10mm["title"].insert(0, "MASSA_UNICA_INT_F1_SERV_10mm")
		elif j == "MASSA_UNICA_INT_F2_SERV_10mm":
			MASSA_UNICA_INT_F2_SERV_10mm[j].append(listOfElementsCategory[listLoop])
			MASSA_UNICA_INT_F2_SERV_10mm["title"].insert(0, "MASSA_UNICA_INT_F2_SERV_10mm")
		elif j == "MASSA_UNICA_INT_F1_SERV_20mm":
			MASSA_UNICA_INT_F1_SERV_20mm[j].append(listOfElementsCategory[listLoop])
			MASSA_UNICA_INT_F1_SERV_20mm["title"].insert(0, "MASSA_UNICA_INT_F1_SERV_20mm")
		elif j == "MASSA_UNICA_INT_F2_SERV_20mm":
			MASSA_UNICA_INT_F2_SERV_20mm[j].append(listOfElementsCategory[listLoop])
			MASSA_UNICA_INT_F2_SERV_20mm["title"].insert(0, "MASSA_UNICA_INT_F2_SERV_20mm")
		elif j == "MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV":
			MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV["title"].insert(0, "MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV")
		elif j == "MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV":
			MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV["title"].insert(0, "MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV")
		elif j == "MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV":
			MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV["title"].insert(0, "MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV")
		elif j == "MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV":
			MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV["title"].insert(0, "MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV")
		elif j == "MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV":
			MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV["title"].insert(0, "MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV")
		elif j == "MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV":
			MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV["title"].insert(0, "MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV")
		elif j == "PINTURA_PVA_INT_F1_SERV":
			PINTURA_PVA_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			PINTURA_PVA_INT_F1_SERV["title"].insert(0, "PINTURA_PVA_INT_F1_SERV")
		elif j == "PINTURA_PVA_INT_F2_SERV":
			PINTURA_PVA_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			PINTURA_PVA_INT_F2_SERV["title"].insert(0, "PINTURA_PVA_INT_F2_SERV")
		elif j == "PINTURA_ACRILICA_INT_F1_SERV":
			PINTURA_ACRILICA_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			PINTURA_ACRILICA_INT_F1_SERV["title"].insert(0, "PINTURA_ACRILICA_INT_F1_SERV")
		elif j == "PINTURA_ACRILICA_INT_F2_SERV":
			PINTURA_ACRILICA_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			PINTURA_ACRILICA_INT_F2_SERV["title"].insert(0, "PINTURA_ACRILICA_INT_F2_SERV")
		elif j == "PINTURA_ACRILICA_EXT_TERREO_SERV":
			PINTURA_ACRILICA_EXT_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			PINTURA_ACRILICA_EXT_TERREO_SERV["title"].insert(0, "PINTURA_ACRILICA_EXT_TERREO_SERV")
		elif j == "TEXTURA_ACRILICA_INT_F1_SERV":
			TEXTURA_ACRILICA_INT_F1_SERV[j].append(listOfElementsCategory[listLoop])
			TEXTURA_ACRILICA_INT_F1_SERV["title"].insert(0, "TEXTURA_ACRILICA_INT_F1_SERV")
		elif j == "TEXTURA_ACRILICA_INT_F2_SERV":
			TEXTURA_ACRILICA_INT_F2_SERV[j].append(listOfElementsCategory[listLoop])
			TEXTURA_ACRILICA_INT_F2_SERV["title"].insert(0, "TEXTURA_ACRILICA_INT_F2_SERV")
		elif j == "TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV":
			TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV["title"].insert(0, "TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV")
		elif j == "TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV":
			TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV[j].append(listOfElementsCategory[listLoop])
			TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV["title"].insert(0, "TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV")
		elif j == "ENCUNHAMENTO_SERV":
			ENCUNHAMENTO_SERV[j].append(listOfElementsCategory[listLoop])
			ENCUNHAMENTO_SERV["title"].insert(0, "ENCUNHAMENTO_SERV")
		elif j == "ISOLAMENTO_DRYWALL_SERV":
			ISOLAMENTO_DRYWALL_SERV[j].append(listOfElementsCategory[listLoop])
			ISOLAMENTO_DRYWALL_SERV["title"].insert(0, "ISOLAMENTO_DRYWALL_SERV")
		elif j == "DEMOLI????O_CER??MICA_SERV":
			DEMOLI????O_CER??MICA_SERV[j].append(listOfElementsCategory[listLoop])
			DEMOLI????O_CER??MICA_SERV["title"].insert(0, "DEMOLI????O_CER??MICA_SERV")
		elif j == "APICOAMENTO_SERV":
			APICOAMENTO_SERV[j].append(listOfElementsCategory[listLoop])
			APICOAMENTO_SERV["title"].insert(0, "APICOAMENTO_SERV")	
	listLoop = listLoop + 1

# Assign your output to the OUT variable.
OUT = PAREDE_BLC_GESSO_10cm["title"] + CHAPISCO_INT_F1_SERV["title"] + CHAPISCO_INT_F2_SERV["title"] + DIVISORIA_EUCATEX_PAINEL["title"] + DIVISORIA_EUCATEX_PAINEL_VIDRO["title"] + DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL["title"] + DIVISORIA_PISO_TETO_PAINEL["title"] + DIVISORIA_PISO_TETO_VIDRO["title"] + DIVISORIA_PVC_PAINEL["title"] + DIVISORIA_PVC_PAINEL_VIDRO["title"] + DIVISORIA_PVC_PAINEL_VIDRO_PAINEL["title"] + DIVISORIA_GRANITO["title"] + SELADOR_ACRILICO_INT_F1_SERV["title"] + SELADOR_ACRILICO_INT_F2_SERV["title"] + SELADOR_PVA_INT_F1_SERV["title"] + SELADOR_PVA_INT_F2_SERV["title"] + SELADOR_ACRILICO_EXT_TERREO_SERV["title"] + MASSA_UNICA_INT_F1_SERV_10mm["title"] + MASSA_UNICA_INT_F2_SERV_10mm["title"] + MASSA_UNICA_INT_F1_SERV_20mm["title"] + MASSA_UNICA_INT_F2_SERV_20mm["title"] + MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV["title"] + MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV["title"] + MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV["title"] + MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV["title"] + MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV["title"] + MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV["title"] + PINTURA_PVA_INT_F1_SERV["title"] + PINTURA_PVA_INT_F2_SERV["title"] + PINTURA_ACRILICA_INT_F1_SERV["title"] + PINTURA_ACRILICA_INT_F2_SERV["title"] + PINTURA_ACRILICA_EXT_TERREO_SERV["title"] + TEXTURA_ACRILICA_INT_F1_SERV["title"] + TEXTURA_ACRILICA_INT_F2_SERV["title"] + TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV["title"] + TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV["title"] + ENCUNHAMENTO_SERV["title"] + ISOLAMENTO_DRYWALL_SERV["title"] + DEMOLI????O_CER??MICA_SERV["title"] + APICOAMENTO_SERV["title"], PAREDE_BLC_GESSO_10cm["PAREDE_BLC_GESSO_10cm"], CHAPISCO_INT_F1_SERV["CHAPISCO_INT_F1_SERV"], CHAPISCO_INT_F2_SERV["CHAPISCO_INT_F2_SERV"], DIVISORIA_EUCATEX_PAINEL["DIVISORIA_EUCATEX_PAINEL"], DIVISORIA_EUCATEX_PAINEL_VIDRO["DIVISORIA_EUCATEX_PAINEL_VIDRO"], DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL["DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL"], DIVISORIA_PISO_TETO_PAINEL["DIVISORIA_PISO_TETO_PAINEL"], DIVISORIA_PISO_TETO_VIDRO["DIVISORIA_PISO_TETO_VIDRO"], DIVISORIA_PVC_PAINEL["DIVISORIA_PVC_PAINEL"], DIVISORIA_PVC_PAINEL_VIDRO["DIVISORIA_PVC_PAINEL_VIDRO"], DIVISORIA_PVC_PAINEL_VIDRO_PAINEL["DIVISORIA_PVC_PAINEL_VIDRO_PAINEL"], DIVISORIA_GRANITO["DIVISORIA_GRANITO"], SELADOR_ACRILICO_INT_F1_SERV["SELADOR_ACRILICO_INT_F1_SERV"], SELADOR_ACRILICO_INT_F2_SERV["SELADOR_ACRILICO_INT_F2_SERV"], SELADOR_PVA_INT_F1_SERV["SELADOR_PVA_INT_F1_SERV"], SELADOR_PVA_INT_F2_SERV["SELADOR_PVA_INT_F2_SERV"], SELADOR_ACRILICO_EXT_TERREO_SERV["SELADOR_ACRILICO_EXT_TERREO_SERV"], MASSA_UNICA_INT_F1_SERV_10mm["MASSA_UNICA_INT_F1_SERV_10mm"], MASSA_UNICA_INT_F2_SERV_10mm["MASSA_UNICA_INT_F2_SERV_10mm"], MASSA_UNICA_INT_F1_SERV_20mm["MASSA_UNICA_INT_F1_SERV_20mm"], MASSA_UNICA_INT_F2_SERV_20mm["MASSA_UNICA_INT_F2_SERV_20mm"], MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV["MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV"], MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV["MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV"], MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV["MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV"], MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV["MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV"], MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV["MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV"], MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV["MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV"], PINTURA_PVA_INT_F1_SERV["PINTURA_PVA_INT_F1_SERV"], PINTURA_PVA_INT_F2_SERV["PINTURA_PVA_INT_F2_SERV"], PINTURA_ACRILICA_INT_F1_SERV["PINTURA_ACRILICA_INT_F1_SERV"], PINTURA_ACRILICA_INT_F2_SERV["PINTURA_ACRILICA_INT_F2_SERV"], PINTURA_ACRILICA_EXT_TERREO_SERV["PINTURA_ACRILICA_EXT_TERREO_SERV"], TEXTURA_ACRILICA_INT_F1_SERV["TEXTURA_ACRILICA_INT_F1_SERV"], TEXTURA_ACRILICA_INT_F2_SERV["TEXTURA_ACRILICA_INT_F2_SERV"], TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV["TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV"], TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV["TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV"], ENCUNHAMENTO_SERV["ENCUNHAMENTO_SERV"], ISOLAMENTO_DRYWALL_SERV["ISOLAMENTO_DRYWALL_SERV"], DEMOLI????O_CER??MICA_SERV["DEMOLI????O_CER??MICA_SERV"], APICOAMENTO_SERV["APICOAMENTO_SERV"]