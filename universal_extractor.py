"""
/-----------------------------AUTHOR DETAILS----------------------------------/
    Author: Himanshu kanojiya
    Location: India
    Created On: 16 June 2019
    Contact Email ID: himanshukanojiya825@gmail.com
    Github ID: https://github.com/HimanshuKanojiya
    Repository URL: https://github.com/HimanshuKanojiya/infocollector
    Website: https://hackerzyard.blogspot.com
    Program/Software Name: Info Collector
    Version: 1.0
/-----------------------------------------------------------------------------/
"""



banner ="""
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

sitemap_internal = []


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

class extracts():

    def __init__(self, url, supports):
        self.url = url
        self.supports = supports


    def email_collects(ec):
        email_garbage = []
        total_url = len(ec.url)
        print("Total URL's Found during scanning: " + str(total_url))
        print("Process Initiated....It will take some time to show the results")
        proc = tqdm(ec.url)
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
    collected_urls = []
    robos = extracts(url, url)
    send = robos.robots()
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
    print("Total Founded Email ID's/Phone Numbers are: ")
    for num, show in enumerate(emails):
        print(str(num + 1) + ". " + str(show))
    

if __name__ == "__main__":
    os.system("CLS")
    print(banner)
    print("\n Created By Himanshu Kanojiya, From India\n")
    
    while True:
        url = input("\nEnter the URL to collect the email addresses/phone number or press 'Enter' to exit:\n > ")
        sitemap_internal = []
        if len(url)!= 0:
            option = input("Do you wanna launch the script: (Y/N) > ")
            if option.lower() == 'y':
                try:
                    initator_of(url)
                except:
                    print("Your URL is not supported...")
            elif option.lower() == "n":
                break
            else:
                print("Wrong option choosed, do it again")
                continue
        elif len(url) == 0:
            print("No Value has been given...")
            sys.exit()
        
