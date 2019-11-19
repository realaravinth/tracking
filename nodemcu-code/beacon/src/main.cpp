#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Arduino.h>
//Beacon name and password
String ssid = "ESPWebServer";   //Put beacon name here
const char *password = "12345678";//Change password to something very complex

ESP8266WebServer server(80); //Server on port 80 to test beacon's status
 
void handleRoot() {
  String message="You are connected to beacon: "+ssid;
  server.send(200, "text/plain", message);
}
 
void setup(void){
  Serial.begin(9600);
  Serial.println("");
  
 
  //Start NodeMCU in ACCESS POINT Mode
  WiFi.mode(WIFI_AP);           
 
  //Turn beacon on
  WiFi.softAP(ssid,password);
 
 
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
