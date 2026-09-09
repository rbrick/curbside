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
