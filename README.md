# OrderGen
OrderGen App has two major router endpoints (functionalities), one is order CRUD (**/orders**) and another is data generator API router (**/gen**).

## How To Build And Run

### Build
* cd OrderGen
* pip install -r requirements.txt

### Run

#### First Set Your .env File
* SERVICE_NAME -
* BASE_PATH -
* SERVER_PORT -
* DATABASE_URL - mongodb srv url based on env
* DO NOT CHANGE other properties until unless it needs to be changed

#### Run In Pycharm
* just run: run.py file
* NOTE: before running, add ENVIRONMENT as 'local' in env variables

#### Run with Uvicorn Server
* uvicorn order_gen:app  --host 0.0.0.0  --port 8000  --workers 1  --env-file .env

#### Run with Uvicorn Server (with auto reload)
* uvicorn order_gen:app  --host 0.0.0.0  --port 8000  --workers 1  --env-file .env  --reload

#### Try healthcheck APIs
* /order-gen-app/internal/ping
* /order-gen-app/internal/health

## How To Dockerize and Deploy in AKS

### Dockerize and Push image to AQYSACRQA registry

#### Build image
* docker build --no-cache . -t buy-order-gen-app

#### Run image (just for dev testing)
* docker run -p 8000:8000  --name order-gen-app  --env-file .env  -d buy-order-gen-app

#### Tag and Push image
* docker tag buy-order-gen-app agysacrqa.azurecr.io/buy-order-gen-app
* docker push agysacrqa.azurecr.io/buy-order-gen-app

### Deploy in AKS

#### Set Your k8s.service.configMap.yaml File
* Ensure Your azure-pipelines\k8s.service.configMap.yaml File is updated correctly with env values

#### Deploy
* kubectl apply -f azure-pipelines\k8s.service.configMap.yaml
* kubectl apply -f azure-pipelines\k8s.service.virtualService.yaml
* kubectl apply -f azure-pipelines\k8s.service.yaml

#### Undeploy
* kubectl delete -f azure-pipelines\k8s.service.yaml
* kubectl delete -f azure-pipelines\k8s.service.virtualService.yaml
* kubectl delete -f azure-pipelines\k8s.service.configMap.yaml
