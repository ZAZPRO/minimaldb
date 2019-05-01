# Minimaldb

Minimaldb is a very simple document oriented database.

## Supported Python Versions
Minimaldb is tested with Python 3.7

## Installation
From PyPi:
```
$ pip install pynamodb
```

## Example Code
```python
from minimaldb import MinimalDB


db = MinimalDB("database_name.db")

# Setting a value
db.set("key_name", value)

# Getting a value
db.get("key_name")

# Deleting a value
db.delete("kay_name")
