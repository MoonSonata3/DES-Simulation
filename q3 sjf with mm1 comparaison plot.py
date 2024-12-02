import random
import simpy
import numpy as np
import matplotlib.pyplot as plt

# Function to generate the inter-arrival time
def generate_interval(A, rho, mu):
    if A == 'M':
        return random.expovariate(rho * mu)  

# Function to generate service time based on distribution
def generate_service(B, mu):
    if B == 'M':  # Markovian (exponential) service
        return random.expovariate(mu)
    elif B == 'D':  # Deterministic service
        return 1 / mu
    elif B == 'H':  # Hyperexponential service
        if random.random() < 0.75:
            return random.expovariate(1)
        else:
            return random.expovariate(1 / 5)

def customerprocessing_sjf(env, wait_times, B, mu, server):
    t_arrival = env.now
    service_time = generate_service(B, mu)

    with server.request(priority=service_time) as request:
        yield request
        t_wait = env.now - t_arrival
        wait_times.append(t_wait)
        yield env.timeout(service_time)

def simulation_sjf(env, A, B, rho, mu, wait_times):
    while True:
        interarrival_time = generate_interval(A, rho, mu)
        yield env.timeout(interarrival_time)
        env.process(customerprocessing_sjf(env, wait_times, B, mu, servers))

def main_sjf(A, B, rho, mu):
    env = simpy.Environment()
    global servers
    servers = simpy.PriorityResource(env, capacity=1)
    wait_times = []
    env.process(simulation_sjf(env, A, B, rho, mu, wait_times))
    env.run(until=20000)  # Simulation run time
    return sum(wait_times) / len(wait_times)

mu = 2
rho_values = np.linspace(0.1, 0.99, 20)
waiting_times_SJF_1 = []

for rho in rho_values:
    mean_wait_time_SJF_1 = main_sjf(A='M', B='M', rho=rho, mu=mu)
    waiting_times_SJF_1.append(mean_wait_time_SJF_1)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(rho_values, waiting_times_SJF_1, label='SJF - M/M/1')
plt.plot(rho_values, waiting_times_M_1, label='M/M/1')
plt.xlabel('System Load (ρ)', fontsize=15)
plt.ylabel('Mean Waiting Time', fontsize=15)
plt.title('Mean Waiting Time vs System Load', fontsize=15)
plt.legend(fontsize=15)
plt.grid()
plt.show()
