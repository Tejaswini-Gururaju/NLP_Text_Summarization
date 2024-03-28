import shutil

# Replace "myenv" with the name of your virtual environment
virtual_env_name = ".venv"

# Delete the virtual environment directory
shutil.rmtree(virtual_env_name)

print(f"Virtual environment '{virtual_env_name}' has been deleted.")