### Structured Diagram with Horizontal Jobs and Stored Procedures Intersecting Vertical Containers

```mermaid
flowchart TB
    %% Define styles for components
    classDef jobStyle fill:#FFD700,stroke:#333,stroke-width:1px;
    classDef spStyle fill:#87CEEB,stroke:#333,stroke-width:1px;
    classDef containerStyle fill:#8AC6D1,stroke:#333,stroke-width:1px;

    %% Vertically aligned containers in a single column
    subgraph VERTICAL_FLOW["Data Enrichment Steps"]
        direction TB
        ScheduleLegContainer["Schedule Leg Vessel"]:::containerStyle
        DocumentsContainer["Documenti Container Export"]:::containerStyle
        DeadlineContainer["Deadline Vessel"]:::containerStyle
        ShippingInstructionsContainer["Shipping Instructions"]:::containerStyle
        ExportEventsContainer["Eventi Container Export"]:::containerStyle
        TransportEventsContainer["Eventi Trasporto Export"]:::containerStyle
        ChargesContainer["Charges Container"]:::containerStyle
        PaymentTermsContainer["Termini di Pagamento Cliente"]:::containerStyle
        HazardousInfoContainer["Informazioni Merce Pericolosa"]:::containerStyle
    end

    %% Horizontal rows with Jobs and Stored Procedures intersecting containers
    ScheduleLegJob["Job_DCC_EXP_ScheduleLeg"]:::jobStyle --> ScheduleLegSP["SP_PBI_DCC_Exp_Schedule_Leg_Cache"]:::spStyle --> ScheduleLegContainer
    DocumentsJob["Job_DCC_EXP_CSC"]:::jobStyle --> DocumentsSP["SP_PBI_DCC_Exp_BK_BL_CSC_Cache"]:::spStyle --> DocumentsContainer
    DeadlineJob["Job_DCC_EXP_Planner"]:::jobStyle --> DeadlineSP["SP_PBI_DCC_Exp_Planner_NextPOD_CT"]:::spStyle --> DeadlineContainer
    SIJob["Job_DCC_EXP_SI"]:::jobStyle --> SISp["SP_PBI_DCC_Exp_SI_Cache"]:::spStyle --> ShippingInstructionsContainer
    EventJob["Job_DCC_EXP_Event"]:::jobStyle --> EventSP["SP_PBI_DCC_Exp_Event_Cache"]:::spStyle --> ExportEventsContainer
    TransportJob["Job_DCC_EXP_Transport"]:::jobStyle --> TransportSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle --> TransportEventsContainer
    ChargesJob["Job_DCC_EXP_Charge"]:::jobStyle --> ChargesSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle --> ChargesContainer
    PaymentTermsJob["Job_DCC_EXP_Term_Pymt"]:::jobStyle --> PaymentTermsSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle --> PaymentTermsContainer
    HazardousJob["Job_DCC_EXP_Haz"]:::jobStyle --> HazardousSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle --> HazardousInfoContainer

    %% Vertical connections between containers to show the sequence
    ScheduleLegContainer --> DocumentsContainer
    DocumentsContainer --> DeadlineContainer
    DeadlineContainer --> ShippingInstructionsContainer
    ShippingInstructionsContainer --> ExportEventsContainer
    ExportEventsContainer --> TransportEventsContainer
    TransportEventsContainer --> ChargesContainer
    ChargesContainer --> PaymentTermsContainer
    PaymentTermsContainer --> HazardousInfoContainer
