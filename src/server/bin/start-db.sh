#!/bin/bash

docker run -d --rm --name skyci-db -v migrations:/migrations -e POSTGRES_PASSWORD=123456 -p 5433:5432 postgres:10
