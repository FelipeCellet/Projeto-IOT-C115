import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do MQTT
broker = "test.mosquitto.org"  # Pode usar um broker público ou local
port = 1883
topic = "sensor/glicose"

# Função para publicar dados
def publish_data(client, topic, data):
    client.publish(topic, json.dumps(data))
    print(f"Published {data} to topic {topic}")

# Configurando o cliente MQTT
client = mqtt.Client()
client.connect(broker, port)

# Função para simular variação de glicemia
def simulate_glucose_interaction(initial_glucose):
    glucose_level = initial_glucose
    print(f"Simulação iniciada. Glicemia atual: {glucose_level} mg/dL")
    
    try:
        while True:
            print("\nEscolha uma ação:")
            print("1 - Comer (aumentar glicemia)")
            print("2 - Injetar insulina (reduzir glicemia)")
            print("3 - Monitorar sem interação (publicar valor atual)")
            print("0 - Sair")
            
            choice = input("Digite sua escolha: ")

            if choice == "1":
                food_value = float(input("Quantos gramas de carboidratos você consumiu? "))
                glucose_increase = food_value * 2  # Aumento proporcional ao carboidrato
                print(f"Glicemia aumentando em ~{glucose_increase} mg/dL...")
                for i in range(10):  # Publica a cada 1 segundo após ação
                    glucose_level += glucose_increase / 10
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    data = {"timestamp": timestamp, "glucose_level": round(glucose_level, 1)}
                    publish_data(client, topic, data)
                    time.sleep(1)
            
            elif choice == "2":
                insulin_units = float(input("Quantas unidades de insulina você injetou? "))
                glucose_decrease = insulin_units * 10  # Redução proporcional à insulina
                print(f"Glicemia diminuindo em ~{glucose_decrease} mg/dL...")
                for i in range(10):  # Publica a cada 1 segundo após ação
                    glucose_level -= glucose_decrease / 10
                    if glucose_level < 0:
                        glucose_level = 0  # Evita glicemia negativa
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    data = {"timestamp": timestamp, "glucose_level": round(glucose_level, 1)}
                    publish_data(client, topic, data)
                    time.sleep(1)

            elif choice == "3":
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                data = {"timestamp": timestamp, "glucose_level": round(glucose_level, 1)}
                publish_data(client, topic, data)
                print(f"Glicemia atual publicada: {round(glucose_level, 1)} mg/dL")
                time.sleep(5)  # Intervalo padrão para monitoramento

            elif choice == "0":
                print("Encerrando simulação...")
                break

            else:
                print("Escolha inválida. Tente novamente.")
    
    except KeyboardInterrupt:
        print("\nSimulação interrompida.")
    finally:
        client.disconnect()

# Iniciar o modo de simulação ou automático
def main():
    print("Bem-vindo ao simulador de sensor de glicemia.")
    print("Escolha o modo de operação:")
    print("1 - Modo automático (simulação aleatória)")
    print("2 - Modo interativo (simulação manual)")
    
    mode = input("Digite sua escolha: ")
    
    if mode == "1":
        print("Iniciando modo automático...")
        try:
            while True:
                glucose_level = round(random.uniform(70, 180), 1)
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                data = {"timestamp": timestamp, "glucose_level": glucose_level}
                publish_data(client, topic, data)
                time.sleep(5)  # Publicação a cada 5 segundos
        except KeyboardInterrupt:
            print("\nModo automático encerrado.")
            client.disconnect()
    elif mode == "2":
        initial_glucose = float(input("Digite o valor inicial de glicemia (mg/dL): "))
        simulate_glucose_interaction(initial_glucose)
    else:
        print("Modo inválido. Saindo...")

if __name__ == "__main__":
    main()
