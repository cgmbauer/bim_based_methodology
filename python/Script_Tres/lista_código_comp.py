# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfElementsCategory = IN[0]
rvtCodeValue = IN[1]
listOfAllRvtCodeValues = IN[2]
listOfCompCode = IN[3]

elements = []
codeCompositionParam = []
codeCompositionValue = []

# Place your code below this line
for i in range(len(rvtCodeValue)):
  for k in range(len(rvtCodeValue[i])):
    for j in range(len(listOfAllRvtCodeValues)):
      if rvtCodeValue[i][k] == listOfAllRvtCodeValues[j]:
        elements.append(listOfElementsCategory[i])
        if rvtCodeValue[i][k] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_VÃO_<6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_SEM_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CERAMICO_9X19X19cm_SEM_VÃO_<6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_VÃO_<6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_SEM_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_9X19X39cm_SEM_VÃO_<6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_VÃO_<6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_SEM_VÃO_>=6m2' or rvtCodeValue[i][k] == 'ALVENARIA_BLC_CONCETO_14X19X39cm_SEM_VÃO_<6m2' or rvtCodeValue[i][k] == 'PAREDE_BLC_GESSO_10cm' or rvtCodeValue[i][k] == 'DRYWALL_SIMPLES_VÃO' or rvtCodeValue[i][k] == 'DRYWALL_SIMPLES_SEM_VÃO' or rvtCodeValue[i][k] == 'DRYWALL_DUPLAS_VÃO' or rvtCodeValue[i][k] == 'DRYWALL_DUPLAS_SEM_VÃO':
          codeCompositionParam.append('PAREDE_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CHAPISCO_INT_F1_SERV':
          codeCompositionParam.append('CHAPISCO_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CHAPISCO_INT_F2_SERV':
          codeCompositionParam.append('CHAPISCO_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CHAPISCO_EXT_SERV_VÃO' or rvtCodeValue[i][k] == 'CHAPISCO_EXT_SERV_SEM_VÃO':
          codeCompositionParam.append('CHAPISCO_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_35mm_SEM_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_35mm_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_25mm_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_25mm_SEM_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_45mm_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_45mm_SEM_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_50mm_VÃO' or rvtCodeValue[i][k] == 'EMBOCO_EXT_SERV_50mm_SEM_VÃO':
          codeCompositionParam.append('EMBOCO_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])  
        elif rvtCodeValue[i][k] == 'DIVISORIA_GRANITO' or rvtCodeValue[i][k] == 'DIVISORIA_PVC_PAINEL_VIDRO_PAINEL' or rvtCodeValue[i][k] == 'DIVISORIA_PVC_PAINEL_VIDRO' or rvtCodeValue[i][k] == 'DIVISORIA_PVC_PAINEL' or rvtCodeValue[i][k] == 'DIVISORIA_PISO_TETO_VIDRO' or rvtCodeValue[i][k] == 'DIVISORIA_PISO_TETO_PAINEL_VIDRO' or rvtCodeValue[i][k] == 'DIVISORIA_PISO_TETO_PAINEL' or rvtCodeValue[i][k] == 'DIVISORIA_EUCATEX_PAINEL_VIDRO_PAINEL' or rvtCodeValue[i][k] == 'DIVISORIA_EUCATEX_PAINEL_VIDRO' or rvtCodeValue[i][k] == 'DIVISORIA_EUCATEX_PAINEL':
          codeCompositionParam.append('DIVISORIA_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_10mm_<5m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_20mm_<5m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_10mm_>=5m2_E_<=10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_20mm_>=5m2_E_<=10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_10mm_>10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F1_SERV_20mm_>10m2':
          codeCompositionParam.append('EMBOCO_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_10mm_<5m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_20mm_<5m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_10mm_>=5m2_E_<=10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_20mm_>=5m2_E_<=10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_10mm_>10m2' or rvtCodeValue[i][k] == 'EMBOCO_INT_F2_SERV_20mm_>10m2':
          codeCompositionParam.append('EMBOCO_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_MEIA_PAREDE_SERV_33x45cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_SERV_33x45cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F1_SERV_33x45cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F1_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F1_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F1_SERV_5x10cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F1_MEIA_PAREDE_SERV_5x10cm_<5m2':
          codeCompositionParam.append('CERAMICA_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_MEIA_PAREDE_SERV_33x45cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_SERV_33x45cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_INT_F2_SERV_33x45cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F2_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANATO_INT_F2_MEIA_PAREDE_SERV_30x60cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm_<5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F2_SERV_5x10cm_>=5m2' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_INT_F2_MEIA_PAREDE_SERV_5x10cm_<5m2':
          codeCompositionParam.append('CERAMICA_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_UNICA_INT_F1_SERV_10mm' or rvtCodeValue[i][k] == 'MASSA_UNICA_INT_F1_SERV_20mm':
          codeCompositionParam.append('CERAMICA_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_UNICA_INT_F2_SERV_10mm' or rvtCodeValue[i][k] == 'MASSA_UNICA_INT_F2_SERV_20mm':
          codeCompositionParam.append('CERAMICA_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_50mm_SEM_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_45mm_SEM_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_35mm_SEM_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_25mm_SEM_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_50mm_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_45mm_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_35mm_VÃO' or rvtCodeValue[i][k] == 'MASSA_UNICA_EXT_SERV_25mm_VÃO':
          codeCompositionParam.append('MASSA_UNICA_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'SELADOR_PVA_INT_F1_SERV' or rvtCodeValue[i][k] == 'SELADOR_ACRILICO_INT_F1_SERV':
          codeCompositionParam.append('SELADOR_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'SELADOR_PVA_INT_F2_SERV' or rvtCodeValue[i][k] == 'SELADOR_ACRILICO_INT_F2_SERV':
          codeCompositionParam.append('SELADOR_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_EXT_SERV_5x10cm_SEM_VÃO' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_EXT_SERV_5x10cm_VÃO' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_EXT_SERV_5x5cm_SEM_VÃO' or rvtCodeValue[i][k] == 'CERAMICA_PORCELANA_EXT_SERV_5x5cm_VÃO':
          codeCompositionParam.append('CERAMICA_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'SELADOR_ACRILICO_EXT_MULTPAV_SERV_SEM_VÃO' or rvtCodeValue[i][k] == 'SELADOR_ACRILICO_EXT_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'SELADOR_ACRILICO_EXT_TERREO_SERV':
          codeCompositionParam.append('SELADOR_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_CORRIDA_LATEX_INT_F1_DUAS_DEMAOS_SERV' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_LATEX_INT_F1_UMA_DEMAO_SERV':
          codeCompositionParam.append('MASSA_CORRIDA_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_CORRIDA_LATEX_INT_F2_DUAS_DEMAOS_SERV' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_LATEX_INT_F2_UMA_DEMAO_SERV':
          codeCompositionParam.append('MASSA_CORRIDA_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_MULTPAV_SERV_SEM_VÃO' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_DUAS_DEMAOS_TERREO_SERV' or rvtCodeValue[i][k] == 'MASSA_CORRIDA_ACRILICA_EXT_UMA_DEMAO_TERREO_SERV':
          codeCompositionParam.append('MASSA_CORRIDA_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'PINTURA_PVA_INT_F1_SERV' or rvtCodeValue[i][k] == 'PINTURA_ACRILICA_INT_F1_SERV':
          codeCompositionParam.append('PINTURA_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'PINTURA_PVA_INT_F2_SERV' or rvtCodeValue[i][k] == 'PINTURA_ACRILICA_INT_F2_SERV':
          codeCompositionParam.append('PINTURA_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'PINTURA_ACRILICA_EXT_TERREO_SERV' or rvtCodeValue[i][k] == 'PINTURA_ACRILICA_EXT_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'PINTURA_ACRILICA_EXT_MULTPAV_SERV_SEM_VÃO':
          codeCompositionParam.append('PINTURA_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_INT_F1_SERV':
          codeCompositionParam.append('TEXTURA_INT_F1_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_INT_F2_SERV':
          codeCompositionParam.append('TEXTURA_INT_F2_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_UMA_COR_TERREO_SERV' or rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_TERREO_SERV' or rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_UMA_COR_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_MULTPAV_SERV_VÃO' or rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_UMA_COR_MULTPAV_SERV_SEM_VÃO' or rvtCodeValue[i][k] == 'TEXTURA_ACRILICA_EXT_DUAS_CORES_MULTPAV_SERV_SEM_VÃO':
          codeCompositionParam.append('TEXTURA_EXT_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'ENCUNHAMENTO_SERV':
          codeCompositionParam.append('ENCUNHAMENTO_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'ISOLAMENTO_DRYWALL_SERV':
          codeCompositionParam.append('ISOLAMENTO_DRYWALL_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'DEMOLIÇÃO_CERÂMICA_SERV':
          codeCompositionParam.append('DEMOLICAO_CERAMICA_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'APICOAMENTO_SERV':
          codeCompositionParam.append('APICOAMENTO_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])
        elif rvtCodeValue[i][k] == 'JA_0.9x2.15m_A' or rvtCodeValue[i][k] == 'PM1_1x2.1m_A':
          codeCompositionParam.append('ESQUADRIA_COMP_COD')
          codeCompositionValue.append(listOfCompCode[j])

# Assign your output to the OUT variable.
OUT = elements, codeCompositionParam, codeCompositionValue #paredes, código_param + código_value