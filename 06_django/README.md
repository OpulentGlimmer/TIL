# 01. django

## c\폴더 이름 1\폴더 이름2 폴더 만들기
- mkdir 폴더 이름 1
- cd 폴더 이름 1
- mkdir 폴더 이름 2
- cd 폴더 이를 2

## 가상환경 생성 & Django 라이브러리 설치
- pip install virtualenv==20.13.2 : 가상 환경을 만들어 주는 라이브러리
- virtualenv django_env : django_env 라는 이름으로 가상 환경을 새로 만들어 준다.
- django_env\Scripts\activate : Scripts 폴더 내의 activate 파일을 실행해 가상 환경을 활성화

# 02. Django & OpenCV 설치하기 (활성화된 env 내에 설치)

- pip install django==3.2 
- pip install opencv-python==4.5.5.62 
- pip install pillow==8.2.0 
- pip freeze : 가상 환경에 설치된 라이브러리들의 리스트를 확인

# 03. 장고 프로젝트 생성
- django-admin startproject 프로젝트 이름 : 프로젝트 폴더가 생긴다.
- cd 프로젝트 이름