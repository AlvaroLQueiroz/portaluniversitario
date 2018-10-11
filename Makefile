reset:
	rm -rf db.sqlite3
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver
