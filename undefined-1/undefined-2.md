# 깃허브 명령어 가이드

### GIT 소스 코드 관련 명령어

```bash
### 소스코드 추가 관련 명령어

# 깃허브 저장소에서 소스코드 가져오기
git clone URL

# 저장소와 소스코드 최신화하고 merget
git pull 

# 저장소와 최신코드 받아오기
git fetch

# 수정한 코드 선택
git add source_filename

# 선택한 소스 코드 설명 적기
git commit -m "commit_description"

# 저장소에 소스 코드 추가하기
git push remote_name branch_name 

# 커밋 내역 확인
git log
```

### 

### 

### 브랜치 관련 명령어 

```bash
### 브렌치 관련 명령어

# 깃 브랜치 생성
git branch branch_name

# 깃 브랜치 삭제
git branch -d branch_name

# 깃 원격 브랜치 목록보기
git branch -r

# 깃 로컬 브랜치 목록보기
git branch -a
```

### 

### commit, merge 취소 관 명령어

```bash
### 이전 commit, merge 취소 관련 명령어

# commit한 이전 코드 취소하기 
git reset hard HEAD^

# commit한 이전 코드는 살리고 커밋만 취소하기
git reset soft HEAD^
```



### 깃 계정관련 명령

```bash

### 깃 계정관련 명령어

# git 계정 Name 변경하기
git conifg user.name "user_name" 

# git 계정 Mail 변경하기
git config user.email "user_email"

```



