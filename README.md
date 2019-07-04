# Info collector

Info collector is data harvesting/web scraping tool which is used to gather the hidden and unstructured data on the website. It has the capability of collecting email addresses and phone numbers. It is CLI (Command line interface) program which runs on the black screen of cmd like below: 

![image](https://1.bp.blogspot.com/-JOoGQ2wQzvE/XRszVeA61KI/AAAAAAAACsY/pKIBbthLh-gV3rht2pRCEsPp4OZrHwM0wCLcBGAs/s640/header_info_collector.png)

It is a little bit difficult to run for some non tech background people due to command line interface.

Some features of this script are:
1. Optimized to work on any website.
2. Provide results quickly as soon as possible (depends on the size of data).
3. Work switcher: 
If any approach fails to get data then it will initiate the second approach to deal with that data.
4. Progress bar to see results and processing items.

#### Note: This script is in under development. 
In the coming days, you can see these things:
- GUI, No need to use CLI to run the program.
- Collect Meta tags.
- Speed will be enhanced.
- Simultaneous Processing.

### Instructions to use this script:

Install python latest version 3.7.2 if not installed yet.

For now, most of the items will not install automatically. Install these libraries first:

1. Module tqdm 
("https://pypi.org/project/tqdm/")

2. Module requests
("https://pypi.org/project/requests/")

3. Module beautifulsoup4 ("https://pypi.org/project/beautifulsoup4/")

4. google-search
("https://pypi.org/project/google-search/")

In a future version, this process will be fixed. 

#### How to run this script:
if you have already installed the python and set the python environment variable then you just need to follow below steps:
- Step 1: Extract the folder.
- Step 2: Open the CMD
- Step 3: After opening the CMD, write "python <program name/full program path>". Example "python universal_extractor.py".

if you don't set the python environment variable then you will follow these steps:
- Step 1: Open the CMD.
- Step 2: GO to drive C:/D:/E: where you have installed the python via CMD.
- Step 3: After entering the Python Folder/directory, type "python.exe <Full Path of Universal Program>". 
  
  Example: python.exe "F:\MyCodes\infocollector\universal_extractor.py"
  
## Instrunctions to use this script:
 
After running the script, you need to give the URL's in console screen. Type the URL of target website after this ">".
> Example: https://hackerzyard.blogspot.com 

### More Info/documentation will be added soon.
