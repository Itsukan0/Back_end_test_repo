# Back_end_test_repo
Learning Repo for my backend interview project

## Setup
This repo will run on Python, so setup a virtual environnement and copy the requirements !
- `python.exe -m venv .ven`
- `python.exe -m pip install --upgrade pip`
- `pip install -r requirements.txt`

We will just describe how to run the serv !

I'm using the PostgreSQL db, set with the following instructions :

- Install the PostgreSQL toolset : https://www.postgresql.org/download/
- Setup your master credentials

On Windows 11:
- Add `C:\Program Files\PostgreSQL\<Your Version>\bin` to your PATH to use psql from the Terminal
- Add the PGSERVICEFILE to your environnement variables, this will allow your Django server to acces your DB service 


`$env:PGSERVICEFILE = "C:\Users\<Your User>\AppData\Roaming\postgresql\pg_service.conf"`,


- Add the PGPASSFILE to your environnement variables, this will allow your Django server to log into your service


`$env:PGPASSFILE = "C:\Users\<Your User>\AppData\Roaming\postgresql\pgpass.conf"`,


- [Optionnal] Make them permanent for consistent use :


`[System.Environment]::SetEnvironmentVariable("PGSERVICEFILE", "C:\Users\<Your User>\AppData\Roaming\postgresql\pg_service.conf", [System.EnvironmentVariableTarget]::User)`


`[System.Environment]::SetEnvironmentVariable("PGPASSFILE", "C:\Users\<Your User>\AppData\Roaming\postgresql\pg_service.conf", [System.EnvironmentVariableTarget]::User)`


- Run `psql -U postgres` in your terminal (preferably Powershell)
- Inside the psql env : 
    - `CREATE DATABASE library_db;`
    - `CREATE USER library_user WITH PASSWORD 'your_password';`
    - `GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;`
    - `GRANT ALL ON SCHEMA public TO library_user;`
    - `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO library_user;`
    - Quit the psql env `\q`

- Then, inside a terminal, root of the directory: `python manage.py migrate`

## Running the server

- For basic use, do in this order :
    - run a terminal with the venv enabled
    - Start the Django server with : `python manage.py runserver` (exemples often run on 8000)
    - run another terminal with the venv enabled
    - Start the FastAPI service with : `uvicorn fastapi_app:app --reload --port <your_port>` (for exemple : 8001)

With a browser of Postman, you can now:
    - Do basic CRUD operations with the `/api/` endpoint
    - If you set a django superuser, administer from `<local_host>:<django_port>/admin/`
    - If the swagger doc with `<local_host>:<fast_api_port>/docs/`




