# Itemania

## Setting up and Running the Application

- Add environment variables as seen in .env.example
        - Make sure the secret key matches the one set on the frontend.
- Make sure to launch a PostgreSQL database either locally or using Docker.
- Start a virtual environment

```bash
python -m venv env
source env/bin/activate
```

- Install requirements:

```bash
pip install -r requirements.txt
```

- Start a virtual environment using Poetry which will probably spawn to the activated one:

```bash
poetry shell
```

- Install project requirements

```bash
poetry install
```

- Add static and media directories

```bash
mkdir itemania/static
mkdir -p itemania/media/items
```

- Migrate to database:

```bash
poetry run python manage.py migrate
```

- Generate some fake items (default is 10 items):

```bash
poetry run python manage.py generate_items --number <number>
```

- Run the server:

```bash
poetry run python manage.py runserver
```

## Why PostgreSQL?

The reason behind choosing Postgres besides its performance, reliability and the wide community support is that it is highly compatible with Django. This is relatively a simple project, however, I would also consider Postgres’s support for transactions which ensures data integrity and consistency. Other than that, it is easy to run and interact with Postgres locally especially for development, both using a CLI tool like psql or through a container.

## Why Django?

The immediate reason behind choosing Django is that it is what I am most experienced with. Besides, Django is one of the most prominent backend/fullstack frameworks, it has a thriving community, has batteries included, and excellent documentation. In addition, Django’s ORM is really great when it comes to interacting with data and it allows for great control over it. Now I still think that Next.js could have handled the entirety of this project, but I had to stick to a client-server architecture.

## Design

The layout of the project is inspired by django cookie cutter. When it comes to design, we can see that there are two apps, one that is concerned with configuring the default user model which only supports using a username and a password. The other app “items” is the one responsible for handling items’ related functionality, like defining models/database tables, the API, custom commands, validations and routing. When it comes to the APIs, we can see that there are the serializers which handle serializing, deserializing and validating incoming and outgoing data to ensure consistency and correctness. In the views we can see a viewset, which implements a number of mixins necessary to our application, these mixins include common functionality for operations like CRUD operations and making use of permissions and authentication.
