#!/usr/bin/env python3
"""
A simple Hello World program to demonstrate GitHub CLI capabilities.
"""

def main():
    print("Hello, GitHub CLI!")
    print("This repository was created and managed using GitHub CLI.")
    
    # Demonstrate some basic functionality
    features = [
        "Repository creation",
        "Issue management", 
        "Pull request handling",
        "Release management",
        "Workflow automation"
    ]
    
    print("\nGitHub CLI Features Demonstrated:")
    for i, feature in enumerate(features, 1):
        print(f"{i}. {feature}")

if __name__ == "__main__":
    main()

