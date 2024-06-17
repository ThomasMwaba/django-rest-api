## REST API

1. **API** means application programming interface

2. **API** allows two piece of software to talk to each other even if they are written in different languages.

3. The **'REST'** part says how the API is communicating over standard web requests.


#### API Application Example

![django-rest-api-example](rest_project/static/images/Django_api.png)


4. **JSON** is the language of communication


5. An **API** says what we want to communicate


#### Examples Of API Use Cases

>> 1. Get a list of products
>> 2. Delete a product
>> 3. Updating a product

These are use cases are called **Api Endpoints**

#### Serializer

A serializer is a part used in Django-Rest-Framework to change a Python object into a **JSON** format


#### HTTP Methods

All API viewpoints are based on certain API methods which are:

>> * **GET**  (Obtain / retrieve data)
>> * **POST**  (Create or send data)
>> * **PUT**  (Update and replace current data)
>> * **DELETE**  (Remove data)


#### CRUD

**CRUD** has a group of functions that need to be done by a database

These functions have got:

>> * **CREATE** &rarr; **POST** request(HTTP method)

>> * **READ** &rarr;   **GET** request(HTTP method)

>> * **UPDATE** &rarr; **PUT** request(HTTP method)

>> * **DELETE** &rarr; **DELETE** request(HTTP method)