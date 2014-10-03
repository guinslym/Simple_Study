import gzip
with gzip.open("test.txt.gz","rb") as file:
    print file.read()
