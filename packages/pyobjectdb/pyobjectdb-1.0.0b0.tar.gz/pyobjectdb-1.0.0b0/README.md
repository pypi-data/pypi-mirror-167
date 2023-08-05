# PyobjectDB

This is a simple non-relational database for python. It was created for
facilitate portable data storage like SQLite.

> [OBS] This database was made for python, it doesn't provide support
> other languages


Supported data types are all python types plus
``TypeChangeOrientedObject``, which is a type like a ``python dict``, has
keys and values, but your way of accessing the values of each ``TypeChangeOrientedObject``
is for properties, but can be converted to a ``python dict``.

---

## Quick example
````python
from pyobjectdb import create, obj, database

create('database.pyb', {
    'languages': obj(keys={
        'language1': 'Python',
        'language2': 'Javascript'
    }),
    'frameworks': obj(keys={
        'python': ['Kivy', 'Django', 'FastAPI'],
        'javascript': ['ReactNative', 'Express.js']
    })
})

db = database('database.pyb')
db.connect()

print(db.query().languages.convert())
print(db.query().frameworks.python)
````
output:
````
{'language1': 'python', 'language2': 'javascript'}
['Kivy', 'Django', 'FastAPI']

Process finished with exit code 0
````

## How To use
### creating a database

````python
from pyobjectdb import create

create('main.pyb', {'FooBar': ['Foo', 'Bar']})
````

In ```create()``` pass the name of the file where the data will be stored,
then pass a ``python dict`` (will be converted to a ``StandardStorageBase`` class),
as an argument and put all the initial data there. So when ``create``
is called, it will create your database.

### Connecting and making queries

````python
from pyobjectdb import database

db = database('main.pyb')

# connecting
db.connect()

my_list = db.query().FooBar

print(my_list) # output: ['Foo', 'Bar']

print(my_list[0]) # output: Foo

# creating another key in the database
db.submit('langs', ['Python', 'Javascript'])

print(db.query().langs) # output: ['Python', 'Javascript']

db.remove('FooBar') # this key no longer exists
````

To start a database instantiate ``database`` to a variable, and to
connect to the database call ``database.connect()``. queries are
done with ``databese.query()``, which returns a database instance,
then access your keys by attributes.

Like ``database.submit()`` you can add new data to the database
passing a name and a value as an argument. calling ``database.submit()`` will be
saves this change immediately to the file. The query can be made
immediately when adding this new key.

As ``databade.remove()`` will remove the key in question. This change is
immediately saves to the file.

## API Reference
The entire library reference is contained here.

 - [pyobjectdb.core.TypeChangeOrientedObject](#TypeChangeOrientedObject())
 - [pyobjectdb.core.DatabaseCore](#DatabaseCore)
 - [pyobjectdb.core.create](#)

### TypeChangeOrientedObject()
````
pyobjectdb.core.TypeChangeOrientedObject()
````
- your shortcut is: ``obj``

It is a composite data type similar to a ``python dict``, key and value.

parameters:

|   name   | type     | description                   |
|:--------:|----------|-------------------------------|
| ``keys`` | ``dict`` | is a dictionary with any data |

methods:

- ``TypeChangeOrientedObject.add(<key>: str | int, <value>: <any type>)``:

 add a new key.

- ``TypeChangeOrientedObject.remove(<key>: str | int)``:

remove a key

- ``TypeChangeOrientedObject.comvert()``: 

Returns itself as a ``python dict``

---

### DatabaseCore()

````
pyobjectdb.core.DatabaseCore()
````

- your shortcut is ``database``

It is the controller of the database, operations are done on it.

parameters:

|  name  | type    | description                                                      |
|:------:|---------|------------------------------------------------------------------|
| ``fp`` | ``str`` | name of the database file where the operations will be performed |

methods:

- ``DatabaseCore.connect()``:

connects to a database

- ``DatabaseCore.query()``

Returns base storage object for queries, access your keys as class attributes

- ``DatabaseCore.submit(<key>: str, <value>: <any type>)``:

adds a new key to the database base, and after that saves this change

- ``DatabaseCore.remove(<key>: str)``

remove a key in the database base, and after that save this change

- ``DatabaseCore.commit()``

saves all changes to the database

---

### create

````
pyobjectdb.core.create(<file>: str, keys: dict)
````

create a database if it doesn't already exist.
