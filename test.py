# 라이브러리 로딩 -----------------------------
import urllib

from bs4 import BeautifulSoup
import urllib.request as req

# 데이터 변수 선언 ------------------------------------
comName = input("회사명을 입력하세요 : ")
# url 검색 + 검색어 한글변환
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + urllib.parse.quote_plus(comName)

# 데이터 가져오기 urlopen() ----------------------------
res = req.urlopen(url)
print(type(res))

# 데이터 분석하기 -------------------------------------
soup = BeautifulSoup(res, "html.parser")


# 원하는 데이터 추출 ---------------------------------
# copy selector해서 바로 원하는 데이터 가져오기
#usddata = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")


기업명 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(1) > span.txt > span")
기업구분 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(2) > span.txt > span > a")
대표자 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(3) > span.txt")
업종 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(4) > span.txt > span")
설립일 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(5) > span.txt > span")
상장일 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(6) > span.txt > span")
매출액 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(7) > span.txt")
종업원 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(8) > span.txt > span")
평균연봉 = soup.select_one("section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(9) > span.txt > span")

# 텍스트만 추출하기 .get_text() 사용
print(f"기업명 : {기업명.get_text()}\n"
      f"기업구분 : {기업구분.get_text()}\n"
      f"대표자 : {대표자.get_text()}\n"
      f"업종 : {업종.get_text()}\n"
      f"설립일 : {설립일.get_text()}\n"
      f"상장일 : {상장일.get_text()}\n"
      f"매출액 : {매출액.get_text()}\n"
      f"종업원 : {종업원.get_text()}\n"
      f"평균연봉 : {평균연봉.get_text()}\n")
