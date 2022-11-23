# tar파일의 압축과 압축해제

import tarfile

# 폴더를 tar.gz 압축
with tarfile.open('compress.tar.gz', 'w:gz') as tr:
    tr.add('compress')

# tar.gz 파일의 압축 해제
with tarfile.open('compress.tar.gz', 'r:gz') as tr:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tr, path="compress_tar")

# tar 파일 내용을 확인하기
with tarfile.open('compress.tar.gz', 'r:gz') as tr:
    with tr.extractfile('compress/test.txt') as f:
        print(f.read())
