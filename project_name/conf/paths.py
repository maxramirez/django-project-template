import os
import sys


# =============================================================================
# Calculation of directories relative to the module location
# =============================================================================
# TODO USE pathlib, avoid referencing paths as string

def project_dir_and_name():
    this_path = os.path.realpath(__file__)
    conf_path = os.path.dirname(this_path)
    django_project_path = os.path.dirname(conf_path)
    return os.path.split(django_project_path)


PROJECT_DIR, PROJECT_NAME = project_dir_and_name()

PYTHON_BIN = os.path.dirname(sys.executable)
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # Assume that the presence of 'activate_this.py' in the python bin/
    # directory means that we're running in a virtual environment. Set the
    # variable root to $VIRTUALENV/var.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
    if not os.path.exists(VAR_ROOT):
        os.mkdir(VAR_ROOT)
else:
    # Set the variable root to the local configuration location (which is
    # ignored by the repository).
    VAR_ROOT = os.path.join(PROJECT_DIR, PROJECT_NAME, 'var')


class EnvironmentWrapper():
    """
        A simple wrapper for os.environ, it is no more than syntactic sugar.
    """

    def __init__(self) -> None:
        self._memoized_keys = set()

    def __getattr__(self, item):
        self._memoized_keys.add(item)
        return os.getenv(item, None)

    def __setattr__(self, name: str, value) -> None:
        if type(value) == str:
            os.environ[name] = value
        else:
            super().__setattr__(name, value)


E = EnvironmentWrapper()
