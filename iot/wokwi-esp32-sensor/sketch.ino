#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <DHTesp.h>

const char* WIFI_SSID = "Wokwi-GUEST";
const char* WIFI_PASSWORD = "";
const int WIFI_CHANNEL = 6;

const char* API_URL = "http://host.wokwi.internal:8000/api/readings";
const char* DEVICE_ID = "esp32-wokwi-01";
const char* LOCATION = "lab-simulation";

const int DHT_PIN = 15;

DHTesp dhtSensor;

void connectToWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD, WIFI_CHANNEL);

  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void sendReading(float temperature, float humidity) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected, skipping request");
    return;
  }

  HTTPClient http;
  http.begin(API_URL);
  http.addHeader("Content-Type", "application/json");

  JsonDocument payload;
  payload["device_id"] = DEVICE_ID;
  payload["location"] = LOCATION;
  payload["temperature"] = temperature;
  payload["humidity"] = humidity;

  String requestBody;
  serializeJson(payload, requestBody);

  int httpResponseCode = http.POST(requestBody);
  Serial.print("HTTP response code: ");
  Serial.println(httpResponseCode);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(response);
  } else {
    Serial.print("Request failed: ");
    Serial.println(http.errorToString(httpResponseCode));
  }

  http.end();
}

void setup() {
  Serial.begin(115200);
  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
  connectToWiFi();
}

void loop() {
  TempAndHumidity data = dhtSensor.getTempAndHumidity();

  Serial.print("Temperature: ");
  Serial.print(data.temperature);
  Serial.print(" C, Humidity: ");
  Serial.print(data.humidity);
  Serial.println(" %");

  sendReading(data.temperature, data.humidity);
  delay(5000);
}
