# C4 Container Diagram - SP_PBI_Container_In_Storage_Demurrage_Pending_Status

```mermaid
flowchart TD
    subgraph LeNavi_Reporting_System ["LeNavi Reporting System"]
        direction TB
        
        StoredProc["SP_PBI_Container_In_Storage_Demurrage_Pending_Status"]
        StoredProc:::containerStyle
        Database["LeNavi_LOCAL Database\n(SQL Database)\nStores container and demurrage data"]
        Database:::containerStyle
        DataFeed["Interlink Data Feed\n(External Data Source)\nProvides real-time container updates"]
        DataFeed:::externalStyle
    end

    %% Define Relationships
    StoredProc --> Database
    StoredProc --> DataFeed

    %% Define Styles for containers
    classDef containerStyle fill:#8AC6D1,stroke:#333,stroke-width:2px;
    classDef externalStyle fill:#FFD700,stroke:#333,stroke-width:2px;
