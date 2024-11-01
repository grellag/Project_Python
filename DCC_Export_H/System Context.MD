# Diagramma di Controllo Documentazione

```mermaid
flowchart TB
    classDef boundary fill:#FFEBCD,stroke:#333,stroke-width:2px;

    %% Central DCC Node
    DCC["Documentation Control Console (DCC)"]:::central

    %% Departments (Top)
    Accounting["Accounting Department"] -->|Accesses Reports| DCC
    ExportCommercials["Export Commercials"] -->|Accesses Reports| DCC
    FreightCashier["Freight Cashier"] -->|Accesses Reports| DCC
    DocumentationOffice["Documentation Office"] -->|Accesses Reports| DCC
    PortOperationsOffice["Port Operations Office"] -->|Accesses Reports| DCC

    %% Data Sources (Bottom)
    MSCLink["MSCLink System"] -->|Data Feed| DCC
    SharePoint["SharePoint Folders (Excel Files)"] -->|Data Feed| DCC
    BarcodeReader["Barcode Reading Tools"] -->|Data Feed| DCC

    %% Layout Adjustments for Top/Bottom Positioning
    subgraph Top[" "]
        direction TB
        Accounting
        ExportCommercials
        FreightCashier
        DocumentationOffice
        PortOperationsOffice
    end

    subgraph Bottom[" "]
        direction TB
        MSCLink
        SharePoint
        BarcodeReader
    end

    class DCC fill:#8AC6D1,stroke:#333,stroke-width:2px;



