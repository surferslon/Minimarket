project_name := minimarket

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:  ## Start the app
	docker build -t ${project_name} .
	docker run --rm -d -p 8000:8000 --name ${project_name} ${project_name}

stop:  ## Stop the app
	docker stop ${project_name}

create_superuser:  ## Create admin user
	docker exec -it ${project_name} python manage.py createsuperuser

get_products:  ## Get products
	curl http://localhost:8000/api/products
	@printf "\n"

get_categories:  ## Get categories
	curl http://localhost:8000/api/categories
	@printf "\n"

tests:  ## Run tests
	docker exec ${project_name} python manage.py test
