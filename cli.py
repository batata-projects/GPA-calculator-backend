import argparse
import os
import subprocess

FILES_TO_CLEAN = ["src", "tests", "cli.py"]


def clean():
    subprocess.run(
        [
            "autoflake",
            "--remove-all-unused-imports",
            "--remove-unused-variables",
            "--recursive",
            *FILES_TO_CLEAN,
            "-i",
            "--exclude=__init__.py",
        ]
    )
    subprocess.run(["isort", *FILES_TO_CLEAN, "--profile", "black"])
    subprocess.run(["black", *FILES_TO_CLEAN])
    subprocess.run(["mypy", *FILES_TO_CLEAN])


def run():
    subprocess.run(["uvicorn", "src.main:app", "--reload"])


def generate_empty_tests():
    src_dir = "src"
    test_dir = "tests"
    for dirpath, dirnames, filenames in os.walk(src_dir):
        # Compute the corresponding path in the test directory
        relative_path = os.path.relpath(dirpath, src_dir)
        test_path = os.path.join(test_dir, relative_path)

        # Create the corresponding directory in the test structure
        os.makedirs(test_path, exist_ok=True)

        # Create an empty __init__.py in each directory
        init_file = os.path.join(test_path, "__init__.py")
        open(init_file, "w").close()

        # Create empty test files for each .py file in the src directory
        for filename in filenames:
            if filename.endswith(".py"):
                test_filename = (
                    "test_" + filename if filename != "__init__.py" else filename
                )
                test_file = os.path.join(test_path, test_filename)
                open(test_file, "w").close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="Command to run")
    args = parser.parse_args()
    if args.command == "clean":
        clean()
    elif args.command == "run":
        run()
    elif args.command == "generate-empty-tests":
        generate_empty_tests()
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
