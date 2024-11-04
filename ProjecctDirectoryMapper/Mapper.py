import os

def map_java_files(directory):
    project_structure = {}

    # Traverse the directory structure
    for root, _, files in os.walk(directory):
        # Only consider files that end with .java
        java_files = [f for f in files if f.endswith('.java')]

        # Skip if there are no Java files in this directory
        if not java_files:
            continue

        # Determine package name by converting directory structure to dot notation
        package_path = os.path.relpath(root, directory)
        package_name = package_path.replace(os.path.sep, '.')

        # Add package to dictionary if it doesn't exist
        if package_name not in project_structure:
            project_structure[package_name] = []

        # Append each Java file (without extension) to the package entry
        for java_file in java_files:
            class_name = os.path.splitext(java_file)[0]
            project_structure[package_name].append(class_name)

    return project_structure

def display_structure(structure):
    for package, classes in structure.items():
        print(f"Package: {package}")
        for class_name in classes:
            print(f"  - {class_name}")
        print()

# Specify the path to your project directory
project_directory = r'path/of/the/project'
structure = map_java_files(project_directory)
display_structure(structure)
