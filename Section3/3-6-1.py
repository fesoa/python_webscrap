import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class ncafeWriteAtt:
    # Init(Setting Webdriver)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #for Cli
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="c:/Webdriver/chromedriver")
        self.driver.implicitly_wait(5) #login기다림

    # Login & Check
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('bboming9')
        self.driver.find_element_by_name('pw').send_keys('j5j7h28!@')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/rowingkorea?iframe_url=/AttendanceView.nhn%3Fsearch.clubid=27187553%26search.menuid=10')
        # iframe 화면으로 변환
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_elemnet_b_id('cmtinput').send_keys('출 석 체 크.')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        #self.driver.close() # 현재 포커스된 영역 종료
        self.driver.quit() # Selenium 전체 종료
        print('removed driver')

# 실행 영역
if __name__ == '__main__':
    # 객체 생성
    a = ncafeWriteAtt()
    # 시작 시간
    start_time = time.time()
    # 프로그램 실행
    a.writeAttendCheck()
    # 종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    # 객체 소멸
    del a
