#!/usr/bin/env python3
"""
Pre-commit hook to validate that all file paths referenced in README.md tables exist.
"""

import re
import sys
from pathlib import Path
from typing import List


def extract_file_paths(readme_content: str) -> List[str]:
    """
    Extract file paths from markdown table rows in the README.md content.
    Matches patterns like [Python](/l33tcode/example.py) and extracts the path.

    Args:
        readme_content: The content of the README.md file

    Returns:
        A list of file paths extracted from the README.md
    """
    # Match file paths in format [Language](/path/to/file.ext)
    pattern: str = r'\[(?:\w+)\]\((/[^)]+)\)'
    matches: List[str] = re.findall(pattern, readme_content)
    
    # Remove the leading slash from each path as mentioned in requirements
    file_paths: List[str] = [path[1:] if path.startswith('/') else path for path in matches]
    return file_paths


def validate_file_paths(file_paths: List[str], repo_root: Path) -> List[str]:
    """
    Validate that all extracted file paths exist in the repository.

    Args:
        file_paths: List of file paths to validate
        repo_root: Path to the repository root directory

    Returns:
        A list of missing files
    """
    missing_files: List[str] = []
    
    for file_path in file_paths:
        full_path: Path = repo_root / file_path
        if not full_path.exists():
            missing_files.append(file_path)
    
    return missing_files


def main() -> int:
    """
    Main function to validate README.md file references.

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    # Get the repository root directory (assuming the hook is in .git/hooks)
    repo_root: Path = Path(__file__).resolve().parents[2]
    
    # Path to README.md
    readme_path: Path = repo_root / "README.md"
    
    # Check if README.md exists
    if not readme_path.exists():
        print("README.md not found in repository root")
        return 1
    
    # Read README.md content
    readme_content: str
    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            readme_content = file.read()
    except Exception as e:
        print(f"Error reading README.md: {e}")
        return 1
    
    # Extract file paths from README.md
    file_paths: List[str] = extract_file_paths(readme_content)
    
    if not file_paths:
        print("No file paths found in README.md tables")
        return 0
    
    # Validate file paths
    missing_files: List[str] = validate_file_paths(file_paths, repo_root)
    
    if missing_files:
        print("The following files referenced in README.md do not exist:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        return 1
    
    print("All files referenced in README.md exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
