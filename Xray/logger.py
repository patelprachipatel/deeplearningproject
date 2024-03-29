import os 
 from Xray.constant.training_pipeline import TIMESTAMP

 LOG_FILE: F"{TIMESTAMP}.log"

 logs_path = os.file.join(os.getcwd(), "logs" , TIMESTAMP)

 os.makedirs(logs_path, exist_ok=True)

 LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

 logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s -%(message)s"

 )