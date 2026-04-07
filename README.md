# FarmTech Solutions - Projeto FIAP

Projeto acadêmico para Agricultura Digital com:

- aplicação em Python com vetores, menu, loop e decisão;
- cálculo de área plantada para 2 culturas;
- cálculo de manejo de insumos;
- exportação de dados para CSV;
- script em R para média e desvio padrão;
- script em R para integração com API meteorológica pública.

## Culturas escolhidas

- **Milho** → área em **retângulo**
- **Café** → área em **círculo**

## Estrutura

```text
farmtech-solutions/
├── README.md
├── dados/
│   └── dados_farmtech.csv
├── python/
│   └── farmtech_menu.py
└── r/
    ├── estatisticas.R
    └── clima_api.R
```

## Como executar

### Python

```bash
python python/farmtech_menu.py
```

### Exportar CSV

No menu Python, use a opção `5 - Exportar dados para CSV`.

### Estatísticas em R

```bash
Rscript R/estatisticas.R
```

### API meteorológica em R

Instale o pacote necessário:

```r
install.packages("jsonlite")
```

Depois execute:

```bash
Rscript R/clima_api.R
```
