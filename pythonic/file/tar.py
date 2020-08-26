# tar파일의 압축과 압축해제

import tarfile

# 폴더를 tar.gz 압축
with tarfile.open('compress.tar.gz', 'w:gz') as tr:
    tr.add('compress')

# tar.gz 파일의 압축 해제
with tarfile.open('compress.tar.gz', 'r:gz') as tr:
    tr.extractall(path='compress_tar')

# tar 파일 내용을 확인하기
with tarfile.open('compress.tar.gz', 'r:gz') as tr:
    with tr.extractfile('compress_tar/compress/test.txt') as f:
        print(f.read())
