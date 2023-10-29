**Additions made:**
- A firewall is a network security device that filters incoming and outgoing traffic, serving to block unauthorized access and protect a network from threats. Three firewalls were added: one before the load balancer, and two before each physical server. The firewalls protect each of the components from malicious traffic.
- One SSL certificate to serve `www.foobar.com` over HTTPS. Traffic is served over HTTPS to provide encryption and secure communication, protecting data from interception and ensuring the authenticity of websites and servers.
- Three monitoring Sumologic clients were added for real-time visibility into system and application performance, security, and logs. This helps the sys admins detect issues, troubleshoot problems, and ensure compliance. To monitor web server QPS (Queries Per Second), monitoring tools like Prometheus or Grafana can be used and appropriate web server metrics configured.

*Issues with the design:*
- Having servers with the same components can be problematic because it lacks redundancy and fault tolerance. If one component fails, it affects all servers, increasing the risk of system-wide outages. Diverse server roles and redundancy strategies enhance system reliability. This is also the case when there is only one MySQL server capable of accepting writes.
- Terminating SSL at the load balancer level can be an issue for security reasons. While it offloads the encryption overhead from backend servers, it means that data is decrypted at the load balancer, potentially exposing it to security risks before re-encryption for transmission to the backend.

