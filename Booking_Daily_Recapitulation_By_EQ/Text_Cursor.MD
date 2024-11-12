```mermaid
# Crea un diagramma di flusso in Mermaid.js che rappresenta un processo decisionale:
# - Inizia con una scelta.
# - Se "Sì", procedi con due passaggi.
# - Se "No", termina il processo.

graph TD
    A[Inizio] --> B{Fai una scelta}
    B -->|Sì| C[Primo passaggio]
    C --> D[Secondo passaggio]
    D --> E[Fine]
    B -->|No| E[Fine]