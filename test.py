# 네이버 금융으로 부터 환율 정보 추출하기
# 라이브러리 로딩 -----------------------------
from bs4 import BeautifulSoup
import urllib.request as req

# comName = input("기업명을 입력하세요 : ")

# 데이터 변수 선언 ------------------------------------
# url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + comName

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"

# 데이터 가져오기 urlopen() ----------------------------
res = req.urlopen(url)
print(type(res))

# 데이터 분석하기 -------------------------------------
soup = BeautifulSoup(res, "html.parser")


# 원하는 데이터 추출 ---------------------------------
# copy selector해서 바로 원하는 데이터 가져오기
# exchangeList > li.on > a.head.usd > div > span.value
#usddata = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")

print(soup.find_all('span', 'id=""'))

기업명 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(1) > span.txt > span")
기업구분 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(2) > span.txt > span > a")
대표자 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(3) > span.txt")
업종 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(4) > span.txt > span")
설립일 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(5) > span.txt > span")
상장일 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(6) > span.txt > span")
매출액 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(7) > span.txt")
종업원 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(8) > span.txt > span")
평균연봉 = soup.select_one("#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(9) > span.txt > span")



테스트 = soup.find_all('#sub_pack > section.sp_company.sc_new._au_company_search._au_company_answer > div > div.company_area > div:nth-child(2) > ul > li:nth-child(1) > span.txt > span')
print(f"테스트 : {테스트}")

print(f"기업명 : {기업명}\n"
      f"기업구분 : {기업구분}\n"
      f"대표자 : {대표자}\n"
      f"업종 : {업종}\n"
      f"설립일 : {설립일}\n"
      f"상장일 : {상장일}\n"
      f"매출액 : {매출액}\n"
      f"종업원 : {종업원}\n"
      f"평균연봉 : {평균연봉}\n")

#usddata = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
#print("usddata= ", usddata)
#print("usd/krw= ", usddata.string)

#jpy = soup.select_one("#exchangeList >  li:nth-child(2) > a.head.jpy > div > span.value")
#print("jpy = ", jpy)
#print("jpy/krw= ", jpy.string)
