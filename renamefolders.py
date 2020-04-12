import os

# Unzip all folders to same place
folders_path = 'path with all folders'
folders = os.listdir(folders_path)

# Folder name example: lnamefname_numbers_HelloWorld.zip
for f in folders:
  x = f.split("_")
  os.rename(f, x[0]) # lnamefname
			
