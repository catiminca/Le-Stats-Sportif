from flask import Flask
from app.data_ingestor import DataIngestor
from app.task_runner import ThreadPool
import os
import logging
from logging.handlers import RotatingFileHandler

webserver = Flask(__name__)
webserver.tasks_runner = ThreadPool()

# webserver.task_runner.start()

webserver.data_ingestor = DataIngestor("./nutrition_activity_obesity_usa_subset.csv")
webserver.job_counter = 0

webserver.dir = "./results/"
os.makedirs(os.path.dirname(webserver.dir), exist_ok=True)
webserver.allJobs = []
webserver.shutDown = 0


webserver.logger = logging.getLogger('webserver.log')
handler = RotatingFileHandler('file.log', maxBytes=2000, backupCount=10)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
webserver.logger.setLevel(logging.INFO)
webserver.logger.addHandler(handler)

from app import routes
