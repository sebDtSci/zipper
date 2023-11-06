import argparse
import zipfile
import os

# Fonction pour ajouter des dossiers au zip
def add_folder_to_zip(zip_file, folder_path):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path, os.path.relpath(file_path, os.path.dirname(folder_path)))

# Fonction principale
def main(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        add_folder_to_zip(zipf, folder_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zip a folder.")
    parser.add_argument('folder', help='Folder to zip')
    parser.add_argument('-o', '--output', required=True, help='Output zipfile name')

    args = parser.parse_args()
    main(args.folder, args.output)
