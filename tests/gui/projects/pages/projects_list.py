from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ...utils import AbstractBasePage



class ProjectsListPage(AbstractBasePage):
    header = (By.CSS_SELECTOR, 'h1')
    subheader_projects_count = (By.CSS_SELECTOR, 'h2.page-subheader')

    def get_header (self):
        self.wait.until(EC.visibility_of_element_located(self.subheader_projects_count))
        h1 = self.browser.find_element(*self.header).get_attribute('innerText')
        return h1

    def get_projects_count(self):
        self.wait.until(EC.visibility_of_element_located(self.subheader_projects_count))
        h2 = self.browser.find_element(*self.subheader_projects_count).get_attribute('innerText')
        return int(h2.split(' ')[-1])
