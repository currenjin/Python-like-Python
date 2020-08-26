# tar파일의 압축과 압축해제

import tarfile

# 폴더를 tar.gz 압축
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('tar')

# tar.gz 파일의 압축 해제
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')

# tar 파일 내용을 확인하기
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('tar/tar_test.txt') as f:
        print(f.read())
