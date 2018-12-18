.PHONY: start check-db drop-db

start:
	celery -A manager worker --loglevel=info -B -s ~/celery/celerybeat-schedule

check-db:
	python3 -c "from manager import db_info; db_info()"

drop-db:
	python3 -c "from manager import db_drop; db_drop()"