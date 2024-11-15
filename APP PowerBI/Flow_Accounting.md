# IT016 - Accounting

Questo documento illustra come, partendo dal **Power BI Service**, sia la sede centrale di **MSC Italia a Genova** che le sedi distaccate di **Ravenna**, **Trieste**, **Venezia** e **Napoli** possono utilizzare diverse sorgenti dati tramite le tre app Power BI: **IT016-EXPORT**, **IT016-Accounting** e **IT016-Container Rental**.

---

## Schema Generale di Utilizzo

```mermaid
%%{init: {'theme': 'forest'}}%%

graph TD
    I[IT016-Accounting] --> Q[Sorgenti Dati:\nCharges manifestate/non manifestate]
    Q --> R[Mediterranean Shipping Company - Ginevra]
    I --> S[Tipi di Analisi Dati]
    S --> T[Analisi spese registrate/non registrate]
    S --> U[Confronto charges manifestate e non]
    S --> V[Identificazione discrepanze finanziarie]
    S --> W[Supporto decisioni contabili e finanziarie]




```