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
    %% Tabelle temporanee e principali
    TempScheduleLegCTE["#TempScheduleLegCTE\nIndice Clustered: idx_TempScheduleLegCTE_schedule_leg_id\nColonna: Schedule_Leg_id"]
    TempCSCCTE["#TempCSCCTE\nIndice Clustered: idx_TempCSCCTE\nColonna: Schedule_Leg_id"]
    Z_PBI_Equipment_Event["#Z_PBI_Equipment_Event\nIndice Clustered: idx_Z_PBI_Equipment_Event\nColonne: Event_Id, Equipment_Id"]
    PBI_Vessel_Reconciliation_temp["LeNavi_LOCAL.dbo.PBI_Vessel_Reconciliation_temp\nIndice Clustered: PK_PBI_Vessel_Reconciliation_temp\nColonna: ID"]

    %% Funzioni e database di aggiornamento
    FNTB_Container_Last_Event["FNTB_Container_Last_Event() - da Interlink_DFeed90"]

    %% Flusso dei dati e join
    TempScheduleLegCTE -->|Join usando idx_TempScheduleLegCTE_schedule_leg_id su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    TempCSCCTE -->|Join usando idx_TempCSCCTE su Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    Z_PBI_Equipment_Event -->|Update usando idx_Z_PBI_Equipment_Event su Event_Id e Equipment_Id| PBI_Vessel_Reconciliation_temp

%% Relazioni di update
FNTB_Container_Last_Event -->|Aggiorna Last Event Date, Last Event DateTime, Last Event Type, Last Event Description| PBI_Vessel_Reconciliation_temp
Interlink_DFeed90 -->|Aggiorna dati| FNTB_Container_Last_Event
