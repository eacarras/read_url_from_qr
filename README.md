# Cli for different utils script
You can run the command to see al the tools in the reports side
```
python main.py -h
```

```
usage: main.py [-h] [-u URL] [-j JSON]

Cli Tool for different utils functions

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL for download QR code.
  -j JSON, --json JSON  Json file name.
```

For the first flag `-u` you can pass a url and you can get the decode of the QR Code

For the second flag `-j` you can or not pass a json file if you don't pass the default option it will show

In the code there is 3 constants in the top, you need to custom that values