### Structured Diagram with Jobs, Stored Procedures, and Containers Aligned in Separate Columns

```mermaid
flowchart LR
    %% Define styles for components
    classDef jobStyle fill:#FFD700,stroke:#333,stroke-width:1px;
    classDef spStyle fill:#87CEEB,stroke:#333,stroke-width:1px;
    classDef containerStyle fill:#8AC6D1,stroke:#333,stroke-width:1px;

    %% Jobs in the left column
    subgraph JOBS_COLUMN["Jobs"]
        direction TB
        ScheduleLegJob["Job_DCC_EXP_ScheduleLeg"]:::jobStyle
        DocumentsJob["Job_DCC_EXP_CSC"]:::jobStyle
        DeadlineJob["Job_DCC_EXP_Planner"]:::jobStyle
        SIJob["Job_DCC_EXP_SI"]:::jobStyle
        EventJob["Job_DCC_EXP_Event"]:::jobStyle
        TransportJob["Job_DCC_EXP_Transport"]:::jobStyle
        ChargesJob["Job_DCC_EXP_Charge"]:::jobStyle
        PaymentTermsJob["Job_DCC_EXP_Term_Pymt"]:::jobStyle
        HazardousJob["Job_DCC_EXP_Haz"]:::jobStyle
    end

    %% Stored Procedures in the middle column
    subgraph SPS_COLUMN["Stored Procedures"]
        direction TB
        ScheduleLegSP["SP_PBI_DCC_Exp_Schedule_Leg_Cache"]:::spStyle
        DocumentsSP["SP_PBI_DCC_Exp_BK_BL_CSC_Cache"]:::spStyle
        DeadlineSP["SP_PBI_DCC_Exp_Planner_NextPOD_CT"]:::spStyle
        SISp["SP_PBI_DCC_Exp_SI_Cache"]:::spStyle
        EventSP["SP_PBI_DCC_Exp_Event_Cache"]:::spStyle
        TransportSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle
        ChargesSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle
        PaymentTermsSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle
        HazardousSP["SP_PBI_DCC_Exp_Transport_Cache"]:::spStyle
    end

    %% Containers in the right column
    subgraph CONTAINERS_COLUMN["Data Enrichment Steps"]
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

    %% Horizontal connections from Jobs to Stored Procedures to Containers
    ScheduleLegJob --> ScheduleLegSP --> ScheduleLegContainer
    DocumentsJob --> DocumentsSP --> DocumentsContainer
    DeadlineJob --> DeadlineSP --> DeadlineContainer
    SIJob --> SISp --> ShippingInstructionsContainer
    EventJob --> EventSP --> ExportEventsContainer
    TransportJob --> TransportSP --> TransportEventsContainer
    ChargesJob --> ChargesSP --> ChargesContainer
    PaymentTermsJob --> PaymentTermsSP --> PaymentTermsContainer
    HazardousJob --> HazardousSP --> HazardousInfoContainer

    %% Vertical connections between Containers for the sequence flow
    ScheduleLegContainer --> DocumentsContainer
    DocumentsContainer --> DeadlineContainer
    DeadlineContainer --> ShippingInstructionsContainer
    ShippingInstructionsContainer --> ExportEventsContainer
    ExportEventsContainer --> TransportEventsContainer
    TransportEventsContainer --> ChargesContainer
    ChargesContainer --> PaymentTermsContainer
    PaymentTermsContainer --> HazardousInfoContainer
