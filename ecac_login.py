import logging
import datetime
import random
import time
from seleniumbase import SB

# Configuração do log
logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    
    url_esocial = "https://cav.receita.fazenda.gov.br/autenticacao/login"

    with SB(uc=True) as sb:
        sb.open(url_esocial)
        
        # Esperar e clicar no botão de login do Gov BR
        sb.wait_for_element("input[alt='Acesso Gov BR']", timeout=30)
        sb.click("input[alt='Acesso Gov BR']")
        
        # Esperar e clicar no certificado de login
        sb.wait_for_element("#login-certificate", timeout=30)
        sb.click("#login-certificate")
        
        # Usando AutoSelectCertificateForUrls src="https://gist.github.com/PaulaM96/625b791dea44bde465712b9c46e1a175.js"

        # Esperar pelo estado completo e adicionar pausas
        sb.wait_for_ready_state_complete(timeout=40)
        time.sleep(random.uniform(4, 6))  # Pausa aleatória entre 4 e 6 segundos
        
        # Esperar e clicar no botão "Declarações e Demonstrativos"
        sb.wait_for_element("#btn214", timeout=30)
        sb.hover("#btn214")  # Simular movimento do mouse
        time.sleep(random.uniform(1, 3))  # Pausa aleatória entre 1 e 3 segundos
        sb.click("#btn214")
        
        time.sleep(random.uniform(2, 4))  # Pausa aleatória entre 2 e 4 segundos
        
        # Esperar e clicar no link "Assinar e Transmitir DCTFWeb"
        sb.wait_for_element("li.showTooltip a[href*='Aplicacao.aspx?id=10015&origem=menu']", timeout=30)
        sb.hover("li.showTooltip a[href*='Aplicacao.aspx?id=10015&origem=menu']")  # Simular movimento do mouse
        time.sleep(random.uniform(1, 3))  # Pausa aleatória entre 1 e 3 segundos
        sb.click("li.showTooltip a[href*='Aplicacao.aspx?id=10015&origem=menu']")
        
        time.sleep(random.uniform(2, 4))  # Pausa aleatória entre 2 e 4 segundos

if __name__ == "__main__":
    main()
