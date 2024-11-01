# Diagramma di Controllo Documentazione

```mermaid
graph TB
    classDef boundary fill:#FFEBCD,stroke:#333,stroke-width:2px;

    subgraph "Documentation Control Console (Power BI)"
        class PowerBI fill:#8AC6D1,stroke:#333,stroke-width:2px;
        PowerBI["Documentation Control Console (Power BI)"]
    end

    Accounting[Accounting Department] -->|Accesses Reports| PowerBI
    ExportCommercials[Export Commercials] -->|Accesses Reports| PowerBI
    FreightCashier[Freight Cashier] -->|Accesses Reports| PowerBI
    DocumentationOffice[Documentation Office] -->|Accesses Reports| PowerBI
    PortOperationsOffice[Port Operations Office] -->|Accesses Reports| PowerBI

    subgraph boundary ["Data Sources"]
        MSCLink[MSCLink System]
        SharePoint[SharePoint Folders (Excel Files)]
        BarcodeReader[Barcode Reading Tools]
    end

    MSCLink -->|Data Feed| PowerBI
    SharePoint -->|Data Feed| PowerBI
    BarcodeReader -->|Data Feed| PowerBI

