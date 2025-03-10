# run_pytest_report.py
import subprocess

def generate_pytest_report():
    # Run pytest with JUnit XML output format for report generation.
    result = subprocess.run(
        ["pytest", "--maxfail=1", "--disable-warnings", "-q", "--junitxml=report.xml"],
        capture_output=True, text=True
    )
    print("Pytest report generated as report.xml")
    print(result.stdout)

if __name__ == "__main__":
    generate_pytest_report()
