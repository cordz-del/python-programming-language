# command_runner.py
import subprocess

def run_command(command):
    """
    Runs a shell command and returns its output.
    
    Args:
        command (str): The shell command to execute.
    
    Returns:
        str: The standard output from the command.
    
    Raises:
        Exception: If the command fails.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr}")
    return result.stdout.strip()

if __name__ == "__main__":
    try:
        output = run_command("echo Hello")
        print("Command output:", output)
    except Exception as e:
        print("Error:", e)
