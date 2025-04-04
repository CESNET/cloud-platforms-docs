# Contributing guide

## How to compile on a local station

1. Clone the this repo:

    ```
    $ git clone https://github.com/CESNET/cloud-platforms-docs.git
    ```

2. Run the provided [run-local-dev.sh](./run-local-dev.sh) script:

    ```bash
    $ cd ./cloud-platforms-docs
    $ ./run-local-dev.sh

    > e-infra-docs@0.0.0 dev /opt/fumadocs
    > next dev

    [MDX] update map file: 9.22ms
    [MDX] started dev server
      ▲ Next.js 15.2.3
      - Local:        http://localhost:3000
      - Network:      http://147.251.17.208:3000

    ✓ Starting...
    ⚠ `devIndicators.appIsrStatus` is deprecated and no longer configurable. Please remove it from next.config.mjs.
    ⚠ `devIndicators.buildActivity` is deprecated and no longer configurable. Please remove it from next.config.mjs.
    Attention: Next.js now collects completely anonymous telemetry regarding usage.
    This information is used to shape Next.js' roadmap and prioritize features.
    You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
    https://nextjs.org/telemetry

    ✓ Ready in 1303ms
    ```

    Requires a container management CLI tool, uses `podman` by default.
    - Override by setting `CONTAINER_BIN` environment variable.

    Uses `cerit.io/docs/fuma:v15.1.2` image by default.
    - Override by setting `FUMA_IMAGE` environment variable.
    - See https://cerit.io/harbor/projects/243/repositories/fuma/ for available image versions (e-INFRA login).

    By default, the container runs the `pnpm dev` command, which deploys the docs in DEV mode (dynamic reload, dev console in browser).
    Alternatively, you can pass another command to the container:
    - `pnpm build` - Perform a production build of the docs. Usefull for showing all errors.
    - `bash` - Enter the container's shell and do what you need.

    ```bash
    $ ./run-local-dev.sh bash
    ```

3. In a web browser, see the docs at `http://localhost:3000/en/docs/`.

    Fumadocs is able to dynamically re-compile modified content while running in DEV mode. However, some syntax errors can crash it.

**Notes**

- 4 GB RAM or more is recommended to run the local build.


## Writing docs in Fumadocs

TODO
