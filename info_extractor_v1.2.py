"""
/-----------------------------AUTHOR DETAILS----------------------------------/
    Author: Himanshu kanojiya
    Location: India
    Created On: 19 July 2019
    Contact Email ID: himanshukanojiya825@gmail.com
    Github ID: https://github.com/HimanshuKanojiya
    Repository URL: https://github.com/HimanshuKanojiya/infocollector
    Website: https://hackerzyard.blogspot.com
    Program/Software Name: Info Collector
    Version: 1.2
/-----------------------------------------------------------------------------/
"""



banner = """
 ___ _   _ _____ ___     ____ ___  _     _     _____ ____ _____ ___  ____  
|_ _| \ | |  ___/ _ \   / ___/ _ \| |   | |   | ____/ ___|_   _/ _ \|  _ \ 
 | ||  \| | |_ | | | | | |  | | | | |   | |   |  _|| |     | || | | | |_) |
 | || |\  |  _|| |_| | | |__| |_| | |___| |___| |__| |___  | || |_| |  _ < 
|___|_| \_|_|   \___/   \____\___/|_____|_____|_____\____| |_| \___/|_| \_\

"""

import info_extractor_raw as raw
import requests
import re
import sys
from tqdm import tqdm
import os
import socket
import ast
from bs4 import BeautifulSoup
import codecs
import info_bot as my_bot

sitemap_internal = []
prev_url = ""

class raw_collects():
    def __init__(self, url, data = "NO DATA HAS BEEN GIVEN YET"):
        self.url = url
        self.data = data

    def raw_collector(rc):
        data = requests.get(str(rc.url) + "/robots.txt")
        datas = data.content
        data.close()
        return str(datas)

    def raw_collector_site(rc):
        data = requests.get(str(rc.url))
        datas = data.content
        data.close()
        return str(datas)

    def raw_filters(rfc):
        filter_out = []
        if str(".xml") in str(rfc.data) and len(str(rfc.data))!=0:

            scheme = raw.re_strings("sitemaps")

            for start in scheme:
                #print("Scheme Used: " + str(rfc.url + start))
                pattern = re.findall(str(rfc.url+start), str(rfc.data))

                if len(pattern)!=0:
                    #print(pattern)
                    return pattern, True

                else:
                    continue
        else:
            return str("Have some malfunctions"), False


    def server_location(slc):
        pure_url = slc.url.partition("//")[::-1][0]
        ip = socket.gethostbyname(pure_url)
        #accessing the server
        for path, token in (raw.re_strings("server")).items():
            #print(str(path) + str(ip) + str(token))
            send = requests.get(str(path)+str(ip)+str(token))
            receive = send.content
            send.close()

            if str(send.status_code) == "200":
                filtering_output = ast.literal_eval(str(receive.decode("utf-8")))
                try:
                    simple = "Server Information: \n1. IP Address: {} \n2. Location: {},{},{}\n3. Postal Code: {}\n4. Langtitude & Longtitude: {}".format(filtering_output["ip"],filtering_output["city"],filtering_output["region"],filtering_output['country'],filtering_output['postal'], filtering_output['loc'])
                    #print(simple)
                    return simple
                except:
                    #print(filtering_output)
                    return filtering_output
            else:
                print("Server Issues")


    def version_check(vcs):
        ver = raw_collects(vcs.url)
        html_code = ver.raw_collector_site()
        version_raw = BeautifulSoup(html_code, "html.parser")
        vers = version_raw.find_all("span",{"class":"css-truncate-target"})
        version = re.findall('v[0-9.]+', str(vers[0]))
        return str(version[0])



class extracts():

    def __init__(self, url, supports):
        self.url = url
        self.supports = supports


    def email_collects(ec):
        email_garbage = []
        total_url = len(ec.url)
        print("Total URL's Found during scanning: " + str(total_url))
        #print("Process Initiated....It will take some time to show the results")
        print("\n Warning! : For Better Results Scan All URL's")
        ask = input("Type number which is < " + str(total_url) + " or Hit the 'Enter' Button to scan all URL's: ")

        proc = ""

        if len(ask) == 0:
            proc = tqdm(ec.url[:])
        elif len(ask)!= 0:
            proc = tqdm(ec.url[:int(ask)])

        for items in proc:
            proc.set_description("Completed")
            eoc = raw_collects(items)
            data = eoc.raw_collector_site()

            for schemes in raw.re_strings("strs_data"):
                pattern = re.findall(schemes, str(data))
                if len(pattern)!=0:
                    for ids in pattern:
                        email_garbage.append(ids)
                else:
                    continue


        return list(set(email_garbage))


    def robots(rob):
        st = raw_collects(str(rob.url))
        datas = st.raw_collector()

        for used, strs in enumerate(raw.re_strings("robos")):
            pattern = re.findall(str(rob.url) + strs, str(datas))

            if len(pattern) == 0:
                continue

            elif len(pattern) != 0:
                return pattern

    def in_sitemap(insit):
        print("Received URL's: " + str(insit.url))
        content = raw_collects(insit.url)
        garbage = content.raw_collector_site()
        content.data = garbage
        content.url = insit.supports
        filtering, site_con = content.raw_filters()

        if site_con == True:
            for saving in filtering:
                #print("used: " + str(saving))
                fetch = raw_collects(saving)
                datas = fetch.raw_collector_site()
                for scheme in raw.re_strings("sitemaps"):
                    #print(str(insit.supports)+str(scheme))
                    pattern = re.findall(str(insit.supports)+str(scheme), str(datas))
                    if len(pattern)!=0:
                        for feed in pattern:
                            sitemap_internal.append(feed)
                    elif len(pattern) == 0:
                        continue


        elif site_con == False:
            second_app = raw_collects(insit.url)
            urls_app = second_app.raw_collector_site()
            for scheme in raw.re_strings("sitemaps"):
                    pattern = re.findall(str(insit.supports)+str(scheme), str(urls_app))
                    if len(pattern)!=0:
                        return pattern
                    elif len(pattern) == 0:
                        continue



def initator_of(url):
    """
    initator_of(url):
	   url: In this argument, we will give the url of the website.

	working:
	   It will perform the sitemap method to collect the URLs.
"""
    collected_urls = []
    robos = extracts(url, url)
    send = robos.robots()

    if str(send) == str("None"):
        print("Initiating Second Approach....")
        for puting in raw.re_strings("sec_app"):
            robos.url = str(url) + str("/") + str(puting)
            urls = robos.in_sitemap()

            try:
                for urls_in in urls:
                    sitemap_internal.append(urls_in)
            except:
                pass


        final_url = list(set(sitemap_internal))
        robos.url = final_url
        emails = robos.email_collects()
        loct = raw_collects(url)
        pos = loct.server_location()
        print("\nTotal Founded Email ID's/Phone Numbers are: ")
        for num, show in enumerate(emails):
            print(str(num + 1) + ". " + str(show))

        if type(pos) == str:
            print("\nTarget Server Information:")
            print(pos)

        elif type(pos) == dict:
            print("\nTarget Server Information:")
            for items, datas in pos.items():
                print(str(items) + " : " + str(datas))

    elif str(send) is not str("None"):
        for items in send:
            robos.url = items
            urls = robos.in_sitemap()

            try:
                for urls_in in urls:
                    sitemap_internal.append(urls_in)
            except:
                pass

        final_url = list(set(sitemap_internal))
        robos.url = final_url
        emails = robos.email_collects()
        loct = raw_collects(url)
        pos = loct.server_location()
        print("\nTotal Founded Email ID's/Phone Numbers are: ")
        for num, show in enumerate(emails):
            print(str(num + 1) + ". " + str(show))

        if type(pos) == str:
            print("\nTarget Server Information:")
            print(pos)

        elif type(pos) == dict:
            print("\nTarget Server Information:")
            for keys, data in pos.items():
                print(str(keys) + " : " + str(data))


def initiator_quick(url):
    """
    initiator_quick(url):
	   url: In this argument, we will give the url of the website.

       Working:
       It will send the url to the "info_bot" module to perform the link
       following method. After completing the process, this module will
       access the process_queue to collect the url.
"""
    my_bot.bot_proc.ignore = []
    my_bot.bot(url)
    urls = my_bot.bot_proc.completed_process()
    robos = extracts(url, url)
    robos.url = urls
    emails = robos.email_collects()
    loct = raw_collects(url)
    pos = loct.server_location()
    print("\nTotal Founded Email ID's/Phone Numbers are: ")

    for num, show in enumerate(emails):
        print(str(num + 1) + ". " + str(show))

    if type(pos) == str:
        print("\nTarget Server Information:")
        print(pos)

    elif type(pos) == dict:
        print("\nTarget Server Information:")
        for keys, data in pos.items():
            print(str(keys) + " : " + str(data))



if __name__ == "__main__":
    #It is a CLI menu function to take the user inputs.
    #inputs should be website url and bot working selection.

    #ver_check will go to the releases and take the latest version name.
    ver_check = raw_collects("https://github.com/HimanshuKanojiya/infocollector/releases")
    version_ver = ver_check.version_check()

    os.system("CLS")
    print(banner)
    print("\n Created By Himanshu Kanojiya, From India\n * Current Version: {}".format("1.2"))

    #If this copy of the program is the latest version then, the below conditional statement will work.
    #Otherwise, it will produce a warning to update the copy of the program.
    if str('v1.2') == str(version_ver):

        while True:
            url = input("\nEnter the URL to collect the email addresses/phone number or press 'Enter' to exit:\n > ")
            prev_url = url
            sitemap_internal = []
            if len(url)!= 0:
                search = input("Press: {} for Link Following method (href)\nPress: {} for sitemap method\n(1/2) > ".format(1,2))
                option = input("Do you wanna launch the script: (Y/N) > ")
                if option.lower() == 'y':
                    try:
                        #It will launch the url following method
                        if str(search) == "1":
                            initiator_quick(url)

                        #It will lanuch the sitemap method
                        elif str(search) == "2":
                            initator_of(url)

                        else:
                            print("You have not chosen anything, executing long method!")
                            initator_of(url)
                    except Exception as error:
                        print("Your URL is not supported/Internet Connectivity Issue")
                        print(error)
                elif option.lower() == "n":
                    break
                else:
                    print("Wrong option choosed, do it again")
                    continue
            elif len(url) == 0:
                print("No Value has been given...")
                sys.exit()

    else:
        # WARNING Message
        print("\n Your Version is outdated, Kindly update to {}".format(version_ver))
        sys.exit()
