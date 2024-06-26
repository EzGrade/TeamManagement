# Team Management

## Installation

To install the project, you need to have docker and docker-compose installed on your machine. Then, you can run the
following command:

```bash
docker-compose build
docker-compose up
```

Also, you need to create a superuser to access the admin page. You can create a superuser by running the following
command:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Usage

To use the project, you can access the following URLs:

- [http://localhost:8000/](http://localhost:8000/): The main page of the project.
- [http://localhost:8000/admin/](http://localhost:8000/admin/): The admin page of the project.
- [http://localhost:8000/swagger/](http://localhost:8000/swagger/): The Swagger page of the project.
- [http://localhost:8000/redoc/](http://localhost:8000/redoc/): The ReDoc page of the project.

## Details

You can change database credentials in the '.env' file. By default, the project uses the following credentials:

```bash
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

__Warning:__ Don't remove PYTHONUNBUFFERED=1 from the '.env' file. It is necessary for the project to work properly.