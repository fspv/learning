#!/bin/bash
# Script to install the README.md file validation pre-commit hook

# Set the source and destination paths
HOOK_SOURCE="$(pwd)/bin/readme-check-hook.py"
HOOK_DEST="$(git rev-parse --git-dir)/hooks/pre-commit"

# Make sure the source file exists
if [ ! -f "$HOOK_SOURCE" ]; then
  echo "Error: Hook source file not found at $HOOK_SOURCE"
  exit 1
fi

# Copy the hook to the git hooks directory
cp "$HOOK_SOURCE" "$HOOK_DEST"

# Make the hook executable
chmod +x "$HOOK_DEST"

echo "Pre-commit hook installed successfully!"
echo "The hook will run automatically on each commit to validate README.md file references."
