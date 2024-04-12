import os
import shutil

def remove_db_and_pycache(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".db"):
                os.remove(os.path.join(root, file))
                print(f"Removed file: {os.path.join(root, file)}")

        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Removed directory: {pycache_path}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    remove_db_and_pycache(current_dir)