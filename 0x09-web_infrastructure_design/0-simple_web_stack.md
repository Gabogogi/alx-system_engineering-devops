What is a server?
A server is a physical computer, a virtual machine, or a computer program that provides a service to another computer known as a client. A computer can be a server, and a server can be a computer. The main difference is capacity, where servers are computers with faster processing and request-handling capabilities. 

What is the role of the domain name?
Domain names provide a user-friendly and human-readable way to access the internet. Domain names serve as alternatives to numeric IP addresses, which are not intuitive for the most part. 

What type of DNS record is www in www.foobar.com?
The “www” in a domain name is a type of DNS record known as a “CNAME” Canonical Name record. The CNAME points to the primary domain or the root domain., which in this case is foobar.com. CNAME allows a user to alias the “www” subdomain to the root domain, allowing www.foobar.com to resolve to the same as “foobar.com”. This configuration simplifies maintenance and configuration since changes applied to the root domain apply to the “www” domain as well. 
What is the role of the web server?
The primary responsibility of a web server is to handle HTTP/S requests from clients and return HTTP/S responses typically consisting of HTML< CSS, JavaScript, and other static assets, images, and videos. When a web server receives a request from the client, it determines which static assets need to be returned in response to the request. If the response requires static files only, the web server serves the client the requested file from the codebase without calling the application server. If the response is dynamic and requires application logic such as user authentication, data retrieval, etc., the web server forwards the request to the application server. Once the application server processes the request, it responds appropriately to the web server. The server, as before, returns a suitable request to the user.
What is the role of the application server?
Application servers handle the core business of web applications. Core functions include authentication, authorization, data validation, and execution of the core tasks of the application. The application server handles dynamic content generation based on user requests. It executes server-side code in Python, Ruby, Java, Noge.js, etc. This code processes data, performs calculations, interacts with databases, and generates suitable responses such as HTML, JSON, and XML files.
What is the role of the database?
The fundamental role of databases is to store and manage data in a structured and efficient manner. Databases facilitate the criterion, retrieval, updating/manipulation, and deleting of data or CRUD manipulation. Typical structures of databases include relational databases, non-relational databases, cloud databases, and NoSQL databases, among others. 

What is the server using to communicate with the computer of the user requesting the website?
Servers use the HTTP (Hypertext Transfer Protocol) to communicate with computers. This protocol is ubiquitous on the World Wide Web, involving client requests and server responses. A typical HTTP Request contains information on what the user is asking for and the format they wish it returned to. Conversely, an HTPP response contains the information the user requested in the format specified.


You must be able to explain what the issues are with this infrastructure.

SPOF
Single point of Failure (SPOF) refers to a condition where if one component in a system fails, the entire system fails. SPOF arises due to a lack of redundancy or failover mechanisms that ensure operations when a system fails. SPOF events are associated with downtime, data loss, interruptions, and security vulnerabilities.
Downtime when maintenance is needed (like deploying new code web server needs to be restarted)
Similarly, when any mode in the system needs to be repaired, the entire system has to be shut down. During such times, the website is unavailable, and client requests cannot be processed.
Cannot scale if too much incoming traffic
When there is an influx of incoming traffic, there are no mechanisms to address the increased load of the server. Excess traffic leads to a possible breakdown of the web age when traffic surpasses the server's capacity.



