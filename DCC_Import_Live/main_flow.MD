```mermaid
---
config:
  look: handDrawn
  theme: forest
---
flowchart LR
    A((PBI_BK_BL_CSC)) --(popola)--> Z_PBI_BK_BL_CSC_IMPORT
    A1((LNAV_ACC_ALL_Charges_cache)) --(popola)--> LNAV_ACC_ALL_CHARGES_CACHE_IMPORT
    A2((Interlink_DFeed90.dfeed.FNTB_TSPorts_CSC)) --(popola)--> Z_PBI_BK_BL_CSC_IMPORT_TS
    A3((Z_PBI_Dwell_Import)) --(popola)--> Z_PBI_BK_BL_CSC_IMPORT_IDV

    subgraph Calcolo e Staging
      Z_PBI_BK_BL_CSC_IMPORT --(JOIN)--> T((PBI_DCC_Import_cache_temp))
      Z_PBI_BK_BL_CSC_IMPORT_TS --(JOIN)--> T
      Z_PBI_BK_BL_CSC_IMPORT_IDV --(JOIN)--> T
      LNAV_ACC_ALL_CHARGES_CACHE_IMPORT --(JOIN)--> T
      PBI_CHARGE_ILIM_CACHE --(JOIN)--> T
      PBI_ADDITIONAL_INFO_AGENCY_INVOICES --(JOIN)--> T
      PBI_DCC_Intermodal_cache --(JOIN)--> T
      PBI_DCC_Import_Pending_emc_cache --(JOIN)--> T
      PBI_VPC_Local_Actual_ToBeNotified --(JOIN)--> T
      PBI_DCC_Import_Disch_Ves_temp --(JOIN)--> T
    end

    T --(RENAME/FINALE)--> PBI_DCC_Import_cache
```