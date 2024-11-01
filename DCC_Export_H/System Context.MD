# Diagramma di Controllo Documentazione

```mermaid
flowchart TB
    classDef departmentColor fill:#FFD700,stroke:#333,stroke-width:2px;  %% Top color
    classDef dccColor fill:#8AC6D1,stroke:#333,stroke-width:2px;         %% Center color
    classDef dataSourceColor fill:#FF6347,stroke:#333,stroke-width:2px;  %% Bottom color
    classDef invis stroke-width:0px,fill:none;

    %% Departments (Top)
    subgraph Departments ["Departments"]
        direction TB
        Accounting["Accounting Department"]:::departmentColor
        ExportCommercials["Export Commercials"]:::departmentColor
        FreightCashier["Freight Cashier"]:::departmentColor
        DocumentationOffice["Documentation Office"]:::departmentColor
        PortOperationsOffice["Port Operations Office"]:::departmentColor
    end

    %% Central DCC Node
    DCC["Documentation Control Console (DCC)"]:::dccColor

    %% Data Sources (Bottom)
    subgraph DataSources ["Data Sources"]
        direction TB
        MSCLink["MSCLink System"]:::dataSourceColor
        SharePoint["SharePoint Folders (Excel Files)"]:::dataSourceColor
        BarcodeReader["Barcode Reading Tools"]:::dataSourceColor
    end

    %% Invisible Node to Bridge Layout Without Affecting Positioning
    invisConnector[ ]:::invis

    %% Connections with Layout Constraints
    Departments -->|Accesses Reports| DCC
    MSCLink -->|Data Feed| invisConnector
    SharePoint -->|Data Feed| invisConnector
    BarcodeReader -->|Data Feed| invisConnector
    invisConnector --> DCC
