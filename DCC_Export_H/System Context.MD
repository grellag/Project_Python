# Diagramma di Controllo Documentazione

```mermaid
graph TB
    classDef boundary fill:#FFEBCD,stroke:#333,stroke-width:2px;

    %% Define departments at the top
    subgraph "Departments"
        direction LR
        Accounting["Accounting Department"]
        ExportCommercials["Export Commercials"]
        FreightCashier["Freight Cashier"]
        DocumentationOffice["Documentation Office"]
        PortOperationsOffice["Port Operations Office"]
    end

    %% Center the Documentation Control Console (DCC)
    classDef central fill:#8AC6D1,stroke:#333,stroke-width:2px;
    DCC["Documentation Control Console (DCC)"]:::central

    %% Define data sources at the bottom
    subgraph boundary ["Data Sources"]
        direction LR
        MSCLink["MSCLink System"]
        SharePoint["SharePoint Folders (Excel Files)"]
        BarcodeReader["Barcode Reading Tools"]
    end

    %% Connections from departments to DCC
    Accounting -->|Accesses Reports| DCC
    ExportCommercials -->|Accesses Reports| DCC
    FreightCashier -->|Accesses Reports| DCC
    DocumentationOffice -->|Accesses Reports| DCC
    PortOperationsOffice -->|Accesses Reports| DCC

    %% Connections from data sources to DCC
    MSCLink -->|Data Feed| DCC
    SharePoint -->|Data Feed| DCC
    BarcodeReader -->|Data Feed| DCC
