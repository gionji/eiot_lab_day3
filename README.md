# eiot_lab_day3

The udooEiotLib.py file must be in the same folder of your test file.

## Run the code on your host machine
The board must be powered and connected to internet, otherwise you'll read old values and you can use the actuators.

## Run the code directly on the UDOO Board
You must run these two commands before launch test.py

```
sudo apt-get install python-dev libssl-dev libffi-dev
sudo pip install -U pyopenssl==0.13.1 pyasn1 ndg-httpsclient
```

After that run:

python test.py
