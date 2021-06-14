#include "mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"

Ticker servo_ticker;
PwmOut pin5(D10), pin6(D11);
BufferedSerial xbee(D1, D0);

BBCar car(pin5, pin6, servo_ticker);

int main() {

//     // please contruct you own calibration table with each servo
//    double pwm_table0[] = {-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150};
//    double speed_table0[] = {-7.255, -7.095, -6.856, -7.733, -5.102, 0.000, 5.262, 7.095, 7.095, 7.414, 7.095};
//    double pwm_table1[] = {-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150};
//    double speed_table1[] = {-10.284, -9.806, -10.364, -10.364, -6.457, 0.000, 4.863, 9,248, 9.885, 10.443, 9.886};
// // 0.000, 6.457, 10.364, 10.364, 9.806, 10.284  ----  0->-150
//    // first and fourth argument : length of table
//    car.setCalibTable(11, pwm_table0, speed_table0, 11, pwm_table1, speed_table1);

   char buf[256], outbuf[256];
   FILE *devin = fdopen(&xbee, "r");
   FILE *devout = fdopen(&xbee, "w");
   while (1) {
      memset(buf, 0, 256);
      for( int i = 0; ; i++ ) {
         char recv = fgetc(devin);
         if(recv == '\n') {
            printf("\r\n");
            break;
         }
         buf[i] = fputc(recv, devout);
      }
   RPC::call(buf, outbuf);
   }
}