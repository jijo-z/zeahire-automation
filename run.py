import subprocess


def run_tests():
    """
    Runs pytest and generates Allure results
    """
    subprocess.run([
        "pytest",
        "--alluredir=allure-results"
    ])


if __name__ == "__main__":
    run_tests()