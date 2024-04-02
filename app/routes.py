from asyncio import sleep
from threading import Timer
from app import webserver
from flask import request, jsonify
from app import ThreadPool

import os
import json

from app.task_runner import TaskRunner

# Example endpoint definition
@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():
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
    print(f"JobID is {job_id}")
    # TODO
    # Check if job_id is valid
    job_id = int(job_id)
    if job_id > webserver.job_counter:
        return jsonify({'status': 'error', 'reason': 'Invalid job id'}), 200
    
    for job in webserver.allJobs:
        if job_id in job:
            if job[job_id] == 'running':
                return jsonify({'status': 'running'}), 200
            elif job[job_id] == 'done':
                path = os.path.join(webserver.dir, str(job_id)) 
                with open(path, "r") as f:
                    res = json.load(f)
                    return jsonify({'status': 'done', 'data': res}), 200
    
    # Check if job_id is done and return the result
    #    res = res_for(job_id)
    #    return jsonify({
    #        'status': 'done',
    #        'data': res
    #    })

    # If not, return running status
    
    return jsonify({'status': 'Server Error'})

@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    # Get request data
    data = request.json
    print(f"Got request {data}")

    # TODO
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.states_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.states_mean, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id
    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.state_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.state_mean, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200


@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.best5, [data, webserver.data_ingestor])
    item = (TaskRunner.best5, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.worst5, [data, webserver.data_ingestor])\
    item = (TaskRunner.worst5, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.global_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.global_mean, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.diff_from_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.diff_from_mean, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    #print(webserver.allJobs)
    # item = (TaskRunner.state_dif_from_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.state_dif_from_mean, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)


    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id
    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    # item = (TaskRunner.state_dif_from_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.mean_by_category, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200


@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    # TODO
    # Get request data
    # Register job. Don't wait for task to finish
    # Increment job_id counter
    # Return associated job_id

    data = request.json
    webserver.job_counter += 1
    webserver.allJobs.append({webserver.job_counter: 'running'})
    #webserver.tasks_runner.allJobs.append({webserver.job_counter, 'running'})
    webserver.tasks_runner.job_count = webserver.job_counter
    # item = (TaskRunner.state_dif_from_mean, [data, webserver.data_ingestor])
    item = (TaskRunner.state_mean_by_category, (data, webserver.data_ingestor, webserver.job_counter, webserver.allJobs))

    webserver.tasks_runner.submit(item)

    return jsonify({"job_id": webserver.job_counter}), 200

@webserver.route('/api/graceful_shutdown', methods=['GET'])
def graceful_shutdown_request():
    webserver.tasks_runner.shutdown()
    webserver.shutDown = 1

    return jsonify({"graceful_shutdown":"done"}), 200

@webserver.route('/api/jobs', methods=['GET'])
def jobs_request():
    return jsonify({"status": "done", "data": webserver.allJobs}), 200

@webserver.route('/api/num_jobs', methods=['GET'])
def num_jobs_request():
    cnt = 0
    for elem in webserver.allJobs:
        for _, v in elem.items():
            if v == 'running':
                cnt += 1
    if cnt == 0:
        if webserver.shutDown == 1:
            print('ok')
            #use something else than sleep
            Timer(10, os._exit, [os.EX_OK])
            #sleep(100)
            #write me a command that exit the program
           # os._exit(os.EX_OK)



            # os._exit(os.EX_OK)
            
        return jsonify({'status':'done', 'data': cnt}), 200

# You can check localhost in your browser to see what this displays
@webserver.route('/')
@webserver.route('/index')
def index():
    routes = get_defined_routes()
    msg = f"Hello, World!\n Interact with the webserver using one of the defined routes:\n"

    # Display each route as a separate HTML <p> tag
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"

    msg += paragraphs
    return msg

def get_defined_routes():
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f"Endpoint: \"{rule}\" Methods: \"{methods}\"")
    return routes
