# <ins>Prerequisites</ins>

* Python =>3
* Django =>3
* MongoDb Atlas

## Create an account

Create a mongodb atlas account and set up the network and database access

## Setting up Environment Variables

create an .env file in /sweepsouth directory and add the following

```
DB_CONN_STRING= <Your mongo db uri>
```

## Testing The connection

To test the connection you can use the seed.py file provide in the management directory

```
python manage.py seed --seed
```

This will test the database and create a product collection in the database

## Running the API

```
pip install -r requirements.txt
```

Once we have the above steps completed, you can run 

```
python manage.py runserver
```

To spin up the development server then on your browser you can go to http://127.0.0.1:8000/products/ 

## Running Tests

```
pytest
```


# <ins>Architectural Decisions</ins>

## Programming language(Python web framework)

I chose django as a python web framework because of its easy of use and together with
django rest framework you can quickly and easily build a CRUD API without having a lot 
of configurations. Django also provides an ORM that makes it very efficient to communicate
with any database.

## Database Backend

I chose MongoDb atlas because I wanted to have my data on the cloud. With this you can run
your application on localhost or as a docker container and still pull the data from 
the same backend database.

