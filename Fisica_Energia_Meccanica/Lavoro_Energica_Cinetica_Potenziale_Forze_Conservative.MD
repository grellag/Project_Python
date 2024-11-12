```mermaid
graph TD
    A[Inizio] --> B[Forza Conservativa Agisce sul Punto Materiale]
    B --> C{La Forza Compie Lavoro?}
    C -- Sì --> D[Calcolo del Lavoro <br><span>\( W \)</span>]
    D --> E[Relazione: <br><span>\( W_{A \rightarrow B} = -\Delta U = -(U_B - U_A) \)</span>]
    E --> F[Calcolo di <span>\( \Delta U \)</span>]
    F --> G[Determinazione di <span>\( U_A \)</span> e <span>\( U_B \)</span>]
    G --> H{Variazione dell'Energia Cinetica}
    H -- Aumenta --> I[<span>\( \Delta K = -W \)</span>]
    H -- Diminuisce --> J[<span>\( \Delta K = -W \)</span>]
    I --> K[Conservazione dell'Energia Meccanica: <br><span>\( K + U = \text{Costante} \)</span>]
    J --> K
    C -- No --> L[<span>\( U \)</span> e <span>\( K \)</span> Rimangono Invariati]
    L --> K
    K --> M[Fine]
