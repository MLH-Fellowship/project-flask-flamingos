#!/bin/bash

cd ~/project-flask-flamingos

git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compoes -f docker-compose.prod.yml up -d --build

