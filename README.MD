## running locally on mac

1) install and start container runtime  
```
brew install docker colima docker-compose
colima start
```  
wait until all packages installed. check install

```
docker ps
```

2) install python environment

```
brew install --cask miniconda
conda init
conda env create -f environment.yml
conda activate TemperatureApi
```

2) start application - run starter and server commands in separate terminals for debug purposes
```
chmod +x starter.sh
chmod +x temperatureapi/manage.py

./starter.sh
./temperatureapi/manage.py migrate
./temperatureapi/manage.py runserver
```
api can be accessed from http://127.0.0.1:8000/graphql


## running tests

```
cd temperatureapi
pytest
```
## deployment

dockerfile is only meant to run the server in a managed container, any migrations should be run before hand using a pipeline. a dockerfile was built and not fully tested due to time constraints. to build dockerfile

```
docker build -t temperatureapi -f temperatureapi/Dockerfile . 

```

## note on removed code
An attempt was made to remove unncessary auth and migration of auth tables, unfortunately, it appears that graphene is dependent on some of the models in the auth addon, and thus they were left in place