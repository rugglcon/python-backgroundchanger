# Contributing to python-backgroundchanger

## Development Environment

1. To start developing on python-backgroundchanger, clone this repository
    * Go to https://github.com/rugglcon/python-backgroundchanger and click the "fork" button to create your own copy of the project.
    * In a direcotry of your choice, download the "forked" copy to your local computer:
        ```sh
        git clone https://github.com/<your-username>/python-backgroundchanger.git
        ```
    * Navigate to the project folder
        ```sh
        cd python-backgroundchanger
        ```
    * Add the upstream (original) python-backgroundchanger repository.
        ```sh
        git remote add upstream https://github.com/rugglcon/python-backgroundchanger.git
        ```
    * There will now be two remote repositories listed by `git remote -v`
        * `upstream` which refers to the original `python-backgroundchanger` repository
        * `origin` which is your copy of the project

        Periodically, you will have to [sync your copy of the project with the original](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).

2. Next, create a virtual environment.

    Using `venv`:
    ```sh
    # Create a virtual environment with venv
    python -m venv ./venv
    # Activate the virutal environment
    source ./venv/bin/activate
    ```

    Using `pyenv`:
    ```sh
    # Create a virtual environment with pyenv
    pyenv virtualenv 3.8.2 backgroundchanger
    # Activate the virutal environment
    pyenv local backgroundchanger
    ```

3. Next, install the program requirements as well as the development requirements.

    > When developing on MacOS, first test if you have `tkinter` directly installed with your Python version first:
    > ```sh
    > python3
    > >>> import tkinter
    > ```
    > If that doesn't cause an error, you're good. If it does, follow [this](https://stackoverflow.com/a/60469203/9565946) Stack Overflow Post to get that correctly set up. Then you can continue with the rest of the steps.

    ```sh
    # install dev requirements and project requirements
    pip install -r requirements-dev.txt -r requirements.txt
    ```

4. Finally, in the repository root, build the `backgroundchanger` project and install it in editable mode
   ```sh
   python setup.py bdist_wheel
   pip install -e .
   ```

5. Run the project with
    ```sh
    backgroundchanger
    ```

## Tests
Run tests with the following command:
```sh
pytest tests
```
