# Romanian Notice Collection
Get data about Romanian notices.

## Features available
 - Automated API crawl and data exctraction with [Scrapy](https://scrapy.org) request.
 - Process it and check whether it's valid with a [JSON Schema](https://python-jsonschema.readthedocs.io/en/stable/) validation.
 - Create an [SQLite](https://docs.python.org/3/library/sqlite3.html) database to store processed data.
 
## Planned features
 - Visualize database info in [Django with REST](https://www.django-rest-framework.org) API

## How to use it
Right now, the script automatically downloads the required data and creates the database. 
To run it, simply run **main.py**
You can tweak the schema in the respective module, as well as the way the database is created. The bulk of the processing is in the main script,
while if you want to tweak the requests, you'll have to go into *collection/collection/spiders/**collector.py***

Visualization incoming.
