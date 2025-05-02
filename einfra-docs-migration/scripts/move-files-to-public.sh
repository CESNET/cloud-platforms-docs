#!/bin/bash

find . -type f -not -name '*.md' -print0 | while IFS= read -r -d '' file; do
    # Strip leading ./ from the file path
    relative_path="${file#./}"
    # Create target directory path
    target_dir="../public/img/openstack/$(dirname "$relative_path")"
    # Create directory structure if it doesn't exist
    mkdir -p "$target_dir"
    # Move the file
    mv "$file" "$target_dir"
done
