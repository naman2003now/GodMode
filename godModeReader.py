from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.implicitly_wait(10)
driver.get('https://app.erudex.com/login/index.html')
time.sleep(1)
driver.find_element_by_name('username').send_keys('nine.9103')
driver.find_element_by_name('password').send_keys('NineEdu1998')
driver.find_element_by_name('login').click()
questionID = open('questionID.txt', 'w+')
answerText = open('answers.txt', 'w+')
input()
x = 90
for i in range(x):
    print((i+1)/x)
    Question= driver.find_element_by_xpath('//*[@id="qwn-'+str(i+1)+'"]/tbody/tr[1]/td')
    id = False
    QID = ''
    for char in Question.get_attribute('innerHTML'):
        if char == '(':
            id = True
        if id:
            QID += char
    questionID.write(QID + '\n')
    for h in range(3, 7):
        try:
            option = driver.find_element_by_xpath('//*[@id="qwn-'+str(i+1)+'"]/tbody/tr[' + str(h) + ']')
            if option.get_attribute('class')[-1] == 't':
                answerText.write(str(h-2) + '\n')
        except IndexError:
            numeric = driver.find_element_by_xpath(f'/html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[{i + 5}]/table/tbody/tr[3]/td/div/label[2]').get_attribute("innerHTML")
            ins = False
            for char in numeric:
                if ins and char != " ":
                    numericAns += char
                if char == ":":
                    ins = True
                    numericAns = ""
            answerText.write(str(numericAns) + "\n")
            break
# //*[@id="qwn-1"]/tbody/tr[1]/td
# //*[@id="qwn-1"]/tbody/tr[5]
# /html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[90]/table/tbody/tr[3]/td/div/label[2]
#/html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[89]/table/tbody/tr[3]/td/div/label[2]
# /html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[88]/table/tbody/tr[3]/td/div/label[2]

#/html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[57]/table/tbody/tr[3]/td/div/label[2]
#/html/body/div[4]/div[2]/div[2]/div/div[5]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[25]/table/tbody/tr[3]/td/div/label[2]
