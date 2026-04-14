# yaraify/__init__.py
import subprocess
import sys
import os

__version__ = "1.0.0"


def _run(script_name):
    """Internal helper to execute the scripts as they are."""
    script_path = os.path.join(os.path.dirname(__file__), f"{script_name}.py")
    # We use subprocess to run the script in a fresh process,
    # ensuring it gets its own sys.argv and environment.
    cmd = [sys.executable, script_path] + sys.argv[1:]
    subprocess.run(cmd)


# Function pointers for the pyproject.toml entry points
def submit():
    _run("yaraify_submit")


def lookup_hash():
    _run("yaraify_lookup_hash")


def lookup_rule():
    _run("yaraify_lookup_yara-rule")


def check_task():
    _run("yaraify_check_taskid")


def list_tasks():
    _run("yaraify_list_tasks")


def rescan():
    _run("yaraify_rescan")


def upload_rule():
    _run("upload_yara_rule")
