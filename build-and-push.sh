#!/bin/bash

aws ecr get-login-password --region us-east-1 | podman login --username AWS --password-stdin YYYYYY.dkr.ecr.us-east-1.amazonaws.com --tls-verify=false --log-level=debug

podman buildx build -t currencynotification:latest -f Dockerfile --platform linux/amd64

podman tag localhost/currencynotification:latest YYYYYY.dkr.ecr.us-east-1.amazonaws.com/indrayana/currencynotification:latest

podman push YYYYYY.dkr.ecr.us-east-1.amazonaws.com/indrayana/currencynotification:latest
