
# Diagramma di Controllo Documentazione

```mermaid
flowchart TB
    classDef boundary fill:#FFEBCD,stroke:#333,stroke-width:2px;

    %% Invisible Spacer Nodes to Force Layout
    invisTop[ ]:::invis
    invisBottom[ ]:::invis

    %% Central DCC Node
    DCC["Documentation Control Console (DCC)"]:::central

    %% Departments (Top)
    invisTop --> Accounting["Accounting Department"] -->|Accesses Reports| DCC
    invisTop --> ExportCommercials["Export Commercials"] -->|Accesses Reports| DCC
    invisTop --> FreightCashier["Freight Cashier"] -->|Accesses Reports| DCC
    invisTop --> DocumentationOffice["Documentation Office"] -->|Accesses Reports| DCC
    invisTop --> PortOperationsOffice["Port Operations Office"] -->|Accesses Reports| DCC

    %% Data Sources (Bottom)
    DCC -->|Data Feed| MSCLink["MSCLink System"]
    DCC -->|Data Feed| SharePoint["SharePoint Folders (Excel Files)"]
    DCC -->|Data Feed| BarcodeReader["Barcode Reading Tools"]
    MSCLink --> invisBottom
    SharePoint --> invisBottom
    BarcodeReader --> invisBottom

    %% Class Definitions for Styling
    class DCC fill:#8AC6D1,stroke:#333,stroke-width:2px;
    classDef invis stroke-width:0px,fill:none;
