# zip의 압축과 압축 해제

import glob
import zipfile

with zipfile.ZipFile('compress.zip', 'w') as z:
    # z.write('compress')
    # z.write('compress/test.txt')
    for f in glob.glob('compress/**', recursive=True):
        z.write(f)

with zipfile.ZipFile('compress.zip', 'r') as z:
    # z.extractall('zzz2')
    with z.open('compress_zip/test.txt') as f:
        print(f.read())
