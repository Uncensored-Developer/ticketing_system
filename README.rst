================
ticketing_system
================


.. image:: https://img.shields.io/pypi/v/ticketing_system.svg
        :target: https://pypi.python.org/pypi/ticketing_system

.. image:: https://img.shields.io/travis/Uncensored-Developer/ticketing_system.svg
        :target: https://travis-ci.org/Uncensored-Developer/ticketing_system

.. image:: https://readthedocs.org/projects/ticketing-system/badge/?version=latest
        :target: https://ticketing-system.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A tool that would allow a customer to directly reach out to a customer support from within any app via a ticketing system.


* Free software: MIT license
* Documentation: https://ticketing-system.readthedocs.io.


Usage
--------

* install the dependencies in the 'requirements_dev.txt' file
* setup up the DATABASE_URL in environment variable
* run the 'initial_db_setup.py' file to setup the database and table and load some test data
* run 'flask run' to start the project (i.e running of localhost:5000 by default)
* This is just a simple project nothing production level or real world here
* There is no standard authentication system for this project

Endpoints
-----------

* GET /users
	To get a list of users to work with. It's just the token that is needed for a simple auth system.
	To be authenticated pass one other the tokens in the header as 'Authorization: Bearer <token>'.
	There are two user_types: customer and staff with different priviledges. E.g a customer can only view and
	reply a ticket created by them only but a staff can view and reply all tickets

* GET /tickets
	To list all the tickets to a customer or all tickets if authemticated as a staff.
	Some parameters can be passed to filter the list like code, closed, department, priority.
	Example: https://localhost:5000/tickets?priority=low

* POST /tickets
	To create(open) a ticket. it takes the paramenters: subject, priority (i.e low, medium and high), department
	(i.e sales, technical and security) and message. When a ticket is created  unique code is assigned to it for
	identification.
	Example: 
	{
		"subject": "CAN'T LOGIN",
		"priority": "high",
		"department": "technical",
		"message": "lorem ipsum..."
	}

* PATCH /tickets/<code>
	To update a ticket with a code=<code>, which in this case the only update that can be done is to close it.
	Example:
	{
		"closed": true,
	}

* GET /replies?ticket=<code>
	To list all the replies/conversations between a customer and a staff for a ticket

* POST /replies
	To create a reply to a ticket.
	Example:
	{
		"ticket": "<code>",
		"message": "lorem ipsum..."
	}


Note
------

* All endpoints require authentication except /users
* This project was designed to be small so it lacks at of features an actual ticketing system has

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
