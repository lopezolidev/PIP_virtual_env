# PIP_virtual_env
A brief educational repository about the use of PIP and handling virtual environments 

# Steps 

## Game project

- A classic game of rock, paper, scissors made in python.
- To run this game in your terminal type the following:
```sh
$ cd game
$ python3 rps.py
```

## Country Pupulation/Data App project
- This simlpe app makes use of matplotlib and other libraries to create a png image about a typed country population.
- Type the following commands:
```sh
$ git clone git@github.com:lopezolidev/PIP_virtual_env.git
$ cd app
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```
- The program will ask you to type a country in english language. Then a bar chart png image of the population of the decades from 1970 to 2020 will appear in the 'imgs' directory.
- Also the program will output the data in a dictonary format of the typed country.

- As an update, this app can now run in a docker environment. Therefore you mustfollow the following steps to compose, build and activate such environment if you would like to run the dockerized app
- Additionally make sure you have the docker engine running in your computer, be it via the Docker Desktop application or by command line in terminal. Also if you're not in the Docker group (as an user with permission to execute docker commands, consider executing the following commands with ```sudo```)
```sh
# first we need to build the container
$ docker compose build

# then we activate it
$ docker compose up -d

# now let's see if our docker is in running status
$ docker compose ps

# this is to enter in our dockerized environment of the app connected via a bash terminal
$ docker compose exec app-csv bash

# if we want to exit the bash terminal of our dockerized app
$ exit

# to turn off our container
$ docker compose down 
``` 
- An important mention is that a rewritten dockerfile document doesn't 'turn off' our docker environment. We need to do it manually after composing it again with the new configuration (rewriting of dockerfile). Hence the importance of turning of the container

## How do we make live changes in our code and reflect that into a docker app?
- As simple as writing the following in our docker-compose.yml file:
```yml
services:
  app-csv:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
    - .:/app
```
- the vital part is in the last 2 lines. 'volumes:' indicates specific files to capture during activation process and pointing '.:/app' reffers to make the live change in any file of our current directory into the directory of the docker working directory
 
## How do we run the same docker virtualization in the web-server app?
- The dockerfile and docker-compose-yml are already in web-server directory.
- The difference in the dockerfile are the following in the last lines:
```dockerfile
FROM python:3.11.2

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```
- In this last line we send as instructions the server, location of the files for execution, and the ports to take place the connection.
- And this is the docker-compose.yml:
```yml
services:
  web-server:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
    - .:/app
    ports:
    - '80:80'
```
- The main difference aside from the name of the service is including the ports, therfore connecting our port '80' to the container port '80'
- then we would only need to run the following commands:
```sh
# create the container
$ docker compose build

# activate the container
$ docker compose up -d

# check status of our container so as our ports
$ docker compose ps

# then connect to localhost to verify connection seeing the displayed page
```


# What is PIP?
- **PIP** stands for _Python Package Manager_. Therefore allows you to install/uninstall, and manage python modules and packages. That means that _acts_ through python. Therefore we'll have to install it through python.
- Also, we can access python directly in the terminal using this command:
```shell
$ python3
>>> # type whatever instruction for a program in python...
```
- To install PIP you must type in your terminal:
```shell
$ sudo apt install python3-pip
```
- To know which version do you have type:
```bash
$ pip -V
```
- To install a package through pip:
```shell
$ pip install <package-name>
```
- Uninstall:
```shell
$ pip uninstall <package-name>
```
- List the packages installed in your system:
```shell
$ pip list
```
- Inform about your python environment and where is being executed:
```shell
$ pip inspect

# you can also redirect the output of that command to a text file with:

$ pip inspect >> <file_name>.txt
```
- For developing with python professionally in our local environment, we need to install the following dependencies:
```shell
$ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

## What does the flag '-y' mean in the linux terminal?
- -y , --yes , --assume-yes. **Automatic yes to prompts**; assume "yes" as answer to all prompts and run non-interactively. If an undesirable situation, such as changing a held package, trying to install a unauthenticated package or removing an essential package occurs then apt-get will abort.
