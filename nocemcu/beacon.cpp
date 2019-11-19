//credits to Gowtham S from mybtechprojects.tech


//Header Files
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
 
//Hotspot Name and Password
const char* ssid = "ESPWebServer";
const char* password = "12345678";
 
ESP8266WebServer server(80); //Server on port 80
 
void handleRoot() {
  server.send(200, "text/plain", "Thank You for using www.mybtechprojects.tech");
}
 
void setup(void){
  Serial.begin(9600);
  Serial.println("");
  
 
  //Start NodeMCU in ACCESS POINT Mode
  WiFi.mode(WIFI_AP);           
 
  //Start Hotspot wiith the specified SSID and Password with password
  WiFi.softAP(ssid,password);
 
  //Start Hotspot wiith the specified SSID and Password without password
  //WiFi.softAP(ssid);
 
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("HotSpt IP:");
  Serial.println(myIP);
 
  //If requested on this url execute this function
  //server.on("Requested url",Function); 
  server.on("/", handleRoot);      
 
  server.begin();                 
  Serial.println("HTTP server started");
}
 
void loop(void){
  server.handleClient();          
}

