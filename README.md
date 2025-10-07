# Bot Comparador de Preços

Este projeto é um bot de automação web desenvolvido em Python que compara preços de produtos em diferentes sites de e-commerce. O script automatiza a navegação, busca por um termo específico e extrai os dados mais relevantes dos primeiros resultados encontrados.

---

## Funcionalidades

- **Busca Automatizada:** O bot navega até os sites de e-commerce, localiza a barra de pesquisa e insere o termo desejado.
- **Extração de Múltiplos Dados:** Utiliza Selenium para extrair título, preço e link dos 5 primeiros resultados da busca.
- **Estruturação dos Dados:** As informações coletadas são armazenadas de forma organizada (lista de dicionários) para facilitar a visualização e o processamento posterior.
- **Execução Robusta:** Implementa esperas explícitas (`WebDriverWait`) para lidar com o carregamento dinâmico das páginas, tornando a extração mais confiável.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Selenium:** Para a automação e controle do navegador web.