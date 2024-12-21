# Documentazione del Job SQL Server: [LN][Rebuild Cache] - PBI - Trasporti - History

Questo documento descrive il flusso del job SQL Server schedulato tramite SQL Server Agent, che esegue una serie di stored procedure e termina con l'aggiornamento di un cubo SSAS.

## Flusso del Job SQL Server

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'handdraw': true}}}%%
flowchart TB
    A[Inizio Job] --> C[Refresh CSC Cache]
    C --> D[Refresh Final Cache]
    D --> E[Refresh Local Cube]
    E --> F[Fine Job]

    %% Descrizione dei passi:

    C -->|Refresh cache CSC| H[SP_PBI_Build_Agency_CSC_Cache]
    D -->|Refresh cache finale| I[SP_PBI_DCC_ITALY_H]
    E -->|Refresh cubo SSAS| J[Cubo: DCC_ITALY]

    %% Stili personalizzati:
    style H fill:#FFD700,stroke:#000,stroke-width:2px
    style I fill:#FFD700,stroke:#000,stroke-width:2px
    style J fill:#87CEFA,stroke:#000,stroke-width:2px
```