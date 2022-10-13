#!/bin/bash

curl --request POST http://localhost:5000/api/timeline_post -d 'name=Paulin&email=paulin@paulin.com&content=Enjoying my day in beautiful Tijuana!'

curl http://localhost:5000/api/timeline_post