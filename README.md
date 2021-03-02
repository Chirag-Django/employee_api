# employee_api_testing
Employee API Testing using pytest

## Running the Project Locally

First, clone the repository to your local machine:

```bash
mkdir <company_project>

cd company_project

git clone https://github.com/Chirag-Django/employee_api.git
```

## Running The Project

Create a virtual environment using commands

```
pip install virtualenv
```

```
virtualenv venv
```

That will create a new folder `venv` in your project directory. Next activate it with this command in bash:

```
source venv/bin/active
```

Install the project dependencies with

```bash
pip install -r requirements.txt
```

Setup the local configurations:


Create the database:

```bash
python manage.py migrate
```
Create Dummy Employee data using populate_employee.py. Change value of n as required.

```bash
python populate_employee.py
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

## Testing setup

The projects uses pytest.

To initiate tests follow the steps below:

1.  Run the pytest command

    ```bash
    pytest
    ```

The testing results will be displayed and there will also be a `htmlcov` folder generated inside the project that will contain the code coverage details.

Open up the folder and open the `index.html` in your browser to see this information.

2.  Run below command to get test report in html format

    ```bash
    py.test -v -s test1.py  --html=results.html  
    ```

