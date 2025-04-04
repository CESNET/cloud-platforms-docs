#!/bin/bash

# Runs Fuma build container. By default, it builds and deploys the docs in DEV mode. Accepts alternative commands.
#
# Usage:
#     ./run-local-dev.sh [container_command]
# Arguments:
#     [container_command] - Optional, default is "pnpm dev", alternatively: "pnpm build", "bash", ...
# Environment variables:
#     CONTAINER_BIN - Container tool, default "podman".
#     FUMA_IMAGE    - Fuma container image, default "cerit.io/docs/fuma:v15.1.2".


CONTAINER_BIN=${CONTAINER_BIN:-"podman"}
FUMA_IMAGE=${FUMA_IMAGE:-"cerit.io/docs/fuma:v15.1.2"}
CONTAINER_COMMAND=${@:-"pnpm dev"}

FAKE_OPENAI_API_KEY="fake-openai-api-key"

${CONTAINER_BIN} run -it --rm \
  -p 3000:3000 \
  -v ./content/docs:/opt/fumadocs/content/docs \
  -v ./public:/opt/fumadocs/public \
  -e STARTPAGE=/en/docs \
  -e OPENAI_API_KEY=${FAKE_OPENAI_API_KEY} \
  ${FUMA_IMAGE} ${CONTAINER_COMMAND}
