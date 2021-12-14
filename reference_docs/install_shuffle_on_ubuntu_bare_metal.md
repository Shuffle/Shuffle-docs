
# Shuffle Bare Metal Build Log #
1. Install Ubuntu 18.04 server with SSH access
2. sudo apt-get update 
3. sudo apt-get upgrade -y
4. Install Dependencies
5. Install Nodejs
6. Install Golang - Make sure you edit ~/.profile and set GOPATH, GoROOT and Export PATH
7. Install Nginx - Make sure you fix proxy pass and comment out SSL for now
8. cd /opt/
9. cd backend
10. start screen to have process in background
11. export DATASTORE_EMULATOR_HOST=0.0.0.0:8000  
12. go run *.go
13. detach from screen
14. start anther screen
15. cd /opt/Shuffle/functions/onprem/orborus
16. go build
17. export ORG_ID=DefenceLogic
18. export ENVIRONMENT_NAME=DefenceLogic
19. export BASE_URL=http://192.168.1.200:5001
20. go get github.com/docker/docker/api/types
21. go get github.com/docker/docker/api/types/container
22. go get github.com/docker/docker/client
23. go run ./oborborus.go - Oborous breaks as docker not installed - we are beaten :(
24. detach from screen
25. star another screen
26. Run frontend something like
27. cd /opt/Shuffle/frontend
28. npm install
29. npm install-peers
30. npm start
   
## Install Dependencies ##

### General Dependencies ###
```
sudo apt-get install -y python3 git build-essential nginx
sudo systemctl enable nginx  
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates

sudo apt-get install libgdbm-compat-dev libgdbm-dev  gdbmtool gdbm-l10n
sudo apt-get install libreadline7

```
### Node Js ###
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```
### Golang ###
```
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt update
sudo apt install golang-1.15-go
sudo apt-get install golang-go

```


### Nginx ###
```
sudo systemct;l stop nginx

cd ~/Shuffle/frontend/confd/templates
sudo cp nginx.conf /etc/nginx/nginx.conf
Fix proxy pass -  proxy_pass http://192.168.1.194:5001;
Disable ssl directives for certificates at present.
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

