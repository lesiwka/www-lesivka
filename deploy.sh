#!/bin/bash

gcloud config get project | grep 'lesi[vw]ka' | grep -E 'web|www' || { echo ERROR: WRONG PROJECT; exit 1; }

gcloud beta app repair
gcloud app deploy app.yaml --version current
# shellcheck disable=SC2046
gcloud storage rm -r $(gcloud storage buckets list | grep storage_url | cut -d " " -f 2)
