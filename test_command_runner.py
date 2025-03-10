# test_command_runner.py
from command_runner import run_command

def test_run_command():
    # Test a command that should succeed
    output = run_command("echo Hello")
    assert output == "Hello", f"Expected 'Hello', got {output}"
    # Test a command that is expected to fail
    try:
        run_command("false")
        assert False, "Command should have failed"
    except Exception as e:
        print("Caught expected exception:", e)
    print("test_run_command passed.")

if __name__ == "__main__":
    test_run_command()
