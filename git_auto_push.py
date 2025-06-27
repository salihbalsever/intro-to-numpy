import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Error running command: {cmd}")
        exit(1)

def main():
    commit_message = input("Enter commit message: ")

    run_cmd("git add .")
    run_cmd(f'git commit -m "{commit_message}"')
    run_cmd("git push")

if __name__ == "__main__":
    main()
