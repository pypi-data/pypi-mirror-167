'''
This is the entry point for Artemis
'''

# pylint: disable=line-too-long
# pylint: disable=too-many-branches
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

import os
import sys
import json
from glob import glob

from .artemis_loader import ArtemisLoader
from .artemis_licensing import ArtemisLicensing

def main() -> None:
    '''
    Entry point when called from command line
    :return: None
    '''

    # Validate we're on nt
    if os.name != 'nt':
        print("Artemis Labs only supports Windows at this time")
        sys.exit(1)

    # Check if user is querying license status
    if len(sys.argv) == 2 and sys.argv[1] == 'license_status':
        license_key = ArtemisLicensing.get_cached_license()
        if license_key is None:
            print("No license found")
        else:
            print("License found")
        sys.exit(1)

    # Check if user is activating license
    if len(sys.argv) == 3 and sys.argv[1] == 'activate_license':
        license_key = sys.argv[2]
        print('Checking license key: ', license_key)
        if not ArtemisLicensing.verify_license(license_key):
            print("Invalid license")
            sys.exit(1)
        ArtemisLicensing.set_cached_license(license_key)
        print("License activated")
        sys.exit(1)

    # Ensure user has activated license
    if ArtemisLicensing.get_cached_license() is None:
        print("Please activate your license")
        sys.exit(1)

    # Ensure license is valid
    if not ArtemisLicensing.verify_license(ArtemisLicensing.get_cached_license()):
        print("Invalid license")
        sys.exit(1)

    # Validate input
    if len(sys.argv) < 2:
        print('Artemis Labs')
        print("Usage:")
        print("Launch project: artemis_labs <artemis_project_dir>")
        print("Create project: artemis_labs init")
        print("Create config file: artemis_labs config")
        print("Clean project: artemis_labs clean")
        sys.exit(1)

    # Call command
    runner_path = sys.argv[0].replace('\\', '\\\\')

    # Project path
    project_path = sys.argv[1].strip()
    project_path = project_path.replace('\\', '\\\\')

    # Dev
    dev = False

    # Check cli arg
    launch_command = ''
    if len(sys.argv) == 2:
        launch_command = sys.argv[1].strip()

    # Check launch arg
    launch = True
    if len(sys.argv) > 4:
        if sys.argv[4].strip() == "nolaunch":
            launch = False

    # Launch
    main_direct(runner_path, project_path, launch_command, launch=launch, dev=dev)

def main_direct(runner_path, project_path, launch_command, dev=True, launch=True):
    '''
    Entry point when called from test_runner.py
    :param runner_path: Path to artemis_labs_base
    :param project_path: Path to Artemis project file
    :param launch_command: Command to launch script. Example: python
    :param dev: Whether in dev mode or not
    :param launch: Whether or not to spawn browser
    :return:
    '''

    # Validate we're on nt
    if os.name != 'nt':
        print("Artemis Labs only supports Windows at this time")
        sys.exit(1)

    # Check if user is opening config file
    if launch_command == 'config':

        # Load config template
        file_dir = os.path.dirname(os.path.realpath(__file__))
        config_template_path = os.path.join(file_dir, 'artemis_config_template.py')
        with open(config_template_path, encoding='utf-8') as file:
            config_template = file.read()

        # Write config template
        out_dir = os.getcwd()
        config_template_path_out = os.path.join(out_dir, 'config_template.py')

        # Ensure file doesn't already exist
        if os.path.exists(config_template_path_out):
            print('[Artemis] Error: config_template.py already exists in current directory')
            sys.exit(1)

        # Generate template
        with open(config_template_path_out, 'w', encoding='utf-8') as file:
            print('[Artemis] Generate config template: config_template.py')
            file.write(config_template)
            sys.exit(0)

    # Check if user is creating Artemis project
    if launch_command == 'init':

        # Get project directory
        cur_dir = os.getcwd()
        project_dir = os.path.join(cur_dir, 'artemis_project')

        # Create project directory or empty it if it already exists
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)
        else:
            for file in os.listdir(project_dir):
                file_path = os.path.join(project_dir, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

        # Create project file
        project_template_path = os.path.join(project_dir, 'project.json')
        with open(project_template_path, 'w', encoding='utf-8') as file:
            default_template = {
                "name": "Artemis Project",
                "root_dir" : cur_dir,
                'entry_point': 'main.py',
                "files": []
            }
            file.write(json.dumps(default_template, indent=4))
            print('[Artemis] Generate project file: project.art')
            file.write('')
        sys.exit(0)

    # Clean project
    if launch_command == 'clean':

        # Ensure Artemis project file exists
        project_file_path = os.path.join(project_path, 'project.json')
        if not os.path.exists(project_file_path):
            print('[Artemis] Error: project file not found')
            sys.exit(1)

        # Load Artemis project file
        with open(project_file_path, encoding='utf-8') as file:
            project_file = json.load(file)

        # Get project directory
        cur_dir = os.getcwd()
        project_dir = os.path.join(cur_dir, 'artemis_project')

        # Clean project files
        project_root_dir = project_file['root_dir']
        for project_file in project_file['files']:

            # Load base file path
            file_path = os.path.join(project_root_dir, project_file)

            # Select all files
            matching_files = glob(file_path)

            # Prcocess each file
            for matching_file in matching_files:

                # Get artemis temp file name
                artemis_temp_file = matching_file[:-3] + '_artemis.py'

                # Delete artemis temp file
                if os.path.exists(artemis_temp_file):
                    os.unlink(artemis_temp_file)

        sys.exit(0)

    # Verify script path exists and is an artemis file
    if not os.path.exists(project_path):
        print(f'[Artemis] Error: path {project_path} not found')
        sys.exit(1)
    if not os.path.isdir(project_path):
        print(f'[Artemis] Error: path {project_path} is not a directory')
        sys.exit(1)

    # Ensure user has activated license
    if ArtemisLicensing.get_cached_license() is None:
        print("[Error] Please activate your license before continuing")
        sys.exit(1)

    # Ensure license is valid
    if not ArtemisLicensing.verify_license(ArtemisLicensing.get_cached_license()):
        print("[Error] Invalid license")
        sys.exit(1)

    # Ensure Artemis project file exists
    project_file_path = os.path.join(project_path, 'project.json')
    if not os.path.exists(project_file_path):
        print('[Artemis] Error: project file not found')
        sys.exit(1)

    # Load Artemis project file
    with open(project_file_path, encoding='utf-8') as file:
        project_settings = json.load(file)

    # Ensure project file is valid
    if 'root_dir' not in project_settings or 'files' not in project_settings or 'entry_point' not in project_settings:
        print('[Artemis] Error: project file is invalid')
        sys.exit(1)

    # Clear old config files
    ArtemisLoader.clear_config_files()

    # Process project files
    project_root_dir = project_settings['root_dir']
    project_entry_point = project_settings['entry_point']
    project_files = []
    for project_file in project_settings['files']:

        # Load base file path
        file_path = os.path.join(project_root_dir, project_file)

        # Select all files
        matching_files = glob(file_path)

        # Prcocess each file
        for matching_file in matching_files:

            # Store project file
            project_files.append(matching_file)

    # Process project files
    for project_file in project_files:

        # Check if file is entry point
        is_entry_point = project_file == os.path.join(project_root_dir, project_entry_point)

        # Report
        print(f'[Artemis] Processing file: {project_file}')

        # Setup config files
        import_content = ArtemisLoader.load_imports(project_file)
        ArtemisLoader.setup_config_files(import_content)

        # Process script
        ArtemisLoader.process_script(runner_path, launch_command, project_file, project_files, is_entry_point=is_entry_point, project_name=project_settings['name'], project_path=project_path, dev=dev, launch=launch)

    # Get entry point file name
    entry_point_file_name = os.path.basename(project_entry_point)
    entry_point_path = os.path.join(project_root_dir, project_entry_point)
    if os.path.isfile(os.path.join(project_root_dir, entry_point_file_name[:-3] + "_artemis.py")):
        entry_point_path = os.path.join(project_root_dir, entry_point_file_name[:-3] + "_artemis.py")

    # Escape entry point
    entry_point_path = entry_point_path.replace("\\", "/")

    # Run processed script
    print("[Artemis] Running script: " + entry_point_path)

    # Escape entry point
    os.system(f'python "{entry_point_path}"')

def check_cached_license():
    '''
    Quick test which retrieves the cached license
    '''
    license_key = ArtemisLicensing.get_cached_license()
    if license_key is None:
        print("No license found")
    else:
        print("License found")
    sys.exit(1)

def activate_license(license_key):
    '''
    Quick test which tries to activate the provided license key
    '''
    if not ArtemisLicensing.verify_license(license_key.strip()):
        print("Invalid license")
        sys.exit(1)
    ArtemisLicensing.set_cached_license(license_key)
    print("License activated")
    sys.exit(1)

def check_license():
    '''
    Quick test which checks if th computer has an authorized license
    '''
    # Ensure user has activated license
    if ArtemisLicensing.get_cached_license() is None:
        print("Please activate your license")
        sys.exit(1)

    # Ensure license is valid
    if not ArtemisLicensing.verify_license(ArtemisLicensing.get_cached_license()):
        print("Invalid license")
        sys.exit(1)

    # License is valid
    print("License is valid")

if __name__ == '__main__':
    main()
