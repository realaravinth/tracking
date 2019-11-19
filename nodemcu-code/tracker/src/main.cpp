#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
const char *ssid =  "ESPWebServer";     // replace with your wifi ssid and wpa2 key
const char *pass =  "12345678";
const char *host = "192.168.42.211:9000/";
 
WiFiClient client;
 
void setup()
{
       Serial.begin(9600);
       delay(10);
               
       Serial.println("Connecting to ");
       Serial.println(ssid);
 
       WiFi.begin(ssid, pass);
       while (WiFi.status() != WL_CONNECTED)
          {
            delay(500);
            Serial.print(".");
          }
      Serial.println("");
      Serial.println("WiFi connected");
}
 
void loop() {
   HTTPClient http;
 
 int n = WiFi.scanNetworks();
    Serial.println("scan done");
    if (n == 0) {
      Serial.println("no networks found");
    } else {
      String strenght_val, bssid_val, url_val, host_with_session_id;
      Serial.print(n);
      Serial.println(" networks found");
      for (int i = 0; i < n; ++i) {
        bssid_val=(WiFi.SSID(i));
        strenght_val=(WiFi.RSSI(i));
        String postData = "employee_num=emp001&bssid="+bssid_val+"&signal_strength="+strenght_val;
        host_with_session_id="http://192.168.4.2:8000/getdata/?";
        url_val=host_with_session_id+postData;
         http.begin(url_val);
         http.addHeader("Content-Type", "text/html");
        delay(10);
        int httpCode = http.POST(url_val);   //Send the request
       String payload = http.getString();
      }
    }
    Serial.println("");
   delay(3000);
}