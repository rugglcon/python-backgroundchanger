from shutil import rmtree
import subprocess
from os import path
from sys import exit
from sh import git

def make_dist():
    subprocess.call(['python3', 'setup.py', 'sdist', 'bdist_wheel', 'bdist_egg'])

def twine_upload():
    subprocess.call(['twine', 'upload', 'dist/*'])

def clean():
    if path.exists('dist'):
        rmtree('dist')

status = git.status()
branch = git.branch()

if 'master' not in branch:
    print('Must be on branch "master". Exiting.')
    exit(1)

if 'Changes not staged for commit' in status or 'Untracked files' in status or 'Changes to be committed' in status:
    # get user input for if they want to commit all current changes
    # and continue with the deploy script
    # exit if no
    commit = input('Changes were detected, would you like to commit all current changes? (y/n) ')
    if commit != 'y' and commit != 'n':
        print('Expected "y" or "n", instead found {}. Exiting.'.format(commit))
        exit(1)
    elif commit == 'n':
        print('Not committing changes; please commit all changes and try again. Exiting.')
        print(status)
        exit(2)
    commit_msg = input('Committing, please provide a commit message: ')
    git.add('.')
    git.commit('-am', commit_msg)
    push_result = git.push()
    print(push_result)

if 'Your branch is ahead of' in status:
    print('Found unpushed commits. Pushing...')
    push_result = git.push()
    print(push_result)
clean()
make_dist()

upld = input('About to upload to PyPi, are you sure you want to do this? (y/n) ')
if upld != 'y' and upld != 'n':
    print('Expected "y" or "n", instead found {}. Exiting.'.format(upld))
    exit(1)
if upld == 'n':
    print('Not uploading. Exiting.')
    exit(1)

print('Uploading...')
twine_upload()