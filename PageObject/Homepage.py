from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def click_buytab(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()

    def select_location(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()

    def for_particular_location(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()

    def to_get_selected_location(self):
        self.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()

    def click_buytab(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()

    def select_for_particular_location(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()

    def choose_for_particular_location(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()

    def search_bar_is_shown(self):
        self.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()

    def find_agent_is_shown(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div/div[2]/div[4]/div/div/div[1]/div[2]/ul/li[3]/a").click()

    def click_buytab(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()

    def buyer_location_choices(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()

    def buyer_selected_location(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()

    def search_under_budjet(self):
        self.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[3]/div[1]").click()

    def feeding_minimum_budjet(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[2]/div[2]").click()

    def feeding_maximum_budjet(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[1]/input[2]").click()

    def fixing_the_budjet(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[3]/div[8]").click()

    def searching_under_feeded_budjet(self):
        self.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()

    def click_buytab(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()

    def rates_and_trends(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[2]/a").click()

    def click_buytab(self):
        self.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()

    def tips_and_guides(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[4]/a").click()

    def switch_to_the_window(self):
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)

    def scroll_to_middle(self):
        self.driver.execute_script("window.scrollTo(0,500,document.body.scrollHeight);")

    def choose_first_location(self):
        self.driver.find_element(By.ID, "locOne").send_keys("Chennai")

    def select_first_location(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/a").click()

    def choose_second_location(self):
        self.driver.find_element(By.ID, "locTwo").send_keys("Chennai")

    def select_second_location(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[3]/a").click()

    def click_compare_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/input").click()

    def click_buytab(self):
        self.driver.find_element(By.XPATH,"/html/body/header/section[2]/div/ul/li[1]/a").click()
    def propworth(self):
        self.driver.find_element(By.XPATH,
                            "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[1]/a").click()
