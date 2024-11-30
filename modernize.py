#!/usr/bin/env python3
"""
Python 3 Modernization Script for py-faster-rcnn
This script tracks and applies Python 3 compatibility changes.
"""

import os
import sys
import re
from pathlib import Path

PYTHON2_PATTERNS = {
    'print_stmt': r'^\s*print\s+[^(]',  # print statements without parentheses
    'xrange': r'\bxrange\b',
    'basestring': r'\bbasestring\b',
    'unicode': r'\bunicode\b',
    'raw_input': r'\braw_input\b',
    'bare_except': r'except\s*:',  # bare except clauses
}

REPLACEMENTS = {
    'xrange': 'range',
    'basestring': 'str',
    'unicode': 'str',
    'raw_input': 'input',
}

def find_python_files(start_dir):
    """Find all Python files in the directory tree."""
    return list(Path(start_dir).rglob("*.py"))

def check_file(filepath):
    """Check a single file for Python 2 patterns."""
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern_name, pattern in PYTHON2_PATTERNS.items():
                if re.search(pattern, line):
                    issues.append((i, pattern_name, line.strip()))
    return issues

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    python_files = find_python_files(root_dir)
    
    print(f"Found {len(python_files)} Python files to check")
    
    all_issues = {}
    for filepath in python_files:
        issues = check_file(filepath)
        if issues:
            all_issues[filepath] = issues
    
    print("\nPython 2.x patterns found:")
    for filepath, issues in all_issues.items():
        print(f"\n{filepath}:")
        for line_num, pattern_name, line in issues:
            print(f"  Line {line_num}: {pattern_name}")
            print(f"    {line}")

if __name__ == '__main__':
    main()
