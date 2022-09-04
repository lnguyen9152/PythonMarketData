This file was created by Lance Nguyen to send current market data notifications based on an input from an algo.

Please run setup.py to fully set up the requirements for the projects before starting development and testing.

Current Price uses BetterSoup4 to get market data from CNBC and format accordingly.

Main calls upon current price in a thread and updates to be compared to other values.

MsgSnd is used as a method to send messages to the OneSignal Client.
