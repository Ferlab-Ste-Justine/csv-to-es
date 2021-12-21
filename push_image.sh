#!/bin/sh

export VERSION=$(git rev-parse --short "$GITHUB_SHA")
export IMAGE=ferlabcrsj/csv-to-es:$VERSION
export LATEST_IMAGE=ferlabcrsj/csv-to-es:latest
docker build -t $IMAGE .
docker tag $IMAGE $LATEST_IMAGE

docker push $IMAGE
docker push $LATEST_IMAGE