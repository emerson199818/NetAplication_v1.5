import os
import shutil


temp_folder_path = os.environ['temp']

for filename in os.listdir(temp_folder_path):
    file_path = os.path.join(temp_folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'Error al eliminar {file_path}. Razón: {e}')