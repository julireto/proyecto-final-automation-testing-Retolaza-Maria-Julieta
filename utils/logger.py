import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("automation")

logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler("logs/automation.log", encoding="utf-8")

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
