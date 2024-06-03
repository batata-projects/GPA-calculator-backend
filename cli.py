import argparse
import os
import subprocess

FILES_TO_CLEAN = ["src", "tests", "cli.py"]

SEP = os.path.sep


def run():
    """
    command: run
    Run the fastapi backend server
    """
    subprocess.run(["uvicorn", "src.main:app", "--reload"])


def clean():
    """
    command: clean
    Clean up the code
    """
    subprocess.run(
        [
            "autoflake",
            "--remove-all-unused-imports",
            "--remove-unused-variables",
            "--recursive",
            *FILES_TO_CLEAN,
            "-i",
            "--exclude=conftest.py",
        ]
    )
    subprocess.run(["isort", *FILES_TO_CLEAN, "--profile", "black"])
    subprocess.run(["black", *FILES_TO_CLEAN])
    subprocess.run(["mypy", *FILES_TO_CLEAN, "--check-untyped-defs"])


def generate_test_files():
    """
    command: generate-test-files
    Generate empty test files in the `tests` and `tests/fixtures`
    directories for all the files in the `src` directory.
    """
    src_dir = "src"
    test_dir = "tests"
    fixtures_dir = f"tests{SEP}fixtures"
    for dirpath, dirnames, filenames in os.walk(src_dir):
        if "__pycache__" in dirpath:
            continue
        relative_path = os.path.relpath(dirpath, src_dir)
        test_path = os.path.join(test_dir, relative_path)
        fixtures_path = os.path.join(fixtures_dir, relative_path)

        os.makedirs(test_path, exist_ok=True)
        os.makedirs(fixtures_path, exist_ok=True)

        init_file = os.path.join(test_path, "__init__.py")
        open(init_file, "w").close()

        init_file = os.path.join(fixtures_path, "__init__.py")
        open(init_file, "w").close()

        for filename in filenames:
            if filename.endswith(".py"):
                if filename == "__init__.py":
                    continue
                test_filename = "test_" + filename
                test_file = os.path.join(test_path, test_filename)
                open(test_file, "a").close()

                fixture_file = os.path.join(fixtures_path, filename)
                open(fixture_file, "a").close()


def import_fixtures():
    """
    command: import-fixtures
    This command imports all the fixtures in the
    `tests/fixtures` directory to the `conftest.py` file.
    """
    conftest = open(f"tests{SEP}conftest.py", "w")
    fixtures = os.path.join("tests", "fixtures")
    for dirpath, dirnames, filenames in os.walk(fixtures):
        for filename in filenames:
            if filename.endswith(".py"):
                lines = open(os.path.join(dirpath, filename)).read().split("\n")
                i = 0
                function_names = []
                while i < len(lines):
                    line = lines[i]
                    if "@pytest.fixture" in line:
                        line = lines[i + 1]
                        function_names.append(line.split("def ")[1].split("(")[0])
                    i += 1
                if function_names:
                    path = os.path.relpath(dirpath, fixtures).replace(SEP, ".")
                    path = f".fixtures.{path}.{filename.split('.')[0]}"
                    while ".." in path:
                        path = path.replace("..", ".")
                    conftest.write(f"from {path} import {', '.join(function_names)}\n")
    conftest.close()


def run_tests():
    """
    command: run-tests
    This command runs all the tests in the `tests` directory.
    """
    subprocess.run(["pytest", "tests"])


def pre_stage():
    """
    command: pre-stage
    This command runs the `import-fixtures`,
    `clean` and `run-tests` commands in this order.
    """
    import_fixtures()
    clean()
    run_tests()


def help():
    """
    command: help
    Show help
    """
    print("Usage: python cli.py [command]")
    print("Commands:")
    commands: list[dict[str, str]] = []
    for name, func in globals().items():
        if callable(func):
            if type(func.__doc__) != str:
                continue
            commands.append(
                {
                    "command": func.__doc__.split("\n")[1].split(":")[1].strip(),
                    "description": "\n".join(func.__doc__.split("\n")[2:-1]),
                }
            )
    max_command_length = max([len(command["command"]) for command in commands])
    for cmd in commands:
        command = cmd["command"]
        description = cmd["description"]
        desc_lines = description.split("\n")
        print(f"\t{command:<{max_command_length}}:\t{desc_lines[0]}")
        for line in desc_lines[1:]:
            print(f"\t{'':<{max_command_length}} \t{line}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="Command to run")
    args = parser.parse_args()
    if args.command == "clean":
        clean()
    elif args.command == "run":
        run()
    elif args.command == "generate-test-files":
        generate_test_files()
    elif args.command == "import-fixtures":
        import_fixtures()
    elif args.command == "run-tests":
        run_tests()
    elif args.command == "pre-stage":
        pre_stage()
    elif args.command == "help":
        help()
    else:
        print("Invalid command")
        help()
        exit(1)
