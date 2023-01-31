# BioniCat

## Introduction

This project aims at controlling my robot [PiCar-X](https://docs.sunfounder.com/projects/picar-x/en/latest/), built around a Rasperry Pi 4.

The is natively compatible with a proprietary software, but I chose to redevelop the features that interest me, based on the [robot-hat](https://github.com/sunfounder/robot-hat.git) library.

If you want to do the same installation, please follow [this guide](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_start/quick_guide_on_python.html)

## Tools

Debugging tools are available in the `tools` folder.

### Mechanics

- motors.py : makes the two motors run forward and then backward
- reset.py : resets the main controller
- servo.py : moves the selected servo motor to the requested angle

## Launching

### Server

```
./start-server.sh server/main.py
```

### Client

The client allows to control the robot via the browser. An XBox controller (or similar) is required.

**The client project will be published later.**
