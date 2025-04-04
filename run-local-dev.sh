#!/bin/bash

# Run local development build of the documentation: builds the docs and deploys in DEV mode.
# Usage: ./run-local-dev.sh

CONTAINER_BIN=${CONTAINER_BIN:-"podman"}
FUMA_IMAGE="cerit.io/docs/fuma:v15.1.2"

${CONTAINER_BIN} run -it --rm \
  -p 3000:3000 \
  -v ./content/docs:/opt/fumadocs/content/docs \
  -v ./public:/opt/fumadocs/public \
  -e STARTPAGE=/en/docs \
  ${FUMA_IMAGE} pnpm dev
