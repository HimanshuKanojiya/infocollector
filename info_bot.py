from bs4 import BeautifulSoup
import requests
import re


class process_queue():
    """
    This object is for processing the data in the FIFO(First Input, First Output)
    method. We can call it queue.

    Available functions:
	   add_in(): It will add the urls in the queue.
	   take_out(): It will remove the first input(url) from list.
	   size_of(): It will return the size of queue.
	   completed_process(): It will return the completed task(urls) from the
       queue.
	   garbages(): It will return non processable urls from queue.
    """
    def __init__(self):
        self.items = []
        self.ignore = []
        self.garbage = []

    def add_in(self,item):
        """
        add_in(arg1):
            arg1 should be a url except NULL.
            It will add an item at zero index position.
        """
        self.items.insert(0,item)
        self.ignore.append(item)

    def take_out(self):
        """
        take_out(self):
	       It does not require any argument. It will return and remove the
           first item(url) from the queue.
        """
        return self.items.pop()

    def size_of(self):
        """
        size_of(self):
	       It does not require any argument. It will return the size of the
           queue.
        """
        return len(self.items)

    def completed_process(self):
        """
        completed_process(self):
	       It does not require any argument. It will return the completed
           urls from the queue.
        """
        return self.ignore

    def garbages(self,item):
        """
        garbages(self,item):
	       It requires an item(URL) which are not supportable
           for the bot process.
        """
        self.garbage.append(item)



#Now process_queue will be accessible globally
global bot_proc
bot_proc = process_queue()


#starting of the bot process
def bot(url):
    """
    This bot follows the same rule which google bot follows to index
    your website. It will follow the link following method(href) to
    capture the new pages.

    bot(url):
	   Give the website url in the url argument.
	      Ex: bot("www.xyz.com")
    """

    page = requests.get(url)
    page_data = page.content
    page.close()

    #if we get the 200 (OK) code then it will execute the link following steps.
    if str(page.status_code) == str("200"):
        html_parse = BeautifulSoup(page_data, "html.parser")

        #It will take out only href links from website HTML codes.
        for items in html_parse.findAll("a"):
            link = items.get("href")
            #below is the regex condition to take out required URLs from the code.
            links = re.findall(str(url) + "[a-zA-Z0-9/-_.%=]+[a-zA-Z0-9-/_%=.]+", str(link))

            for items in links:
                while items not in bot_proc.completed_process() and items not in bot_proc.garbage:
                    #Below conditional statement is used to ignore some URLs to go to the process_queue (add_in method).
                    #Through conditional statements we ignore some URLs which contains media files and also ignore labels.
                    #But these ignored files will save in the process_queue garbage.
                        if str("pdf") not in items and str("png") not in items and str("jpg") not in items and str("jpeg") not in items and str("csv") not in items and str("label") not in items:
                            bot_proc.add_in(items)

                        else:
                            bot_proc.garbages(items)
                            continue

        while bot_proc.size_of():
            #recursion method used below
            bot(bot_proc.take_out())

    else:
        pass
