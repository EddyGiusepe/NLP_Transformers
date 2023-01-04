# Python Web Scraping Tutorial – Como extrair dados de qualquer site com Python

A raspagem da Web é o processo de extração automática de dados específicos da Internet. Tem muitos casos de uso, como obter dados para um projeto de aprendizado de máquina, criar uma ferramenta de comparação de preços ou qualquer outra ideia inovadora que exija uma quantidade imensa de dados.

Embora você possa teoricamente fazer a extração de dados manualmente, o vasto conteúdo da Internet torna essa abordagem irreal em muitos casos. Portanto, saber como construir um `web scraper` pode ser útil.

O objetivo deste artigo é ensiná-lo a criar um web scraper em Python. Você aprenderá como inspecionar um site para se preparar para a raspagem, extrair dados específicos usando o BeautifulSoup, aguardar a renderização do JavaScript usando o Selenium e salvar tudo em um novo arquivo `JSON` ou `CSV`.

<font color="red">De um modo geral, você deve sempre ler os termos e condições de um site antes de raspar para se certificar de que não está indo contra suas políticas. Se você não tiver certeza de como proceder, entre em contato com o proprietário do site e peça seu consentimento.</font>


Para esta tarefa precisamos ter o `Python` instalado. Além disso, para nosso `web scraper`, usaremos os pacotes `Python BeautifulSoup` (para selecionar dados específicos) e `Selenium` (para renderizar conteúdo carregado dinamicamente). Para instalá-los, basta executar estes comandos:
 
```
pip3 install beautifulsoup4

```
e
```
pip3 install selenium
```

# Como inspecionar a página

Você deve escolher o site que deseja scrape (raspar) com base em suas necessidades. Lembre-se de que cada site estrutura seu conteúdo de maneira diferente; portanto, você precisará ajustar o que aprender aqui quando começar a `raspar` por conta própria. Cada site exigirá pequenas alterações no código.

Para este script, decidi coletar informações sobre os dez primeiros filmes da lista dos $250$ melhores filmes do `IMDb`:

```
https://www.imdb.com/chart/top/
```

Primeiro, vamos pegar os títulos, depois vamos nos aprofundar extraindo informações da página de cada filme. Alguns dos dados exigirão `renderização de JavaScript`.

Para começar a entender a estrutura do conteúdo, você deve clicar com o botão direito do mouse no primeiro título da lista e escolher `“Inspecionar”`.


Ao pressionar `CTRL+F` e pesquisar na estrutura do código `HTML`, você verá que existe apenas uma tag `<table>` na página. Isso é útil, pois nos fornece informações sobre como podemos acessar aos dados.


Um seletor `HTML` que nos dará todos os títulos da página é `table tbody tr td.titleColumn a`. Isso porque todos os títulos estão em uma âncora dentro de uma célula da tabela com a classe `“titleColumn”`.


Usar o seletor de `CSS` e obter o `innerText` de cada âncora nos dará os títulos de que precisamos. Você pode simular isso no console do navegador a partir da nova janela que acabou de abrir e usando a linha `JavaScript`:

```
document.querySelectorAll("table tbody tr td.titleColumn a")[0].innerText
```


# Como usar o BeautifulSoup para extrair conteúdo carregado estaticamente

Os títulos de filmes da nossa lista são <font color="orange">conteúdo estático</font>. Isso porque, se você olhar a fonte da página (`CTRL + U` na página ou clicar com o botão direito do mouse e escolher Exibir fonte da página), verá que os títulos já estão lá.

<font color="orange">O conteúdo estático</font> geralmente é mais fácil de extrair, `pois não requer renderização de JavaScript`. Para extrair os dez primeiros títulos da lista, usaremos o `BeautifulSoup` para obter o conteúdo e depois imprimi-lo na saída do nosso scraper (raspador).


# Como extrair conteúdo carregado dinamicamente

Com o avanço da tecnologia, `os sites começaram a carregar seu conteúdo dinamicamente`. Isso melhora o desempenho da página, a experiência do usuário e até remove uma barreira extra para os scrapers (raspadores).

Isso complica as coisas, pois o `HTML` recuperado de uma solicitação simples não conterá o conteúdo dinâmico. `Felizmente`, com o `Selenium`, podemos simular uma requisição no navegador e aguardar a exibição do <font color="red">conteúdo dinâmico</font>.


# Como usar o Selenium para solicitações

Você precisará saber a localização do seu `chromedriver`. O código a seguir é idêntico ao apresentado no segundo passo, mas desta vez estamos utilizando o `Selenium` para fazer a requisição. Ainda vamos analisar o conteúdo da página usando `BeautifulSoup`, como fizemos antes.

Siga o seguinte vídeo do YouTube para instalar o [chromedriver](https://www.youtube.com/watch?v=Ot10qzrb13c).


Não se esqueça de substituir `“SEU-CAMINHO-PARA-O-CHROMEDRIVER”` pelo local onde você extraiu o `chromedriver`. Além disso, você deve observar que ao invés de `page.content`, quando estamos criando o objeto `BeautifulSoup`, agora estamos usando `driver.page_source`, que fornece o conteúdo `HTML` da página.


# Como extrair conteúdo carregado estaticamente usando o Selenium

Usando o código acima, agora podemos acessar cada página de filme chamando o método click em cada uma das âncoras.

```
first_link = driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
first_link.click()
```

Isso simulará um clique no link do primeiro filme. No entanto, neste caso, recomendo que você continue usando `driver.get instead`. Isso ocorre porque você não poderá mais usar o método `click()` depois de acessar uma página diferente, pois a nova página não possui links para os outros nove filmes.


# Como extrair conteúdo carregado dinamicamente usando o Selenium

O próximo grande passo no `web scraping` é extrair o conteúdo que é `carregado dinamicamente`. Você pode encontrar esse conteúdo em cada uma das páginas do filme (como https://www.imdb.com/title/tt0111161/ ) na seção Listas editoriais.


Se você olhar usando `inspect` na página, verá que pode encontrar a seção como um elemento com o atributo `data-testid` definido como `firstListCardGroup-editorial`. Mas se você procurar na fonte da página, não encontrará esse valor de atributo em nenhum lugar. Isso ocorre porque a seção `Listas Editoriais` é carregada pelo `IMDB dinamicamente`.

No exemplo a seguir, vamos raspar a lista editorial de cada filme e adicioná-la aos nossos resultados atuais do total de informações raspadas.

Para isso, vamos importar mais alguns pacotes que permitem aguardar o carregamento do nosso conteúdo dinâmico.


# Como salvar o conteúdo copiado

Agora que temos todos os dados que queremos, podemos salvá-los como um arquivo `.json` ou `.csv` para facilitar a leitura.

Para fazer isso, vamos apenas usar os pacotes `JSON` e `CVS` do `Python` e gravar nosso conteúdo em novos arquivos.