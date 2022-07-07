# **PhysComp**
This repo is intended to serve as a basic tool for physiological computing.
Currently, it supports acquiring blood volume pulse or photoplethysmography signal using PulseSensor (https://pulsesensor.com/) connected to PC via Arduino.


## **Installation**
Unzip the package

cd to the directory where requirements.txt is located.

activate your virtual environment

In your shell/ terminal, execute following: 

``` bash
pip install -r requirements.txt
```

Note: If you face the following error:
TypeError: 'PySide6.QtWidgets.QGraphicsScene.addWidget' called with wrong argument types: PySide6.QtWidgets.QGraphicsScene.addWidget(LivePlotFigCanvas) Supported signatures: PySide6.QtWidgets.QGraphicsScene.addWidget(PySide6.QtWidgets.QWidget, PySide6.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags))

Uninstall and install matplotlib package as below:
``` bash    
    pip uninstall matplotlib
    pip install matplotlib
```

## **Terminal command to execute the program**
``` bash
python main.py
```
This shall open a UI as below:
<p align="left">
<img src="images/ui_interface_main.png" alt="Landing screen for UI Interface" width="512"/>
</p>

## **Hardware Setup**
### **PPG**
The setup for PPG is as shown below:
<p align="left">
<img src="images/ppg_setup.png" alt="Hardware setyp for acquiring PPG signal" width="340"/>
</p>