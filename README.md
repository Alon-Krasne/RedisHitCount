# RedisHitCount

## Overview
This project is a simple Redis-based counter that tracks the number of times a page is visited.

## Deployment
The project is running on Docker, which means it can be deployed everywhere using
Docker and Docker Compose

## Running
To run the project, run the following commands:
* `docker-compose up --build` - To build and run the project
* `docker-compose down` - To stop the project

*NOTE: The flag `-d` allows you to run the project in the background.*

## Improvements
Improvements that can extend this project to be more production-ready
* Currently the Redis instance is not configured, it should be configured according to the needs of the project.
* Retry mechanism in the case of Redis connection failure. Can be achieved (in Python) 
using the [tenacity](https://pypi.org/project/tenacity/) package.
* The Redis DB should be persisted to disk, we can do this using the `volumes` option in the docker compose.
* This is a small project so there are no tests for the code, but in order to extend it we should introduce some tests.
* I was using `Flask` for this backend, but generally I prefer [FastAPI](https://fastapi.tiangolo.com/) for Backend implementations.
* Make this project configurable, either using a `.env`, environment variables or even a config file that can be injected.