\section{Theoretical $M/M/1$ and $M/M/2$ Waiting Times}
In this section, theoretical results will be derived for the waiting time in the queue in a so-called $M/M/n$-system. This system may be described as one where the inter-arrival times between customers as well as the service time per customer is distributed in a memory-less way according to an exponential distribution, known as a Markovian system. This average waiting time will be calculated for:
\begin{itemize}[noitemsep, topsep=0pt]
    \setlength{\itemsep}{1pt}
    \item an $M/M/1$ queue with system load $\rho$ and processing capacity $\mu$. Here, $\rho=\frac{\lambda}{\mu}$, with $\lambda$ the customer arrival rate and $\mu$ the service time rate/service capacity. 
    \item an $M/M/n$ queue, also with system load $\rho$ and processing capacity $\mu$. In this case, $\rho=\frac{\lambda}{n\mu}$, so the capacity is multiplied by the amount of servers.
\end{itemize}
We want show that the average waiting time is shorter for the $M/M/n$ queue than for the $M/M/1$ queue. In this case specifically for $n=2$.\\
We may use Little's law to derive the average waiting time:
\begin{equation}
    E(N) = \lambda E(T),
\end{equation}
where $E(N)$ is the average number of customers in the system, $\lambda$ the rate of arrivals and $E(T)$ is the average time spent in the system. $E(T)$ is however the average time in the queue and the service time combined. We're only interested in the time in the queue (the waiting time), so we need:
\begin{equation}
    E(N^q) = \lambda E(T^q),
\end{equation}
where $E(N^q)$ is now the average number of customers in the queue, $\lambda$ is still the rate of arrivals and $E(T^q)$ is the average time spent in the queue (the quantity we're looking for).


\begin{itemize}
    \item 
The $M/M/1$-case. From queuing theory, we know that (Myers, n.d.):
\begin{equation}
    E(N) = \frac{\rho}{1-\rho},
\end{equation}
where $\rho$ again is the system load. Straightforwardly, if we subtract the system load (maximum amount of customers the system can handle) from the total number of people in the system, we get the number of customers in the queue: 
\begin{equation}
    E(N^q)=E(N)-\rho = \frac{\rho}{1-\rho} - \rho = \frac{\rho^2}{1-\rho}
\end{equation}
If we now substitute this into Little's law, we get the average waiting time that we're looking for:
\begin{equation}
    E(T^q)=\frac{E(N^q)}{\lambda} = \frac{E(N^q)}{\rho\mu} = \frac{\rho^2}{\rho\mu(1-\rho)} = \frac{\rho}{\mu(1-\rho)}.
\end{equation}
    \item
The $M/M/2$-case. We now need to adapt the average number of people in the queue to include the probabilities that there are either zero or one server in use or that there's 2 or more servers in use (there's a queue), giving some $P_{\text{wait}}$. The average number of people is then given by:
\begin{equation}
    E(N^q) = \frac{\rho P_{\text{wait}}}{\mu(1-\rho)}.
\end{equation}
This $P_{\text{wait}}$ is in turn given by (Myers, n.d.):
\begin{equation}
    P_{\text{wait}} = \frac{(\lambda / \mu)^n}{n!} P_0,
\end{equation}
where $P_0 =(1-\rho)/(1+\rho)$, the probability of zero customers for $n=2$.
Then for the average waiting time, we use Little's law again and find:
\begin{equation}
    E(T^q)= \frac{2\rho^2}{\mu(1-\rho)^2}
\end{equation}
\end{itemize}
Now let's show that the average waiting time for the $M/M/2$ queue is shorter than that of the $M/M/1$ queue. For this, we could look at the difference of both formulas after first expressing them in terms of $\lambda$ and $\mu$:
\begin{align}
\Delta T^q = E(T^q_{M/M/1}) - E(T^q_{M/M/2}) = \frac{\rho}{1-\rho} - \frac{2\rho^2}{\mu(1-\rho)^2} \\
= \frac{\lambda}{\mu(\mu-\lambda)} - \frac{\lambda^2}{\mu(4\mu^2-\lambda^2)}= \frac{\lambda(4\mu^2-\lambda^2) - \lambda^2(\mu-\lambda)}{\mu(\mu-\lambda)(4\mu^2-\lambda^2)} \\
= \frac{\lambda \mu (4\mu-\lambda)}{\mu(\mu-\lambda)(4\mu^2-\lambda^2)}.
\end{align}
We know that $\rho < 1$, which means $\lambda < \mu$. For the nominator we then see that $\mu\lambda>0$ and $4\mu-\lambda>0$, so the nominator is positive. For the denominator we  see that $\mu>0$, $\mu-\lambda>0$ and $4\mu^2-\lambda^2>0$, so also the denominator is positive. This means the difference ($\Delta T^q$) will as well be positive and thus $E(T^q_{M/M/1}) > E(T^q_{M/M/2})$, meaning that the average waiting time in the queue shorter is for an $M/M/2$ queue, as desired.\\
A non-mathematical explanation would be that, in a straightforward way, the customers are divided over more servers, so the server capacity increases and the probability that 'all' servers are in use is smaller when working with 2 servers instead of 1. 
