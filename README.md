# Django Coding Test

The purpose of this coding test is to evaluate your skills using Python and the Django web framework.


### The Problem

Luizalabs' team is growing every month and now we need to have some application to manage employees' information, such as name, e-mail and department. As any application written at Luizalabs, it must have an API to allow integrations.


### Deliverables

"Luizalabs Employee Manager" app must have:

* A Django Admin panel to manage employees' data
* An API to list, add and remove employees


### API example (list)

Request

```bash
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

Response
```json
[
    {
        "name": "Arnaldo Pereira",
        "email": "arnaldo@luizalabs.com",
        "departament": "Architecture"
    },
    {
        "name": "Renato Pedigoni",
        "email": "renato@luizalabs.com",
        "departament": "E-commerce"
    },
    {
        "name": "Thiago Catoto",
        "email": "catoto@luizalabs.com",
        "departament": "Mobile"
    }
]
```

---

# Usage

Clone the repository and create a virtualenv

```bash
$ git clone https://github.com/rodolphopivetta/luizalabs.git
$ cd luizalabs
$ virtualenv .venv
```

Active virtualenv and install all dependencies
```bash
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Migrate and create a superuser to access admin pages
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

Perform tests
```bash
$ python manage.py test
```

Start the server
```bash
$ python manage.py runserver
```

### Create an employee by curl

```bash
$ curl -H "Content-Type: application/json" -X POST -d '{"name":"Arnaldo Pereira", "email":"arnaldo@luizalabs.com", "departament": "Architecture"}' http://localhost:8000/employee/
```


### Update an employee by curl

URL format: http://localhost:8000/employee/id/

```bash
$ curl -H "Content-Type: application/json" -X PUT -d '{"name":"Arnaldo Pereira", "email":"arnaldo@luizalabs.com", "departament": "Mobile"}' http://localhost:8000/employee/1/
```

### Delete an employee by curl

URL format: http://localhost:8000/employee/id/

```bash
$ curl -X DELETE http://localhost:8000/employee/1/
```

### List employees by curl

This endpoint is paginated with 10 elements per page, so `?page=2` can be used.

```bash
$ curl -H "Content-Type: application/json" http://localhost:8000/employee/
$ curl -H "Content-Type: application/json" http://localhost:8000/employee/?page=2
```


### Retrieve an employee by curl

URL format: http://localhost:8000/employee/id/

```bash
$ curl -H "Content-Type: application/json" http://localhost:8000/employee/1/
```

---

Admin page to manage employees: http://localhost:8000/admin/employee/employee/
