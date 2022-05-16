# Sample Behave tests

## Configuring a Python virtual environment

Let’s start by installing the **python3-venv** package that provides the venv module.

```$ sudo apt install python3-venv```


To create a virtual environment using Python use the following command:

```$ python3 -m venv venv```


Now it’s time to activate the environments created.

```$ source venv/bin/activate```


Installing Packages regarding dependencies.

```$ pip3 install -r requirements.txt```

## Configuring GRPC

Installing GRPC tools.

```pip3 install grpcio grpcio-tools```

Generating GRPC client and server.

```python3 -m grpc_tools.protoc --proto_path=./grpcproto --python_out=./grpcstub --grpc_python_out=./grpcstub ./grpcproto/*.proto```

## Environments
There are 3 environments such as ```DEVELOP```, ```SANDBOX``` and ```LOCAL``` in which has to be exported as an **env** variable. 

__Note: ```develop``` is the default environment.__

- Develop:
```export TARGET_ENV="DEVELOP"```

- Sandbox:
```export TARGET_ENV="SANDBOX"```

- Local:
```export TARGET_ENV="LOCAL"```

## Running

- Using behave to run all test scenarios
> behave

- Using behave to run by tags
> behave --tags=tag-name

- For CI/CD (Develop environment)
> python3 main.py
