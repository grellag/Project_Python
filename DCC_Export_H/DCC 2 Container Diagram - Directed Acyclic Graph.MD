### 3. **Directed Acyclic Graph (DAG)**

A **Directed Acyclic Graph** (DAG) allows for more complex dependencies between steps. In a DAG, nodes are connected in a way that doesn’t loop back, which is ideal if some steps rely on multiple previous steps and aren’t strictly linear.

#### Example in Mermaid.js

```mermaid
graph TD
    classDef stepStyle fill:#8AC6D1,stroke:#333,stroke-width:1px,color:#000000;
%% Define styles with increasing transparency and darker text color for better visibility
    classDef step1Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:1,color:#000000;
    classDef step2Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.9,color:#000000;
    classDef step3Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.8,color:#FFFFFF;
    classDef step4Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.7,color:#FFFFFF;
    classDef step5Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.6,color:#FFFFFF;
    classDef step6Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.5,color:#FFFFFF;
    classDef step7Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.4,color:#FFFFFF;
    classDef step8Style fill:#8AC6D1,stroke:#333,stroke-width:1px,fill-opacity:0.3,color:#FFFFFF;
    classDef finalOutput fill:#8AC6D1,stroke:#333,stroke-width:2px,color:#000000;

    %% Nodes with increasing transparency and corresponding text color

    Schedule["Schedule Leg by Vessel/Voyage"]:::stepStyle --> Documents["CSC Document"]:::step1Style
    Documents --> Deadlines["Deadline Vessel/Voyage"]:::step2Style
    Deadlines --> ShippingInstructions["Shipping Instructions"]:::step3Style
    ShippingInstructions --> EventsContainer["CSC Export Events"]:::step4Style
    EventsContainer --> EventsTransport["CSC Export Transport"]:::step5Style
    EventsTransport --> Charges["CSC Charges"]:::step6Style
    Charges --> PaymentTerms["Termini di Pagamento Cliente"]:::step7Style
    PaymentTerms --> DangerousGoods["CSC Info Hazardous"]:::step8Style


        %% Final Source - DCC
    DCC["Documentation Control Console (DCC)"]:::finalOutput

    DangerousGoods --> DCC