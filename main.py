# 버전 1.0
# 자신의 정보를 입력해주세요
data = {
    "이름": "홍길동",
    "생년월일": "YYMMDD",
    "학교": "**초 ㅁㅁ중 ㅇㅇ고",
    "비밀번호": "1234",
    "시/도": "**시",
    "학교급": "유치원"
}
sido = {
    "서울특별시": "01",
    "부산광역시": "02",
    "대구광역시": "03",
    "인천광역시": "04",
    "광주광역시": "05",
    "대전광역시": "06",
    "울산광역시": "07",
    "세종특별자치시": "08",
    "경기도": "10",
    "강원도": "11",
    "충청북도": "12",
    "충청남도": "13",
    "전라북도": "14",
    "전라남도": "15",
    "경상북도": "16",
    "경상남도": "17",
    "제주특별자치도": "18"
}
crseScCode = {
    "유치원": "1",
    "초등학교": "2",
    "중학교": "3",
    "고등학교": "4",
    "특수학교 등": "5"
}

if data["시/도"] not in sido.keys():
    print("'", data["시/도"], "'은(는) 잘못된 시/도명입니다.", sep="")
    exit()
else:
    data["시/도"] = sido[data["시/도"]]

if data["학교급"] not in crseScCode.keys():
    print("'", data["학교급"], "'은(는) 잘못된 학교급입니다.", sep="")
    exit()
else:
    data["학교급"] = crseScCode[data["학교급"]]



import selenium.webdriver, time, logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


driver = selenium.webdriver.Chrome("chromedriver.exe")
def clickByQuery(query):
    driver.find_element_by_css_selector(query).click()

try:
    driver.get("https://hcs.eduro.go.kr")
    driver.implicitly_wait(1000)
    driver.find_element_by_id("btnConfirm2").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_id("schul_name_input").click()
    driver.implicitly_wait(1000)
    select1 = Select(driver.find_element_by_id('sidolabel'))
    select1.select_by_value('10')
    select2 = Select(driver.find_element_by_id('crseScCode'))
    select2.select_by_value('3')
    driver.find_element_by_id("orgname").send_keys(data["학교"])
    clickByQuery('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button')
    clickByQuery("#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a:nth-child(1)")
    clickByQuery("#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input")
    driver.find_element_by_id("user_name_input").send_keys(data["이름"])
    driver.find_element_by_id("birthday_input").send_keys(data["생년월일"])
    clickByQuery("#WriteInfoForm > table > tbody > tr:nth-child(4) > td > div > button")
    clickByQuery("a[aria-label='" + data["비밀번호"][0] + "']")
    clickByQuery("a[aria-label='" + data["비밀번호"][1] + "']")
    clickByQuery("a[aria-label='" + data["비밀번호"][2] + "']")
    clickByQuery("a[aria-label='" + data["비밀번호"][3] + "']")
    clickByQuery("#btnConfirm")
    time.sleep(1)
    clickByQuery("#container > div > section.memberWrap > div:nth-child(2) > ul > li:nth-child(1) > a")
    driver.implicitly_wait(1000)
    clickByQuery("#survey_q1a1")
    clickByQuery("#survey_q2a3")
    clickByQuery("#survey_q3a1")
    clickByQuery("#btnConfirm")
except selenium.common.exceptions.UnexpectedAlertPresentException as e:
    print("오류 발생 : ", str(e.alert_text).replace("\n", " "))
    driver.quit()
    exit()
except Exception as e:
    print("예상치 못한 오류 발생 : ", e.msg)
    driver.quit()
    exit()