# Troubleshooting
Documentation for troubleshooting Shuffle known issues.

## How to stop executions in loop
1. Run **docker ps**
```
CONTAINER ID   IMAGE                                     COMMAND                  CREATED       STATUS      PORTS                                                  NAMES
869c99231ed0   opensearchproject/opensearch:latest       "./opensearch-docker…"   5 weeks ago   Up 2 days   9300/tcp, 9600/tcp, 0.0.0.0:9200->9200/tcp, 9650/tcp   shuffle-opensearch
```

2. Run **docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id**
```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 869c99231ed0
or
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' shuffle-opensearch
```
2.1. Output 
```
172.21.0.4
```

3. Run **curl -XDELETE http://<container_ip>:9200/workflowqueue-shuffle**
```
curl -XDELETE http://172.21.0.4:9200/workflowqueue-shuffle
```
3.1. Output
```
{"acknowledged":true}
```

## Opensearch permissons Error
![image](https://user-images.githubusercontent.com/21691729/124939209-d5694580-e000-11eb-8025-e2d475432e1b.png)
![image](https://user-images.githubusercontent.com/21691729/124939333-ec0f9c80-e000-11eb-9e56-5fbd06c7bfe3.png)
Give permissions to shuffle-database folder
````
sudo chown 1000:1000 -R shuffle-database
````

