#include <ESP8266WiFi.h>

#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>

const char *ssid =  "FD-26";     // replace with your wifi ssid and wpa2 key
const char *pass =  "122223455";
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
  //     HTTPClient http;
  //     String postData = "csrftoken=na271ZDAZwshqNzBqmxtHwwh3TfRZ1Yiwh3wemo3Pn6nG2mOFL9SDVda0yhyK0e4&uername=emp001&password=amaravativitap" ;
  //     http.begin("http://192.168.43.154:9000/admin/login/?next=/admin/");              //Specify request destination
  // http.addHeader("Content-Type", "text/html");    //Specify content-type header
 
  // int httpCode = http.POST(postData);   //Send the request
  // String payload = http.getString();
}
void loop() {
   HTTPClient http;

String postData = "employee_num=emp001&bssid=esp8266&signal_strength=43" ;
  //postData = "status=" + ADCData + "&station=" + station ;
  
 http.begin("http://192.168.43.154:9000/getdata/");              //Specify request destination
  http.addHeader("Content-Type", "text/html");    //Specify content-type header
 
  int httpCode = http.GET(postData);   //Send the request
  String payload = http.getString();
// if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
// HTTPClient http;  //Declare an object of class HTTPClient
 
// http.begin("http://192.168.43.154:9000/testing/?testing_field=a");  //Specify request destination
// int httpCode = http.GET();                                                                  //Send the request
 
// if (httpCode > 0) { //Check the returning code
 
// String payload = http.getString();   //Get the request response payload
// Serial.println(payload);                     //Print the response payload

// }
//   Serial.println(WiFi.localIP()); 
// http.end();   //Close connection
 

 
 
  
 
  delay(3000);
}
