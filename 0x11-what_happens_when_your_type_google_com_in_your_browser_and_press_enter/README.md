# what happens when you type a url in the web browser?

In this article, you are going to learn a few important things or processes that happens under the hood when you type a url in your web browser (chrome, safari, edge, firefox, brave, etc).
you will learn about the following:
* domain name 
* domain name service
* HTTPS/SSL
* OSI model
* Load balancer
* Firewall
* Web server
* Web Application
* Database

When you type in a url into your web browser, in this case `www.google.com`,your browser converts it to the following: `https://www.google.com`. Lets analyze all the info within the url taking one part at a time to explain the concept behind how they function and do what they do.  

### https:  
This is a protocol scheme that is use to indicate a method for initiating communication connection on the web. HTTPS means Hypertext Transfer Protocol Secure. It simply means that at the establishment of the connection, all communication will be secured and encrypted between client(browser) and web server. HTTPS is just one among many other web connection protocol e.g `http`, `ftp` e.t.c .  

### www:
This is subdomain which means the "World Wide Web", you can customize it as the need arises for various section of your website.  

### Google:
This is a second level domain and it usually identify the name of organization which in this case identifies Google

### Top Level domain (.com, .org, .gov, .net, .edu ...)
dot com is a top level domain that serves many interpretation,but in this case, we have `.com` and it interpret it as a commercial entity. Some could be `.org` that is it for an organization, others could be `.edu`, it therefore serve the purposes of education. There are other top level domain.  

Having understood the url, let's proceed to press enter key on the keyboard. At this stage, we will discuss about DNS.

### Domain Name Service/system (DNS)  
Humans find it hard to remember numbers while computer easily work with numbers. Because of this, the DNS was create to match a domain A record name (google.com) to the ip address of the web-server. instead of you to memorize the ip address (216.58.223.238) and type it into your browser you could just easily remember google.com and type it into your browser. So you can think of DNS as a phone-book where you do not need to remember the phone number but the contact name of whomever you want to call.  
    There are a series of processes/steps associated with DNS. First, your computer operating system checks it's local cache to see if a previously resolved ip address is found for the given domain name if not, it sends a query to a DNS resolver which is typically provided by your ISP (internet service provider) or public DNS server like cloudflare DNS.  
The resolver interacts with the DNS hierarchy, starting with the root DNS server. These servers provides information about TLD(top level domain) servers (.com, .org, .edu). The resolver contacts the right TLD server, which directs it to the authoritative name server for the specific domain.  
The authoritative name server holds the ip address associated with the domain name, and the resolver retrieves it and returns it to your browser. Does that make sense up to this point?  
Now, your browser takes the ip address and initiate a connection with the web server hosting the requested website. The server will respond by sending back the requested web page of which your browser renders for you to interact with.  

Now to initiate the connection, let quickly OSI model and discuss briefly about the network layer, transport layer and application layer. They all come into play to establish the connection.
* IP is the section of the Network layer
* TCP is the section of the Transport layer
* HTTPS is the section of the application layer

To establish connection, your browser indicates a TCP 3-way handshake which involves 3 steps:
* **SYN**:  Browser sends a synchronize (SYN) packet to the web server, indicating it desire to establish a connection.
* **SYN-ACK**: The web-server sends a responds with a synchronize-acknowledge (SYN-ACK) packet, which means that it acknowledge the request and indicates it willingness to establish a connection.
* **ACK**: Your browser sends an acknowledge (AWK) packet back to the server, confirming the connection establishment.  

After the handshake is complete, connection  is established between client and web-server. This connection allows for the transmission of HTTP request and response.  

## HTTPS/SSL 
Accessing a website over a secure connection such as https://www.google.com, the HTTPS protocol indicates that the communication is encrypted. HTTPS which stands for "Hypertext Transfer Protocol Secure" add an extra layer of security by encrypting the data exchanged between client and the server. With HTTPS protocol, the http request and response are encrypted using SSL/TLS (Secure Sockets Layer / Transport Layer Security) protocols, which ensures that the data remains private and protected from bring eavesdropped/tampered.

### Load Balancing
Large websites like Google receive an enormous number of requests every second. To distribute this load and ensure the server doesn't get overwhelmed, load balancers come into play.
Load balancer such as high availability proxy (HAProxy) distributes incoming requests across the multiple servers to ensures efficient utilization and prevents overload while optimizing resource utilization and providing better response times. Load balancer utilize any of the following balancing algorithms to determine how requests are distributed, such as random, round-robin, weighted round robin, least connection, dynamic round robin, fastest, observed, predictive.
Load balancer aids in building a fault-tolerant web application, improve performance while scaling the web app.

### Firewall
Firewall servers as he first line of defense security against any or all potential threats to your network. Firewall control and monitors incoming and outgoing network traffic based on some already defined rules, enforcing these rules, firewall helps prevent unauthorized access to private network mitigate any potential security risk and safe guard sensitive data.  
How does it work? You might ask. It works by examining network packets and determining whether to allow or block them based on the predefined rule set. These rules could specify criteria such as source and destination IP addresses, port numbers and more. It therefore filter traffic based on these criteria, it ensures that only authorizes and safe connections are permitted while blocking potential malicious traffic.

### Web server
Nginx web server and other web server softwares are responsible for managing incoming connections, handling request/response cycle and ensuring the efficient delivery of web content. Few things you might need to know about web server, they use couple of mechanism to handle requests efficiently such as multi-threading architecture to handle concurrent connections and max server performance. Web server are designed to scale web services enabling them to handle large numbers of simultaneous request.

### Application Server
The web server may need to interact with an application server, especially when dynamic content is involved. The application server processes server-side scripts, database queries, and other application-specific tasks. In the case of Google, the application server may handle search queries, user authentication, and other complex operations.

### Database
Behind every dynamic website like Google, there is a powerful database server that stores and retrieves data. 
caching method is implemented to enhance the performance and reduce response times, the caching method or technique stores frequently accessed or popular data, such as trending keyword, search results, images all in the cache database.
When a client makes a request, the web app check the cache before checking the main database to retrieve data, this allows for faster retrieval and reduces the load on the main database.
Google uses different types of databases, including relational and non-relational DB based on the access patterns requirement.
The application server communicates with the database to fetch the necessary information and return it to the web server for rendering.
The database works in sync with other component of the web such as web server, load balancer, caching systems all to provide a seamless and efficient user experience when accessing google.com.