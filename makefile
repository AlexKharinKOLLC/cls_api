.PHONY: create clean check-db drop-db

create:
	python3 -c "from manager import add_task; add_task(user = '$(shell whoami)', command = '$(shell pwd)/fetcher.py', timeout = 1)" && \
	python3 -c "from manager import add_task; add_task(user = '$(shell whoami)', command = '$(shell pwd)/processor.py', timeout = 5)"

clean:
	python3 -c "from manager import remove_tasks; remove_tasks(user = '$(shell whoami)')"

check-db:
	python3 -c "from manager import db_info; db_info()"

drop-db:
	python3 -c "from manager import db_drop; db_drop()"