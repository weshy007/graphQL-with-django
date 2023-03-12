serve:
	python3 manage.py runserver
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
develop:
	python manage.py runserver_plus --cert-file cert.crt