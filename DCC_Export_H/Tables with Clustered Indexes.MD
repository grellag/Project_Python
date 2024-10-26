# Progetto XYZ

## Diagramma delle Tabelle e degli Indici

```mermaid
erDiagram
    \#Z_PBI_Equipment_Event_H {
        indexes {
            idx_ZPE_Equipment_Event_Cycle_Booking_H (Eq_Cycle_id, EC_Booking_Number, Equipment_Number)
            idx_ZPE_Equipment_Event_Type_Date_H (EventType, Event_Date, Event_Time)
        }
    }

    PBI_DCC_Export_H_Cache_temp {
        
    }

    \#TempScheduleLegCTE_H {
        indexes {
            idx_TempScheduleLegCTE_H_schedule_leg_id (Schedule_Leg_id)
            idx_TempCSCCTE_H (schedule_leg_id)
        }
    }

    \#TempCSCCTE_H {
        
    }
