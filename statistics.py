import random
import simpy
import numpy as np
import pandas as pd
from scipy import stats

#functions below are generally the same as before
def generate_interval(A, n, rho, mu):
    if A == 'M':
        return random.expovariate(n * rho * mu)

def generate_service(B, mu):
    if B == 'M':  # Markovian service time
        return random.expovariate(mu)
    elif B == 'D':  # Deterministic service time
        return 1 / mu
    elif B == 'H':  # Hyperexponential service time
        if random.random() < 0.75:
            return random.expovariate(1)
        else:
            return random.expovariate(1 / 5)

def customerprocessing(env, wait_times, B, mu):
    t_arrival = env.now
    with servers.request() as request:
        yield request
        t_wait = env.now - t_arrival
        wait_times.append(t_wait)
        service_time = generate_service(B, mu)
        yield env.timeout(service_time)

def simulation(env, A, B, n, rho, mu, wait_times):
    while True:
        interarrival_time = generate_interval(A, n, rho, mu)
        yield env.timeout(interarrival_time)
        env.process(customerprocessing(env, wait_times, B, mu))

def main(A, B, n, rho, mu):
    env = simpy.Environment()
    global servers
    servers = simpy.Resource(env, capacity=n)
    wait_times = []
    env.process(simulation(env, A, B, n, rho, mu, wait_times))
    env.run(until=20000)
    return sum(wait_times) / len(wait_times)

#Run simulation multiple times (num_runs_
def run_simulations(A, B, n, rho, mu, num_runs):
    mean_wait_times = []
    for _ in range(num_runs):
        mean_wait_time = main(A, B, n, rho, mu)
        mean_wait_times.append(mean_wait_time)
    return mean_wait_times

#Calculate statistics for the different runs
def calculate_statistics(mean_wait_times, confidence_level=0.95):
    mean = np.mean(mean_wait_times)
    standard_dev = np.std(mean_wait_times, ddof=1)
    n = len(mean_wait_times)
    alpha = 1 - confidence_level
    t_value = stats.t.ppf(1 - alpha/2, df=n - 1)
    margin_of_error = t_value * standard_dev / np.sqrt(n)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return mean, standard_dev, (lower_bound, upper_bound)

#Simulation parameters
mu = 2
rho = 0.75
num_runs = 30
confidence_level = 0.95

configurations = [
    {'A': 'M', 'B': 'M', 'n': 1, 'rho': rho, 'mu': mu, 'label': 'M/M/1'},
    {'A': 'M', 'B': 'M', 'n': 2, 'rho': rho, 'mu': mu, 'label': 'M/M/2'},
    {'A': 'M', 'B': 'M', 'n': 4, 'rho': rho, 'mu': mu, 'label': 'M/M/4'},
    {'A': 'M', 'B': 'D', 'n': 1, 'rho': rho, 'mu': mu, 'label': 'M/D/1'},
    {'A': 'M', 'B': 'D', 'n': 2, 'rho': rho, 'mu': mu, 'label': 'M/D/2'},
    {'A': 'M', 'B': 'D', 'n': 4, 'rho': rho, 'mu': mu, 'label': 'M/D/4'},
    {'A': 'M', 'B': 'H', 'n': 1, 'rho': rho, 'mu': 1/mu, 'label': 'M/H/1'},
    {'A': 'M', 'B': 'H', 'n': 2, 'rho': rho, 'mu': 1/mu, 'label': 'M/H/2'},
    {'A': 'M', 'B': 'H', 'n': 4, 'rho': rho, 'mu': 1/mu, 'label': 'M/H/4'},
]

# Run simulations and print results
for config in configurations[6:]:
    #print(f"Running {config['label']}")
    mean_wait_times = run_simulations(A=config['A'], B=config['B'], n=config['n'], rho=config['rho'], mu=config['mu'], num_runs=num_runs)
    mean, standard_dev, (lower_bound, upper_bound) = calculate_statistics(mean_wait_times, confidence_level)
    print(f"System: {config['label']}")
    print(f"Mean Waiting Time: {mean:.6f}")
    print(f"Standard Deviation: {standard_dev:.6f}")
    print(f"{int(confidence_level*100)}% Confidence Interval: ({lower_bound:.6f}, {upper_bound:.6f})\n")
