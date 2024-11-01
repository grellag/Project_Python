# Diagramma di Controllo Documentazione

```mermaid
flowchart TB
    classDef boundary fill:#FFEBCD,stroke:#333,stroke-width:2px;

    %% Departments (Top)
    subgraph Departments ["Departments"]
        direction TB
        Accounting["Accounting Department"]
        ExportCommercials["Export Commercials"]
        FreightCashier["Freight Cashier"]
        DocumentationOffice["Documentation Office"]
        PortOperationsOffice["Port Operations Office"]
    end

    %% Central DCC Node
    DCC["Documentation Control Console (DCC)"]:::central

    %% Data Sources (Bottom)
    subgraph DataSources ["Data Sources"]
        direction TB
        MSCLink["MSCLink System"]
        SharePoint["SharePoint Folders (Excel Files)"]
        BarcodeReader["Barcode Reading Tools"]
    end

    %% Connections to Central DCC Node
    Departments -->|Accesses Reports| DCC
    DCC -->|Data Feed| DataSources

    %% Class Definitions for Styling
    class DCC fill:#8AC6D1,stroke:#333,stroke-width:2px;
