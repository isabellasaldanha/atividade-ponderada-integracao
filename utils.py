import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='beauty_app.log',
        filemode='a'
    )

def check_python_version():
    """Verifica se a versão do Python é compatível."""
    if sys.version_info < (3, 6):
        logging.error("Versão do Python não suportada. Utilize Python 3.6 ou superior.")
        raise RuntimeError("Versão do Python não suportada. Utilize Python 3.6 ou superior.")
    else:
        logging.info(f"Versão do Python: {sys.version}")