# MSC Italy - SharePoint Site

Questo documento illustra come, partendo dal **sito SharePoint MSC Italy**, sia possibile documentare tutte le cartelle contenute al suo interno.

---

## Schema Generale del flusso

```mermaid
%%{init: {'theme': 'forest', 'themeVariables': { 'edgeLabelBackground':'#fff', 'handdraw': 'true' }}}%%
classDiagram
    class MainScript {
        - access_token : str
        - site_id : str
        - drive_id : str
        - folder_id : str
        + main()
        + get_all_folders()
        + retrieve_subfolder_data()
        + truncate_table()
        + insert_into_table()
        + send_email()
    }

    class SharePointAPI {
        + get_all_items_under_folder()
        + retrieve_subfolder_data()
    }

    class Manager by Database {
        + truncate_table()
        + insert_into_table()
        + create_excel_writer()
    }

    class EmailManager {
        + send_email()
    }

    %% Relationships
    MainScript --> SharePointAPI : Calls
    MainScript --> Manager by Database : Save into DB
    MainScript --> EmailManager : Send

    %% Inline styles
    style MainScript fill:#fdfd96,stroke:#000,stroke-width:2;  %% Yellow
    style SharePointAPI fill:#9ad1f5,stroke:#000,stroke-width:2;  %% Blue
    style Manager by Database fill:#f5a9a9,stroke:#000,stroke-width:2;  %% Red
    style EmailManager fill:#d5f5d5,stroke:#000,stroke-width:2;  %% Green


```