from zipfile import ZipFile

zip_obj = ZipFile('unzip_me_for_instructions.zip', 'a')
zip_obj.extractall()