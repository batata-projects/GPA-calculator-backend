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


def update_test_files():
    src_dir = "src"
    test_dir = "tests"
    for dirpath, dirnames, filenames in os.walk(src_dir):
        if "__pycache__" in dirpath:
            continue
        relative_path = os.path.relpath(dirpath, src_dir)
        test_path = os.path.join(test_dir, relative_path)

        os.makedirs(test_path, exist_ok=True)

        init_file = os.path.join(test_path, "__init__.py")
        open(init_file, "w").close()

        for filename in filenames:
            if filename.endswith(".py"):
                test_filename = (
                    "test_" + filename if filename != "__init__.py" else filename
                )
                test_file = os.path.join(test_path, test_filename)
                open(test_file, "a").close()
    
    for dirpath, dirnames, filenames in os.walk(test_dir):
        if "__pycache__" in dirpath:
            continue
        relative_path = os.path.relpath(dirpath, test_dir)
        src_path = os.path.join(src_dir, relative_path)

        for filename in filenames:
            if filename == "__init__.py":
                continue
            src_file = os.path.join(src_path, filename)
            if not os.path.exists(src_file):
                test_file = os.path.join(dirpath, filename)
                os.remove(test_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="Command to run")
    args = parser.parse_args()
    if args.command == "clean":
        clean()
    elif args.command == "run":
        run()
    elif args.command == "update-test-files":
        update_test_files()
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
