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

2) start application - run commands in separate terminals for debug purposes
```
chmod +x starter.sh
chmod +x temperatureapi/manage.py

./starter.sh
./temperatureapi/manage.py migrate
./temperatureapi/manage.py runserver
```


## running tests

```
cd temperatureapi
pytest
```