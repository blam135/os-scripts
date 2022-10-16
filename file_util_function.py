## Converts a given extension within into a uuid format

import glob
import uuid
import os

# Set Variables
root_dir = "F:\Some random Folder\/"
exclude_file_dir = []

'''
Renames all files in a root director given an extension
'''
def rename(root_dir, extension):
  glob_string = "{}**\*{}".format(root_dir, extension)
  # 
  for file in glob.glob(glob_string, recursive= True):
    curr_file_arr_format = file.split("\\")
    is_excluded = len(list(set(exclude_file_dir) & set(curr_file_arr_format))) != 0
    if (not is_excluded):
      curr_file_arr_format[-1] = "{}.{}".format(uuid.uuid4(), extension)
      new_file_name = "\\".join(curr_file_arr_format)
      print("Changing {} to {}".format(file, new_file_name))
      os.rename(file, new_file_name)

'''
Renames every single file regardless of the extension
'''
def rename_all_extensions(root_dir):
  extensions = list_extensions(root_dir)
  for ext in extensions:
    rename(root_dir, ext)

'''
Lists all the extensions which exists in a root dir
'''
def list_extensions(root_dir):
  glob_string = "{}**\*.*".format(root_dir)
  result = set()
  for file in glob.glob(glob_string, recursive=True):
    extension = (file.split("\\")[-1]).split(".")[-1]
    result.add(extension)
  return result

'''
Lists all files in a root dir given an extension
'''
def get_files_by_extension(root_dir, extension):
  glob_string = "{}**\*.{}".format(root_dir, extension)
  files = []
  for file in glob.glob(glob_string, recursive=True):
    files.append(file)
  return files

'''
!! WARNING !!
Deletes all files in a root dir given an extension
'''
def delete_files_by_extension(root_dir, extension):
  glob_string = "{}**\*.{}".format(root_dir, extension)
  for file in glob.glob(glob_string, recursive=True):
    print(file)
    os.remove(file)