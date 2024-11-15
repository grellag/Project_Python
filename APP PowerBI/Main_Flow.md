# Utilizzo delle App Power BI da parte di MSC Italia e delle Sedi Distaccate

Questo documento illustra come, partendo dal **Power BI Service**, sia la sede centrale di **MSC Italia a Genova** che le sedi distaccate di **Ravenna**, **Trieste**, **Venezia** e **Napoli** possono utilizzare diverse sorgenti dati tramite le tre app Power BI: **IT016-EXPORT**, **IT016-Accounting** e **IT016-Container Rental**.

---

## Schema Generale di Utilizzo

```mermaid
%%{init: {'theme': 'forest'}}%%

graph LR
    A[Power BI Service] -->|Accesso| B[MSC Italia - Genova]
    A -->|Accesso| C[Sedi Distaccate]
    subgraph Sedi Distaccate
        D[Ravenna]
        E[Trieste]
        F[Venezia]
        G[Napoli]
    end
    B -->|Utilizza| H[IT016-EXPORT]
    B -->|Utilizza| I[IT016-Accounting]
    B -->|Utilizza| J[IT016-Container Rental]
    D -->|Utilizza| H
    D -->|Utilizza| I
    D -->|Utilizza| J
    E -->|Utilizza| H
    E -->|Utilizza| I
    E -->|Utilizza| J
    F -->|Utilizza| H
    F -->|Utilizza| I
    F -->|Utilizza| J
    G -->|Utilizza| H
    G -->|Utilizza| I
    G -->|Utilizza| J


```