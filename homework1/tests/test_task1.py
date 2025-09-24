# Test for Task 1

import subprocess

def test_hello_output():
    
    result = subprocess.run(['python3', 'task1.py'], 
capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"

