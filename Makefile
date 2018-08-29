reset:
	rm -rf db.sqlit3
	python manage.py createsuperuser

run:
	python manage.py runserver
