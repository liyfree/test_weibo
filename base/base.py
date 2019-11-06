class BasePage:
    """基础page层"""

    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def open_page(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    # id定位
    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    # name定位
    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    # class定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # xpath等位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # css定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    # 获取title
    def get_title(self):
        return self.driver.title
    def get_url(self):
        return self.driver.current_url

    # 获取页面文本，使用xpath
    def get_text(self, xpath):
        return self.by_xpath(xpath).text
    # 执行js脚本
    def js(self,script):
        self.driver.execute_script(script)



