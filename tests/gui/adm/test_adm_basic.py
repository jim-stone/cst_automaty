from .pages.adm_landing import AdmLandingPage


def test_can_see_dictionaries(logged_adm, chrome_browser):
    adm_page = AdmLandingPage(chrome_browser)
    names = adm_page.navigate_to_dictionaries().get_dict_names()
    assert len(names) == 62
    assert names[0] == 'Cel polityki'
    assert names[-1] == 'Zakres interwencji'
