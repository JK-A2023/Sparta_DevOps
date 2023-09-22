# API's

1. An Application Programming Interface (API) is a way for computer programs to communicate. 
2. It contrasts with a user interface, which allows for a person to use a computer; an API connects computers or pieces of software together. 
3. An API exists to hide the inner workings of a system, and provide a programmer with the valuable resources the API provides. 
4. API's are made to be 'called' upon - a call to an API is accessing a specific part of the API to provide access to a resource or information. 
5. They define the methods and data formats that applications can use to request and exchange information.

### API uses:

API's are used in every industry, across every sector of collaborative / online programming. Here are some common uses:

1. Web Dev:
   1. API's facilitate communication between web applications and services frequently.
2. Data Pipelines:
   1. 
3. Search Engines:
   1. Enables developers to put search engine functionality into their websites / applications.
4. Weather Data:
   1. Real-time and forecasted weather data is often integrated into applications, mobile apps, websites, or even search engine searches.
5. Social Media:
   1. 

# Rest API

### What is REST API?

A REST API is an API that conforms to the design principles of the REST, or "Representational State Transfer" architectural style.
Hence, RESTful API.

### What is an API RESTful?

Here are the design elements that makes an API RESTful:

- Uniform Interface:
  - Information is transferred in a standard format.
- Client-server Decoupling:
  - Client and server applications must be completely independent of each other.
  - Client application should only know the URL of requested resource.
  - Client application cannot interact with server application in any other way.
  - Server application shouldn't modify client application other than passing it to the requested data via HTTP.
- Statelessness:
  - Each request from a client to a server must contain all the information needed to understand and process the request.
  - The server should not store any client state between requests.
  - This makes RESTful interactions independent and scalable.
- Cacheability:
  - The process of storing some responses on client / intermediary to improve server response time.
  - Each time you visit a new website, the server must send all images and banners once again.
  - Client caches store these images after the first use, and pull them from the cache to reduce server response time.
- Layered System Architecture:
  - A layered system that organizes each type of server (security, load-balancing, etc) involved the retrieval of requested information into hierarchies, invisible to the client.

# HTTP

### What is HTTP?

- Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML.
- It is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks.

### What is HTTP used for?

### Diagrams:

### HTTP Request Structure



### The Five HTTP Verbs:

1. GET
2. POST
3. PUT
4. PATCH
5. DELETE

### Statelessness

### Caching