from zeep import Client
from zeep.exceptions import Fault
from zeep.transports import Transport
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth

import logging
from datetime import datetime

# Configura il logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Funzione per testare la raggiungibilità e il servizio SOAP
def test_soap_service():
    url = "https://saas.hrzucchetti.it/Gpres3lenavispa/servlet/SQLDataProviderServer/SERVLET/hptg_timbrature_g2?wsdl"
    today = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Inizializza il client SOAP
        client = Client(url)
        
        # Effettua una richiesta al servizio (adatta i parametri alla tua esigenza)
        response = client.service.hptg_timbrature_g2_TabularQuery(
            'hrwebservice',  # username
            'Zucchetti123!', # password
            '000001',        # codice
            '2021-01-01',    # data inizio
            today            # data fine
        )
        
        # Se il servizio risponde, logga la lunghezza della risposta
        logger.info(f"Service is reachable. Response length: {len(response)}")
    except Fault as e:
        logger.error(f"SOAP Fault occurred: {e}")
    except RequestException as e:
        logger.error(f"Request failed: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
# URL del servizio WSDL
    url = "https://saas.hrzucchetti.it/Gpres3lenavispa/servlet/SQLDataProviderServer/SERVLET/hptg_timbrature_g2"
    username = 'hrwebservice',  # username
    password = 'Zucchetti123!', # password
    # Configura l'autenticazione HTTP
    session = requests.Session()
    session.auth = HTTPBasicAuth(username, password)  # Inserisci le credenziali

    # Inizializza il trasporto con la sessione
    transport = Transport(session=session)

    # Crea il client SOAP
    client = Client(url, transport=transport)

    # Effettua una chiamata al servizio (adatta i parametri alla tua esigenza)
    try:
        today = '2024-11-23'  # Data di esempio
        response = client.service.hptg_timbrature_g2_TabularQuery(
            username,  # username
            password, # password
            '000001',        # codice
            '2021-01-01',    # data inizio
            today            # data fine
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")

    test_soap_service()
