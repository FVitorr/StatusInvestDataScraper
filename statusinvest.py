from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class StatusInvestScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tratStr(self, string_, pos):
        string = string_.split()
        return string[pos]

    def adcColor(self, dado, param):
        if dado < param:
            return '\033[91m'  # Vermelho
        else:
            return '\033[92m'  # Verde

    def obter_dados_acao(self, acao):
        driver = self.driver
        url = f"https://statusinvest.com.br/acoes/{acao}"
        driver.get(url)
        dy_color = '\033[91m'

        try:
            dividend_yield_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main-2"]/div[2]/div/div[1]/div/div[4]'))
            )
            dividend_yield = dividend_yield_element.text
            vl_dividend = float(self.tratStr(dividend_yield, 9).replace(",", "."))
            dividend_yield = float(self.tratStr(dividend_yield, 3).replace(",", "."))
            dy_color = self.adcColor(round(dividend_yield), 6)
        except Exception as e:
            dividend_yield = 0

        p_l = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong'))
        )
        p_l = float(p_l.text.replace(",", "."))
        pl_color = self.adcColor(10, round(abs(p_l)))
        if p_l < 0:
            pl_color = '\033[91m'
        divida_liquida = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[2]/div').text
        try:
            divida_liquida = self.tratStr(divida_liquida, 3).replace(",", ".")
            dl_color = self.adcColor(3.5, round(float(divida_liquida)))
            if float(divida_liquida) < 0:
                dl_color = '\033[91m'
        except:
            divida_liquida = "Indefinido"
            dl_color = '\033[0m'

        margem_liquida = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div').text
        margem_liquida = self.tratStr(margem_liquida, 3).replace(",", ".").replace("%", "")
        ml_color = self.adcColor(round(float(margem_liquida)), 10)
        roe = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div').text
        roe = self.tratStr(roe, 2).replace(",", ".").replace("%", "")
        roe_color = self.adcColor(float(roe), 15)
        p_vp = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong').text
        pvp_color = self.adcColor(1.5, (float(p_vp.replace(",", "."))))

        s_atuacao = driver.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong').text

        return {
            'dy_color': dy_color,
            'Dividend Yield': dividend_yield,
            'V. Dividendo': vl_dividend,
            'pl_color': pl_color,
            'P/L': p_l,
            'dl_color': dl_color,
            'Dívida Líquida': divida_liquida,
            'ml_color': ml_color,
            'Margem Líquida': margem_liquida,
            'roe_color': roe_color,
            'ROE': roe,
            'pvp_color': pvp_color,
            'P/VP': p_vp,
            'color_reset': '\033[0m',
            'S. Atuacao': s_atuacao
        }

if __name__ == '__main__':
    scraper = StatusInvestScraper()
    acoes = ['ABEV3', 'AMAR3', 'BBAS3', 'BBDC4', 'COGN3', 'CPLE6', 'ITSA4', 'KLBN4', 'SANB4', 'SAPR4', 'TAEE4', 'TRPL4']
    
    for acao in acoes:
        dados_acao = scraper.obter_dados_acao(acao)
        
        if dados_acao is not None:
            print(f"\n\nDados da ação {acao}:")
            chave = []
            valor = []

            for chave, valor in dados_acao.items():
                if "color" not in chave:
                    print(f" |{chave.ljust(14)} |", end="")
                else:
                    print(f"{valor}", end="")

            print()
            for chave, valor in dados_acao.items():
                if "color" not in chave:
                    print(f" |{str(valor).ljust(14)} |", end="")
                else:
                    print(f"{valor}", end="")
