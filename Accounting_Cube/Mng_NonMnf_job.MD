# SQL Server Jobs: Refresh 'Mnf & Non Mnf Charges'

Questo diagramma descrive il flusso dei jobs SQL Server schedulati tramite SQL Server Agent, che eseguono una serie di stored procedure e termina con l'aggiornamento di un cubo SSAS.

## Flusso del Job SQL Server

```mermaid
flowchart LR

    %% ------------------------------------------------------------------
    %% FLUSSO PRINCIPALE (STEPS 1–8)
    %% ------------------------------------------------------------------

    A1["Step 1: AgCheck\n\nIF (SELECT repstate.role_desc\nFROM sys.dm_hadr_availability_replica_states repstate\nINNER JOIN sys.availability_groups ag\nON repstate.group_id = ag.group_id\nAND repstate.is_local = 1)\n!= 'Primary'\n\nRAISERROR('Not Primary', 2, 1)"]
    A2["Step 2: Manifest Partitioned 2024\n\nEXEC ACC_SP_MANIFEST_ReBuildCache\n'2024-01-01','2024-12-31'"]
    A3["Step 3: Manifest Partitioned 2025\n\nEXEC ACC_SP_MANIFEST_ReBuildCache\n'2025-01-01','2025-12-31'"]
    A4["Step 4: Non Manifest Partitioned 2024\n\nEXEC ACC_SP_NonMANIFEST_ReBuildCache\n'2024-01-01','2024-12-31'"]
    A5["Step 5: Non Manifest Partitioned 2025\n\nEXEC ACC_SP_NonMANIFEST_ReBuildCache\n'2025-01-01','2025-12-31'"]
    A6["Step 6: Manifest + Non Manifest UNION 2024->2025\n\nEXEC ACC_SP_ALL_Charges_ReBuildCache\n'2024-01-01','2025-12-31'"]
    A7["Step 7: Refresh Cube\n\nPowershell:\nAzureAs-Partitions.ps1\n-Tables 'PBI_ACC_ALL_Charges_cache'\n-RefreshType 'Full'"]
    A8["Step 8: Refresh Date\n\nPowershell:\nAzureAs-Partitions.ps1\n-Tables 'LNAV_ACC_ALL_Charges_vw_Last_Refresh'\n-RefreshType 'Full'\n\n(On success => Job Ends)"]

    %% Flusso delle frecce
    A1 -->|On Success| A2
    A1 -->|On Fail| Fail1((Job Fails))

    A2 -->|On Success| A3
    A2 -->|On Fail| Fail2((Job Fails))

    A3 -->|On Success| A4
    A3 -->|On Fail| Fail3((Job Fails))

    A4 -->|On Success| A5
    A4 -->|On Fail| Fail4((Job Fails))

    A5 -->|On Success| A6
    A5 -->|On Fail| Fail5((Job Fails))

    A6 -->|On Success| A7
    A6 -->|On Fail| Fail6((Job Fails))

    A7 -->|On Success| A8
    A7 -->|On Fail| Fail7((Job Fails))

    A8 -->|On Success| EndOk((Job Ends - Success))
    A8 -->|On Fail| Fail8((Job Fails))


    %% ------------------------------------------------------------------
    %% STEPS 9–15 (NELLO SCRIPT MA NON COLLEGATI AL FLUSSO 1–8)
    %% ------------------------------------------------------------------

    subgraph Steps_9_15["Steps 9–15 (non collegati al flusso principale)"]
    direction TB

    B9["Step 9: Non Manifest Partitioned 2023\n\nEXEC ACC_SP_NonMANIFEST_ReBuildCache\n'2023-01-01','2023-12-31'"]
    B10["Step 10: Manifest Partitioned 2023\n\nEXEC ACC_SP_MANIFEST_ReBuildCache\n'2023-01-01','2023-12-31'"]
    B11["Step 11: Non Manifest Partitioned 2022\n\nEXEC ACC_SP_NonMANIFEST_ReBuildCache\n'2022-01-01','2022-12-31'"]
    B12["Step 12: Manifest Partitioned 2022\n\nEXEC ACC_SP_MANIFEST_ReBuildCache\n'2022-01-01','2022-12-31'"]
    B13["Step 13: Manifest_Invoiced_CACHE\n\nEXEC SP_RPT_GOA_ACC_Manifest_Invoiced_CACHE NULL"]
    B14["Step 14: Manifest_Not_Invoiced_CACHE\n\nEXEC SP_RPT_GOA_ACC_Manifest_Not_Invoiced_CACHE NULL"]
    B15["Step 15: Refresh Cube - FULL 2022,2023,2024\n\nPowershell:\nAzureAs-Partitions.ps1\n-Partitions '2022,2023,2024'\n-RefreshType 'Full'"]

    B9 --> B10
    B10 --> B11
    B11 --> B12
    B12 --> B13
    B13 --> B14
    B14 --> B15
    end




```