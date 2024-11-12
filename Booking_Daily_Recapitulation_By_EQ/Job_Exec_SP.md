# SQL Server Job Execution Diagram

## Container Diagram for SQL Server Job

Il seguente diagramma rappresenta l'esecuzione della stored procedure `SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ` come step di un job SQL Server: `[LN][Rebuild Cache] - PBI - Booking Daily Recapitulation`. Il diagramma mostra i parametri passati e la relazione tra il job, lo script SQL e la stored procedure nel database.

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
flowchart LR
    job["Job:<br>[LN][Rebuild Cache]-PBI-Booking Daily Recapitulation<br>Executes a s.p."]

    sql_job["SQL Server Job<br>Executes s.p. with parameters"]

    db["Database [OVA-PR-IT-REP02].Lenavi_LOCAL"]

    stored_proc["SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ<br>S.P.<br>Generates daily booking recap by equipment"]

    job         -->     |On schedule|sql_job
    sql_job     -->     |With parameters|stored_proc
    stored_proc -->     |Executes query on|db
```