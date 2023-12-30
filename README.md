# Assignment



The assignment
---------
A company specialised in car parts wants to modernise their company, and start selling their parts online. Being the pro car salesmen that they are, they decided to develop the front-end via another agency. They entrust the back-end to none other than Label A.

After some initial research, we've defined the following user stories on top of our backlog:

* get access token 
~~~bash 
curl -X 'POST' \
  'http://127.0.0.1:8000/api/token/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "string",
  "password": "string"
}'
~~~
* As a company, I want all my products in a database, so I can offer them via our new platform to customers
~~~bash 
curl -X 'GET' \
  'http://127.0.0.1:8000/products/products/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b'
~~~
* As a client, I want to add a product to my shopping cart, so I can order it at a later stage
~~~bash 
curl -X 'POST' \
  'http://127.0.0.1:8000/carts/shopping-carts/1/add-item/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b' \
  -H 'Content-Type: application/json' \
  -d '{
  "product": {
    "name": "string",
    "description": "string",
    "price": "string"
  },
  "quantity": 0,
  "created_at": "2023-12-30T07:44:35.939Z",
  "user": 1,
  "cart": 1
}'
~~~
* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
~~~bash 
curl -X 'DELETE' \
  'http://127.0.0.1:8000/products/products/1/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b'
~~~
* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
~~~bash 
curl -X 'GET' \
  'http://127.0.0.1:8000/products/products/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b'
~~~
* As a client, I want to select a delivery date and time, so I will be there to receive the order
~~~bash 
curl -X 'POST' \
  'http://127.0.0.1:8000/orders/deliveries/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b' \
  -H 'Content-Type: application/json' \
  -d '{
  "delivery_date_time": "2023-12-30T07:47:21.832Z",
  "order": 0
}'
~~~
* As a client, I want to see an overview of all the products, so I can choose which product I want
~~~bash 
curl -X 'GET' \
  'http://127.0.0.1:8000/orders/orders/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b'
~~~
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs
~~~bash 
curl -X 'GET' \
  'http://127.0.0.1:8000/products/products/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 081dd47a89caeb09709bb66103594ce5e62f227b'
~~~


**Want to run the project in Docker?**

- ```docker build -t autocompany .```
- ``` docker run -p 80:80 -d autocompany```
- Navigate to ```http://127.0.0.1/```

