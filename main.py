import subprocess
import sys

def main():
    result = subprocess.run(
        ["behave", "--no-capture", "bdd_tests/features/search.feature"],
        capture_output=True,    # Capture stdout and stderr
        text=True               # Return strings, not bytes
    )

    # Fallback if stdout is None
    stdout = result.stdout or ""
    stderr = result.stderr or ""

    print("=== STDOUT ===")
    print(stdout)
    print("=== STDERR ===")
    print(stderr)
    print("Status:", "✅ passed" if result.returncode == 0 else "❌ failed")

    # Optionally write to a log file
    with open("test_output.log", "w", encoding="utf-8") as f:
        f.write("=== STDOUT ===\n")
        f.write(stdout)
        f.write("\n=== STDERR ===\n")
        f.write(stderr)

    sys.exit(result.returncode)

if __name__ == "__main__":
    main()

