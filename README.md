## GraphQL with Django
### What is GraphQL?
- GraphQL is a query language designed to build client applications by providing an alternative to RESTful API. 
With GraphQL, clients can request only the data they need, eliminating the over-fetching problem that occurs with 
traditional RESTful APIs. GraphQL also enables multiple resources to be retrieved using a single request, 
which makes it more efficient than RESTFul APIs.


#### When to use GraphQL over REST?
1. **Multiple requests are required:** RESTFul services make use of many endpoints, so it is not ideal for cases where 
you need to send multiple requests to retrieve related data. In contrast, GraphQL allows you to define your custom queries 
to collect related data in a single HTTP request, being powerful for applications that require fetching a lot of data.

2. **Limited Network Bandwidth:** If the client is on a limited bandwidth network like mobile, using GraphQL, reducing 
transit times and only retrieving necessary data, will enhance performance due to fewer API requests.

3. **Complex Queries:** Working with complex queries is where GraphQL really shines. By its nature, GraphQL is built to handle 
complex queries, making it a powerful tool that knows to limit the depth of concurrency to avoid over-exhaustion of the resources.

4. **Front-end-friendly:** GraphQL makes it easy for front-end developers because you can easily ask for the exact properties 
that you want in your app, without overloading your database since you are getting specific items out whenever you need them. 