# C4 System Context Diagram - SP_PBI_Container_In_Storage_Demurrage_Pending_Status

```mermaid
C4Context
title System Context for SP_PBI_Container_In_Storage_Demurrage_Pending_Status

Person(User, "End User", "Requests the container status report")
System_Boundary(ContainerSystem, "Container Demurrage Reporting System") {
    System(System, "LeNavi Reporting System", "Main system executing the stored procedure")
    SystemDb(Database, "LeNavi_LOCAL Database", "Stores container data, events, and related information")
}

Rel(User, System, "Requests container status information")
Rel(System, Database, "Executes stored procedure SP_PBI_Container_In_Storage_Demurrage_Pending_Status on")
