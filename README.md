## Dockerized Python + PostgreSQL Project

This project demonstrates how to containerize a Python application and connect it to a PostgreSQL database using Docker.
The Python app creates a table, inserts a row, retrieves the data, and displays it in a clean table format inside the terminal.

## Project Overview

### This project covers:

Creating a Python application

Writing a Dockerfile

Building and running Docker images

Creating a Docker network

Running PostgreSQL in a separate container

Connecting Python to PostgreSQL using psycopg2

Creating a table and inserting data

Printing results using tabulate

Optionally pushing the Docker image to Docker Hub

## Project Structure
my-docker-app/
├── app.py
├── Dockerfile
└── README.md

## Python Application

### The Python app:

Waits for PostgreSQL to start

Connects to the database

Drops the old table

Creates a new table (id, name, age, course)

Inserts 1 row into the table

Fetches and prints the result in table format

## Sample output:

+----+--------+-------+-----------+
| ID | Name   | Age   | Course    |
+----+--------+-------+-----------+
| 1  | Bunny  | 21    | DevOps    |
+----+--------+-------+-----------+

## Dockerfile

The Dockerfile sets up the Python environment, installs dependencies, and runs the application.

### How to Run This Project
### 1. Build the Docker image
docker build -t my-python-app .

### 2. Create a Docker network
docker network create mynetwork

### 3. Run PostgreSQL container
docker run -d \
  --name my-postgres \
  --network mynetwork \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=mydb \
  postgres

### 4. Run the Python app container
docker run --rm --network mynetwork my-python-app

## Pushing Image to Docker Hub (Optional)
docker login
docker tag my-python-app:latest 9148428653/my-python-app:v1
docker push 9148428653/my-python-app:v1

## Technologies Used

Python 3.10

PostgreSQL

Docker

Docker Networks

psycopg2 (PostgreSQL driver)

tabulate (Table formatting)
