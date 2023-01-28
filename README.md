# ObserverPatternWSTI
Task for passing the course Multi-layer systems

  As part of this task, you need to prepare a class that will represent the sensor
temperature and humidity. In addition, you need to prepare two simple classes that
will represent an air humidifier and a fan reacting to changes in parameters
sensor.
When changing sensor parameters, the following actions should occur:
  - Temperature above 28 degrees - The fan turns on.
  - Temperature below 23 degrees - The fan turns off.
  - Humidity above 60 percent - Humidifier shuts down.
  - Humidity below 30 percent - The humidifier turns on.
  
  Assumptions
Both the fan and the humidifier can only display messages in the console (they don't have to
store information about its current state, i.e. on/off)
