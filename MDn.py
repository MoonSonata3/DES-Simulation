import random
import simpy
import numpy as np
import matplotlib.pyplot as plt

#function for the interarrival time distribution
def generate_interval(A, n, rho, mu):
    if A == 'M':
        return random.expovariate(n * rho * mu)
#function for the service time distribution
def generate_service(B, mu):
    if B == 'M':  # Markovian service time
        return random.expovariate(mu)
    elif B == 'D':  # Deterministic service time
        return 1 / mu
    elif B == 'H':  # Hyperexponential service time
        if random.random() < 0.75:
            return random.expovariate(mu)
        else:
            return random.expovariate(mu / 5)

#function for the journey the customer takes
def customerprocessing(env, wait_times, B, mu):
    t_arrival = env.now
    with servers.request() as request:
        yield request
        t_wait = env.now - t_arrival
        wait_times.append(t_wait)
        service_time = generate_service(B, mu)
        yield env.timeout(service_time)

#simulating the queing
def simulation(env, A, B, n, rho, mu, wait_times):
    while True:
        interarrival_time = generate_interval(A, n, rho, mu)
        yield env.timeout(interarrival_time)
        env.process(customerprocessing(env, wait_times, B, mu))

#main function that runs everything to get the waiting times
def main(A, B, n, rho, mu):
    env = simpy.Environment()
    global servers
    servers = simpy.Resource(env, capacity=n)
    wait_times = []
    env.process(simulation(env, A, B, n, rho, mu, wait_times))
    env.run(until=20000)
    return sum(wait_times) / len(wait_times)
 

#simulation parameters
mu = 2

rho_values = np.linspace(0.1, 0.99, 30)

waiting_times_D_1 = []
waiting_times_D_2 = []
waiting_times_D_4 = []

#simulation for each p
for rho in rho_values:
    mean_wait_time_D_1 = main(A='M', B='D', n=1, rho=rho, mu=mu)
    mean_wait_time_D_2 = main(A='M', B='D', n=2, rho=rho, mu=mu)
    mean_wait_time_D_4 = main(A='M', B='D', n=4, rho=rho, mu=mu)
    
    waiting_times_D_1.append(mean_wait_time_D_1)
    waiting_times_D_2.append(mean_wait_time_D_2)
    waiting_times_D_4.append(mean_wait_time_D_4)

#plot
plt.figure(figsize=(10, 6))
plt.plot(rho_values, waiting_times_D_1, label='M/D/1')
plt.plot(rho_values, waiting_times_D_2, label='M/D/2')
plt.plot(rho_values, waiting_times_D_4, label='M/D/4')
plt.xlabel('system load (ρ)', fontsize=14)
plt.ylabel('Mean Waiting Time', fontsize=14)
plt.title('Mean Waiting Time vs system load', fontsize=14)
plt.legend(fontsize=14)
plt.grid()
plt.show()
