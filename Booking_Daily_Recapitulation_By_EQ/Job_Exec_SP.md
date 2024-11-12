# SQL Server Job Execution Diagram

## Container Diagram for SQL Server Job

Il seguente diagramma rappresenta l'esecuzione <br><br>della stored procedure `SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ` <br><br>come step di un job SQL Server: `[LN][Rebuild Cache] - PBI - Booking Daily Recapitulation`.<br><br>Il diagramma mostra i parametri passati e la relazione tra:

1. il job  
2. lo script SQL  
3. la stored procedure nel database

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
flowchart TB
    %% Definisci una classe personalizzata per il nodo parameters
    classDef parametersStyle fill:#e6f7ff,stroke:#007acc,stroke-width:2px,color:#333,font-weight:bold;
    classDef jobStyle fill:#FFD700,stroke:#333,stroke-width:2px,color:#333,font-weight:bold;
    classDef storedProcStyle fill:#8AC6D1,stroke:#333,stroke-width:2px,color:#333,font-weight:bold;
    classDef databaseStyle fill:#D1C4E9,stroke:#333,stroke-width:2px,color:#333,font-weight:bold;
    classDef scheduleStyle fill:#C5E1A5,stroke:#333,stroke-width:2px,color:#333,font-weight:bold;

    job["Job:<br>[LN][Rebuild Cache]-PBI-Booking Daily Recapitulation<br>Executes a s.p."]

    sql_job["SQL Server Job<br>Executes s.p. with parameters"]

    schedule["Job Schedule<br><b>Start Date:</b> 2020-10-09<br><b>End Date:</b> 9999-12-31<br><b>Frequency:</b> Every 30 mins from 09:00 to 15:00"]

    db["Database [OVA-PR-IT-REP02].Lenavi_LOCAL"]

    stored_proc["SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ<br>S.P.<br>Generates daily booking recap by equipment"]

    %% Simula l'allineamento a sinistra utilizzando <div> con text-align:left
    parameters["<div style='text-align:left'>
    Parameters:<br>
    - @DBToken_Id: INT<br>
    - @POL_Id: INT<br>
    - @Days_Back: INT<br>
    - @StartBookingDate: DATE<br>
    - @EndBookingDate: DATE<br>
    - @Service: INT<br>
    - @Is_Spadoni: INT<br>
    - @BK_#: VARCHAR(20)
    </div>"]

    %% Applica lo stile personalizzato al nodo parameters
    class parameters parametersStyle;
    %% Applica gli stili personalizzati ai nodi specifici
    class job jobStyle;
    class stored_proc storedProcStyle;
    class db databaseStyle;
    class schedule scheduleStyle;

    job         -->     |On schedule|sql_job
    sql_job     -->     |With parameters|stored_proc
    stored_proc -->     |Executes query on|db
    job -->|Has schedule| schedule
    sql_job -->|Passes| parameters
    parameters -->|Parameters to| stored_proc
```