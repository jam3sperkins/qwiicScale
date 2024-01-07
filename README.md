# qwiicScale
This is a for testing and modifying Python code to read data from 8 qwiic scales connected to a qwiic mux breakout board on a Raspberry Pi

There is no official supported code from SparkFun for the SparkFun Qwiic Scale - NAU7802 - especially if you connect in a Qwiic Mux board to allow the connection of multiple Qwiic Scale's to the same Raspberry Pi.

This project is a modification of existing code repo's to turn of all the ports on the Mux board, turn them on one at a time, read the weight and write it to a local CSV file.
