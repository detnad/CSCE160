import os
import re
import zipfile
import time


def perform_zip(dir_name):
    pattern = re.compile(r'(?!^\.)(?!^__)')
    zip_name = f'{dir_name}_{time.strftime("%Y%m%d-%H%M%S")}.zip'
    with zipfile.ZipFile(zip_name, 'w') as zippy:
        os.chdir(dir_name)
        for file_name in os.listdir():
            if re.match(pattern, file_name):
                zippy.write(file_name)
                print(f'added {file_name}')
        if len(zippy.filelist) == 0:
            raise Exception("No files found to zip!")
    return zip_name


def main():
    dir_name = input('Enter the name of the directory name to zip: ')
    if not os.path.exists(dir_name):
        print(f'The directory "{dir_name}" was not found.')
    elif not os.path.isdir(dir_name):
        print(f'The name "{dir_name}" is not a directory.')
    elif os.path.exists(f"{dir_name}/{dir_name}"):
        raise Exception("Nested directories found!")
    else:
        zip_name = perform_zip(dir_name)
        print(f'Zip file {zip_name} was created.')


if __name__ == '__main__':
    main()
