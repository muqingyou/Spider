import time
from tkinter import Image

import cv2
import canndy_test
from selenium import webdriver
from selenium.webdriver import ActionChains

class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """
    def __init__(self):
        super(CrackSlider, self).__init__()
        # 实际地址
        self.url = 'http://3g.163.com/wap/special/newsapp_idol_personal/?starId=14#/home'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.zoom = 2

    def open(self):
        self.driver.get(self.url)

    def get_pic(self):
        time.sleep(2)
        target = browser.find_element_by_class_name("yidun_bg-img")
        template = browser.find_element_by_class_name("yidun_jigsaw")
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 320 / int(size_loc[0])


    def get_tracks(self, distance):
        print(distance)
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3 / 5
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}


    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template, 0)
        run = 1
        w, h = template.shape[::-1]
        print(w, h)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            if threshold < 0:
                print('Error')
                return None
            loc = np.where(res >= threshold)
            # print(len(loc[1]))
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2

        return loc[1][0]


    def crack_slider(self, browser):
        # self.open()
        target = 'target.jpg'
        template = 'target.jpg'
        self.get_pic()
        distance = self.match(target, template)
        zoo = 1.36  # 缩放系数，需要自己调整大小
        tracks = self.get_tracks((distance + 7) * zoo)  # 对位移的缩放计算
        # print(tracks)
        slider = browser.find_element_by_class_name("yidun_slider")
        ActionChains(browser).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.5)
        for back_tracks in tracks['back_tracks']:
            ActionChains(browser).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        ActionChains(browser).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(browser).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(browser).release().perform()
        try:
            failure = WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_tips__text'), '向右滑动滑块填充拼图'))
            print(failure)
        except:
            print('验证成功')
            return None

        if failure:
            self.crack_slider(browser)



# 新建selenium浏览器对象，后面是geckodriver.exe下载后本地路径
browser = webdriver.Chrome(executable_path='D:\pycharm-file\chromedriver_win32\chromedriver.exe')
# 网站登陆页面
browser.get('https://www.zhihu.com/signin?next=%2F')
handle = browser.current_window_handle
# 等待3s用于加载脚本文件
browser.implicitly_wait(3)
#browser.find_element_by_class_name('SignFlow-tab')[1].click()
browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
input_name = browser.find_element_by_name('username')
input_name.clear()  # 清楚文本框中的内容
input_name.send_keys('15884279122')  # 输入账号
input_pass = browser.find_element_by_name('password')
input_pass.clear()
input_pass.send_keys('7204242qingyou')  # 输入密码
# 点击登陆按钮，弹出滑动验证码
#btn = browser.find_element_by_class_name('Button SignFlow-submitButton Button--primary Button--blue')
btn = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')
btn.click()
# 获取iframe元素，切到iframe
#frame = browser.find_element_by_class_name('yidun_cover-frame')
#frame = browser.find_element_by_xpath('/html/body/div[4]/iframe')
time.sleep(5)
frame = browser.find_element_by_xpath('//iframe[@class="yidun_cover-frame"]')
browser.switch_to.frame(frame)
#time.sleep(3)
browser.switch_to.default_content();

target = browser.find_element_by_class_name("yidun_bg-img")
        template = browser.find_element_by_class_name("yidun_jigsaw")
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 320 / int(size_loc[0])
# # 获取背景图src
# #targetUrl = browser.find_element_by_class_name('yidun_bg-img').get_attribute('src')
# targetUrl = browser.find_element_by_xpath('//img[@class="yidun_bg-img"]').get_attribute('src')
# # 获取拼图src
# #tempUrl = browser.find_element_by_class_name('yidun_jigsaw').get_attribute('src')
# tempUrl = browser.find_element_by_xpath('//img[@class="yidun_jigsaw"]').get_attribute('src')
# # 新建标签页
# browser.execute_script("window.open('');")
# # 切换到新标签页
# browser.switch_to.window(browser.window_handles[1])
# # 访问背景图src
# browser.get(targetUrl)
# time.sleep(3)
# # 截图
# browser.save_screenshot('temp_target.png')
# w = 680
# h = 390
# img = cv2.imread('temp_target.png')
# size = img.shape
# top = int((size[0] - h) / 2)
# height = int(h + ((size[0] - h) / 2))
# left = int((size[1] - w) / 2)
# width = int(w + ((size[1] - w) / 2))
# cropped = img[top:height, left:width]
# # 裁剪尺寸
# cv2.imwrite('temp_target_crop.png', cropped)
# # 新建标签页
# browser.execute_script("window.open('');")
# browser.switch_to.window(browser.window_handles[2])
# browser.get(tempUrl)
# time.sleep(3)
# browser.save_screenshot('temp_temp.png')
# w = 136
# h = 136
# img = cv2.imread('temp_temp.png')
# size = img.shape
# top = int((size[0] - h) / 2)
# height = int(h + ((size[0] - h) / 2))
# left = int((size[1] - w) / 2)
# width = int(w + ((size[1] - w) / 2))
# cropped = img[top:height, left:width]
# cv2.imwrite('temp_temp_crop.png', cropped)
# browser.switch_to.window(handle)
# # 模糊匹配两张图片
# move = canndy_test.matchImg('temp_target_crop.png', 'temp_temp_crop.png')
# # 计算出拖动距离
# distance = int(move / 2 - 27.5) + 2
# draggable = browser.find_element_by_id('tcaptcha_drag_thumb')
# ActionChains(browser).click_and_hold(draggable).perform()
# # 拖动
# ActionChains(browser).move_by_offset(xoffset=distance, yoffset=0).perform()
# ActionChains(browser).release().perform()
# time.sleep(10)

# driver = webdriver.Chrome(executable_path='D:\pycharm-file\chromedriver_win32\chromedriver.exe')
# driver.get('https://passport.weibo.cn/signin/login?entry=mweibo')
# driver.implicitly_wait(5)# 延迟，为了加载元素，否则照顾到元素，出现异常
# input_name = driver.find_element(By.ID, 'loginName')
# input_name.clear()  # 清楚文本框中的内容
# input_name.send_keys('15608190701')  # 输入账号
# input_pass = driver.find_element(By.ID, 'loginPassword')
# input_pass.clear()
# input_pass.send_keys('7204242qingyou')  # 输入密码
# time.sleep(5)
# driver.find_element(By.ID, 'loginAction').click()
# print(driver.page_source)  # 查看源代码