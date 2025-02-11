## Flusso dei XBooking - Agenti Esteri

```mermaid
graph TD;
    A[XBooking arriva in IMPORT] --> B{Incluso nel manifesto?};
    B -- NO --> C[Confermato come non incluso nel manifesto];
    B -- SI --> L[Passa a processo EXPORT];
    C --> D{Necessario Cargo per trasbordi?};
    D -- SI --> E[Acquisizione Cargo];
    E --> F[Cargo compare in IMPORT];
    D -- NO --> G[L'agente estero manifesta];
    F --> H[BL con Cargo viene cancellata];
    H --> I[Acquisizione DTX];
    H --> L;
    G --> I;
    I --> L;
    L --> J[Aggiunta costi da recuperare];
    J --> K[Flusso completato];


```