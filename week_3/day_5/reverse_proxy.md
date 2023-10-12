# Reverse Proxy

A reverse proxy is a server that sits in front of webservers and forwards client requests to those web servers. Helps to increase security, performance, and reliability.



Nginx inspects each HTTP request and identifies which backend system, be it an Apache, Tomcat, Express or NodeJS server, should handle the request

The reverse proxy then forwards the request to that server, allows the request to be processed, obtainsa  response from that backend server, and then sends the response back to the client.

![img.png](images/nginx_reverse_proxy_setup.png)

### What is regular Proxy server?
