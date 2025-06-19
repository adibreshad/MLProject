import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True) # Create the directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__== "__main__": # This line was already present, no change needed for indentation.
    logging.info("Logging setup complete.")
    print(f"Logs will be saved to {LOG_FILE_PATH}")
    # Example log messages
    logging.info("This is an info message.")
    logging.error("This is an error message.")
    logging.debug("This is a debug message.")
    logging.warning("This is a warning message.")