#!/bin/zsh

# Function to check if a file contains multiple H1 headings
check_multiple_h1() {
    local file=$1
    # Use grep to count lines starting with "# " (H1 in Markdown)
    local count=$(grep -c '^# ' "$file")

    # If count is greater than 1, output the file path
    if (( count > 1 )); then
        echo "$file"
    fi
}

# Find all .md files and check each for multiple H1 headings
find . -type f -name '*.md' -exec zsh -c '
    check_multiple_h1() {
        local file=$1
        # Use grep to count lines starting with "# " (H1 in Markdown)
        local count=$(grep -c "^# " "$file")
        
        # If count is greater than 1, output the file path
        if (( count > 1 )); then
            echo "$file"
        fi
    }
    # Call the function with the passed file name
    check_multiple_h1 "$0"
' {} \;