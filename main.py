import subprocess

def main():
    result = subprocess.run(
        ["behave", "bdd_tests/features/search.feature"],
        capture_output=True,
        text=True
    )
    print("=== STDOUT ===")
    print(result.stdout)
    print("=== STDERR ===")
    print(result.stderr)
    print("Status:", "passed" if result.returncode == 0 else "failed")

if __name__ == "__main__":
   main()
