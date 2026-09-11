# what is this?

this is an example takehome project I did for myself as a learning exercise

# Project Setup


Setup the database:

Start the database through docker compose:
```
docker compose up -d
```

Add to `.env`:

```
DB_URL=postgresql+psycopg://<user>:<password>@<host>:<port>/<database>
```


Run migrations:

```
uv run alembic upgrade head
```
