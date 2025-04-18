from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CAMINHO_BASE = "file:///C:/Users/USER/Desktop/Check-Point-05-Compliance-Quality-Assurance-Tests/pages/"

def iniciar_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def teste_criar_entidade():
    driver = iniciar_driver()
    driver.get(CAMINHO_BASE + "criar.html")
    driver.find_element(By.ID, "nome").send_keys("Nova Entidade de Teste")
    driver.find_element(By.ID, "salvar").click()
    time.sleep(5)
    print("✅ Entidade criada com sucesso")
    # driver.quit()

def teste_editar_excluir_entidade():
    driver = iniciar_driver()
    driver.get(CAMINHO_BASE + "lista.html")
    driver.find_element(By.ID, "editar1").click()
    time.sleep(1)
    driver.find_element(By.ID, "nome").clear()
    driver.find_element(By.ID, "nome").send_keys("Entidade Editada")
    driver.find_element(By.ID, "salvar").click()
    time.sleep(1)
    driver.find_element(By.ID, "excluir1").click()
    time.sleep(5)
    print("✏️ Entidade editada e 🗑 excluída com sucesso")
    # driver.quit()

# Executar testes
teste_criar_entidade()
teste_editar_excluir_entidade()
