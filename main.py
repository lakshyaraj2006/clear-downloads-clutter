from pathlib import Path
import os
import shutil
import platform

system = platform.uname().system

DOWNLOADS_FOLDER_PATH = Path.home() / "Downloads"

from project.constants import AUDIO_FORMATS, VIDEO_FORMATS, IMAGE_FORMATS, DOCUMENT_FORMATS, COMPRESSED_FORMATS, SPREADSHEET_FORMATS, DATABASE_FORMATS, PROGRAMMING_FORMATS, FONT_FORMATS, ARCHIVE_FORMATS, MODEL_FORMATS, WEB_FORMATS, AV_FORMATS, VERSIONING_FORMATS, INSTALLER_FORMATS, MISCELLANEOUS_FORMATS

FORMAT_GROUPS = {
    "Audio Files": AUDIO_FORMATS,
    "Video Files": VIDEO_FORMATS,
    "Image Files": IMAGE_FORMATS,
    "Document Files": DOCUMENT_FORMATS,
    "Compressed Files": COMPRESSED_FORMATS,
    "Spreadsheet Files": SPREADSHEET_FORMATS,
    "Database Files": DATABASE_FORMATS,
    "Programming Files": PROGRAMMING_FORMATS,
    "Font Files": FONT_FORMATS,
    "Archive Files": ARCHIVE_FORMATS,
    "3D Model Files": MODEL_FORMATS,
    "Web Files": WEB_FORMATS,
    "Audio-Visual Files": AV_FORMATS,
    "Versioning Files": VERSIONING_FORMATS,
    "Installer Files": INSTALLER_FORMATS,
    "Miscellaneous Files": MISCELLANEOUS_FORMATS,
}

files_list = [file for file in os.listdir(DOWNLOADS_FOLDER_PATH) if os.path.isfile(os.path.join(DOWNLOADS_FOLDER_PATH, file))]

for key, value in FORMAT_GROUPS.items():
    for file in files_list:
        if os.path.splitext(file)[1].lower() in value:
            dir_name = key.replace(" ", "_").replace("-", "_")
            curr_dir = os.path.join(DOWNLOADS_FOLDER_PATH, dir_name)
            if not os.path.exists(curr_dir):
                os.makedirs(curr_dir)
            if os.path.exists(os.path.join(DOWNLOADS_FOLDER_PATH, file)):
                shutil.move(os.path.join(DOWNLOADS_FOLDER_PATH, file), os.path.join(curr_dir, file))
else:
    print("Your downloads folder has been organized successfully!")
    choice = input("Do you want to open {} directory ? (y/n)".format(DOWNLOADS_FOLDER_PATH))
    
    if choice in ["y", "n"]:
        if choice == "y":
            if system == "Windows":
                os.startfile(DOWNLOADS_FOLDER_PATH)
            elif system == "Linux":
                    os.system('xdg-open ' + str(DOWNLOADS_FOLDER_PATH))
            elif system == "Darwin":
                    os.system('open ' + str(DOWNLOADS_FOLDER_PATH))
            else:
                raise OSError('Unsupported operating system: ' + os.name)
            exit(1)
    else:
        print("Please enter valid choice!")