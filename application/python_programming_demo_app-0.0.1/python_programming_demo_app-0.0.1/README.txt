Roboter
====

## Install

1. 이하 패키지를 인스톨하거나, 실행하실 디렉토리에 roboter 폴더를 옮겨주시기 바랍니다. 
$ python setup.py develop

or

$ ls
roboter


## Requirement
pip install termcolor==1.1.0


## Usage

1. 이하와 같이 talk_about_restaurant 함수를 불러오면 실행할 수 있습니다.

# vim main.py
import roboter.controller.conversation
roboter.controller.conversation.talk_about_restaurant()

2. 실행해주세요 
$ python main.py

(옵션: 보존할 csv 나 템플릿을 변경할 경우는 settings.py 에 아래를 추가합니다)

# vim settings.py
CSV_FILE_PATH = '/tmp/test.csv'
TEMPLATE_PATH = '/tmp/templates/'

# settings.py 파일을 작성한 경우에는, 변경하지 않은 경우의 default 는 다음과 같이 설정합니다.
CSV_FILE_PATH = None
TEMPLATE_PATH = None

