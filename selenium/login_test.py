from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def iniciar_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def teste_login_sucesso():
    driver = iniciar_driver()
    driver.get(r"file:///C:/Users/USER/Desktop/Check-Point-05-Compliance-Quality-Assurance-Tests/pages/login.html")

    driver.find_element(By.ID, "username").send_keys("usuario123")
    driver.find_element(By.ID, "password").send_keys("senha123")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(5)  # tempo para visualizar
    print("✅ Login com sucesso")
    # driver.quit()

def teste_login_erro():
    driver = iniciar_driver()
    driver.get(r"file:///C:/Users/USER/Desktop/Check-Point-05-Compliance-Quality-Assurance-Tests/pages/login.html")

    driver.find_element(By.ID, "username").send_keys("usuario_errado")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(5)
    print("❌ Login com erro (teste negativo)")
    # driver.quit()

# Executar testes
teste_login_sucesso()
teste_login_erro()
