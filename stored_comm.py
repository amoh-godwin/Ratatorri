"""
from misc import rand_num
>>> import tb_sel
>>> import model
>>> all_other = select_all_others()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'select_all_others' is not defined
>>> all_other = model.select_all_others()
>>> u_nons = model.select_none_others()
>>> nums = rand_num(6)
>>> other = all_other[nums[0]]
>>> u = u_nons[1]
>>> bow = tb_sel.loggin(u[0], u[1])
>>> bow
<tbselenium.tbdriver.TorBrowserDriver (session="ca83b10a-8d0c-4ca9-b32a-56476944bab9")>
>>> bow.load_url(other[0], wait_on_page=5, wait_for_page_body=True)
>>> el = bow.find_element_by_class_name("styles--btn--express-checkout--28jN4")
>>> el.text
''
>>> el
<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="ca83b10a-8d0c-4ca9-b32a-56476944bab9", element="a1f4d595-be9f-4d39-a4e5-c4f1731e49ef")>
>>> el.text
''
>>> el.click()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: Element <button class="udlite-btn udlite-btn-large udlite-btn-primary udlite-heading-md styles--btn--express-checkout--28jN4" type="button"> could not be scrolled into view

>>> bow.execute_script("window.scrollTo(0,100)")
>>> el.click()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Ampofo\anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: Element <button class="udlite-btn udlite-btn-large udlite-btn-primary udlite-heading-md styles--btn--express-checkout--28jN4" type="button"> could not be scrolled into view

>>> el.click()
>>> s_el = bow.find_element_by_id('billingAddressCountry')
>>> s_el.selectedIndex
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FirefoxWebElement' object has no attribute 'selectedIndex'
>>> s_el.text
'Please select...\nAfghanistan\nÅland Islands\nAlbania\nAlgeria\nAmerican Samoa\nAndorra\nAngola\nAnguilla\nAntarctica\nAntigua and Barbuda\nArgentina\nArmenia\nAruba\nAustralia\nAustria\nAzerbaijan\nBahamas\nBahrain\nBangladesh\nBarbados\nBelarus\nBelgium\nBelize\nBenin\nBermuda\nBhutan\nBolivia\nBonaire\nBosnia and Herzegovina\nBotswana\nBouvet Island\nBrazil\nBritish Indian Ocean Terrritory\nBritish Virgin Islands\nBrunei\nBulgaria\nBurkina Faso\nBurundi\nCambodia\nCameroon\nCanada\nCape Verde\nCayman Islands\nCentral African Republic\nChad\nChile\nChina\nChristmas Island\nCocos [Keeling] Islands\nColombia\nComoros\nCongo\nCook Islands\nCosta Rica\nCroatia\nCuraçao\nCyprus\nCzech Republic\nDemocratic Republic of the Congo\nDenmark\nDjibouti\nDominica\nDominican Republic\nEast Timor\nEcuador\nEgypt\nEl Salvador\nEquatorial Guinea\nEritrea\nEstonia\nEthiopia\nFalkland Islands [Islas Malvinas]\nFaroe Islands\nFiji\nFinland\nFrance\nFrench Guiana\nFrench Polynesia\nFrench Southern Territories\nGabon\nGambia\nGeorgia\nGermany\nGhana\nGibraltar\nGreece\nGreenland\nGrenada\nGuadeloupe\nGuam\nGuatemala\nGuernsey\nGuinea\nGuinea-Bissau\nGuyana\nHaiti\nHeard Island and McDonald Islands\nHonduras\nHong Kong\nHungary\nIceland\nIndonesia\nIraq\nIreland\nIsle of Man\nIsrael\nItaly\nIvory Coast\nJamaica\nJapan\nJersey\nJordan\nKazakhstan\nKenya\nKiribati\nKosovo\nKuwait\nKyrgyzstan\nLaos\nLatvia\nLebanon\nLesotho\nLiberia\nLibya\nLiechenstein\nLithuania\nLuxembourg\nMacau\nMacedonia\nMadagascar\nMalawi\nMalaysia\nMaldives\nMali\nMalta\nMarshall Islands\nMartinique\nMauritania\nMauritius\nMayotte\nMexico\nMicronesia\nMoldova\nMonaco\nMongolia\nMontenegro\nMontserrat\nMorocco\nMozambique\nMyanmar [Burma]\nNamibia\nNauru\nNepal\nNetherlands\nNew Caledonia\nNew Zealand\nNicaragua\nNiger\nNigeria\nNiue\nNorfolk Island\nNorth Mariana Island\nNorway\nOman\nPakistan\nPalau\nPalestinian Territory\nPanama\nPapua New Guinea\nParaguay\nPeru\nPhilippines\nPitcairn Islands\nPoland\nPortugal\nPuerto Rico\nQatar\nRéunion\nRomania\nRussia\nRwanda\nSaint Barthélemy\nSaint Helena\nSaint Kitts and Nevis\nSaint Lucia\nSaint Martin\nSaint Pierre and Miquelon\nSaint Vincent and the Grenadines\nSamoa\nSan Marino\nSão Tomé and Príncipe\nSaudi Arabia\nSenegal\nSerbia\nSeychelles\nSierra Leone\nSingapore\nSint Maarten\nSlovakia\nSlovenia\nSolomon Islands\nSomalia\nSouth Africa\nSouth Georgia and the South Sandwich Islands\nSouth Korea\nSouth Sudan\nSpain\nSri Lanka\nSuriname\nSvalbard and Jan Mayen\nSwaziland\nSweden\nSwitzerland\nTaiwan\nTajikistan\nTanzania\nThailand\nTogo\nTokelau\nTonga\nTrinidad and Tobago\nTunisia\nTurkey\nTurkmenistan\nTurks and Caicos Islands\nTuvalu\nU.S. Outlying Islands\nU.S. Virgin Islands\nUganda\nUkraine\nUnited Arab Emirates\nUnited Kingdom\nUnited States\nUruguay\nUzbekistan\nVanuatu\nVatican City\nVenezuela\nVietnam\nWallis and Futuna\nWestern Sahara\nYemen\nZambia\nZimbabwe'
>>> s_el.value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FirefoxWebElement' object has no attribute 'value'
>>> s_el.index
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FirefoxWebElement' object has no attribute 'index'
>>> s_el.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FirefoxWebElement' object has no attribute 'name'
>>> bow.execute_script("var x = document.getElementById('billingAddressCountry').selectedIndex;console.log(x)")
>>> bow.execute_script("var x = document.getElementById('billingAddressCountry').selectedIndex = '213'")
>>> subs= bow.find_elements_by_class_name("btn-lg")
>>> subs[1].text
'Enroll now'
>>> subs[1].click()
>>> s_el = bow.find_element_by_id("billingAddressCountry")
>>> s_el.click()
>>> s_el.click()
>>> opt = bow.find_elements_by_tag_name("option")
>>> opt[232].click()
>>> subs[1].click()
"""