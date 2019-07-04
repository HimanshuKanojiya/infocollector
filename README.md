# Info collector

Info collector is data harvesting/web scraping tool which is used to gather the hidden and unstructured data on the website. It has the capability of collecting email addresses and phone numbers. It is CLI (Command line interface) program which runs on the black screen of cmd like below: 

![image](https://1.bp.blogspot.com/-JOoGQ2wQzvE/XRszVeA61KI/AAAAAAAACsY/pKIBbthLh-gV3rht2pRCEsPp4OZrHwM0wCLcBGAs/s640/header_info_collector.png)

It is a little bit difficult to run for some non tech background people due to command line interface.

#### Some features of this script are:
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
if you haven't set the python environment variable yet then do below steps or set the variable first:
1. Go to the python37 directory via cmd.
2. Type this:
python.exe "______ Full Path of the Program ______.py"

If you have set the python environment variable then do below steps:
1. Open the cmd.
2. Type this:
python "_____ Full Path of the Program ______.py" 

After running the script, you need to give the URL in the console screen. Type the URL of the target website after this:

> https://hackerzyard.blogspot.com 

**Note: Don't put forward slash "/" after the URL.**

![image](https://1.bp.blogspot.com/-JdYowhWTPoQ/XRtfcJVgTiI/AAAAAAAACso/AVfryrtgAtYaF1tGS-xwShh6UysLuPGzwCLcBGAs/s640/leap_2.png)

As you can see in the above image, there are two methods to scrap/harvest the website. 
1. The first method is to produce quick results. It will target only Google indexed pages of the website.
2. The second method is to allow the info collector to run on the whole website no matter page is indexed or not.

**In the end, you will get the results (See below snap):**

![image](https://1.bp.blogspot.com/-J-4rPhJ97EY/XRtfejFiS5I/AAAAAAAACss/Qusctzdoyso5c-P0ZIRFwk6-P5jvpTVvQCLcBGAs/s640/lead45.png)
