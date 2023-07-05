#!/bin/bash

gcloud app deploy app.yaml --version current
# shellcheck disable=SC2046
gcloud storage rm -r $(gcloud storage buckets list --uri | rev | cut -d / -f 1 | rev | sed 's|^|gs://|')
