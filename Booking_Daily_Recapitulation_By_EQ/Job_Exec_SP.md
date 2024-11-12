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
flowchart TB
    job["Job:<br>[LN][Rebuild Cache]-PBI-Booking Daily Recapitulation<br>Executes a s.p."]

    sql_job["SQL Server Job<br>Executes s.p. with parameters"]

    schedule["Job Schedule<br><b>Start Date:</b> 2020-10-09<br><b>End Date:</b> 9999-12-31<br><b>Frequency:</b> Every 30 mins from 09:00 to 15:00"]

    db["Database [OVA-PR-IT-REP02].Lenavi_LOCAL"]

    stored_proc["SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ<br>S.P.<br>Generates daily booking recap by equipment"]

    parameters["Parameters:<br>
    - @DBToken_Id: INT<br>
    - @POL_Id: INT<br>
    - @Days_Back: INT<br>
    - @StartBookingDate: DATE<br>
    - @EndBookingDate: DATE<br>
    - @Service: INT<br>
    - @Is_Spadoni: INT<br>
    - @BK_#: VARCHAR(20)"]

    job         -->     |On schedule|sql_job
    sql_job     -->     |With parameters|stored_proc
    stored_proc -->     |Executes query on|db
    job -->|Has schedule| schedule
    sql_job -->|Passes| parameters
    parameters -->|Parameters to| stored_proc
```