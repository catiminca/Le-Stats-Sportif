from queue import Queue
import random
from threading import Thread, Event
import time
from os import environ, cpu_count
from decimal import Decimal
import json

class ThreadPool:
    def __init__(self):
        # You must implement a ThreadPool of TaskRunners
        # Your ThreadPool should check if an environment variable TP_NUM_OF_THREADS is defined
        # If the env var is defined, that is the number of threads to be used by the thread pool
        # Otherwise, you are to use what the hardware concurrency allows
        # You are free to write your implementation as you see fit, but
        # You must NOT:
        #   * create more threads than the hardware concurrency allows
        #   * recreate threads for each task
        self.nr_th = 0
        self.thread_list = []
        self.queue = Queue()
        self.th_event = Event()
      
        if 'TP_NUM_OF_THREADS' in environ:
            self.nr_th = 'TP_NUM_OF_THREADS'
            for _ in range('TP_NUM_THREADS'):
                thread = TaskRunner(self.queue, self.th_event)
                self.thread_list.append(thread)
                thread.start()

        else:
            self.nr_th = cpu_count()
            for _ in range(cpu_count()):
                thread = TaskRunner(self.queue, self.th_event)
                self.thread_list.append(thread)
                thread.start()
    
    def submit(self, job_id):
        self.queue.put(job_id)
        #self.job_count += 1
            
    def shutdown(self):
        self.th_event.set()
        for th in self.thread_list:
            th.join()

class TaskRunner(Thread):
    def __init__(self, queue, shutdown_flag):
        Thread.__init__(self)
        # self.file = file
        # self.question = question
        self.queue = queue
        self.result = None
        self.shutdown_flag = shutdown_flag
        #self.allJobs = allJobs

        # TODO: init necessary data structures        
    def run(self):
        while True:
            # TODO
            if self.shutdown_flag.is_set() and self.queue.empty():
                break

            try:
                item = self.queue.get_nowait()
            except:
                continue
            
            (func, args) = item
            #print(args[3][args[2] - 1])


            # print(func(*args))
            # cnt = 0
            # for elem in args[3]:
            #     print(elem)
            #     for k in elem:
            #         print(k, "a")
            #     # if elem[0] == args[2]:
            #     #     args[3][cnt][args[2]] = 'done'
            #     cnt += 1

            file_name = "./results/" + str(args[2])
            
            f = open(file_name, 'w')
            res = func(*args)
            f.write(json.dumps(res))
            f.close()

            args[3][args[2] - 1][args[2]] = 'done'
            #print(args[3])

            # Get pending job
            # Execute the job and save the result to disk
            # Repeat until graceful_shutdown

            self.queue.task_done()
            #self.allJobs[self.job_count] = 'done'

    
    def states_mean(question, data_ingestor, c, j):
        states_list = {}
        allStates = {}
        allMeds = []
        finalStatesMed = {}
        str_question = question['question']
        for row in data_ingestor.allData[str_question]:
            if row[4] in states_list:
                states_list[row[4]].append(row[11])
            else:
                states_list[row[4]] = [row[11]]
        for loc in states_list:
            med_val = 0.0
            len_val = len(states_list[loc])
            sum_val = 0.0
            for med in states_list[loc]:
                sum_val += float(med)
            med_val = sum_val / len_val
            allMeds.append(med_val)
            allStates[loc] = med_val
        allMeds.sort()
        for med in allMeds:
            for state, value in allStates.items():
                if value == med:
                    finalStatesMed[state] = value
        #print(finalStatesMed)
        return finalStatesMed

    def state_mean(question, data_ingestor, c, j):
        states_list = {}
        allStates = {}
        state = question['state']
        for row in data_ingestor.allData[question['question']]:
            if row[4] == state:
                if row[4] in states_list:
                    states_list[row[4]].append(row[11])
                else:
                    states_list[row[4]] = [row[11]]
        #print(states_list)
        med_val = 0.0
        len_val = len(states_list[state])
        sum_val = 0.0
        for med in states_list[state]:
            sum_val += float(med)
        med_val = sum_val / len_val
        allStates[state] = med_val
        #print(allStates)
        return allStates
    
    def best5(question, data_ingestor, c, j):
        states_list = {}
        allStates = {}
        allMeds = []
        finalStatesMed = {}
        for row in data_ingestor.allData[question['question']]:
            if row[4] in states_list:
                states_list[row[4]].append(row[11])
            else:
                states_list[row[4]] = [row[11]]
        for loc in states_list:
            med_val = 0.0
            len_val = len(states_list[loc])
            sum_val = 0.0
            for med in states_list[loc]:
                sum_val += float(med)
            med_val = sum_val / len_val
            allMeds.append(med_val)
            allStates[loc] = med_val
        if question['question'] in data_ingestor.questions_best_is_min:
            allMeds.sort()
        elif question['question'] in data_ingestor.questions_best_is_max:
            allMeds.sort(reverse=True)
        aux = []
        for i in range(5):
            aux.append(allMeds[i])
        for i in range(len(aux)):
            for state, value in allStates.items():
                if value == aux[i]:
                    finalStatesMed[state] = value

        return finalStatesMed
        
    
    def worst5(question, data_ingestor,c, j):
        states_list = {}
        allStates = {}
        allMeds = []
        finalStatesMed = {}
        for row in data_ingestor.allData[question['question']]:
            if row[4] in states_list:
                states_list[row[4]].append(row[11])
            else:
                states_list[row[4]] = [row[11]]
        for loc in states_list:
            med_val = 0.0
            len_val = len(states_list[loc])
            sum_val = 0.0
            for med in states_list[loc]:
                sum_val += float(med)
            med_val = sum_val / len_val
            allMeds.append(med_val)
            allStates[loc] = med_val

        if question['question'] in data_ingestor.questions_best_is_min:
            allMeds.sort(reverse=True)
        elif question['question'] in data_ingestor.questions_best_is_max:
            allMeds.sort()
        aux = []
        for i in range(5):
            aux.append(allMeds[i])
        for med in aux:
            for state, value in allStates.items():
                if value == med:
                    finalStatesMed[state] = value

        return finalStatesMed
    
    def global_mean(question, data_ingestor, count, jobs):
        global_med = 0.0
        sum_med = 0.0
        len_med = len(data_ingestor.allData[question['question']])
        for row in data_ingestor.allData[question['question']]:
            sum_med += float(row[11])
        global_med = sum_med / len_med
        return {'global_mean': global_med}
    
    def diff_from_mean(question, data_ingestor, c, j):
        global_mean_res = TaskRunner.global_mean(question, data_ingestor, c, j)['global_mean']
        
        state_mean_res = TaskRunner.states_mean(question, data_ingestor, c, j)
        final_res = {}
        for loc, med in state_mean_res.items():
            final_res[loc] = float(global_mean_res - med)

        return final_res

    def state_dif_from_mean(question, data_ingestor, c, j):
        global_mean_res = TaskRunner.global_mean(question, data_ingestor, c, j)['global_mean']
        state_mean_res = TaskRunner.states_mean(question, data_ingestor, c, j)
        res = 0
        state = question['state']
        for loc, med in state_mean_res.items():
            if loc == state:
                res = float(global_mean_res - med)
                break
        return {state: res}

    def mean_by_category(question, data_ingestor, c, j):
        allCateg = {}
        finalMed = {}
            
        # print(len(allCateg)) 
        for row in data_ingestor.allData[question['question']]:
            key = (row[4], row[30], row[31])
            if key in allCateg:
                allCateg[key].append(row[11])
            else:
                allCateg[key] = [row[11]]
        #print(allCateg)
        for k, v in allCateg.items():
            sum_categ = 0.0
            len_categ = len(v)
            med_categ = 0.0
            for elem in v:
                sum_categ += float(elem)
            med_categ = sum_categ / len_categ
            if k[0] and k[1] and k[2]:
                finalMed[str(k)] = med_categ

        return finalMed

    def state_mean_by_category(question, data_ingestor, c, j):
        allCateg = {}
        finalMed = {}
        for row in data_ingestor.allData[question['question']]:
            if question['state'] == row[4]:
                key = (row[30], row[31])
                if key in allCateg:
                    allCateg[key].append(row[11])
                else:
                    allCateg[key] = [row[11]]
                
        #print(allCateg)
        aux = {}
        for k, v in allCateg.items():
            sum_categ = 0.0
            len_categ = len(v)
            med_categ = 0.0
            for elem in v:
                sum_categ += float(elem)
            med_categ = sum_categ / len_categ
            finalMed[str(k)] = med_categ
        aux[question['state']] = finalMed 
        return aux


            

# def cool_func(a, b):
#     return f"Numarul a este {a} si numarul b este {b}"


# if __name__ == '__main__':
#     threadPool = ThreadPool()

#     for _ in range(15):
#         for _ in range(15):
#             a = random.random() * 1000
#             b = random.random() * 1000

#             threadPool.submit((cool_func, [a, b]))

#     threadPool.shutdown()



