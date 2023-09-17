# Status Invest Data Scraper

O **Status Invest Data Scraper** é um script Python que utiliza a biblioteca Selenium para extrair informações financeiras de ações listadas no site Status Invest. Ele coleta dados importantes, como Dividend Yield, P/L (Preço/Lucro), Dívida Líquida, Margem Líquida, ROE (Retorno sobre o Patrimônio Líquido) e P/VP (Preço/Valor Patrimonial) para ações específicas.

## Requisitos

Para usar este script, você precisa ter o Python instalado em sua máquina. Além disso, as seguintes bibliotecas Python são necessárias:

- Selenium
- webdriver_manager
- BeautifulSoup
- requests

Você pode instalar essas bibliotecas usando o comando `pip`:

```bash
pip install selenium webdriver_manager beautifulsoup4 requests
```

## Como Usar
Certifique-se de que todas as bibliotecas estão instaladas.

Execute o script Python status_invest_scraper.py.

O script buscará dados das ações listadas no site Status Invest. Você pode personalizar a lista de ações desejadas editando a variável acoes no código.

Os dados das ações serão exibidos no console, incluindo informações como Dividend Yield, P/L, Dívida Líquida, Margem Líquida, ROE e P/VP.

## Observações
Este script utiliza a biblioteca Selenium para automatizar a coleta de dados. Certifique-se de ter o Google Chrome instalado em sua máquina e o ChromeDriver compatível com a versão do Chrome instalada.

O script pode ser personalizado para adicionar mais ações à lista acoes ou para coletar informações adicionais do site Status Invest.

Respeite os termos de uso do site Status Invest e as políticas de acesso aos dados.

Este script é fornecido apenas como uma demonstração e pode exigir ajustes para funcionar com futuras atualizações do site Status Invest.