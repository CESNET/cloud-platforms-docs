#!/bin/bash

# Checks if multiple "title: ..." sections in frontmatter are identical in all .md files.

for i_file in $(find . -iname '*.md'); do
  titlelines=$(grep '^title: ' "${i_file}")
  newtitle=$(echo "${titlelines}" | head -n 1 | sed 's/^title: "*\([^"]*\)"*/\1/')
  oldtitle=$(echo "${titlelines}" | tail -n 1 | sed 's/^title: "*\([^"]*\)"*/\1/')
  if [[ ${newtitle} != ${oldtitle} ]]; then
    echo "filename: ${i_file}"
    echo "titlelines:"
    echo "${titlelines}"
    echo ""
    echo "newtitle: ${newtitle}"
    echo "oldtitle: ${oldtitle}"
    echo "---"
  fi
done