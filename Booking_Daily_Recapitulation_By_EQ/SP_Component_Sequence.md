# Sequence Diagram delle Operazioni SQL

## Diagramma di Sequenza per le Operazioni di `SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ`

Il seguente diagramma mostra la sequenza di operazioni eseguite dalla stored procedure `SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ`, inclusi i `TRUNCATE`, `INSERT`, e `UPDATE` sulle tabelle principali.

```mermaid
sequenceDiagram
    participant SP as SP_RPT_GOA_Booking_Daily_Recapitulation_By_EQ
    participant ZRPT as LeNavi_LOCAL.dbo.Z_RPT_GOA_Booking_Daily_Recapitulation
    participant MyZRPT as Interlink_Temp90.dbo.My_Z_RPT_GOA_Booking_Daily_Recapitulation
    participant DBParam as dbo.DB_Param

    %% Sequenza delle operazioni
    SP ->> ZRPT: TRUNCATE TABLE Z_RPT_GOA_Booking_Daily_Recapitulation

    SP ->> MyZRPT: DELETE FROM My_Z_RPT_GOA_Booking_Daily_Recapitulation
    SP ->> MyZRPT: INSERT INTO My_Z_RPT_GOA_Booking_Daily_Recapitulation (data from FNTB_Booking_BL_CSC_Daily_Bk_Recap_By_EQ)

    SP ->> MyZRPT: UPDATE My_Z_RPT_GOA_Booking_Daily_Recapitulation (data from FNTB_AssocDocCompany)
    SP ->> MyZRPT: UPDATE My_Z_RPT_GOA_Booking_Daily_Recapitulation (totals from FNTB_Charge_Cargo_Shipment_Container)
    
    SP ->> ZRPT: INSERT INTO Z_RPT_GOA_Booking_Daily_Recapitulation (distinct records from My_Z_RPT_GOA)

    SP ->> DBParam: UPDATE DB_Param (set timestamp)
```