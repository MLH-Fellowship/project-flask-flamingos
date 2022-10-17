#!/bin/bash

curl http://localhost:5000/api/timeline_post

curl -X POST http://localhost:5000/api/timeline_post -d 'name=Sebastian&email=holguinsebastian9@gmail.com&content=API Test!'

curl http://localhost:5000/api/timeline_post
