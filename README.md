# django-tutorial

[장고 튜토리얼 문서](https://docs.djangoproject.com/ko/4.2/intro/)에 따라 구현해보는 프로젝트 입니다.

본 프로젝트는 isort, black 기반으로 포멧팅을 해주어서, 튜토리얼 코드와 약간의 차이가 있을 수 있으나, 본질적으로 같은 구현의 내용을 담고 있습니다. 

또한 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) 를 준수하여 작성되었습니다.

Style Guide 는 통일된 컨벤션을 준수함으로써 개인 개발에서의 클린 코딩 뿐만 아니라, 팀 단위의 개발에 있어서 클린 코딩을 지향할 수 있는 좋은 규칙입니다. Google 의 스타일 가이드는 업계의 표준 중 하나로 사용되기도 하니, 한 번 정독해보시는 것도 추천드립니다.


## 개발환경 세팅
저는 개인적으로 pyenv 라는 툴을 사용해서 가상환경을 관리하고 있습니다. pyenv 설치법은 링크 등을 참조하세요. (pyenv 와 pyenv-virtualenv 둘다 설치해주셔야합니다)
- Window : https://kodorricoding.tistory.com/16
- Mac : https://leesh90.github.io/environment/2021/04/03/python-install/
```bash
$ pyenv virtualenv 3.10.9 django-tutorial 
$ pyenv activate django-tutorial
$ pip install -r requirements.txt
```
`django-tutorial` 은 가상환경 이름입니다. pycharm 등의 IDE나 conda, venv 를 사용하여 가상환경을 미리 세팅하셨다면, 하지 않아도 좋습니다.

터미널에서 현재 경로를 django-tutorial/mysite/ 로 이동한 후, 
mysite 안의 README.md 의 안내에 따라 프로젝트를 실행하세요!


## 브랜치
각 파트별로 생성되어있는 브렌치에서, 중간 결과물을 확인하실 수 있습니다.

| Chapter | Branch                                                                                                                                                                                                                          | Documents                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| part 1  | [part-1](https://github.com/fivessun/django-tutorial/tree/part-1/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial01/) |
| part 2  | [part-2](https://github.com/fivessun/django-tutorial/tree/part-2/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial02/) |
| part 3  | [part-3](https://github.com/fivessun/django-tutorial/tree/part-3/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial03/) |
| part 4  | [part-4-without-generic-view](https://github.com/fivessun/django-tutorial/tree/part-4-without-generic-view/mysite) [part-4-with-generic-view](https://github.com/fivessun/django-tutorial/tree/part-4-with-generic-view/mysite) | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial04/) |
| part 5  | [part-5](https://github.com/fivessun/django-tutorial/tree/part-5/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial05/) |
| part 6  | [part-6](https://github.com/fivessun/django-tutorial/tree/part-6/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial06/) |
| part 7  | [part-7](https://github.com/fivessun/django-tutorial/tree/part-7/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial07/) |
| part 8  | [part-8](https://github.com/fivessun/django-tutorial/tree/part-8/mysite)                                                                                                                                                        | [링크](https://docs.djangoproject.com/ko/4.2/intro/tutorial08/) |
