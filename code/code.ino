#include <AFMotor.h>
int Powerpin =11;
int Indicatepin =9;
int Sensorvalue = 0;
int Alclevel =0;
int val;
int Sensorpin;
AF_DCMotor leftFrontWheel(3, MOTOR12_1KHZ);
AF_DCMotor leftRearWheel(4, MOTOR12_1KHZ);
AF_DCMotor rightFrontWheel(2, MOTOR34_1KHZ);
AF_DCMotor rightRearWheel(1, MOTOR34_1KHZ);

void setup() {

  Serial.begin(9600);
//  while (!Serial)
//  {
//    //wait for serial to come
//  }

  pinMode(Indicatepin,OUTPUT);
  pinMode(Powerpin,INPUT);
  leftFrontWheel.setSpeed(255);
  leftRearWheel.setSpeed(255);
  rightFrontWheel.setSpeed(255);
  rightRearWheel.setSpeed(255);
  releaseWheels();
  val =1;
}

void loop()
{
  
  Sensorvalue = analogRead(Sensorpin);
  Alclevel = map(Sensorvalue, 300, 1023, 0, 10);
  Serial.print("\nlevel\n");
  Serial.print(Alclevel);
  if(Alclevel >= 3)
  {
    digitalWrite(Indicatepin,HIGH);
  }
  
  val = digitalRead(Powerpin);
  Serial.print("\nvalue\n");
  Serial.print(val);
 
  
  if(val == HIGH)
  {
  int valueReceived = Serial.read();
  if (valueReceived == '1')
  {
    moveForward();
   
  }
  else if (valueReceived == '2')
  {
    moveBack();
    
  }

  else if (valueReceived == '3')
  {
    moveRight();
    
  }
  else if (valueReceived == '4')
  {
    moveLeft();
    
  }
  else if(valueReceived == '5')
  {
    releaseWheels();
   
  }
  }
  else
  {
    releaseWheels();
  }
  delay(100);
}

void moveForward()
{
  leftFrontWheel.run(FORWARD);
  leftRearWheel.run(FORWARD);
  rightFrontWheel.run(FORWARD);
  rightRearWheel.run(FORWARD);
}

void moveRight()
{
  leftFrontWheel.run(FORWARD);
  leftRearWheel.run(FORWARD);
  rightFrontWheel.run(RELEASE);
  rightRearWheel.run(RELEASE);
  /*delay(5000);
  rightFrontWheel.run(FORWARD);
  rightRearWheel.run(FORWARD);*/
}

void moveLeft()
{
  leftFrontWheel.run(RELEASE);
  leftRearWheel.run(RELEASE);
  rightFrontWheel.run(FORWARD);
  rightRearWheel.run(FORWARD);
  /*delay(5000);
  leftFrontWheel.run(FORWARD);
  leftRearWheel.run(FORWARD);*/
}

void moveBack()
{
  leftFrontWheel.run(BACKWARD);
  leftRearWheel.run(BACKWARD);
  rightFrontWheel.run(BACKWARD);
  rightRearWheel.run(BACKWARD);
}

void releaseWheels()
{
  leftFrontWheel.run(RELEASE);
  leftRearWheel.run(RELEASE);
  rightFrontWheel.run(RELEASE);
  rightRearWheel.run(RELEASE);
}


