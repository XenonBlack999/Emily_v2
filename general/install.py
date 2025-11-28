import subprocess

def run_command(command, shell=False):
    print(f"Running: {command}")
    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with code {e.returncode}")

def main():
    # Update package list
    run_command(["sudo", "apt", "update"])

    # Install Python and related packages
    run_command(["sudo", "apt", "install", "-y", "python3", "python3-venv", "python3-dev"])
    run_command(["sudo", "apt", "install", "-y", "python3.13-venv"])
    run_command(["sudo", "apt", "install", "-y", "python3.12", "python3.12-venv", "python3.12-dev"])

    # Install espeak dependencies
    run_command(["sudo", "apt", "install", "-y", "libespeak1"])
    run_command(["sudo", "apt", "install", "-y", "espeak-ng"])

    # Create Python 3.12 virtual environment
    run_command(["python3.12", "-m", "venv", "venv"])

    print("\n✅ Virtual environment 'venv' created.")
    print("⚠️ To activate it, run the following in your terminal:")
    print("   source venv/bin/activate")

    # Install Python packages inside the venv
    print("\nInstalling Python packages inside the virtual environment...")
    run_command("venv/bin/pip install speechrecognition", shell=True)

    print("\n✅ Setup complete.")

if __name__ == "__main__":
    main()

