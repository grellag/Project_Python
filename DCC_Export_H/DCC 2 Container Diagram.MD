# Information Enrichment Process for Documentation Control Console (DCC)

## Enrichment Flow Diagram

```mermaid
flowchart TB
    classDef enrichmentStage fill:#FFDD57,stroke:#333,stroke-width:2px;
    classDef finalOutput fill:#8AC6D1,stroke:#333,stroke-width:2px;

    %% Information Enrichment Stages
    Schedule["Schedule Leg Vessel"]:::enrichmentStage
    Documents["Documenti Container Export"]:::enrichmentStage
    Deadlines["Deadline Vessel"]:::enrichmentStage
    ShippingInstructions["Shipping Instructions"]:::enrichmentStage
    EventsContainer["Eventi Container Export"]:::enrichmentStage
    EventsTransport["Eventi Trasporto Export"]:::enrichmentStage
    Charges["Charges Container"]:::enrichmentStage
    PaymentTerms["Termini di Pagamento Cliente"]:::enrichmentStage
    DangerousGoods["Informazioni Merce Pericolosa"]:::enrichmentStage

    %% Final Source - DCC
    DCC["Documentation Control Console (DCC)"]:::finalOutput

    %% Flow of Information Enrichment
    Schedule --> Documents
    Documents --> Deadlines
    Deadlines --> ShippingInstructions
    ShippingInstructions --> EventsContainer
    EventsContainer --> EventsTransport
    EventsTransport --> Charges
    Charges --> PaymentTerms
    PaymentTerms --> DangerousGoods
    DangerousGoods --> DCC
