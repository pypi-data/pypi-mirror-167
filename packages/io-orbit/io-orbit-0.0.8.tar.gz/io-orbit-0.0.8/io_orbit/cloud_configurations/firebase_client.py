import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from io_orbit.logger.laccuna_logging import get_logger

logger = get_logger(__name__)


class FirebaseRights:
    def __init__(self) -> None:
        try:
            self.credentials = credentials.Certificate(
                eval(os.getenv("FIREBASE_CREDENTIALS"))
            )
        except Exception as e:
            logger.exception(f"Error while initializing firebase credentials: {e}")
        self.initialize_app = firebase_admin.initialize_app(self.credentials)
        pass

    def initialize_firebase_client(self):
        return firestore.client()


if not firebase_admin._apps:
    logger.info(f"Instantiating Firebase App...")
    firestore_client = FirebaseRights().initialize_firebase_client()
    logger.info(f"Firebase app instantiated.")
else:
    logger.warning(
        f"Firebase app already instantiated as: {firebase_admin.get_app().name} under project: {firebase_admin._apps[firebase_admin.get_app().name].project_id}"
    )
