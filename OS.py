import os
import zipfile

def zip_text_files(directory, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    filepath = os.path.join(root, file)
                    zipf.write(filepath, arcname=file)
                    print(f"Added {file} to archive")

# Example usage
zip_text_files("sample_folder", "texts_archive.zip")
