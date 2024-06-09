from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ...utils import AbstractBasePage
from tests.config import PROJECT_NUMBER


class ProjectsListPage(AbstractBasePage):
    header = (By.CSS_SELECTOR, 'h1')
    subheader_projects_count = (By.CSS_SELECTOR, 'h2.page-subheader')
    quick_search_input = (By.CSS_SELECTOR, '#input-137')
    project_bars = (By.CSS_SELECTOR, 'button.sl-panel__header div.v-toolbar__title[data-v-cb7485aa]')
    burger_button = (By.CSS_SELECTOR, '[aria-label=Menu]')
    # burger_buttons = (By.CSS_SELECTOR, 'span.v-btn__content > i[data-v-391d6f7f].v-icon')
    # burger_menu_items = (By.CSS_SELECTOR, '#list-item-232')
    project_details_link = (By.CSS_SELECTOR, 'a[href="/projects/5674/details/preview/information"]')

    def get_header(self):
        self.wait.until(EC.visibility_of_element_located(self.subheader_projects_count))
        h1 = self.browser.find_element(*self.header).get_attribute('innerText')
        return h1

    def get_projects_count(self):
        self.wait.until(EC.visibility_of_element_located(self.subheader_projects_count))
        h2 = self.browser.find_element(*self.subheader_projects_count).get_attribute('innerText')
        return int(h2.split(' ')[-1])

    def filter_to_one_project(self, project_number=PROJECT_NUMBER):
        self.wait.until(EC.visibility_of_element_located(self.quick_search_input))
        element = self.browser.find_element(*self.quick_search_input)
        element.send_keys(project_number)
        return self

    def click_burger_on_project(self):
        condition = lambda _: len(self.browser.find_elements(*self.burger_button)) == 1
        self.wait.until(condition)
        element = self.browser.find_elements(*self.burger_button)[0]
        element.click()
        return self

    def navigate_to_project_details(self):
        self.wait.until(EC.visibility_of_element_located(self.project_details_link))
        element = self.browser.find_element(*self.project_details_link)
        element.click()
        # return self
