"""Module for routes"""

import os
import json
from flask import request, jsonify
from app import webserver
from app.task_runner import TaskRunner

# Example endpoint definition
@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():
    """Example endpoint definition"""
    if request.method == 'POST':
        # Assuming the request contains JSON data
        data = request.json
        print(f"got data in post {data}")
        # Process the received data
        # For demonstration purposes, just echoing back the received data
        response = {"message": "Received data successfully", "data": data}

        # Sending back a JSON response
        return jsonify(response)
    else:
        # Method Not Allowed
        return jsonify({"error": "Method not allowed"}), 405

@webserver.route('/api/get_results/<job_id>', methods=['GET'])
def get_response(job_id):
    """Get results for a job_id"""
    print(f"JobID is {job_id}")
    # Check if job_id is valid
    job_id = int(job_id)
    if job_id > webserver.job_counter:
        webserver.logger.info("Receive from get_results/%s: Invalid job id :%s", job_id, job_id )
        return jsonify({'status': 'error', 'reason': 'Invalid job id'}), 200
    for job in webserver.allJobs:
        if job_id in job:
            if job[job_id] == 'running':
                webserver.logger.info("Receive from get_results/%s: Job is running :%s",
                                      job_id, job_id)
                return jsonify({'status': 'running'}), 200
            elif job[job_id] == 'done':
                path = os.path.join(webserver.dir, str(job_id))
                with open(path, "r") as f:
                    res = json.load(f)
                    webserver.logger.info("Receive from get_results/%s: Job is done :%s",
                                          job_id, job_id)
                    return jsonify({'status': 'done', 'data': res}), 200
    return jsonify({'status': 'Server Error'})

@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    """Solve states_mean"""
    data = request.json
    print(f"Got request {data}")
    webserver.logger.info("Request for states_mean :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.states_mean, (TaskRunner, data, webserver.data_ingestor, webserver.job_counter,
                                     webserver.allJobs))
    webserver.tasks_runner.submit(item)
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id
    webserver.logger.info("Job id for states_mean :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    """Solve state_mean"""
    data = request.json
    webserver.logger.info("Request for state_mean :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.state_mean, (TaskRunner, data, webserver.data_ingestor, webserver.job_counter,
                                    webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for state_mean :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200


@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    """Solve best5"""
    data = request.json
    webserver.logger.info("Request for best5 :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.best5, (TaskRunner, data, webserver.data_ingestor, webserver.job_counter,
                               webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for best5 :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    """Solve worst5"""
    data = request.json
    webserver.logger.info("Request for worst5 :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.worst5, (TaskRunner, data, webserver.data_ingestor, webserver.job_counter,
                                webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for worst5 :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    """Solve global_mean"""
    data = request.json
    webserver.logger.info("Request for global_mean :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.global_mean, (TaskRunner, data, webserver.data_ingestor, webserver.job_counter,
                                     webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for global_mean :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    """Solve diff_from_mean"""
    data = request.json
    webserver.logger.info("Request for diff_from_mean :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.diff_from_mean, (TaskRunner, data, webserver.data_ingestor,
                                        webserver.job_counter, webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for diff_from_mean :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    """Solve state_diff_from_mean"""
    data = request.json
    webserver.logger.info("Request for state_diff_from_mean :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.state_dif_from_mean, (TaskRunner, data, webserver.data_ingestor,
                                            webserver.job_counter, webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for state_diff_from_mean :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    """Solve mean_by_category"""
    data = request.json
    webserver.logger.info("Request for mean_by_category :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    item = (TaskRunner.mean_by_category, (TaskRunner, data, webserver.data_ingestor,
                                          webserver.job_counter, webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for mean_by_category :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200


@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    """Solve state_mean_by_category"""
    data = request.json
    webserver.logger.info("Request for state_mean_by_category :%s", data)
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    webserver.tasks_runner.job_count = webserver.job_counter
    item = (TaskRunner.state_mean_by_category, (TaskRunner, data, webserver.data_ingestor,
                                                webserver.job_counter, webserver.allJobs))
    webserver.tasks_runner.submit(item)
    webserver.logger.info("Job id for state_mean_by_category :%s", {webserver.job_counter})
    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/graceful_shutdown', methods=['GET'])
def graceful_shutdown_request():
    """Solve graceful shutdown"""
    webserver.tasks_runner.shutdown()
    webserver.logger.info("Request for graceful shutdown: done")
    return jsonify({"graceful_shutdown":"done"}), 200

@webserver.route('/api/jobs', methods=['GET'])
def jobs_request():
    """Solve get all jobs"""
    webserver.logger.info("Request for all jobs: %s", {webserver.allJobs})
    return jsonify({"status": "done", "data": webserver.allJobs}), 200

@webserver.route('/api/num_jobs', methods=['GET'])
def num_jobs_request():
    """Solve get number of jobs"""
    cnt = 0
    for elem in webserver.allJobs:
        for _, v in elem.items():
            if v == 'running':
                cnt += 1
    webserver.logger.info("Number of jobs request are: %s", {cnt})
    return jsonify({'status':'done', 'data': cnt}), 200

# You can check localhost in your browser to see what this displays
@webserver.route('/')
@webserver.route('/index')
def index():
    """index function"""
    routes = get_defined_routes()
    msg = f"Hello, World!\n Interact with the webserver using one of the defined routes:\n"

    # Display each route as a separate HTML <p> tag
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"

    msg += paragraphs
    return msg

def get_defined_routes():
    """Defined routes"""
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f"Endpoint: \"{rule}\" Methods: \"{methods}\"")
    return routes
