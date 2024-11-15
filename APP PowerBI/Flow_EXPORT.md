# IT016 - Export

Questo documento illustra come, partendo dal **Power BI Service**, sia la sede centrale di **MSC Italia a Genova** che le sedi distaccate di **Ravenna**, **Trieste**, **Venezia** e **Napoli** possono utilizzare diverse sorgenti dati tramite le tre app Power BI: **IT016-EXPORT**, **IT016-Accounting** e **IT016-Container Rental**.

---

## Schema Generale di Utilizzo

```mermaid
%%{init: {'theme': 'forest'}}%%

graph TD
    H[IT016-EXPORT] --> K[Sorgenti Dati:\nDocument Control Console]
    H --> L[Tipi di Analisi Dati]
    L --> M[Monitoraggio stato dei documenti]
    L --> N[Analisi tempi di elaborazione]
    L --> O[Identificazione di ritardi o anomalie]
    L --> P[Ottimizzazione del flusso di lavoro]



```