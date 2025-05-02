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


## How to contribute

1. Fork this repo.
2. Push your changes into a branch in your fork.
3. Create a PR into the upstream repo's `main` branch.
4. Go through a review of your PR. Pass any checks.
5. Merge the PR.


## How to deploy to production

Deployment happens automatically.

Procedure:
1. Any `push` event in the repository triggers a webhook delivery to the https://docs.platforms.cloud.e-infra.cz/gh/ endpoint.
    - The delivery only passes for a `push` into the `main` branch.
    - The webhook uses a secret, the value of which is stored as `CLOUD_PLATFORMS_DOCS_WEBHOOK_SECRET` variable in https://gitlab.ics.muni.cz/cloud/knowledgebase.
2. This, in turn, triggers a pull, build and deploy in the production deplyment automation (managed by Lukas Hejtmanek).
    1. If the build is successfull, the new revision is deployed to the production site.
    2. If the build fails, nothing is deployed.


## Writing docs in Fumadocs

See Fumadocs official documentation: https://fumadocs.dev/.
