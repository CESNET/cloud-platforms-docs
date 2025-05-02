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

    # Pattern to match the specific block in the .mdx file, accounting for variable indentation
    pattern = re.compile(
        r'^(?P<indent>\s*)!!! danger\n'
        r'(?P<content>[\s\S]*?)'
        r'(?=\n\s*!!! danger|\n\Z)',
        re.MULTILINE
    )

    # def replacement(match):
    #     indent = match.group('indent')
    #     content = match.group('content')
    #     after = match.group('after')
    #     return f"{indent}<Callout type=\"warn\" title=\"Caution\">\n{content}\n{indent}</Callout>\n{after}"

    indentPattern = re.compile(r'^(\s*)')

    def replacement(match):
        indent = match.group('indent')
        content = match.group('content')
        content_lines = content.splitlines()

        # Process each line to ensure it is more indented than the '!!! info' indentation
        end_index = 0
        empty_lines = 0
        for line in content_lines:
            if line:
                lineIndentMatch = indentPattern.search(line)
                if lineIndentMatch and len(lineIndentMatch.group(1)) <= len(indent):
                    break
                empty_lines = 0
            else:
                empty_lines = empty_lines + 1
            end_index = end_index + 1
        end_index = end_index - empty_lines
        content_lines_inside = content_lines[:end_index]
        content_lines_outside = content_lines[end_index:]
        content_inside = '\n'.join(content_lines_inside).strip('\n')
        content_outside = '\n' + '\n'.join(content_lines_outside)

        return f"{indent}<Callout type=\"error\" title=\"Danger\">\n{content_inside}{indent}</Callout>{content_outside}"

    # Perform the replacement
    new_content = pattern.sub(replacement, content)

    # Write new content to the original MD file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Converted {md_path}")

def main():
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.mdx'):
                md_path = Path(root) / file
                process_md_file(md_path)

if __name__ == '__main__':
    main()
