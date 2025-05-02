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

    # Remove existing hide-toc frontmatter
    hide_toc_pattern = re.compile(
        r'^---\s*\n\s*hide:\s*\n\s*-\s+toc\s*\n---\s*\n*',
        flags=re.MULTILINE
    )
    content = hide_toc_pattern.sub('', content, count=1)

    # Remove leading empty lines
    content = re.sub(r'^\n+', '', content)

    # Process H1 heading
    h1_pattern = re.compile(r'^\s*#\s+(.*)$', re.MULTILINE)
    match = h1_pattern.search(content)

    if match:
        title = match.group(1).strip()
        frontmatter = f'---\ntitle: "{title}"\n---\n'
        
        # Construct new content with frontmatter at beginning
        before_h1 = content[:match.start()].lstrip('\n')
        after_h1 = content[match.end():].lstrip('\n')
        new_content = frontmatter + before_h1 + after_h1
    else:
        print(f"No H1 heading found in {md_path}, creating basic frontmatter")
        frontmatter = '---\ntitle: ""\n---\n\n'
        new_content = frontmatter + content.lstrip('\n')

    # Ensure no empty lines after frontmatter
    lines = new_content.split('\n')
    if len(lines) >= 3 and lines[0] == '---' and lines[2] == '---':
        remaining = lines[3:]
        while remaining and not remaining[0].strip():
            remaining.pop(0)
        new_content = '\n'.join(lines[:3] + remaining)

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
