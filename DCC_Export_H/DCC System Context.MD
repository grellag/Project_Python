# Diagramma della 'Documentation Control Console'

```mermaid
flowchart TB
    classDef departmentColor fill:#FFD700,stroke:#333,stroke-width:2px;  %% Top color
    classDef dccColor fill:#8AC6D1,stroke:#333,stroke-width:2px;         %% Center color
    classDef dataSourceColor fill:#FF6347,stroke:#333,stroke-width:2px;  %% Bottom color

    %% Departments (Top)
    subgraph Departments ["Departments"]
        direction TB
        Accounting["Accounting Department"]:::departmentColor
        ExportCommercials["Export Commercials"]:::departmentColor
        FreightCashier["Freight Cashier"]:::departmentColor
        DocumentationOffice["Documentation Office"]:::departmentColor
        PortOperationsOffice["Port Operations Office"]:::departmentColor
    end

    %% Central DCC Node with link to Container Diagram section
    click DCC "##Container-Diagram" "Go to Container Diagram"
    DCC["Documentation Control Console (DCC)"]:::dccColor

    %% Data Sources (Bottom)
    subgraph DataSources ["Data Sources"]
        direction TB
        MSCLink["MSCLink System"]:::dataSourceColor
        SharePoint["SharePoint (Excel Files)"]:::dataSourceColor
        BarcodeReader["Barcode Reading Tools"]:::dataSourceColor
    end

    %% Connections with Dashed Lines (No Arrows)
    Departments -->|Accesses Reports| DCC
    DCC -.->|Data Feed| MSCLink
    DCC -.->|Data Feed| SharePoint
    DCC -.->|Data Feed| BarcodeReader


```markdown
## Container Diagram

```mermaid
flowchart TB
    classDef containerColor fill:#8AC6D1,stroke:#333,stroke-width:2px;
    classDef serviceColor fill:#B0E0E6,stroke:#333,stroke-width:2px;
    classDef databaseColor fill:#FFD700,stroke:#333,stroke-width:2px;

    subgraph DCC["Documentation Control Console (DCC)"]
        direction TB
        PowerBI["Power BI Service"]:::serviceColor
        SQLDB["SQL Database"]:::databaseColor
        APIGateway["API Gateway"]:::serviceColor
        BarcodeService["Barcode Service"]:::serviceColor
        FileStorage["SharePoint Storage"]:::databaseColor
    end

    PowerBI -->|Data Query| SQLDB
    PowerBI -->|Fetch Data| APIGateway
    APIGateway -->|Retrieve Barcode| BarcodeService
    APIGateway -->|Access Files| FileStorage