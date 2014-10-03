import zipfile

with zipfile.ZipFile("test.zip","r") as zf:
    print zf.namelist()
