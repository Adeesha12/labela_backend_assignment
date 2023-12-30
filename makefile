clean:
	py3clean .

build:
	docker build -t auto_company_srv:dev .

run:
	docker run -p 8000:80 auto_company_srv:dev