# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
elements = IN[0]
rvt_cod = IN[1]
comp_cod = IN[2]
costs = IN[3]
area = IN[4]  ## parede e serviços associados com unidade m²
area_esquad = IN[5] ## esquadrias
length = IN[6] ## serviços associados a parede com unidade m

outData = []
header = ['Elemento Revit', 'Código Composição', 'Unidade', 'Quantidade', 'Custo Unitário', 'Total']
excelRowAndColumn = []
# Place your code below this line

for i in range(len(elements)):
  if rvt_cod[i] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_VÃO_<6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_SEM_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_SEM_VÃO_<6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_VÃO_<6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_SEM_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_SEM_VÃO_<6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_VÃO_<6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_SEM_VÃO_>=6m2' or rvt_cod[i] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_SEM_VÃO_<6m2' or rvt_cod[i] == 'PAREDE_BLC_GESSO_10cm' or rvt_cod[i] == 'DRYWALL_SIMPLES_VÃO' or rvt_cod[i] == 'DRYWALL_SIMPLES_SEM_VÃO' or rvt_cod[i] == 'DRYWALL_DUPLAS_VÃO' or rvt_cod[i] == 'DRYWALL_DUPLAS_SEM_VÃO' or rvt_cod[i] == 'CHAPISCO_INT_F1_SERV' or rvt_cod[i] == 'CHAPISCO_INT_F2_SERV' or rvt_cod[i] == 'CHAPISCO_EXT_SERV_VÃO' or rvt_cod[i] == 'CHAPISCO_EXT_SERV_SEM_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_35mm_SEM_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_35mm_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_25mm_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_25mm_SEM_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_45mm_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_45mm_SEM_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_50mm_VÃO' or rvt_cod[i] == 'EMBOCO_EXT_SERV_50mm_SEM_VÃO' or rvt_cod[i] == 'DIVISORIA_GRANITO' or rvt_cod[i] == 'DIVISORIA_PVC_PAINEL_VIDRO_PAINEL' or rvt_cod[i] == 'DIVISORIA_PVC_PAINEL_VIDRO' or rvt_cod[i] == 'DIVISORIA_PVC_PAINEL' or rvt_cod[i] == 'DIVISORIA_PISO_TETO_VIDRO' or rvt_cod[i] == 'DIVISORIA_PISO_TETO_PAINEL_VIDRO' or rvt_cod[i] == 'DIVISORIA_PISO_TETO_PAINEL' or rvt_cod[i] == 'DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL' or rvt_cod[i] == 'DIVISORIA_EUCATEX_PAINEL_VIDRO' or rvt_cod[i] == 'DIVISORIA_EUCATEX_PAINEL' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_10mm_<5m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_10mm_<5m2' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_20mm_<5m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_20mm_<5m2' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_10mm_>=5m2_E_<=10m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_10mm_>=5m2_E_<=10m2' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_20mm_>=5m2_E_<=10m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_20mm_>=5m2_E_<=10m2' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_10mm_>10m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_10mm_>10m2' or rvt_cod[i] == 'EMBOCO_INT_F1_SERV_20mm_>10m2' or rvt_cod[i] == 'EMBOCO_INT_F2_SERV_20mm_>10m2' or rvt_cod[i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_SERV_33x45cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_SERV_33x45cm_>=5m2' or rvt_cod[i] == 'CERAMICA_INT_F1_SERV_33x45cm_<5m2' or rvt_cod[i] == 'CERAMICA_INT_F2_SERV_33x45cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm_>=5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm_<5m2' or rvt_cod[i] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm_<5m2' or rvt_cod[i] == 'MASSA_UNICA_INT_F1_SERV_10mm' or rvt_cod[i] == 'MASSA_UNICA_INT_F1_SERV_20mm' or rvt_cod[i] == 'MASSA_UNICA_INT_F2_SERV_10mm' or rvt_cod[i] == 'MASSA_UNICA_INT_F2_SERV_20mm' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_50mm_SEM_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_45mm_SEM_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_35mm_SEM_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_25mm_SEM_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_50mm_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_45mm_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_35mm_VÃO' or rvt_cod[i] == 'MASSA_UNICA_EXT_SERV_25mm_VÃO' or rvt_cod[i] == 'SELADOR_PVA_INT_F1_SERV' or rvt_cod[i] == 'SELADOR_ACRILICO_INT_F1_SERV' or rvt_cod[i] == 'SELADOR_PVA_INT_F2_SERV' or rvt_cod[i] == 'SELADOR_ACRILICO_INT_F2_SERV' or rvt_cod[i] == 'CERAMICA_PORCELANA_EXT_SERV_5x10cm_SEM_VÃO' or rvt_cod[i] == 'CERAMICA_PORCELANA_EXT_SERV_5x10cm_VÃO' or rvt_cod[i] == 'CERAMICA_PORCELANA_EXT_SERV_5x5cm_SEM_VÃO' or rvt_cod[i] == 'CERAMICA_PORCELANA_EXT_SERV_5x5cm_VÃO' or rvt_cod[i] == 'SELADOR_ACRILICO_EXT_MULTPAV_SERV_SEM_VÃO' or rvt_cod[i] == 'SELADOR_ACRILICO_EXT_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'SELADOR_ACRILICO_EXT_TERREO_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_MULTPAV_SERV_SEM_VÃO' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV' or rvt_cod[i] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV' or rvt_cod[i] == 'PINTURA_PVA_INT_F1_SERV' or rvt_cod[i] == 'PINTURA_ACRILICA_INT_F1_SERV' or rvt_cod[i] == 'PINTURA_PVA_INT_F2_SERV' or rvt_cod[i] == 'PINTURA_ACRILICA_INT_F2_SERV' or rvt_cod[i] == 'PINTURA_ACRILICA_EXT_TERREO_SERV' or rvt_cod[i] == 'PINTURA_ACRILICA_EXT_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'PINTURA_ACRILICA_EXT_MULTPAV_SERV_SEM_VÃO' or rvt_cod[i] == 'TEXTURA_ACRILICA_INT_F1_SERV' or rvt_cod[i] == 'TEXTURA_ACRILICA_INT_F2_SERV' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_UMA_COR_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_MULTPAV_SERV_VÃO' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_UMA_COR_MULTPAV_SERV_SEM_VÃO' or rvt_cod[i] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_MULTPAV_SERV_SEM_VÃO' or rvt_cod[i] == 'ISOLAMENTO_DRYWALL_SERV' or rvt_cod[i] == 'DEMOLIÇÃO_CERÂMICA_SERV' or rvt_cod[i] == 'APICOAMENTO_SERV':  
    excelRowAndColumn.append(i + 2)
    outData.append([rvt_cod[i], comp_cod[i], 'm²', round(area[i], 2), costs[i], '=D'+str(excelRowAndColumn[i])+'*E'+str(excelRowAndColumn[i])])
  elif rvt_cod[i] == 'ENCUNHAMENTO_SERV':
    excelRowAndColumn.append(i + 2)
    outData.append([rvt_cod[i], comp_cod[i], 'm', round(length[i], 2), costs[i], '=D'+str(excelRowAndColumn[i])+'*E'+str(excelRowAndColumn[i])])
  elif rvt_cod[i] == 'JA_0.9x2.15m_A' or rvt_cod[i] == 'PM1_1x2.1m_A':
    excelRowAndColumn.append(i + 2)
    outData.append([rvt_cod[i], comp_cod[i], 'm²', area_esquad[i], costs[i], '=D'+str(excelRowAndColumn[i])+'*E'+str(excelRowAndColumn[i])])

# Assign your output to the OUT variable.
OUT = header, outData ## título, 