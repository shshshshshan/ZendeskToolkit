import os
import subprocess
import sys
from typing import Final

REQUIREMENTS_FILE_NAME: Final = 'requirements.txt'

def install():
    try:
        # Check if pip is available
        subprocess.check_call(['pip', '--version'])
        package_manager = 'pip'

    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # Check if conda is available
            subprocess.check_call(['conda', '--version'])
            package_manager = 'conda'

        except (subprocess.CalledProcessError, FileNotFoundError):
            print('Error: No supported package manager found (pip, conda, or pipenv)')
            sys.exit(1)

    print(f'Using package manager: {package_manager}')

    try:
        if package_manager == 'pip':
            subprocess.check_call(['pip', 'install', '-r', REQUIREMENTS_FILE_NAME])

        elif package_manager == 'conda':
            subprocess.check_call(['conda', 'install', '--file', REQUIREMENTS_FILE_NAME])

    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        sys.exit(1)

    except Exception as e:
        print(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if not os.path.exists(REQUIREMENTS_FILE_NAME):
        print(f'Error: {REQUIREMENTS_FILE_NAME} not found in root directory. Contact your developer')
        sys.exit(1)

    install()