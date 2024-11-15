# IT016 - Container Rental

Questo documento illustra come, partendo dal **Power BI Service**, sia la sede centrale di **MSC Italia a Genova** che le sedi distaccate di **Ravenna**, **Trieste**, **Venezia** e **Napoli** possono utilizzare diverse sorgenti dati tramite le tre app Power BI: **IT016-EXPORT**, **IT016-Accounting** e **IT016-Container Rental**.

---

## Schema Generale di Utilizzo

```mermaid
%%{init: {'theme': 'forest'}}%%

graph TD
    J[IT016-Container Rental] --> X[Sorgenti Dati:\nILIM - Integrated Logistics Invoicing Module]
    X --> Y[Modulo OVA per fatturazione equipaggiamento]
    J --> Z[Tipi di Analisi Dati]
    Z --> AA[Analisi fatture noleggio container]
    Z --> AB[Monitoraggio charges associate al noleggio]
    Z --> AC[Verifica accuratezza delle fatturazioni]
    Z --> AD[Ottimizzazione processo di fatturazione]




```