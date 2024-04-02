from flask import Flask
from app.data_ingestor import DataIngestor
from app.task_runner import ThreadPool
import os

webserver = Flask(__name__)
webserver.tasks_runner = ThreadPool()

# webserver.task_runner.start()

webserver.data_ingestor = DataIngestor("./nutrition_activity_obesity_usa_subset.csv")
webserver.job_counter = 0

webserver.dir = "./results/"
os.makedirs(os.path.dirname(webserver.dir), exist_ok=True)
webserver.allJobs = []
webserver.shutDown = 0


from app import routes
