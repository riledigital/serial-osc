# pySerial + python-osc example

Simple example reading data from Arduino via serial and creating an Open Sound Control client for multimedia control...

### Instructions

- `poetry install` to set up dependencies
- `poetry shell` to start the virtual env
- `python app.py` to start the app

### Configuration

Be sure to set up the proper OSC constants; default parameters are specified in the class constructor for ArduinoOscInput

Based on
https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial

