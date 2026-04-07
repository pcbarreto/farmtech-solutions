# Script R para estatísticas básicas
# Execute com: Rscript R/estatisticas.R

caminho_arquivo <- file.path("../dados", "dados_farmtech.csv")

if (!file.exists(caminho_arquivo)) {
  stop("Arquivo dados/dados_farmtech.csv não encontrado. Exporte o CSV pelo programa Python primeiro.")
}

dados <- read.csv(caminho_arquivo, stringsAsFactors = FALSE)

if (nrow(dados) == 0) {
  stop("O arquivo CSV está vazio.")
}

cat("==============================\n")
cat("ESTATÍSTICAS GERAIS DO PROJETO\n")
cat("==============================\n\n")

cat(sprintf("Média da área plantada: %.2f m²\n", mean(dados$area_m2)))
cat(sprintf("Desvio padrão da área plantada: %.2f m²\n", sd(dados$area_m2)))
cat(sprintf("Média do insumo total: %.2f L\n", mean(dados$insumo_total_litros)))
cat(sprintf("Desvio padrão do insumo total: %.2f L\n\n", sd(dados$insumo_total_litros)))

cat("==================================\n")
cat("ESTATÍSTICAS SEPARADAS POR CULTURA\n")
cat("==================================\n\n")

culturas_unicas <- unique(dados$cultura)

for (cultura in culturas_unicas) {
  filtro <- dados[dados$cultura == cultura, ]

  cat(sprintf("Cultura: %s\n", cultura))
  cat(sprintf("  Média da área: %.2f m²\n", mean(filtro$area_m2)))
  if (nrow(filtro) > 1) {
    cat(sprintf("  Desvio da área: %.2f m²\n", sd(filtro$area_m2)))
    cat(sprintf("  Média do insumo: %.2f L\n", mean(filtro$insumo_total_litros)))
    cat(sprintf("  Desvio do insumo: %.2f L\n", sd(filtro$insumo_total_litros)))
  } else {
    cat("  Desvio da área: N/A (apenas 1 registro)\n")
    cat(sprintf("  Média do insumo: %.2f L\n", mean(filtro$insumo_total_litros)))
    cat("  Desvio do insumo: N/A (apenas 1 registro)\n")
  }
  cat("\n")
}
