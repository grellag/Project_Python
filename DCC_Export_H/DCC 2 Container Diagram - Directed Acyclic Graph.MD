### 3. **Directed Acyclic Graph (DAG)**

A **Directed Acyclic Graph** (DAG) allows for more complex dependencies between steps. In a DAG, nodes are connected in a way that doesn’t loop back, which is ideal if some steps rely on multiple previous steps and aren’t strictly linear.

#### Example in Mermaid.js

```markdown
```mermaid
graph TD
    classDef stepStyle fill:#8AC6D1,stroke:#333,stroke-width:1px;

    Schedule["Schedule Leg Vessel"]:::stepStyle --> Documents["Documenti Container Export"]:::stepStyle
    Documents --> Deadlines["Deadline Vessel"]:::stepStyle
    Deadlines --> ShippingInstructions["Shipping Instructions"]:::stepStyle
    ShippingInstructions --> EventsContainer["Eventi Container Export"]:::stepStyle
    EventsContainer --> EventsTransport["Eventi Trasporto Export"]:::stepStyle
    EventsTransport --> Charges["Charges Container"]:::stepStyle
    Charges --> PaymentTerms["Termini di Pagamento Cliente"]:::stepStyle
    PaymentTerms --> DangerousGoods["Informazioni Merce Pericolosa"]:::stepStyle

    %% Additional dependencies if needed
    Schedule --> Deadlines
    EventsContainer --> Charges