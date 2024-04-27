	FROM python:3.12
	WORKDIR /app
	
	COPY . /app/
	RUN pip install poetry
	RUN poetry install
	
	CMD [ "poetry","run","unicorn","hello_world.main:app.py" ]
