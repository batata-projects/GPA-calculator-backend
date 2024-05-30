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


def generate_test_files():
    src_dir = "src"
    test_dir = "tests"
    fixtures_dir = "tests/fixtures"
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


def help():
    print("Usage: python cli.py [command]")
    print("Commands:")
    print("  clean: Clean up the code")
    print("  run: Run the application")
    print("  generate-test-files: Generate test files")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="Command to run")
    args = parser.parse_args()
    if args.command == "clean":
        clean()
    elif args.command == "run":
        run()
    elif args.command == "generate-test-files":
        generate_test_files()
    elif args.command == "help":
        help()
    else:
        print("Invalid command")
        help()


if __name__ == "__main__":
    main()