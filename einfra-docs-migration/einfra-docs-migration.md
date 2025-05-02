# Migration from the old e-INFRA docs

Original docs repo: https://github.com/CESNET/eInfra-docs.

## Steps

1. Create basic directory structure in the new docs location.
    ```
    ./components
    ./content/docs
    ./public
    ```
2. Copy common images and fonts from `CERIT-SC/fumadocs` repo.
    ```bash
    $ cp -r <gh-root-dir>/CSRIT-SC/fumadocs/public/img/ <gh-root-dir>/CESNET/cloud-platforms-docs/public/
    $ cp -r <gh-root-dir>/CSRIT-SC/fumadocs/public/fonts/ <gh-root-dir>/CESNET/cloud-platforms-docs/public/
    ```
3. Copy contents of the original repo into the new docs location.
    ```bash
    $ cp -r <gh-root-dir>/CESNET/eInfra-docs/topics/compute/openstack/docs <gh-root-dir>/CESNET/cloud-platforms-docs/content/docs
    ```
4. Check and fix multiple `h1` headings in `.md` files.
    - Use [./scripts/find-multiple-h1.sh](./scripts/find-multiple-h1.sh) to identify files with multiple `h1` headings.
    - Fix duplicates manually - e.g. by converting `h1` to `h2` headings and coming up with a new common `h1` heading.
5. Move images (or other non-markdown files) to `public/img` directory.
    - Use [./scripts/move-files-to-public.sh](./scripts/move-files-to-public.sh)
    ```bash
    $ cd content/docs
    $ ../../einfra-docs-migration/scripts./move-files-to-public.sh
    ```
6. Fix image paths in `.md` files.
    1. Absolute paths:
        ```diff
        -![](/compute/openstack/images/image_visibility.png)
        +![](/img/openstack/image_visibility.png)
        ```
    2. Relative paths:
        ```diff
        -    ![](../images/windows_console.png)
        +    ![](/img/openstack/windows_console.png)
        ```
    3. Special cases:
        ```diff
        -![The simplified map of Czechia with new cloud sites in Brno and Ostrava](map.png)
        +![The simplified map of Czechia with new cloud sites in Brno and Ostrava](/img/openstack/map.png)
        ```
    - Also make sure to check invalid image paths, remove invalid image references etc.
7. Search and remove (manually) unsupported HTML style blocks.
    ```diff
    -<style>
    -  img[alt=login] { height: 300px; }
    -</style>
    ```
8. Generate frontmatter with `title` in all `.md` files.
    - Use [./scripts/make-frontmatter-title.py](./scripts/make-frontmatter-title.py).
        - This adds new frontmatter at the beginning of all files, even the ones which already have one.
    - Use [./scripts/check-frontmatter-title.sh](./scripts/check-frontmatter-title.sh) to identify files with different old and new frontmatter title.
    - Fix inconsistencies manually - consult the original frontmatters and the original docs.
9. Remove redundant old frontmatters.
    - Use [./scripts/remove-redundant-frontmatter.py](./scripts/remove-redundant-frontmatter.py).
    - In most cases, the old frontmatters do not contain anything useful.
10. Rename `.md` files to `.mdx`.
11. Replace old callout syntax with new one.
    ```diff
    -!!! info
    -
    +<Callout type="info" title="Info">
        To create or upload this image you must have an **image_uploader** rights.
    +</Callout>
    ```
    - Use [./scripts/replace-callouts.py](./scripts/replace-callouts.py).
    - Multiple iterations may be needed.
12. Replace collapsible callouts with headings.
    ```diff
    -??? "What to expect from the cloud and cloud computing"
    -
    +## "What to expect from the cloud and cloud computing"
        [Migration of Legacy Systems to Cloud Computing](https://www.researchgate.net/publication/280154501_Migration_of_Legacy_Systems_to_Cloud_Computing) article gives an overview of what to expect when joining a cloud with a personal legacy application.
    
    -    ##  What are the cloud computing benefits?
    +    ###  What are the cloud computing benefits?
    
         The most visible [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) benefits are:
    ```
13. Replace old tabs syntax with new one.
    ```diff
    +
    +import { Tab, Tabs } from 'fumadocs-ui/components/tabs';
    +
    ...
    -=== "CLI"
    -
    -    To delete the load balancer and all resources, run:
    +<Tabs items={["CLI"]}>
    +    <Tab value="CLI">
    +        To delete the load balancer and all resources, run:
    
    -    ```
    -    openstack loadbalancer delete --cascade --wait my_loadbalancer
    -    ```
    +        ```
    +        openstack loadbalancer delete --cascade --wait my_loadbalancer
    +        ```
    +    </Tab>
    +</Tabs>
    ```
    - This is by far the most tedious part of the migration. There is no reliable automation available at the moment.
    - Use some smart find-and-replace techniques.
14. Fix internal links.
    1. Remove `.md` suffixes.
        ```diff
        - - [Brno G1 site FAQ](../technical-reference/brno-g1-site/faq.md)
        - - [Ostrava G2 site FAQ](../technical-reference/ostrava-g2-site/faq.md)
        - - [Brno G2 site FAQ](../technical-reference/brno-g2-site/faq.md)
        + - [Brno G1 site FAQ](../technical-reference/brno-g1-site/faq)
        + - [Ostrava G2 site FAQ](../technical-reference/ostrava-g2-site/faq)
        + - [Brno G2 site FAQ](../technical-reference/brno-g2-site/faq)
        ```
    2. Index pages are special and must include parent directory in relative links.
        ```diff
        - * [List of flavors](./flavors)
        - * [How to get access](./get-access)
        - * [Info on networking](./networking)
        - * [Support](./get-support)
        - * [Info on quotas](./quota-limits)
        - * [Specific FAQ](./faq)
        - * [GPU computing](gpu-computing)
        + * [List of flavors](./brno-g1-site/flavors)
        + * [How to get access](./brno-g1-site/get-access)
        + * [Info on networking](./brno-g1-site/networking)
        + * [Support](./brno-g1-site/get-support)
        + * [Info on quotas](./brno-g1-site/quota-limits)
        + * [Specific FAQ](./brno-g1-site/faq)
        + * [GPU computing](./brno-g1-site/gpu-computing)
        ```
15. Add `meta.json` descriptors.
    - Use `<gh-root-dir>/CESNET/eInfra-docs/topics/compute/openstack/mkdocs.yml` as the source of truth.
    - Include `index` pages - that makes the directory clickable in the navigation menu.
    ```diff
    diff --git a/content/docs/meta.json b/content/docs/meta.json
    new file mode 100644
    index 0000000..7d1abaf
    --- /dev/null
    +++ b/content/docs/meta.json
    @@ -0,0 +1,11 @@
    +{
    +  "title": "OpenStack",
    +  "pages": [
    +    "index",
    +    "migration-to-g2-openstack-cloud",
    +    "getting-started",
    +    "how-to-guides",
    +    "technical-reference",
    +    "additional-information"
    +  ]
    +}
    ```
16. Fix HTML table syntax.
    1. Add `<thead>` and `<tbody>`.
    2. Replace attribute names:
        1. `colspan` -> `colSpan`
        2. `rowspan` -> `rowSpan`
17. Add footer component.
    - Enables to define a custom footer.
    ```diff
    diff --git a/components/footer.tsx b/components/footer.tsx
    new file mode 100644
    index 0000000..7c0c2f6
    --- /dev/null
    +++ b/components/footer.tsx
    @@ -0,0 +1,6 @@
    +export function Footer() {
    +   return (
    +     <footer className="mt-auto border-t py-12 text-fd-secondary-foreground ">
    +     </footer>
    +   );
    +}
    ```
