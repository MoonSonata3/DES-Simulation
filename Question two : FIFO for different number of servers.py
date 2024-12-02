import random
import simpy
import numpy as np
import matplotlib.pyplot as plt

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


#simulation parameters
mu = 2

rho_values = np.linspace(0.1, 0.99, 20)
waiting_times_M_1 = []
waiting_times_M_2 = []
waiting_times_M_4 = []

#simulation for each p
for rho in rho_values:
    mean_wait_time_M_1 = main(A='M', B='M', n=1, rho=rho, mu=2)
    mean_wait_time_M_2 = main(A='M', B='M', n=2, rho=rho, mu=2)
    mean_wait_time_M_4 = main(A='M', B='M', n=4, rho=rho, mu=2)

    waiting_times_M_1.append(mean_wait_time_M_1)
    waiting_times_M_2.append(mean_wait_time_M_2)
    waiting_times_M_4.append(mean_wait_time_M_4)

#plot
plt.figure(figsize=(10, 6))
plt.plot(rho_values, waiting_times_M_1, label='M/M/1')
plt.plot(rho_values, waiting_times_M_2, label='M/M/2')
plt.plot(rho_values, waiting_times_M_4, label='M/M/4')
plt.xlabel('system load (ρ)', fontsize=15)
plt.ylabel('Mean Waiting Time', fontsize=15)
plt.title('Mean Waiting Time vs system load', fontsize=15)
plt.legend(fontsize=15)
plt.grid()
plt.show()
