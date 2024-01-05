# laolee_covid_api

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## About

This is a robust web application built using Django, designed to provide a comprehensive RESTful API with various
features and functionalities.

## Features

- **RESTful API:** Utilizing Django REST Framework to create a powerful and flexible API.
- **Data Validation:** Implementing data validation to ensure the integrity of information.
- **Querying with Serializations:** Leveraging Django serializers for efficient data querying.
- **Unit Testing:** Thorough unit testing of endpoints to maintain code quality.
- **CSV Data Load and Store Scripts:** Python scripts for loading data from .csv files into the SQLite3 database.

## Getting Started

### Prerequisites

Ensure that you have the following installed:

- Python 3.10+ (recommend 3.12)
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/varlamzhordania/laolee_covid_api.git
   ```

2. Install dependencies:

   ```bash
   cd laolee_covid_api
   pip install -r requirements.txt
   ```

3. Create migrations:

   ```bash
   python manage.py makemigrations
   ```
4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

## CLI Command for Loading CSV Data

To conveniently load data from a `.csv` file into your Django application's SQLite3 database, you can use the provided
CLI command. Follow the steps below:

### Load CSV Command

Use the following command to load data from a `.csv` file:

```bash
python manage.py load_csv path_to_csv
```

Replace path_to_csv with the actual path to your .csv file. This command will parse the file and populate your
application's database with the provided data. Example

As an example, if your .csv file is located in the project root directory and named data.csv, the command would be:

```bash
python manage.py load_csv data.csv
```

Ensure that the .csv file adheres to the expected format for successful data loading.

## Usage

Use the following command to start server

```bash
python manage.py runserver
```

Access the application at [http://localhost:8000/](http://localhost:8000/).

## Accessing Swagger Documentation

Explore the API documentation conveniently through Swagger UI. Follow the steps below to access Swagger:

### Swagger URL

Visit the following URL in your browser to access the Swagger documentation:

[http://localhost:8000/api/schema/docs/](http://localhost:8000/api/schema/docs/)

This will open Swagger UI, providing an interactive interface to explore and test the available API endpoints.

### Note

Make sure that your development server is running (`python manage.py runserver`) before accessing the Swagger
documentation.

## Testing

Use the following command to start tests

```bash
python manage.py test
```

