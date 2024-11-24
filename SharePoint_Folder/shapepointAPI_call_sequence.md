# MSC Italy - SharePoint Site - Diagramma di Flusso

Questo documento illustra come, partendo dal **sito SharePoint MSC Italy**, 
<BR>sia possibile documentare tutte le cartelle contenute al suo interno usando <BR>lo script PYTHON: <BR><BR>**docum_folders_SH.pyw**.
<BR>

---

## Schema Generale delle chiamate a Microsoft Graph API

```mermaid

%%{init: {'theme': 'default'}}%%
sequenceDiagram
    actor Script as Script Python
    participant Graph as Microsoft Graph API
    participant DB as SQL Server

    rect rgb(144, 238, 144)
    Note over Script: Inizio Script con Access Token
    end

    rect rgb(173, 216, 230)
    Script->>+Graph: GET /sites/{hostname}:/sites/{site_name}
    Graph-->>-Script: Dettagli Sito {id, name, createdDateTime, webUrl}
    end

    rect rgb(173, 216, 230)
    Script->>+Graph: GET /sites/{site_id}/drive
    Graph-->>-Script: Drive Dettagli {id, name, webUrl, driveType}
    end

    rect rgb(173, 216, 230)
    Script->>+Graph: GET /drives/{drive_id}/root/children
    Graph-->>-Script: File e Cartelle Root {id, name, folder, file, webUrl}
    end

    rect rgb(173, 216, 230)
    loop Per ogni cartella
        Script->>+Graph: GET /drives/{drive_id}/items/{folder_id}/children
        Graph-->>-Script: Sottocartelle {id, name, folder}
        Note over Script: Processa dati cartella
    end
    end

    rect rgb(255, 200, 150)
    Script->>+DB: Salva dati processati
    Note over DB: {folder_id, folder_name, folder_master_id}
    DB-->>-Script: Conferma salvataggio
    end
```