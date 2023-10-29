**For every additional element, why you are adding it**
The improved setup has two master servers and a slave server. The master server will work based on an Active-Active setup with identical configuration. All elements of the previous simple web infrastructure are maintained. The load balancer manages the load-distributing queries using a Robin-Round algorithm. 

**What distribution algorithm your load balancer is configured with, and how it works**
The load balancer in this web infrastructure uses a Round Robin algorithm distribution. In this algorithm, requests are distributed sequentially, one after the other, to each server in a circular order. The load balancer maintains a list of available backend servers and uses a simple counter to keep track of the following server to which it should send a request. It sends the HTTP request to the first server and increments its counter for each subsequent HTTP request. When it reaches the end of the server list, it loops back to the first and continues with the process. The round-robin algorithm ensures equal distribution of requests and is favourable for servers of similar capabilities.

**Is your load balancer enabling an Active-Active or Active-Passive setup? Explain the difference between both.**
The load balancer used in this setup is the Active-Actie setup.
In an Active-Active setup, all servers are handling traffic simultaneously. The setup is suitable for balancing loads and distributing requests across multiple servers. This setup is associated with high performance and helpful redundancy when one server faces downtime. In an Active-Passive setup, one server handles requests while the passive server remains inactive, acting as a backup. This setup is ideal for failover scenarios where, if the main server fails, a viable backup is available. 

**How a database Primary-Replica (Master-Slave) cluster works**
Master slave replication allows data replication from the master database to other databases, i.e., slave databases. The master logs the changes, which are then passed to the individual databases. The slave databases then output confirmation messages to acknowledge the receipt of the changes. Replication can be either synchronous or asynchronous. The difference is simply the timing of the propagation of changes. If the changes are made to the master and slave simultaneously, it is synchronous. If changes are queued up and written later, it is asynchronous.
What is the difference between the Primary node and the Replica node in regard to the application?
The primary node is responsible for write operations, modification, and integrity. It serves as the authoritative source for data changes. The replica nodes are primarily used for read operations, data synchronization, redundancy, and load balancing. By segregating these roles, the Primary-Replica cluster balances high availability and efficient data access for applications.

*Issues with the Set Up:*

**Where are SPOFs?**

There are still several SPOFs within the web infrastructure. If the primary MySQL database server experiences downtime, the entire application cannot change the database. In addition, the server containing the load balancer and application server are also SPOFs that could fail the system.

**Security issues**
Data transmitted over the network lacks encryption via SSL certificates, making it susceptible to interception by potential hackers. Additionally, the absence of a firewall on any server means there is no mechanism to block unauthorized IP addresses, potentially compromising network security.

**No monitoring**
There is a lack of server monitoring in place, meaning there is no real-time tracking or oversight of server performance, health, or security. This absence of monitoring can lead to challenges in identifying and addressing issues promptly.

