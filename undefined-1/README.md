---
description: 소스코드 업로드를 하는 방법을 설명하는 목차
---

# 설치 및 이용방법

## 요구사항

해당 깃허브 스터디는 깃허브를 사용한 방식이므로,  [git](https://git-scm.com/downloads) 설치가 필요합니다.

{% hint style="info" %}
따로 깃허브 데스크 탑 버전을 쓰셔도 상관없고, 깃허브 포크 방식을 사용해서 이용해도 무방합니다.
{% endhint %}

## 

### 깃허브 이용방법

#### 1. 소스코드 받아오기 && 폴더 만들기

```bash
# 저장소에서 깃허브 소스 받아오
git clone https://github.com/hanjiung/AlgorithmCode

# 시즌 3폴더에 들어가서 깃허브 닉네임으로 된 폴더를 만들기
cd season/season3 && mkdir github nickname && cd github nickname
```

{% hint style="info" %}
github nickname은 깃허브 닉네임으로 설정해주세요.
{% endhint %}



### 2. 소스코드 업로드

```bash
# 최신 소스코드 동기화
git pull

# 만들었던 폴더로 이동해서 소스코드를 폴더에 넣은 뒤에 업로드 합니다.
git add 소스파일
git commit -m "커밋 메세지"
git push origin main
```

## 

### 깃허브 포크 방식으로 사용하기

#### git fork 방식은 원격 저장소\(github\)에 있는 다른 사람이 올린 저장소 상태를 그대로 복사해서 자신의 Github 계정에 원격 저장소를 생성하고 복제하는 기능입니다. 

포크 방식 추후 업데이트 할 예정입니다.

{% hint style="info" %}
[https://data-make.tistory.com/228](https://data-make.tistory.com/228) 여기 블로그나 따로 검색해서 사용하길 바랍니다.
{% endhint %}



