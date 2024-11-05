### 3. **Directed Acyclic Graph (DAG)**

A **Directed Acyclic Graph** (DAG) allows for more complex dependencies between steps. In a DAG, nodes are connected in a way that doesn’t loop back, which is ideal if some steps rely on multiple previous steps and aren’t strictly linear.

#### Example in Mermaid.js

```mermaid
---
config:
  look: handDrawn
---
graph TD
    %% Definire lo stile per i nodi
    classDef stepStyle fill:#8AC6D1,stroke:#333,stroke-width:1px,color:#000000;
    classDef finalOutput fill:#FF6347,stroke:#333,stroke-width:2px,color:#000000;

    %% Creare i nodi con collegamenti che suggeriscono una struttura circolare
    Schedule["Schedule Leg by Vessel/Voyage"]:::stepStyle --> Documents["CSC Document"]:::stepStyle
    Documents --> Deadlines["Deadline Vessel/Voyage"]:::stepStyle
    Deadlines --> ShippingInstructions["Shipping Instructions"]:::stepStyle
    ShippingInstructions --> EventsContainer["CSC Export Events"]:::stepStyle
    EventsContainer --> EventsTransport["CSC Export Transport"]:::stepStyle
    EventsTransport --> Charges["CSC Charges"]:::stepStyle
    Charges --> PaymentTerms["Termini di Pagamento Cliente"]:::stepStyle
    PaymentTerms --> DangerousGoods["CSC Info Hazardous"]:::stepStyle

    %% Collegamento del nodo finale
    DangerousGoods --> DCC["Documentation Control Console (DCC)"]:::finalOutput
