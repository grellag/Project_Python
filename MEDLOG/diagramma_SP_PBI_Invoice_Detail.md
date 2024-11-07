```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'handDrawn': true, 'fontSize': '10px', 'nodeSpacing': 10, 'padding': 5 }}}%%
flowchart TD
    %% Inizio del processo
    A0([Avvia processo di creazione PBI_Invoice_Detail]) --> A1([Verifica ed elimina tabella esistente PBI_Invoice_Detail])

    %% Selezione e inserimento dei dati
    A1 --> A2([Seleziona campi da ACC_Invoice, ACC_Invoice_Detail e Charge])

    subgraph Creazione e valorizzazione di PBI_Invoice_Detail
        style Creazione e valorizzazione di PBI_Invoice_Detail fill:#f3f3f3,stroke:#bbb,stroke-width:2px
        
        B1([Invoice_id: I.ACC_Invoice_id]):::table --> B2([Invoice_Number: I.Invoice_Number]):::table
        B2 --> B3([Bill_Of_Lading: I.Bill_Of_Lading]):::table
        B3 --> B4([Original_Date: I.Original_Date]):::table
        B4 --> B5([ACC_Invoice_Detail_id: D.ACC_Invoice_Detail_id]):::table
        B5 --> B6([Charge_id: D.Charge_idx]):::table
        B6 --> B7([Chg_Amount: C.Result_Std]):::table
        B7 --> B8([Currency_id: C.Adjust_Currency_id]):::table
        B8 --> B9([Inv_Amount: D.Result_Standard_Local_Currency]):::table

        %% Campi calcolati
        B9 --> C1([Is_Charge_Deleted: CASE WHEN C.Charge_id IS NULL THEN 1 ELSE 0]):::calculated
        C1 --> C2([RemotePort: CASE WHEN Import_Export_Type = 'E' THEN Port_Of_Discharge ELSE Port_Of_Loading]):::calculated
        C2 --> C3([RemotePortUN: CASE WHEN Import_Export_Type = 'E' THEN POD_City_Code ELSE POL_City_Code]):::calculated
    end

    %% Condizione per anno e completamento del processo
    C3 --> D1([Filtro: WHERE Original_Date >= 2022])
    D1 --> D2([Inserimento in PBI_Invoice_Detail])
    D2 --> E1([Fine del processo])
    
    %% Stile per tabelle e campi calcolati
    classDef table fill:#FFECB3,stroke:#B8860B,stroke-width:1px;
    classDef calculated fill:#BBDEFB,stroke:#1E88E5,stroke-width:1px;

    %% Assegnazione delle classi per colore
    class B1,B2,B3,B4,B5,B6,B7,B8,B9 table;
    class C1,C2,C3 calculated;
