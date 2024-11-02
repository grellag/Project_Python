### Structured Diagram with a Single Red Arrow between "Schedule Leg Vessel" and "Documenti Container Export"

```mermaid
flowchart LR
    %% Define styles for components
    classDef jobStyle fill:#FFD700,stroke:#333,stroke-width:1px;
    classDef spStyle fill:#87CEEB,stroke:#333,stroke-width:1px;
    classDef containerStyle fill:#8AC6D1,stroke:#333,stroke-width:1px;
    classDef dccColor fill:#FFA07A,stroke:#333,stroke-width:2px;
    classDef invisible fill:transparent,stroke:none;
    
    classDef redLink stroke:#FF0000,stroke-width:2px;



    %% Jobs in the first column
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

    %% Stored Procedures in the second column
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

    %% Data Enrichment Containers in the third column
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

    %% Final DCC Container in the fourth column with placeholder nodes
    subgraph FINAL_DCC_COLUMN["Final DCC Container"]
        direction TB
        empty0[" "]:::invisible
        empty1[" "]:::invisible
        empty2[" "]:::invisible
        empty3[" "]:::invisible
        empty4[" "]:::invisible
        %% Central DCC Node with clickable link to Container Diagram file
        click DCC "./DCC Container Diagram.md" "Go to Container Diagram"
        DCC["Documentation Control Console (DCC)"]:::dccColor
        empty5[" "]:::invisible
        empty6[" "]:::invisible
        empty7[" "]:::invisible
        empty8[" "]:::invisible
        empty9[" "]:::invisible
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
    HazardousInfoContainer --> DCC


