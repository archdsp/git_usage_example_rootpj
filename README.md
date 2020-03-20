## 서브모듈 CMD로 추가 하기
git submodule add https://github.com/<username>/<repo name>

## 서브모듈과 같이 클론하기
git clone https://github.com/<username>/<repo name> --recurse-submodules

## 모든 서브모듈 한번에 최신으로 업데이트 하기
git submodule update --remote <서브 모듈 이름>

## 모든 서브모듈 한번에 명령 수행 시키기
### Ex.
git submodule foreach 'git status'

## 여러개의 서브 모듈 명령어 짧게 쓰기, Alias 사용
git config alias.sstatus "submodule foreach 'git status'"
