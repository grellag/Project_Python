# Information Enrichment Treemap for Documentation Control Console (DCC)

```mermaid
graph TD
    classDef enrichmentStage fill:#FFDD57,stroke:#333,stroke-width:1px;
    classDef finalOutput fill:#8AC6D1,stroke:#333,stroke-width:2px;

    %% Top-Level Stage
    Schedule["Schedule Leg Vessel"]:::enrichmentStage

    %% Hierarchical Structure for Enrichment Process
    Schedule --> Documents["Documenti Container Export"]:::enrichmentStage
    Documents --> Deadlines["Deadline Vessel"]:::enrichmentStage
    Deadlines --> ShippingInstructions["Shipping Instructions"]:::enrichmentStage
    ShippingInstructions --> EventsContainer["Eventi Container Export"]:::enrichmentStage
    EventsContainer --> EventsTransport["Eventi Trasporto Export"]:::enrichmentStage
    EventsTransport --> Charges["Charges Container"]:::enrichmentStage
    Charges --> PaymentTerms["Termini di Pagamento Cliente"]:::enrichmentStage
    PaymentTerms --> DangerousGoods["Informazioni Merce Pericolosa"]:::enrichmentStage
    DangerousGoods --> DCC["Documentation Control Console (DCC)"]:::finalOutput
