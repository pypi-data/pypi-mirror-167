import os
import re
import sys
import zipfile

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}


def translate(name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    trans_name = name.translate(TRANS)
    name_re_symb = re.sub(r'[^\w.]+', '_', trans_name)
    return name_re_symb


def cleaner(folder):
    sort(folder)
    archive(folder)
    del_folder(folder)
    print('Done!')


def sort(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            extension = file_path.split('.')[-1]
            if extension in ('jpeg', 'png', 'jpg', 'svg'):
                new_folder = os.path.join(folder, 'image')
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_file = os.path.join(new_folder, translate(file))
                os.replace(file_path, new_file)

            if extension in ('avi', 'mp4', 'mov', 'mkv'):
                new_folder = os.path.join(folder, 'video')
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_file = os.path.join(new_folder, translate(file))
                os.replace(file_path, new_file)

            if extension in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
                new_folder = os.path.join(folder, 'documents')
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_file = os.path.join(new_folder, translate(file))
                os.replace(file_path, new_file)

            if extension in ('mp3', 'ogg', 'wav', 'amr'):
                new_folder = os.path.join(folder, 'music')
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_file = os.path.join(new_folder, translate(file))
                os.replace(file_path, new_file)

            if extension in ('zip', 'tar'):
                new_folder = os.path.join(folder, 'archive')
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                new_file = os.path.join(new_folder, translate(file))
                os.replace(file_path, new_file)

        if os.path.isdir(file_path):
            file_path = os.path.join(folder, file)
            translate_folder = translate(file)
            new_folder = os.path.join(folder, translate_folder)
            os.replace(file_path, new_folder)

            new_folder_path = os.path.join(folder, new_folder)
            sort(new_folder_path)


def archive(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isdir(file_path):
            archive(file_path)
        elif os.path.isfile(file_path):
            extension = file_path.split('.')[-1]
            file_name = file_path.split('.')[-2]
            if extension in ('zip', 'tar'):
                archive_file = zipfile.ZipFile(file_path)
                archive_file.extractall(file_name)
                archive_file.close()


def del_folder(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isdir(file_path):
            del_folder(file_path)
            if not os.listdir(file_path):
                os.rmdir(file_path)


if __name__ == '__main__':
    folder = sys.argv[1]
    cleaner(folder)
