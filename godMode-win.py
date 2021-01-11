from selenium import webdriver
import keyboard
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get("https://app.erudex.com/login/index.html")
driver.implicitly_wait(10)
time.sleep(1)

QID = []
options = []

questionID = open('questionID.txt', 'r')
answerText = open('answers.txt', 'r')

for line in questionID:
    QID.append(line)
for line in answerText:
    options.append(line)


input()
for i in range(90):
    id = False
    QIDcurrent = ""
    currentQuestion = driver.find_element_by_css_selector("body > div.row.fill-height-topbar.main-content-row.block-ui-main.ng-scope.block-ui.block-ui-anim-fade > div.main-content-wrapper.full > div.main-content-view.ng-scope > div > div:nth-child(3) > span.left.ng-binding").get_attribute("innerHTML")
    print(currentQuestion)
    for char in currentQuestion:
        if char == '(':
            id = True
        if id:
            QIDcurrent += char
        if char == ')':
            id = False
    for checkNo in range(len(QID)):
        if QID[checkNo] == QIDcurrent + '\n':
            print(options[checkNo])
            body = driver.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN)
            try:
                driver.find_element_by_xpath('//*[@id="mCSB_7_container"]/div[2]/div[{}]/label'.format(str(int(options[checkNo]) + 4))).click()
            except:
                box = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div[6]/div/div[1]/div[1]/div[1]/div/div[5]/div/div[2]/input")
                box.click()
                box.send_keys(options[checkNo])
            driver.find_element_by_css_selector("body > div.row.fill-height-topbar.main-content-row.block-ui-main.ng-scope.block-ui.block-ui-anim-fade > div.main-content-wrapper.full > div.main-content-view.ng-scope > div > div.assessment-question-page-wrapper.competitive-test > div > div.assessment-pager-wrapper > div > div > div.quiz-panel-footer.competitive_buttons > a:nth-child(1)").click()
#//*[@id="mCSB_7_container"]/div[2]/div[6]/label
#//*[@id="mCSB_7_container"]/div[2]/div[5]/label

##
##html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths body.erudex.ng-scope div.row.fill-height-topbar.main-content-row.block-ui-main.ng-scope.block-ui.block-ui-anim-fade div.main-content-wrapper.full div.main-content-view.ng-scope div.assessment-viewer.ng-scope div.assessment-question-page-wrapper.competitive-test div.ng-scope div.column.small-12.quiz-attempt-main-wrapper div.column.small-8.height-100p.ng-isolate-scope.mCustomScrollbar._mCS_7.mCS-autoHide.mCS_no_scrollbar div#mCSB_7.mCustomScrollBox.mCS-minimal-dark.mCSB_vertical.mCSB_outside div#mCSB_7_container.mCSB_container.mCS_no_scrollbar_y div.row.collapse div.row.collapse.ng-scope div.column.small-2.end input.ng-pristine.ng-valid.ng-isolate-scope.ng-valid-maxlength.ng-touched


