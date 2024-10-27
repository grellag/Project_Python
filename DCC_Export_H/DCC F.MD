# Flusso dei Dati PBI_Vessel_Reconciliation

Questo diagramma mostra il flusso dei dati per aggiornare la tabella `PBI_Vessel_Reconciliation` con relazioni tra le tabelle, incluso l'uso degli indici, delle join e della funzione `FNTB_Container_Last_Event()`.

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
flowchart TD
    %% Definizione delle classi di stile
    classDef tempTable fill:#f9f,stroke:#333,stroke-width:4px
    classDef job fill:#bbf,stroke:#333,stroke-width:4px
    classDef stored_proc fill:#bfb,stroke:#333,stroke-width:4px

    %% Tabelle temporanee e principali
    TempScheduleLegCTE["#TempScheduleLegCTE"]:::tempTable
    TempCSCCTE["#TempCSCCTE"]:::tempTable
    Z_PBI_Equipment_Event["#Z_PBI_Equipment_Event"]:::tempTable
    TempChargeData["#TempChargeData"]:::tempTable
    PBI_Vessel_Reconciliation_temp["PBI_Vessel_Reconciliation_temp"]:::tempTable

    %% Funzioni e database di aggiornamento
    FNTB_Container_Last_Event["FNTB_Container_Last_Event() - da Interlink_DFeed90"]

    %% Flusso dei dati e join
    TempScheduleLegCTE -->|Join usando idx_TempScheduleLegCTE_schedule_leg_id su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    TempCSCCTE -->|Join usando idx_TempCSCCTE su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    Z_PBI_Equipment_Event -->|Update usando idx_Z_PBI_Equipment_Event su Event_Id e Equipment_Id| PBI_Vessel_Reconciliation_temp
    TempChargeData -->|Update usando idx_TempChargeData su Cargo_Shipment_Container_id| PBI_Vessel_Reconciliation_temp

%% Relazioni di update
FNTB_Container_Last_Event -->|Aggiorna Last Event Date, Last Event DateTime, Last Event Type, Last Event Description| PBI_Vessel_Reconciliation_temp
Interlink_DFeed90 -->|Aggiorna dati| FNTB_Container_Last_Event
SP_PBI_DCC_Export_Schedule_Leg_Cache -->|Import Data| TempScheduleLegCTE:::stored_proc
Job_PBI_Export_ScheduleLeg -->|Refresh Data| SP_PBI_DCC_Export_Schedule_Leg_Cache:::job
SP_PBI_Build_BK_BL_CSC_Export_Cache -->|Import Data| TempCSCCTE:::stored_proc
Job_PBI_Export_CSC -->|Refresh Data| SP_PBI_Build_BK_BL_CSC_Export_Cache:::job
SP_PBI_Equipment_Event_EQ_Events -->|Import Data| Z_PBI_Equipment_Event:::stored_proc
Job_PBI_Trasporti_Eq_Events -->|Refresh Data| SP_PBI_Equipment_Event_EQ_Events:::job
SP_PBI_Build_Charge_Lenavi_MEDLOG -->|Import Data| Z_PBI_Equipment_Event:::stored_proc
Job_PBI_Charge_ALL -->|Refresh Data| SP_PBI_Equipment_Event_EQ_Events:::job