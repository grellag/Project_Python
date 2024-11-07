```mermaid
%%{init: {'theme': 'forest', 'themeVariables': { 'handDrawn': true, 'fontSize': '6px', 'nodeSpacing': 5, 'padding': 2, 'edgeSpacingFactor': 0.2, 'lineHeight': 0.6 }}}%%
flowchart TD
    %% Inizio del processo
    A0([Avvia procedura SP_PBI_Container]) --> A1{Verifica esistenza di PBI_Container_temp}
    
    %% Condizione per l'esistenza della tabella temporanea
    A1 -- Sì --> A2([Elimina PBI_Container_temp])
    A1 -- No --> A3([Continua])
    A2 --> A4([Creazione tabella temporanea PBI_Container_temp])

    %% Inserimento dei dati
    A4 --> A5([Inserisci dati in PBI_Container_temp])

    %% Valorizzazione delle colonne (con colore per tabelle e function table)
    subgraph Valorizzazione Colonne di PBI_Container_temp
        style Valorizzazione Colonne di PBI_Container_temp fill:#f3f3f3,stroke:#bbb,stroke-width:2px
        
        B1([Valorizza colonna I_E]):::table --> B2([Valorizza colonna Booking_Number]):::table
        B2 --> B3([Valorizza colonna Bill_Of_Lading_Number]):::table
        B3 --> B4([Valorizza colonna Cargo_Shipment_Container_id]):::table
        B4 --> B5([Valorizza colonna Container_Number]):::table
        B5 --> B6([Valorizza colonna EQ_Type]):::table

        %% Function table valorizzazione
        B6 --> B7([Valorizza colonna Arrival_Date]):::functionTable
        B7 --> B8([Valorizza colonna Departure_Date]):::functionTable
        B8 --> B9([Valorizza colonna RemotePortUN]):::functionTable
    end

    %% Completamento dell'inserimento
    B9 --> C1([Completamento dell'inserimento in PBI_Container_temp])

    %% Transazione di aggiornamento finale
    C1 --> C2([Avvia transazione])
    C2 --> C3{PBI_Container esiste?}
    C3 -- Sì --> C4([Elimina tabella PBI_Container])
    C3 -- No --> C5([Continua])
    C4 --> C6([Rinomina PBI_Container_temp come PBI_Container])
    C5 --> C6
    C6 --> C7([Esegui commit della transazione])

    %% Aggiornamento della tabella DB_Param
    C7 --> D1([Aggiorna data nella tabella DB_Param])
    D1 --> D2([Fine del processo])

    %% Stile per tabelle e function table
    classDef table fill:#FFECB3,stroke:#B8860B,stroke-width:1px;
    classDef functionTable fill:#BBDEFB,stroke:#1E88E5,stroke-width:1px;

    %% Assegnazione delle classi per colore
    class B1,B2,B3,B4,B5,B6 table;
    class B7,B8,B9 functionTable;
