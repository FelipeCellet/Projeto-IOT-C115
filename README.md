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
bash
Copiar código
sensor/glicose
2. Simulação de Glicose
A glicose inicial é configurada pelo usuário ou gerada aleatoriamente.
Alterações dinâmicas baseadas em:
Quantidade de carboidratos ingerida.
Dose de insulina aplicada.
3. Publicação de Dados
Dados publicados em formato JSON:
json
Copiar código
{
  "timestamp": "2024-12-03 12:00:00",
  "glucose_level": 110.5
}
Requisitos
1. Pré-requisitos
Python 3.8+
Biblioteca Paho MQTT:
bash
Copiar código
pip install paho-mqtt
2. Broker MQTT
Este projeto usa o broker público test.mosquitto.org.
Alternativamente, você pode usar seu próprio broker (local ou na nuvem).
Configuração e Execução
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/simulador-glicose.git
cd simulador-glicose
Instale as dependências:

bash
Copiar código
pip install paho-mqtt
Execute o programa:

bash
Copiar código
python simulador_glicose.py
Escolha o modo de operação:

1: Modo Automático.
2: Modo Interativo.
Fluxo de Operação
Modo Automático
O programa gera valores aleatórios de glicose.
Publica os valores em intervalos regulares de 5 segundos.
O programa pode ser interrompido com Ctrl+C.
Modo Interativo
O usuário escolhe uma ação:
Comer: Insere a quantidade de carboidratos ingerida.
Injetar Insulina: Insere a quantidade de unidades aplicadas.
Monitorar: Publica o valor atual sem alterações.
Encerrar: Finaliza o programa.
Após uma ação, o sistema publica valores frequentes (1 segundo) por 10 ciclos para simular mudanças dinâmicas.
Retorna ao intervalo padrão de publicação após os ciclos rápidos.
Formato dos Dados
Os dados publicados estão no seguinte formato JSON:

json
Copiar código
{
    "timestamp": "YYYY-MM-DD HH:MM:SS",
    "glucose_level": 125.5
}
