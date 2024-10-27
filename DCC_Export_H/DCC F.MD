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
    FNTB_Schedule_Leg_TSPorts["FNTB_Schedule_Leg_TSPorts(null)"]
    FNTB_Schedule_Leg_TS_ETA_ETD_Cache["FNTB_Schedule_Leg_TS_ETA_ETD_Cache()"]
    Cargo_Container_Transship["Cargo_Container_Transship"]


    %% Flusso dei dati e join
    TempScheduleLegCTE -->|Join usando idx_TempScheduleLegCTE_schedule_leg_id su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    TempCSCCTE -->|Join usando idx_TempCSCCTE su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    Z_PBI_Equipment_Event -->|Update usando idx_Z_PBI_Equipment_Event su Event_Id e Equipment_Id| PBI_Vessel_Reconciliation_temp
    TempChargeData -->|Update usando idx_TempChargeData su Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    OVAVREC_FNTB_CSC_Hazardous_Info -->|Update 18 colonne usando Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp
    Bill_Of_Lading -->|Update 9 colonne usando Bill_Of_Lading_id| PBI_Vessel_Reconciliation_temp
    FNTB_Schedule_Leg_TSPorts -->|Update 4 colonne usando Schedule_Leg_id se Transship=S| PBI_Vessel_Reconciliation_temp
    FNTB_Schedule_Leg_TS_ETA_ETD_Cache -->|Update 11 colonne usando Schedule_Leg_id se Transship=S| PBI_Vessel_Reconciliation_temp
    Cargo_Container_Transship -->|Update 13 colonne usando Cargo_Container_id se Transship=D| PBI_Vessel_Reconciliation_temp

%% Relazioni di update
FNTB_Container_Last_Event -->|Aggiorna Last Event Date, Last Event DateTime, Last Event Type, Last Event Description| PBI_Vessel_Reconciliation_temp
DCC_Export_FTC -->|Aggiorna . . . | PBI_Vessel_Reconciliation_temp
DCC_Export_DOC_Date_Time -->|Aggiorna . . . | PBI_Vessel_Reconciliation_temp
Interlink_DFeed90 -->|Aggiorna dati| FNTB_Container_Last_Event
Interlink_DFeed90 -->|Aggiorna dati| OVAVREC_FNTB_CSC_Hazardous_Info
Interlink_DFeed90 -->|Aggiorna dati| FNTB_Schedule_Leg_TSPorts(null)
Interlink_DFeed90  -->|Importa dati| FNTB_Schedule_Leg_TS_ETA_ETD_Cache()
Interlink_Main90 -->|Importa dati| DOC_DATE_TIME
Interlink_Main90 -->|Importa dati| BL_CHARGE_TEXT

Interlink_Main90 -->|Importa dati| Cargo_Container_Transship
Interlink_Main90 -->|Importa dati| Bill_Of_Lading

BL_CHARGE_TEXT -->|Importa dati| DCC_Export_FTC
DOC_DATE_TIME -->|Importa dati| DCC_Export_DOC_Date_Time
SP_PBI_DCC_Export_Schedule_Leg_Cache -->|Import Data| TempScheduleLegCTE:::stored_proc
Job_PBI_Export_ScheduleLeg:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 10 minuti| SP_PBI_DCC_Export_Schedule_Leg_Cache:::job_refresh
SP_PBI_Build_BK_BL_CSC_Export_Cache -->|Import Data| TempCSCCTE:::stored_proc
Job_PBI_Export_CSC:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 15 minuti| SP_PBI_Build_BK_BL_CSC_Export_Cache:::job_refresh
SP_PBI_Equipment_Event_EQ_Events -->|Import Data| Z_PBI_Equipment_Event:::stored_proc
Job_PBI_Trasporti_Eq_Events:::job_name -->|Refresh Data: dalle 07:00 AM, ogni 15 minuti| SP_PBI_Equipment_Event_EQ_Events:::job_refresh
SP_PBI_Build_Charge_Lenavi_MEDLOG -->|Import Data| TempChargeData:::stored_proc
Job_PBI_Charge_ALL:::job_name -->|Refresh Data: dalle 10:00 AM, ogni 2 ore| SP_PBI_Build_Charge_Lenavi_MEDLOG:::job_refresh