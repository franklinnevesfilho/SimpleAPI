import re
import sys

def bump_version(version):
    major, minor, patch = map(int, version.split('.'))
    patch += 1

    if patch >= 10:
        patch = 0
        minor += 1

    if minor >= 10:
        minor = 0
        major += 1

    return f"{major}.{minor}.{patch}"

def update_setup_py():
    with open('setup.py', 'r') as file:
        setup_py = file.read()

    # Find the current version
    version_match = re.search(r"version=['\"](\d+\.\d+\.\d+)['\"]", setup_py)
    if not version_match:
        print("Could not find the version in setup.py")
        sys.exit(1)

    current_version = version_match.group(1)
    new_version = bump_version(current_version)

    # Replace the old version with the new version
    new_setup_py = re.sub(
        r"version=['\"]\d+\.\d+\.\d+['\"]",
        f"version='{new_version}'",
        setup_py
    )

    # Write the updated setup.py back
    with open('setup.py', 'w') as file:
        file.write(new_setup_py)

    print(f"Updated version from {current_version} to {new_version}")

if __name__ == "__main__":
    update_setup_py()
