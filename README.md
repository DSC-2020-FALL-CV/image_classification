# image_classification

## Flask

##### 가상환경 생성과 Flask 설치 (Anaconda 3 기준)
* Anaconda Prompt에서 `conda create -n <venv_name>` 실행하여 가상환경 생성
* `Conda activate <venv_name>`을 실행하여 가상환경 활성화
* `conda install -c anaconda flask` 실행하여 가상환경에 Flask Library 설치

##### hello.py 실행
* Anaconda prompt를 실행하여 hello.py가 위치한 폴더로 cd 실행
* `set FLASK_APP=hello.py`를 실행하여 환경변수 설정
* `flask run`  또는 `python -m flask run`을 실행
* http://127.0.0.1:5000/ 에 접속하여 확인

## Server

##### 호스팅 정보
* Platform: Naver Cloud Platform
* Server: Micro Server
* Web Uri: http://118.67.133.25:5000/

##### SSH 접속 - 접속 계정 root에서 변경 예정
* Windows Powershell의 openSSH 사용
* `ssh root@<접속 주소> -p <포트 번호>`를 실행하여 접속 요청
* password에 `<root password>`를 입력하여 접속

##### 서버 실행
* `. venv/bin/activate`를 실행하여 가상환경 활성화
* `cd Flask`를 실행하여 디렉토리 이동
* `set FLASK_APP=app.py`를 실행하여 변수 설정
* `nohup python3 -m flask run --host=0.0.0.0 &`을 실행
* http://118.67.133.25:5000/ 에 접속하여 실행 확인

##### 서버 중지
* `ps -ef | grep flask`를 실행하여 `python3 -m flask run --host=0.0.0.0` 프로세스의 pid 확인
* `kill <pid>`를 실행하여 프로세스 종료


## 테스크 체크하기

- [notion](https://www.notion.so/d19c503e4cef429e91d8e55869f1c854?v=a06e3886e88343b59b18cb6f0797ff2a&p=9fe3db0e8883418e850b5b3c24a6d7b8)에서 할 일을 보고 완료하면 아래 본인의 이름이 적힌 체크 박스 수정해서 README.md push하기
- 모든 박스가 체크되면 notion의 task 상태가 In Progress에서 complete로 넘어갑니다

- [ ] 김현구
- [ ] 엄현식
- [ ] 이근희
- [ ] 이준영
