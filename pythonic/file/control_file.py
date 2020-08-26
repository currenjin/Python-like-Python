# 파일을 조작합니다.

import os
import pathlib
import glob
import shutil

# print(os.path.exists('test.txt'))

# 파일인가?
print(os.path.isfile('test.txt'))

# 디렉토리인가?
print(os.path.isdir('test.txt'))

# 파일의 이름 변경
# os.rename('test.txt', 'renamed.txt')

# 심볼릭 링크
# os.symlink('renamed.txt', 'symlink.txt')

# 디렉토리 생성과 삭제
# os.mkdir('test_dir')
# os.rmdir('test_dir')
# shutil.rmtree('test_dir') 모두 삭제하는 명령

# 파일 생성과 삭제
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# 디렉토리의 목록을 확인하기
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(os.listdir('test_dir'))

# 복사
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')

# 경로 확인
# print(os.getcwd())
