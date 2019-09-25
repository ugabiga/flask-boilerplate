import subprocess

stdout = subprocess.PIPE
stderr = subprocess.STDOUT


# noinspection SpellCheckingInspection
def run_pytest_by_monkey_type():
    subprocess.call(
        "monkeytype run `which pytest`", shell=True, stdout=stdout, stderr=stderr
    )
    print("pytest complete")


# noinspection SpellCheckingInspection
def apply_monkey_type():
    monkeytype_process = subprocess.Popen(
        "monkeytype list-modules", shell=True, stdout=stdout, stderr=stderr
    )

    for line in monkeytype_process.stdout.readlines():
        string_line = line.decode("utf-8").replace("\n", " ").replace("\r", "")

        print(f"processing == {string_line}")
        subprocess.call(
            "monkeytype apply " + string_line, shell=True, stdout=stdout, stderr=stderr
        )


def main():
    run_pytest_by_monkey_type()
    apply_monkey_type()


if __name__ == "__main__":
    main()
