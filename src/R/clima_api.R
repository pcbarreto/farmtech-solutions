library(jsonlite)

# Exemplo: São Paulo/SP
latitude <- -23.55
longitude <- -46.63

url <- paste0(
  "https://api.open-meteo.com/v1/forecast",
  "?latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
  "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum",
  "&timezone=auto",
  "&forecast_days=1"
)

dados <- fromJSON(url)

cat("============================\n")
cat("DADOS CLIMÁTICOS DA FAZENDA\n")
cat("============================\n\n")

cat(sprintf("Latitude: %s\n", dados$latitude))
cat(sprintf("Longitude: %s\n", dados$longitude))
cat(sprintf("Fuso horário: %s\n\n", dados$timezone))

cat("Condições atuais:\n")
cat(sprintf("  Temperatura: %s %s\n", dados$current$temperature_2m, dados$current_units$temperature_2m))
cat(sprintf("  Umidade relativa: %s %s\n", dados$current$relative_humidity_2m, dados$current_units$relative_humidity_2m))
cat(sprintf("  Velocidade do vento: %s %s\n", dados$current$wind_speed_10m, dados$current_units$wind_speed_10m))
cat(sprintf("  Precipitação: %s %s\n\n", dados$current$precipitation, dados$current_units$precipitation))

cat("Previsão diária:\n")
cat(sprintf("  Data: %s\n", dados$daily$time[1]))
cat(sprintf("  Temperatura máxima: %s %s\n", dados$daily$temperature_2m_max[1], dados$daily_units$temperature_2m_max))
cat(sprintf("  Temperatura mínima: %s %s\n", dados$daily$temperature_2m_min[1], dados$daily_units$temperature_2m_min))
cat(sprintf("  Chuva acumulada: %s %s\n", dados$daily$precipitation_sum[1], dados$daily_units$precipitation_sum))
