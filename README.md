# Projeto IOT C115
 
Simulador de Sensor de Glicose - Projeto em Python
Este projeto é um simulador de sensor de glicose desenvolvido em Python. Ele simula medições contínuas de glicose e permite interação dinâmica para ajustar valores, como aumento devido à alimentação ou redução por insulina, publicando os dados em tempo real via protocolo MQTT.

Funcionalidades
1. Modo Automático
O sistema publica valores de glicose gerados aleatoriamente (entre 70 e 180 mg/dL).
Publicações acontecem a cada 5 segundos.
Ideal para monitoramento contínuo sem intervenção manual.
2. Modo Interativo
O usuário controla o sistema:
Comer: Simula aumento da glicose proporcional aos carboidratos ingeridos.
Injetar Insulina: Simula redução da glicose proporcional à dose de insulina.
Monitorar: Publica o valor atual sem alterações.
Encerrar: Finaliza a simulação.
Após cada ação, o sistema publica os dados em intervalos rápidos (1 segundo) para capturar mudanças dinâmicas.
Arquitetura do Sistema


1. Protocolo MQTT
Utiliza a biblioteca Paho MQTT para comunicação com um broker MQTT.
Publicações são feitas no tópico:
sensor/glicose

2. Simulação de Glicose
A glicose inicial é configurada pelo usuário ou gerada aleatoriamente.
Alterações dinâmicas baseadas em:
Quantidade de carboidratos ingerida.
Dose de insulina aplicada.

4. Publicação de Dados
Dados publicados em formato JSON:
json
