import logging
import os
import sys
# Define a logging configuration
LOG_FORMAT = "[%(asctime)s] : %(levelname)s - %(module)s - %(message)s"
LOG_LEVEL = logging.INFO

LOG_DIR='logs'
LOG_FILEPATH=os.path.join(LOG_DIR,'kidneyDiseaseNet.log')

os.makedirs(LOG_DIR,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
        
    ]
)
logger=logging.getLogger('kidneyDiseaseNet')

# Example of using the logger
if __name__ == "__main__":
    logger.info("KidneyDiseaseNet application started.")
    logger.debug("Debugging details.")
    logger.error("An error occurred.")
