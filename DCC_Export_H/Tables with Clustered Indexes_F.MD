# Flusso dei Dati Aggiornato

Questo diagramma mostra il flusso dei dati tra le tabelle, incluso l'uso degli indici, delle join, e della funzione `FNTB_Container_Last_Event()`.

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
flowchart TD
    %% Tabelle temporanee e principali
    TempScheduleLegCTE["#TempScheduleLegCTE"]
    TempCSCCTE["#TempCSCCTE"]
    Z_PBI_Equipment_Event["#Z_PBI_Equipment_Event"]
    PBI_Vessel_Reconciliation_temp["LeNavi_LOCAL.dbo.PBI_Vessel_Reconciliation_temp"]

    %% Funzioni e database di aggiornamento
    FNTB_Container_Last_Event["FNTB_Container_Last_Event() - da Interlink_DFeed90"]

    %% Flusso dei dati e join
    TempScheduleLegCTE -->|Usa indice Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    TempCSCCTE -->|Usa indice Schedule_Leg_id| PBI_Vessel_Reconciliation_temp
    Z_PBI_Equipment_Event -->|Usa indice per Update| PBI_Vessel_Reconciliation_temp

    %% Relazioni di update
    FNTB_Container_Last_Event --> PBI_Vessel_Reconciliation_temp
    Interlink_DFeed90 -->|Aggiorna dati| FNTB_Container_Last_Event
