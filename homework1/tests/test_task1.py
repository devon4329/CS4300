# Test for Task 1

import subprocess
import os

def test_hello_world():
    # Adjust the path to point to the location of task1.py
    script_path = os.path.join(os.path.dirname(__file__), '../src/task1.py')
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"

