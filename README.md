<h1 align="center">자동 자가진단</h1>
<div align="center">

<br>
<a href="https://github.com/Sol-Studio/auto_jagajindan/releases"><img src="https://img.shields.io/github/downloads/Sol-Studio/auto_jagajindan/total" alt="다운로드 수"></a>
<a href="https://discord.gg/auytc6qS83"><img src="https://img.shields.io/discord/851458756532895769?label=discord" alt="디스코드"></a>
</div>

## ✨빠른 시작
파이썬 버전은 3.8 이상으로 설치해주세요!! 구버전에서는 작동하지 않습니다!<br>
### 0. 코드 다운로드 받기
[여기](https://github.com/Sol-Studio/auto_jagajindan/releases/)에서 최신버전을 다운로드받을 수 있습니다.


### 1. pip로 필요 패키지 설치하기
```powershell
$ pip install selenium==3.141.0
```
<br>

### 2. 크롬 드라이버 다운로드 받기
[여기](https://chromedriver.chromium.org/downloads)에서 자신의 크롬버전에 맞는 드라이버를 다운로드 받습니다<br>
> 주소창에 `chrome://version`를 입력하고 들어가면 크롬 버전 정보를 확인할 수 있습니다.

> 자세한 정보는 [여기](https://kminito.tistory.com/78)를 참고해주세요

다운로드 받은 드라이버를 main.py와 같은 폴더에 "`chromedriver.exe`"로 저장해주세요
<br><br>

### 3. 정보 입력하기
main.py 상단에 정보를 자신에 맞게 수정해주세요. <br>
> 입력하신 개인정보는 자가진단 로그인을 위해서만 사용되며 제3자에게 전송되지 않습니다!


```python
# 자신의 정보를 입력해주세요
data = {
    "이름": "홍길동",
    "생년월일": "YYMMDD",
    "학교": "**초 ㅁㅁ중 ㅇㅇ고",
    "비밀번호": "1234",
    "시/도": "**시",
    "학교급": "유치원"
}
```
#### 시/도 리스트
 - 서울특별시
 - 부산광역시
 - 대구광역시
 - 인천광역시
 - 광주광역시
 - 대전광역시
 - 울산광역시
 - 세종특별자치시
 - 경기도
 - 강원도
 - 충청북도
 - 충청남도
 - 전라북도
 - 전라남도
 - 경상북도
 - 경상남도
 - 제주특별자치도

#### 학교급 리스트
 - 유치원
 - 초등학교
 - 중학교
 - 고등학교
 - 특수학교 등

### 4. 실행하기
```powershell
$ python main.py
```
<br>

## 🏆기여자
 - [그저 사람](https://github.com/Sol-Studio)
<br><br>

## 💖후원자
[후원하기](https://toss.me/solstudio)
