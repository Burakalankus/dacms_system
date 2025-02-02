#!/bin/bash

echo "Starting Docker Compose 1 (WordPress & MySQL)..."
cd ~/dacms_system/compose_1
docker compose up -d

echo "Waiting for WordPress to be ready..."
until curl -s http://localhost:8080 > /dev/null; do
    sleep 5
    echo "Waiting..."
done

echo "WordPress is up. Starting Docker Compose 2 (Databases & Python Scripts)..."
cd ~/dacms_system/compose_2
docker compose up -d --build

echo "All services started successfully!"

