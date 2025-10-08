# Bot Comparador de Preços

Esta é uma aplicação web interativa, construída com Streamlit, que utiliza um bot de automação (Selenium) para buscar e comparar preços de produtos em tempo real. O usuário pode inserir o nome de um produto, e a aplicação controla um navegador em segundo plano para extrair e exibir os resultados de forma clara e organizada.

## Visualização

![1759932502452](image/README/1759932502452.png)

## Funcionalidades

- **Interface Web Interativa:** Uma interface amigável construída com Streamlit que permite ao usuário interagir diretamente com o bot.
- **Busca em Tempo Real:** O usuário digita o produto desejado e o bot inicia o processo de scraping no momento do clique.
- **Controle do Navegador:** Botões para iniciar e encerrar a sessão do navegador de forma explícita, permitindo múltiplas buscas sem reabrir o navegador a cada vez.
- **Visualização Clara dos Resultados:** Os dados extraídos (título, preço e link) são exibidos em uma tabela interativa e também em formato de "cards" para melhor leitura.
- **Backend com Selenium:** A automação robusta é feita com Selenium, implementando esperas explícitas (`WebDriverWait`) para lidar com o carregamento dinâmico das páginas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit:** Para a criação da interface web interativa.
- **Selenium:** Para a automação e controle do navegador web (backend).
- **Pandas:** Para a manipulação e estruturação dos dados para exibição
