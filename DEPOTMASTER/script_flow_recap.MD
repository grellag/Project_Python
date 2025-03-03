# Project Flowchart

Below is the flowchart for the main steps in our data processing script:

```mermaid
flowchart TD
    A[Start main] --> B[Initialization]
    B --> C[Configure Logging]
    B --> D[Establish Database Connections - pyodbc & SQLAlchemy]
    B --> E[Define API Parameters & Endpoints]
    E --> F[Data Extraction]
    F --> G[Make API Request - timeout 30s]
    G --> H[Handle API Response & Parse JSON]
    H --> I[Convert JSON to DataFrame]
    I --> J[Data Storage]
    J --> K[Save DataFrame as CSV]
    J --> L[Truncate SQL Table]
    L --> M[Data Insertion]
    M --> N[Insert DataFrame into SQL Server TABLE: dm_release_orders]
    N --> O[Log Insertion Performance]
    O --> P[Finalization]
    P --> Q[Loop through Each Endpoint]
    Q --> R[Log Script Completion]
    R --> S[End main]

```
