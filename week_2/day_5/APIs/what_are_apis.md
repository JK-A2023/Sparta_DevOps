# API's

1. An Application Programming Interface (API) is a way for computer programs to communicate. 
2. It contrasts with a user interface, which allows for a person to use a computer; an API connects computers or pieces of software together. 
3. An API exists to hide the inner workings of a system, and provide a programmer with the valuable resources the API provides. 
4. API's are made to be 'called' upon - a call to an API is accessing a specific part of the API to provide access to a resource or information. 
5. They define the methods and data formats that applications can use to request and exchange information.

### API uses:

API's are used in every industry, across every sector of collaborative / online programming. Here are some common uses:

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

- Retrieving Web Pages
  - Primary used to request and retrieve web pages from web servers.
- Transfer of Resources
- Stateless Communication
  - each request from a client to server is independent and does not retain information about previous requests.
- Uniform Resource Identification.
  - defines uniform way to identify resources.
- Request methods:
  - GET
    - Requests data from a server.
  - POST
    - Submits data to be processed to a specific resource.
  - PUT
    - Updates a resource or creates a new resources if it does not exist.
  - DELETE
    - Removes a specified resource.
  - PATCH
    - Applies partial modifications to a resource.
- Status Codes
- Headers
  - Used to convey additional information about a request or response. Can be content type, length, caching instructions, and more, etc.
- Security
- API's
- Web Services

### HTTP Request Structure

### The Five HTTP Verbs:

  - GET
    - Requests data from a server.
  - POST
    - Submits data to be processed to a specific resource.
  - PUT
    - Updates a resource or creates a new resources if it does not exist.
  - DELETE
    - Removes a specified resource.
  - PATCH
    - Applies partial modifications to a resource.

## VERB URL VERSIONs

This could be GET, POST, PUT, DELETE, etc.

After this is the target URL, and finally the HTTP version.

## Request Headers

HTTP provide additional information about the request or the client making the request.
- Host.
- User-Agent
- Accept
- Content-Type
- Authorization
- Cookie
- Referer

## Request Body

This component is option and only included in requests that require sending data to the server.



![](C:\Users\Andre\Pictures\HTTP_request.png)

## Response Structure

- Status Line
  - HTTP Version
  - Status Code
- Response Headers
  - Content-Type
  - Server
  - Content-Length
  - Cache-Control
  - Location
- Empty Line
- Response Body

![](C:\Users\Andre\Pictures\HTTP_response.png)



### Caching