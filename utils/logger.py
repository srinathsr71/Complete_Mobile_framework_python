import logging
import os
from datetime import datetime


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True
    )

    logging.info("===== Test execution started =====")
