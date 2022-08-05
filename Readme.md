# Minimarket

## Requirements
- Docker

## Description
Once the project is cloned use the following makefile commands to run and test the app <br>

- `make run` <br>
Start the app container. The app listens on port 8000. The database will be filled with dummy data.
- `make stop` <br>
Stop the app container
- `make create_superuser` <br>
Create super user for the admin page
- `make get_products` <br>
Get list of products <br>
- `make get_categories`<br>
Get list of categories <br>
- `make tests` <br>
Run all available tests. The app container should be running.
- `make help` <br>
List available makefile commands
