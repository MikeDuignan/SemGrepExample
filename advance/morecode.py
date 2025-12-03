"""
Bandit Exercise 3: Multiple Advanced Vulnerabilities (Advanced)
This file contains several serious security vulnerabilities for students to find.
"""

import os
import pickle
import subprocess
import tempfile
import yaml

# Command injection vulnerability
def ping_server(hostname):
    # Dangerous: user input directly in shell command
    command = "ping -n 4 " + hostname
    os.system(command)

# Another command injection
def check_file_size(filename):
    result = subprocess.call("dir " + filename, shell=True)
    return result

# Insecure deserialization
def load_user_session(session_data):
    # Pickle is unsafe for untrusted data
    user_session = pickle.loads(session_data)
    return user_session

# Unsafe YAML loading
def load_config(config_file):
    with open(config_file, 'r') as f:
        # yaml.load without Loader is unsafe
        config = yaml.load(f)
    return config

# Insecure temporary file
def create_temp_log():
    # Creates predictable temp file
    temp_file = "/tmp/app_log.txt"
    with open(temp_file, 'w') as f:
        f.write("Log data")
    return temp_file

# Using eval - code injection
def calculate(expression):
    result = eval(expression)
    return result

if __name__ == "__main__":
    ping_server("127.0.0.1")
    result = calculate("2 + 2")