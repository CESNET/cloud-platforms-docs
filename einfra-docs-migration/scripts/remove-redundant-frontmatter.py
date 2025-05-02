#!/usr/bin/python3

import os
import re
from pathlib import Path

def process_md_file(md_path):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping {md_path} - unable to decode as UTF-8")
        return

    # Regular expression to match frontmatters and capture them
    frontmatter_pattern = re.compile(r'(?s)(^---.*?---)', re.MULTILINE)
    
    # Find all frontmatters
    frontmatters = frontmatter_pattern.findall(content)
    
    if not frontmatters:
        print(f"No frontmatter found in {md_path}")
        return

    # Keep only the first frontmatter
    first_frontmatter = frontmatters[0]
    
    # Remove all frontmatters
    new_content = frontmatter_pattern.sub('', content)

    new_content = first_frontmatter + '\n' + new_content.lstrip('\n')

    # Write new content to the original MD file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Converted {md_path}")

def main():
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                md_path = Path(root) / file
                process_md_file(md_path)

if __name__ == '__main__':
    main()
