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
