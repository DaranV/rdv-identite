from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BotId:

    browser = webdriver.Chrome(ChromeDriverManager().install())

    url = "https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointmentsearch&view=search&category=titres"
    text = "Aucun rendez-vous n'est actuellement disponible."

    while True:
        browser.get(url)
        if text in browser.page_source:
            sleep(1)
            print("recherche en cours ...")
        else:
            print("----------------- TROUVE ------------------")
            browser.execute_script("window.open('http://soundbible.com/mp3/analog-watch-alarm_daniel-simion.mp3', '_blank')")
            break;
    print("Réserve vite !")