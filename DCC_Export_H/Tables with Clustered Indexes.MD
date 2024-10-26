# Progetto XYZ

## Diagramma delle Tabelle e degli Indici

```mermaid
erDiagram
    #Z_PBI_Equipment_Event_H {
        int Process_id
        int Eq_Cycle_id
        int Voyage_Port_Call_id
        datetime Event_Time
        date Event_Date
        varchar EventType
        varchar EventDesc
        varchar Depot
        varchar Depot_MSCCode
        varchar Depot_Type
        int POLLoc_id
        int EE_Location_id
        char ET_Depot_In_Out
        smallint EqLength
        int TEU
        varchar ISO_Code
        int Event_id
        int Start_Event_id
        int End_Event_id
        char Event_Kind
        varchar POL
        varchar POLUN
        varchar POD
        varchar PODUN
        varchar Start_Location_UNCode
        varchar EC_Booking_Number
        varchar EC_BIll_Of_Lading_Number
        varchar Equipment_Number
        int Equipment_id
        varchar I_E
        varchar EDI_Filename
        varchar Rail_Truck
        varchar Rail_Truck_ID
        
        idx_ZPE_Equipment_Event_Cycle_Booking_H (Eq_Cycle_id, EC_Booking_Number, Equipment_Number)
        idx_ZPE_Equipment_Event_Type_Date_H (EventType, Event_Date, Event_Time)
    }

    PBI_DCC_Export_H_Cache_temp {
        
    }

    #TempScheduleLegCTE_H {
        int Process_id
        int Schedule_Leg_id
        datetime Local_or_Global_Arrival_DateTime
        datetime Local_or_Global_Departure_DateTime
        datetime Commercial_ETA
        datetime Commercial_ETD
        datetime Commercial_Arrival_Time
        varchar GVA_DocService
        varchar Ownership_Type
        
        idx_TempScheduleLegCTE_H_schedule_leg_id (Schedule_Leg_id)
        idx_TempCSCCTE_H (schedule_leg_id)
    }

    #TempCSCCTE_H {
        
    }
