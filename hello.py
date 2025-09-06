#!/usr/bin/env python3
"""
A simple Hello World program to demonstrate GitHub CLI capabilities.
Enhanced with additional features as requested in issue #1.
"""

import argparse
import datetime
import sys

# ANSI color codes for colored output
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_colored(text, color=Colors.END):
    """Print text with color if supported."""
    if sys.stdout.isatty():
        print(f"{color}{text}{Colors.END}")
    else:
        print(text)

def main():
    parser = argparse.ArgumentParser(description="GitHub CLI capabilities demonstration script")
    parser.add_argument("--no-timestamp", action="store_true", help="Don't include timestamp in output")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    args = parser.parse_args()
    
    # Set color function based on argument
    color_print = print if args.no_color else print_colored
    
    # Print timestamp if requested
    if not args.no_timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color_print(f"[{timestamp}] Starting GitHub CLI demonstration", Colors.BLUE)
    
    color_print("Hello, GitHub CLI!", Colors.GREEN + Colors.BOLD)
    color_print("This repository was created and managed using GitHub CLI.", Colors.GREEN)
    
    # Demonstrate some basic functionality
    features = [
        "Repository creation",
        "Issue management", 
        "Pull request handling",
        "Release management",
        "Workflow automation",
        "Command line argument parsing",
        "Colored output support",
        "Timestamp functionality"
    ]
    
    color_print("\nGitHub CLI Features Demonstrated:", Colors.YELLOW + Colors.BOLD)
    for i, feature in enumerate(features, 1):
        color_print(f"{i}. {feature}", Colors.YELLOW)
    
    color_print("\nEnhanced version addressing issue #1!", Colors.RED + Colors.BOLD)

if __name__ == "__main__":
    main()

