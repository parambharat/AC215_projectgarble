# Garble: Audio Summarizer- Setup & Code Organization

## Introduction
This app aims to summarize speech audio and creates a summary of the audio.

The code is organized into a few sections:

- [garble-app](https://github.com/parambharat/AC215_projectgarble/tree/main/garble-app):  contains all deployement code and docker containers etc.
- [notebooks](https://github.com/parambharat/AC215_projectgarble/tree/main/notebooks): contains all notebooks used for EDA and model training.
- [submissions](https://github.com/parambharat/AC215_projectgarble/tree/main/submissions): contains submissions for each milestone
- [src](https://github.com/parambharat/AC215_projectgarble/tree/main/src): contains all code and utilities used in the project.

## Deployment

For deployment of this app, we set up 3 containers:

* api-service
* frontend-react
* nginx

The following container architecture is implemented:

![Garble App setup](./images/app_diagram.png)

**See `garble-app/depoyment` directory for all deployment scripts**

## Deployment

### Build and Push Docker Containers to GCR (Google Container Registry)
```
ansible-playbook deploy-docker-images.yml -i inventory.yml
```

## Deploy Garble: Audio Summarizer App to K8s Cluster


We use ansible to create and deploy the app into a Kubernetes Cluster


### Create & Deploy Cluster
```
ansible-playbook deploy-k8s-cluster.yml -i inventory.yml --extra-vars cluster_state=present
```
![Kubernetes setup 1](./images/kubernetesdep-1.png)

### Creation of cluster

![Kubernetes setup 2](./images/kubecluster.png)

### Creation of Nodes

![Kubernetes setup 3](./images/kubenodes.png)

### Node details

![Kubernetes setup](./images/kubenodedetails.png)

### Pod status

![Kubernetes setup](./images/kubstatus.png)

## Services

![Kubernetes setup](./images/kubeservices.png)






### View the App
* Copy the `nginx_ingress_ip` from the terminal from the create cluster command
* Go to `http://<YOUR INGRESS IP>.sslip.io`


### Garble Application 

![Kubernetes setup](./images/kubeappln.png)

### Garble Application Resuslts


![Kubernetes setup](./images/kubeapplnresults.png)
