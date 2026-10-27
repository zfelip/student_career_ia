# Estimativa de energia e emissões

A energia computacional é estimada pela multiplicação da potência de referência pelo tempo de processamento em horas. Para o notebook testado, com Intel Core i5-7200U, foi adotada a referência de 15 W, correspondente ao TDP nominal informado pela Intel. O TDP não equivale à potência elétrica média efetivamente medida.

Energia (kWh) = 0,015 × tempo (s) / 3600.

Emissões (gCO₂) = Energia (kWh) × 45,8.

A metodologia representa um cenário estimativo do processador, não uma medição do consumo elétrico integral do notebook.

Fonte: https://www.intel.com/content/www/us/en/products/sku/95443/intel-core-i57200u-processor-3m-cache-up-to-3-10-ghz/specifications.html
