코알라UNIV에서 5주차까지 배웠던 내용들을 모두 활용하여 수행할 수 있는 자체 제작 과제입니다.

[멜론 TOP100 이동하기](https://www.melon.com/chart/index.htm)
![](https://images.velog.io/images/soo01imm/post/0e04a72f-a2a5-4565-b13c-ff7d064f1de6/2020-05-22%20(1).png)
# 메뉴를 선택하여 해당 탭의 Top 100 차트의 목록을 크롤링하고, 크롤링한 데이터를 xlsx 파일에 저장하기
## Step 1. "실시간" 탭의 Top 100 데이터 추출
추출할 데이터 세트

| 데이터 변수명 | 형식 | 비고 |
|:----------|:----------:|:----------:|
| rank | int | 순위 |
| imgSrc | string | 이미지 링크 |
| song | string | 노래 제목 |
| artist | string | 아티스트명, 복수 가능 |
| album | string | 앨범 제목 |

* artist의 경우, 다음과 같이 **두 명 이상**의 artist인 경우가 존재합니다.
![](https://images.velog.io/images/soo01imm/post/afbc507f-2580-4e89-b47c-e8a51ddd88fd/%EB%B3%B5%EC%88%98%EC%9D%98%20writer.PNG)
해당 경우를 고려하여 데이터를 추출하시고, **artistString**이라는 변수에 '/' 로 artist를 구분하여 새로운 데이터 변수를 생성해주세요.
## Step 2. 메뉴를 선택하여 해당 탭의 Top 100 데이터 추출
* 메뉴 입력 양식입니다.

| 탭 이름 | 메뉴 입력 |
|:-------|:-------|
| 실시간 | realtime |  
| 급상승 | rise | 
| 일간 | day |  
| 주간 | week | 
| 월간 | month |  

* 코드 샘플은 다음과 같습니다.
```
menu = input("멜론차트 옵션을 입력하세요: ")

if menu == "realtime" :
    raw = requests.get("https://www.melon.com/chart/index.htm", headers={"User-Agent": "Mozilla/5.0"})
else :
    # 나머지 경우, url 주소의 규칙을 파악한 후 적절히 raw 변수를 설정해주시면 됩니다.
    # .htm 다음 따라오는 params의 값은 모두 무시하셔도 상관 없습니다. .htm까지를 url로 넣어주세요!
```
* 앨범 커버 이미지의 경우, 입력했던 menu명과 동일한 폴더 를 생성하시고, urllib을 이용하여 **'순위_노래제목.png'**로 저장해주시면 됩니다. 예를 들어 순위가 1, 노래 제목이 '에잇(Prod.&Feat. SUGA of BTS)' 경우, 특수문자를 고려하여 적절히 replace함수와 slicing 기법을 이용하여 '1_에잇.png'로 저장해주시면 됩니다. 

## Step 3. 메뉴 별로 xlsx의 sheet를 생성하여 추출한 데이터 저장하기
```
sheet.append([int(rank), imgSrc, song, artistString, album])
```
로 저장하시면 됩니다! 
* sheet의 제목은 메뉴명과 동일하게 설정해주세요.
* load_workbook()을 통해 엑셀파일 불러오기를 하는 경우 불러올 파일이 없다면 에러를 발생시킵니다. 이 때, **try/except**문을 활용하여 
불러올 파일이 없다면 새로운 파일을 생성하고, 
불러올 파일이 있다면 load_workbook()을 통해 해당 파일을 불러옵니다.
```
try:
    wb = openpyxl.load_workbook("MelonChartSheet.xlsx")
    # 코드 작성
    sheet.append(["순위", "앨범 사진 링크 주소", "곡 명", "아티스트 명", "앨범 명"])
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook()
    # 코드 작성
    sheet.append(["순위", "앨범 사진 링크 주소", "곡 명", "아티스트 명", "앨범 명"])
    print("새로 파일을 만들었습니다")
```
* 예를 들어, realtime에 대한 데이터를 한번 더 크롤링 시도하려 할 때, 이미 생성되어 있는 **realtime xlsx sheet를 삭제하시고, 새로운 sheet를 생성해주세요. ~~구글링을 통해 sheet를 삭제하는 방법을 찾아주세요~~**
## 추가 : 'datetime' 모듈을 활용하여 sheet 맨 위에 크롤링한 현재 시각을 추가해주세요.
~~역시 구글링하면 간단하게 현재 시각 추출하는 법을 알 수 있습니다!~~
