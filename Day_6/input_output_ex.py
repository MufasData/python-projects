# methods are chdir, makedirs, path.split, path.basename (retrieves the last component of the file path, usually the file name), rmdir
from pathlib import Path
import os

# To get the current working directory
path = os.getcwd()
print()
print(f"Here is the current working directory...\n{path}")
print()

# To change a directory
# path = os.chdir("C:\\Users\\mufas\\OneDrive\\Desktop\\SQL")

# file = open('test_file.txt')
# print(file.read())
# file.close()

# new_dir = os.makedirs('C:\\Users\\mufas\\OneDrive\\Desktop\\SQL\\testing_dir')

new_path = 'C:\\Users\\mufas\\OneDrive\\Desktop\\SQL'

element = os.path.split(new_path)

print(element)

folder = Path('C:/Users/mufas/OneDrive/Desktop/SQL/test_file.txt')
# new_file = folder / 'test_file.txt'

# my_file = open(new_file)

# print(my_file.read())

# my_file.close()

print(folder.read_text())

print(folder.name)

print(folder.suffix)

print(folder.stem)

print(folder.exists())

# Practice with PureWindowsPath method

guide = Path('Cameroon','Douala')

print(guide)

print(Path.home())

# guide.with_name(...)
# guide.parent

# To clear the system --- $ from os import system. For Windows, use system(cls)