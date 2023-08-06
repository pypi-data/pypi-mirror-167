import os
import json
from google.cloud import storage
from google.oauth2 import service_account

from io_orbit.logger.laccuna_logging import get_logger

logger = get_logger(__name__)


class GoogleCloudStorageRights:
    def __init__(self) -> None:
        try:
            self.credentials = service_account.Credentials.from_service_account_info(
                eval(os.getenv("GOOGLE_CREDENTIALS"))
            )
        except Exception as e:
            logger.exception(f"Error while initializing google credentials: {e}")
        self.initialize_app = storage.Client(credentials=self.credentials)
        pass

    def initialize_gcs_client(self):
        return storage.Client(credentials=self.credentials)


try:
    logger.info(f"Instantiating GCS Client...")
    google_client = GoogleCloudStorageRights().initialize_gcs_client()
    logger.info(f"GCS Client instantiated.")
except Exception as e:
    logger.error(f"Error instantiating GCS Client: {e}")
