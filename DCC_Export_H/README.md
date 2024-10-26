# DCC Export Historical Documentation

This project processes data from multiple source tables and stores it in a .

## Data Flow Diagram

```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---

graph LR
    %% Source tables
    A1["FNTB_Voyage_Port_Call"] --> B1["Z_PBI_Schedule_Leg"]
    A2["FNTB_Schedule_Leg"] --> B1
    A3["ScheduleLegCTE"] --> B1
    A4["Z_PBI_Equipment_Event_E"] --> B2["PBI_Vessel_Reconciliation_temp"]
    A5["FNTB_Depot"] --> B3["PBI_Vessel_Reconciliation_FTC"]
    A6["FNTB_Location"] --> B3
    A7["Cargo"] --> B4["PBI_Doc_Date_Time"]
    A8["FNTB_AssocDocCompany_BusinessEntity('RTOWNBL')"] --> B5["CTE_Type"]
    A9["FNTB_AssocDocCompany_BusinessEntity('DGTLBL')"] --> B5
    A10["MSCLinkBI_FNTB_Booking_DG_Accept_Finalize_Dates"] --> B6["CTE_NF"]
    A11["FNTB_HSCodes_By_Cargo_Shipment_Container"] --> B7["CTE_DA"]
    A12["FNTB_ContainerSmart_ByContainer"] --> B8["CTE_Intermodal"]

    %% Function tables (intermediate processing)
    C1["OVAVREC_FNTB_CSC_Hazardous_Info"] --> B2
    C2["FNTB_SecUser"] --> B3
    C3["GISSubLocation"] --> B4
    C4["PBI_Vessel_Reconciliation_MFTC"] --> B6

    %% Final tables
    B1["Z_PBI_Schedule_Leg"] --> D1["PBI_Vessel_Reconciliation"]
    B2["PBI_Vessel_Reconciliation_temp"] --> D1
    B3["PBI_Vessel_Reconciliation_FTC"] --> D1
    B4["PBI_Doc_Date_Time"] --> D1
    B5["CTE_Type"] --> D1
    B6["CTE_NF"] --> D1
    B7["CTE_DA"] --> D1
    B8["CTE_Intermodal"] --> D1



    %% Applicare il colore giallo a ciascun nodo
    style B1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style B2 fill:#FFFF99,stroke:#333,stroke-width:1px
    style D1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style B3 fill:#FFFF99,stroke:#333,stroke-width:1px
    style B4 fill:#FFFF99,stroke:#333,stroke-width:1px
