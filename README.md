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

Clone the repository and start a virtualenv

```bash
$ git clone git@github.com:rodolphopivetta/luizalabs.git
$ cd luizalabs
$ virtualenv .venv
```

Install all dependencies
```bash
$ pip install -r requirements.txt
```

Migrate and create a superuser to access admin pages
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

Start the server
```bash
$ python manage.py runserver
```

Create some Employees via admin webpage in http://localhost:8000/admin/employee/employee/add/

Retrieve the employees from curl
```bash
$ curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```
