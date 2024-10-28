# Flusso Dati DCC Export Live

Questo diagramma mostra il flusso dei dati per aggiornare la tabella `PBI_Vessel_Reconciliation` con relazioni tra le tabelle, incluso l'uso degli indici, delle join e della funzione `FNTB_Container_Last_Event()`.

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
flowchart LR
    %% Definizione delle classi di stile
    classDef tempTable fill:#f9f,stroke:#333,stroke-width:4px
    classDef job fill:#bbf,stroke:#333,stroke-width:4px
    classDef job_refresh fill:#ffb,stroke:#333,stroke-width:4px
    classDef job_name fill:#bff,stroke:#333,stroke-width:4px
    classDef stored_proc fill:#bfb,stroke:#333,stroke-width:4px

    %% Tabelle temporanee e principali
    TempScheduleLegCTE["#TempScheduleLegCTE"]:::tempTable
    TempCSCCTE["#TempCSCCTE"]:::tempTable
    Z_PBI_Equipment_Event["#Z_PBI_Equipment_Event"]:::tempTable
    TempChargeData["#TempChargeData"]:::tempTable
    PBI_Vessel_Reconciliation_temp["PBI_Vessel_Reconciliation_temp"]:::tempTable

    %% Funzioni e database di aggiornamento
    FNTB_Container_Last_Event["FNTB_Container_Last_Event()"]
    OVAVREC_FNTB_CSC_Hazardous_Info["OVAVREC_FNTB_CSC_Hazardous_Info()"]
    DCC_Export_FTC["DCC_Export_FTC"]
    DCC_Export_DOC_Date_Time["DCC_Export_DOC_Date_Time"]
    Bill_Of_Lading["Bill_Of_Lading"]
    FNTB_Schedule_Leg_TSPorts["FNTB_Schedule_Leg_TSPorts()"]
    FNTB_Schedule_Leg_TS_ETA_ETD_Cache["FNTB_Schedule_Leg_TS_ETA_ETD_Cache()"]
    Cargo_Container_Transship["Cargo_Container_Transship"]
    Casp_File_7_Container["Casp_File_7_Container"]
    Casp_File_7["Casp_File_7"] 


    %% Flusso dei dati e join
    TempScheduleLegCTE -->|Join usando idx_TempScheduleLegCTE_schedule_leg_id su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    TempCSCCTE -->|Join usando idx_TempCSCCTE su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    Z_PBI_Equipment_Event -->|Update usando idx_Z_PBI_Equipment_Event su Event_Id e Equipment_Id| PBI_Vessel_Reconciliation_temp
    TempChargeData -->|Update usando idx_TempChargeData su Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    OVAVREC_FNTB_CSC_Hazardous_Info -->|Update 18 colonne usando Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    Bill_Of_Lading -->|Update 9 colonne usando Bill_Of_Lading_id| PBI_Vessel_Reconciliation_temp
    Casp_File_7 -->|Update 8 colonne OBLX usando Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    Casp_File_7_Container -->|Update 8 colonne OBLX usando Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    FNTB_Schedule_Leg_TSPorts -->|Update 4 colonne usando Schedule_Leg_id se Transship=S| PBI_Vessel_Reconciliation_temp
    FNTB_Schedule_Leg_TS_ETA_ETD_Cache -->|Update 11 colonne usando Schedule_Leg_id se Transship=S| PBI_Vessel_Reconciliation_temp
    Cargo_Container_Transship -->|Update 13 colonne usando Cargo_Container_id se Transship=D| PBI_Vessel_Reconciliation_temp
    PBI_Vessel_Reconciliation_temp -->|Inner JOIN| SP_PBI_Vessel_Reconciliation_CSC_VGM

%% Relazioni di update
FNTB_Container_Last_Event -->|Aggiorna Last Event Date, Last Event DateTime, Last Event Type, Last Event Description| PBI_Vessel_Reconciliation_temp
DCC_Export_FTC -->|Aggiorna FTC_Flag = 1 | PBI_Vessel_Reconciliation_temp
DCC_Export_DOC_Date_Time -->|Aggiorna 5 colonne: Originals_Last_Set_Printed_Date as OBL_PRINTED + EXPORT_DOC_TO_CASHIER + CASHIER_RECEIVED_FROM_EXPORT + OBL_SENT_TO_CUSTOMER + BL_TELEX_RELEASE_date | PBI_Vessel_Reconciliation_temp
DCC_Payment_Term -->|Aggiorna Deferred_Payment_613, Deferred_Payment_fob, Inv_Company_Address_613, Inv_Company_Address_fob, Inv_Company_Address_id_613, Inv_Company_Address_id_fob, Payment_Type_613 | PBI_Vessel_Reconciliation_temp
#VGMInfoTemp -->|Aggiorna 28 colonne | PBI_Vessel_Reconciliation_temp
PBI_DCC_Export_Planner -->|Aggiorna 10 colonne | PBI_Vessel_Reconciliation_temp
PBI_DCC_Export_H_Cache_final -->|Aggiorna 550 colonne | PBI_Vessel_Reconciliation_temp

Interlink_DFeed90 -->|Aggiorna dati| FNTB_Container_Last_Event
Interlink_DFeed90 -->|Aggiorna dati| OVAVREC_FNTB_CSC_Hazardous_Info
Interlink_DFeed90 -->|Aggiorna dati| FNTB_Schedule_Leg_TSPorts
Interlink_DFeed90 -->|Importa dati| FNTB_Schedule_Leg_TS_ETA_ETD_Cache
Interlink_Main90 -->|Importa dati| DOC_DATE_TIME
Interlink_Main90 -->|Importa dati| BL_CHARGE_TEXT

Interlink_Main90 -->|Importa dati| Cargo_Container_Transship
Interlink_Main90 -->|Importa dati| Bill_Of_Lading
Interlink_Main90 -->|Importa dati| Casp_File_7
Interlink_Main90 -->|Importa dati| Casp_File_7_Container

BL_CHARGE_TEXT -->|Importa dati| DCC_Export_FTC
DOC_DATE_TIME -->|Importa dati| DCC_Export_DOC_Date_Time

Job_PBI_Export_ScheduleLeg:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 10 minuti| SP_PBI_DCC_Export_Schedule_Leg_Cache:::job_refresh
SP_PBI_DCC_Export_Schedule_Leg_Cache -->|Import Data| TempScheduleLegCTE:::stored_proc

Job_PBI_Export_CSC:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 15 minuti| SP_PBI_Build_BK_BL_CSC_Export_Cache:::job_refresh
SP_PBI_Build_BK_BL_CSC_Export_Cache -->|Import Data| TempCSCCTE:::stored_proc

Job_PBI_Trasporti_Eq_Events:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 15 minuti| SP_PBI_Equipment_Event_EQ_Events:::job_refresh
SP_PBI_Equipment_Event_EQ_Events -->|Import Data| Z_PBI_Equipment_Event:::stored_proc

Job_PBI_Charge_ALL:::job_name -->|Refresh Data: dalle 10:00 AM, ogni 2 ore| SP_PBI_Build_Charge_Lenavi_MEDLOG:::job_refresh
SP_PBI_Build_Charge_Lenavi_MEDLOG -->|Import Data| TempChargeData:::stored_proc

Job_PBI_Payment_Term:::job_name -->|Refresh Data: dalle 07:30 AM, ogni 40 minuti| SP_PBI_BL_List_by_freight_debtor:::job_refresh
SP_PBI_BL_List_by_freight_debtor -->|Import Data| DCC_Payment_Term:::stored_proc

Job_PBI_VGM_Info:::job_name -->|Refresh Data: dalle 06:55 AM, ogni 15 minuti| SP_PBI_Vessel_Reconciliation_CSC_VGM:::job_refresh
SP_PBI_Vessel_Reconciliation_CSC_VGM -->|Import Data| #VGMInfoTemp:::stored_proc

Job_PBI_Planner:::job_name -->|Refresh Data: dalle 06:55 AM, ogni 15 minuti| get_Planner_NextPOD_CT:::job_refresh
get_Planner_NextPOD_CT -->|Import Data| PBI_DCC_Export_Planner:::stored_proc

Job_PBI_Planner:::job_name -->|Refresh Data: dalle 06:55 AM, ogni 15 minuti| SP_PBI_DCC_EXPORT_H_Cache_Final:::job_refresh
SP_PBI_DCC_EXPORT_H_Cache_Final -->|Import Data| PBI_DCC_Export_H_Cache_vw:::stored_proc
PBI_DCC_Export_H_Cache_vw -->|Importa dati| PBI_DCC_Export_H_Cache_final_temp

PBI_DCC_Export_H_Cache_final_temp -->|Rename Table| PBI_DCC_Export_H_Cache_final
