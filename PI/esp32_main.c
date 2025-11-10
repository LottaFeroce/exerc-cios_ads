#include <WiFi.h>
#include "AdafruitIO_WiFi.h"
#include <time.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define WIFI_SSID     "NEVADA"
#define WIFI_PASS     "projetoqw"
#define IO_USERNAME   "Projeto_Dengue"
#define IO_KEY        ""

#define FEED_TIMESTAMP "agente_saude"
#define FEED_CONTADOR  "contador_focos"

#define BUTTON_PIN 2
#define LED_PIN 15

bool lastButtonState = HIGH;
bool ledState = false;
int contador = -1;
bool conectadoIO = false;

AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);
AdafruitIO_Feed *feedTimestamp = io.feed(FEED_TIMESTAMP);
AdafruitIO_Feed *feedContador  = io.feed(FEED_CONTADOR);

void atualizarLCD(String linha1, String linha2 = "") {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(linha1);
  lcd.setCursor(0, 1);
  lcd.print(linha2);
}

void handleContador(AdafruitIO_Data *data) {
  contador = data->toInt();
  Serial.println("Valor sincronizado do contador: " + String(contador));
  atualizarLCD("Focos de Dengue:", "Total: " + String(contador));
}

void setupTime() {
  configTime(-4 * 3600, 0, "pool.ntp.org", "time.nist.gov");
  struct tm timeinfo;
  while (!getLocalTime(&timeinfo)) delay(500);
  Serial.println("Horário sincronizado (UTC-4)");
}

String getFormattedTime() {
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) return "Erro!";
  char buffer[30];
  strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", &timeinfo);
  return String(buffer);
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

  lcd.init();
  lcd.backlight();
  atualizarLCD("Iniciando...");

  Serial.println("🔌 Conectando ao Wi-Fi...");
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
  atualizarLCD("WiFi conectado");

  setupTime();

  Serial.println("Conectando ao Adafruit IO...");
  io.connect();

  unsigned long startTime = millis();
  while (io.status() < AIO_CONNECTED && millis() - startTime < 15000) {
    Serial.print(".");
    delay(500);
  }

  if (io.status() < AIO_CONNECTED) {
    Serial.println("\n❌ Falha ao conectar ao Adafruit IO!");
    atualizarLCD("Falha no IO!");
  } else {
    Serial.println("\nConectado ao Adafruit IO!");
    atualizarLCD("IO conectado!");
    conectadoIO = true;

    feedContador->onMessage(handleContador);
    feedContador->get();
  }

  delay(1000);
}

void loop() {
  io.run();

  if (contador < 0 && conectadoIO) {
    contador = 0;
    feedContador->save(contador);
    Serial.println("🔧 Nenhum valor remoto. Iniciando contador em 0.");
    atualizarLCD("Inicializando...", "Total: 0");
  }

  bool currentButton = digitalRead(BUTTON_PIN);

  if (currentButton == LOW && lastButtonState == HIGH && conectadoIO) {
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);

    contador++;
    String timestamp = getFormattedTime();

    feedTimestamp->save(timestamp);
    feedContador->save(contador);

    Serial.println("Novo caso: " + String(contador));
    atualizarLCD("Focos de Dengue:", "Total: " + String(contador));

    delay(500);
  }

  lastButtonState = currentButton;
}
