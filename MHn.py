#using the M/D/n functions we can just directly get the plot for M/H/n

#simulation parameters
mu = 2

rho_values = np.linspace(0.1, 0.99, 30)


waiting_times_H_1 = []
waiting_times_H_2 = []
waiting_times_H_4 = []

#simulation for each p
for rho in rho_values:
    mean_wait_time_H_1 = main(A='M', B='H', n=1, rho=rho, mu=2)
    mean_wait_time_H_2 = main(A='M', B='H', n=2, rho=rho, mu=2)
    mean_wait_time_H_4 = main(A='M', B='H', n=4, rho=rho, mu=2)
    
    waiting_times_H_1.append(mean_wait_time_H_1)
    waiting_times_H_2.append(mean_wait_time_H_2)
    waiting_times_H_4.append(mean_wait_time_H_4)

#plot
plt.figure(figsize=(10, 6))
plt.plot(rho_values, waiting_times_H_1, label='M/H/1')
plt.plot(rho_values, waiting_times_H_2, label='M/H/2')
plt.plot(rho_values, waiting_times_H_4, label='M/H/4')
plt.xlabel('system load (ρ)', fontsize=15)
plt.ylabel('Mean Waiting Time', fontsize=15)
plt.title('Mean Waiting Time vs System Load', fontsize=15)
plt.legend(fontsize=15)
plt.grid()
plt.show()
