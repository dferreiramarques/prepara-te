# Prepara-te (PWA)

Site de cartões de revisão, organizado por ano e por disciplina. O
utilizador escolhe o ano que frequentou, depois escolhe "Geral" (todas
as disciplinas desse ano) ou uma disciplina específica, e entra no ecrã
de estudo (cartão com pergunta, resposta e explicação).

O 5º ano está completo, com as 5 disciplinas do 2º ciclo (541 cartões no
total):

- **Matemática** (131 cartões) — 4 domínios: Números, Geometria e Medida,
  Álgebra, Dados e Probabilidade.
- **Português** (120 cartões) — 5 domínios: Oralidade, Leitura, Educação
  Literária, Escrita e Gramática — com maior peso em Gramática e Educação
  Literária.
- **Ciências Naturais** (100 cartões) — 3 domínios: A água, o ar, as
  rochas e o solo – materiais terrestres; Diversidade de seres vivos e
  suas interações com o meio; Unidade na diversidade de seres vivos.
- **História e Geografia de Portugal** (100 cartões) — 4 domínios: A
  Península Ibérica – localização e quadro natural; Península Ibérica:
  dos primeiros povos à formação de Portugal; Portugal do século XIII a
  1385; Portugal do século XV ao século XVII.
- **Inglês** (90 cartões, nível A1.1/A1.2) — 3 domínios: Vocabulário,
  Gramática Inglesa, Cultura e Países Anglófonos. O domínio chama-se
  "Gramática Inglesa" (e não só "Gramática") para não colidir com o
  domínio homónimo de Português no modo "Geral".

O 6º ano já aparece no seletor, mas marcado como "brevemente" até ter
cartões.

## Como publicar

É um site estático puro (HTML/CSS/JS, sem build step, com ES modules).
Basta fazer upload da pasta completa para o mesmo tipo de alojamento que
usaste no microbit.monco.io (ex: subdomínio `preparate.monco.io`,
Netlify, Vercel, GitHub Pages, etc.) — mantendo a estrutura de pastas tal
como está.

Para testar localmente:
```
python3 -m http.server 8000
```
e abrir `http://localhost:8000`. (Tem de ser servido por http(s), não
aberto como `file://`, porque o service worker, os ES modules e o
`fetch` do JSON exigem uma origem http.)

## Estrutura

- `index.html`, `style.css` — a casca da app (cabeçalho + área onde os
  ecrãs são desenhados).
- `js/app.js` — arranque: carrega o catálogo, liga o router e o service
  worker.
- `js/router.js` — lê o hash do URL (`#/`, `#/ano/5`, `#/ano/5/matematica`)
  e decide que ecrã mostrar.
- `js/views/year-select.js`, `js/views/subject-select.js` — os dois ecrãs
  de escolha (ano, depois geral/disciplina).
- `js/study.js` — o ecrã de cartões (a lógica que antes estava toda em
  `app.js`), agora a carregar o(s) baralho(s) certos consoante o
  ano/disciplina escolhidos.
- `js/catalog.js` — lê `data/catalog.json` e sabe que anos/disciplinas
  estão disponíveis.
- `js/progress.js` — guarda o progresso no `localStorage`, um registo por
  combinação ano+disciplina.
- `manifest.json`, `sw.js`, `icons/` — o que torna isto instalável e
  funcional offline (PWA).
- `data/catalog.json` — a lista de anos, disciplinas e que baralhos
  (ficheiros `.json`) já existem.
- `data/<ano>/<disciplina>.json` — os cartões de cada baralho
  (pergunta/resposta/explicação/domínio/tópico/dificuldade). Hoje existem
  os 5 baralhos do 5º ano: `matematica.json`, `portugues.json`,
  `ciencias-naturais.json`, `hgp.json` e `ingles.json`.
- `build/generate_data.py` — o script que gerou `data/5/matematica.json`.
  Para acrescentar cartões a Matemática do 5º ano, edita este script e
  corre `python3 generate_data.py` a partir da pasta `build/` (grava
  diretamente em `../data/5/matematica.json`). Os restantes baralhos
  foram escritos diretamente em JSON, sem script gerador.
- `build/make_icons.py` — gera os ícones da PWA.

## Como acrescentar um ano ou disciplina novos

1. Cria o ficheiro `data/<ano>/<disciplina>.json` com a mesma forma dos
   cartões existentes (`{"cards": [{id, domain, topic, question, answer,
   explanation, difficulty}, …]}`).
2. Acrescenta uma linha em `data/catalog.json`, dentro de `"decks"`:
   `{ "year": "6", "subject": "portugues", "file": "data/6/portugues.json" }`.
3. Se for um ano ou disciplina que ainda não existe em `catalog.json`,
   acrescenta-o também às listas `"years"` / `"subjects"`.

Não é preciso mudar nenhum código — o tile deixa de aparecer
"brevemente" assim que o deck existe no catálogo.

## Notas sobre o conteúdo

Os cartões são originais, escritos/calculados de raiz com base nas
Aprendizagens Essenciais oficiais do DGE — não são cópias de perguntas de
provas de aferição/exame, que são material protegido. Vale sempre a pena
rever o conteúdo com o teu conhecimento do programa antes de dar aos
alunos, especialmente os cartões marcados como "dificil".

## Progresso

O progresso (cartões já vistos, se sabias ou não, sequência de acertos) é
guardado no `localStorage` do dispositivo, um registo separado por cada
combinação ano+disciplina (e outro para "Geral") — não há conta nem
servidor. Cada telemóvel/browser tem o seu próprio progresso. Quem já
tinha progresso da versão anterior (só 5º ano Matemática) não o perde: é
migrado automaticamente para o novo formato na primeira visita.

## Próximos passos possíveis

- Acrescentar o 6º ano (as 5 disciplinas do 5º ano já estão completas),
  reutilizando a mesma estrutura de dados.
- Mais tarde, alargar ao ensino secundário.
- Ecrã de estatísticas por domínio.
- Modo "exame" com temporizador.
