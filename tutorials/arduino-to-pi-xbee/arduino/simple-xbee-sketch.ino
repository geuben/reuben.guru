#include <XBee.h>
XBee xbee;
ZBTxRequest zbTx;

void setup() {
  xbee = XBee();
  Serial.begin(9600);
  xbee.setSerial(Serial);
  uint8_t payload[] = { 'H', 'e', 'l', 'l', 'o' };
  XBeeAddress64 addr64 = XBeeAddress64(0, 0);
  zbTx = ZBTxRequest(addr64, payload, sizeof(payload));
}

void loop() {
  delay(5000);
  xbee.send(zbTx);
}
