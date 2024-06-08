from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ...utils import AbstractBasePage


class AdmLandingPage(AbstractBasePage):
    header = (By.CSS_SELECTOR, 'h1')
    dictionaries_link = (By.CSS_SELECTOR, '#dictionary')
    labels = (By.CSS_SELECTOR, 'label[data-v-0f1f0c22][tabindex="0"]')


    def navigate_to_dictionaries(self):
        self.wait.until(EC.visibility_of_element_located(self.dictionaries_link))
        element = self.browser.find_element(*self.dictionaries_link)
        element.click()
        return self

    def get_dict_names(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.labels))
        elements = self.browser.find_elements(*self.labels)
        all_names = [e.get_attribute('textContent') for e in elements]
        dict_names = [n.strip() for n in all_names if all_names.index(n) % 4 == 0]
        return dict_names