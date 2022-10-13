# Frontend 
Documentation for Shuffle Frontend.

Note : make sure you know before starting:
Read and understand these well on React's official pages
- Props: How to use them and how to send/receive them
- Fetch: How to get data and make sure things don't crash
- Promises: What they are and when they are useful
- States: How rendering works IN DETAIL with the DOM
- useEffect: How does run by itself, and how does it work with states?

## Installation guide

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed.
2. Download Shuffle
```
git clone https://github.com/frikky/Shuffle
cd Shuffle
```
3. Run docker-compose.
```
docker-compose up -d
```
4. Go to shuffle directory
```
cd frontend
```
5. install all the dependency
```
npm i --legacy-peer-deps
```
6. run the frontend using below command 
```
npm start
```