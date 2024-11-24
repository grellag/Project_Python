# MSC Italy - SharePoint Site

Questo documento illustra come, partendo dal **sito SharePoint MSC Italy**, 
<BR>sia possibile documentare tutte le cartelle contenute al suo interno usando <BR>lo script PYTHON: <BR><BR>**docum_folders_SH.pyw**.
<BR>

---

## Schema Generale delle chiamate a Microsoft Graph API

```mermaid
%%{init: {'theme': 'forest', 'themeVariables': { 'edgeLabelBackground':'#fff', 'handdraw': 'true' }}}%%
graph LR
    A[Inizio Script] -->|Access Token| B[API: Recupera Dettagli Sito]
    B -->|GET &#123;hostname, site_name&#125;| C[API: Recupera Drive]
    C -->|GET &#123;site_id&#125;| D[API: Recupera File e Cartelle Root]
    D -->|GET &#123;drive_id&#125;/root/children| E[Processa Cartelle]
    E -->|Ricorsione su Sottocartelle| F[API: Recupera Sottocartelle]
    F -->|GET &#123;folder_id&#125;/children| E
    E -->|Salva Dati| G[Salva in SQL Server]

    %% Etichette esterne per subgraph
    L1[Endpoints Usati]
    L2[Dati Ingresso/Uscita]

    %% Subgraph per Endpoints
    L1 --> B
    subgraph Endpoints
        B[Dettagli Sito \n URL: /v1.0/sites/&#123;hostname&#125;:/sites/&#123;site_name&#125;]
        C[Recupera Drive \n URL: /v1.0/sites/&#123;site_id&#125;/drive]
        D[File e Cartelle Root \n URL: /v1.0/drives/&#123;drive_id&#125;/root/children]
        F[Sottocartelle \n URL: /v1.0/drives/&#123;drive_id&#125;/items/&#123;folder_id&#125;/children]
    end

    %% Subgraph per Dati
    L2 --> Input1
    subgraph Dati
        Input1[Access Token \n Usato per Autenticazione]
        Output1[Sito Dettagli \n &#123;id, name, createdDateTime, webUrl&#125;]
        Output2[Drive Dettagli \n &#123;id, name, webUrl, driveType&#125;]
        Output3[File e Cartelle Root \n &#123;id, name, folder, file, webUrl&#125;]
        Output4[Sottocartelle \n &#123;id, name, folder&#125;]
        Output5[Dati Cartelle Processati \n &#123;folder_id, folder_name, folder_master_id&#125;]
    end

    %% Relazioni tra nodi
    B --> Output1
    Output1 --> C
    C --> Output2
    Output2 --> D
    D --> Output3
    Output3 --> F
    F --> Output4
    Output4 --> G
    G --> Output5

```