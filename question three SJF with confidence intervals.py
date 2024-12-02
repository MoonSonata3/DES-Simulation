import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

lambdaa = 1.5
mu = 2
time = 1000
waitingtime = []

def customerprocessing_sjf(env, clientnumber, server):
    arrival_time = env.now
    service_time = random.expovariate(mu)

    with server.request(priority=service_time) as request:
        yield request
        wait_time = env.now - arrival_time
        waitingtime.append(wait_time)

        yield env.timeout(service_time)

def simulation_sjf():
    global waitingtime
    waitingtime = []

    env = simpy.Environment()
    server = simpy.PriorityResource(env, capacity=1)

    for i in range(1, 60):
        env.process(customerprocessing_sjf(env, i, server))

    env.run(until=time)

    return np.mean(waitingtime)

def simulation_complex_sjf(itermax=500):
    all_wait_times = []

    for _ in range(itermax):
        avg_wait_time = simulation_sjf()
        all_wait_times.append(avg_wait_time)

    mean_waiting_time = np.mean(all_wait_times)
    std_dev = np.std(all_wait_times)
    return mean_waiting_time, std_dev, all_wait_times

mean_waiting_time, std_dev, all_wait_times = simulation_complex_sjf(500)

print(f"Average waiting time for M/M/1 with Shortest Job First (SJF) after 500 iterations: {mean_waiting_time} ± {std_dev}")

def confidence_interval(wait_time_list, no_of_runs, p=0.95):
    standard_dev = np.std(wait_time_list)
    mean = np.mean(wait_time_list)
    z_value = norm.ppf((p + 1) / 2)
    margin_of_error = z_value * standard_dev / math.sqrt(no_of_runs)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound

lower_bound, upper_bound = confidence_interval(all_wait_times, len(all_wait_times), p=0.95)

print(f"95% Confidence interval for the average waiting time: ({lower_bound}, {upper_bound})")

