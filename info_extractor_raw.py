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

    Note: This file is used to find the sensitive information format,
    if any issues come in results then we need to do some changes in this
    file.
/-----------------------------------------------------------------------------/
"""


def re_strings(content):
    strs_data = ["[a-zA-Z0-9.-]+@[a-zA-Z.-]+com","[\d]{2,3}\s[\d]{2,4}.\s[\d]{3,4}"]
    sitemaps = ["[a-zA-Z0-9.-/]+[a-z0-9._-]+xml","[a-zA-Z0-9.-/]+[a-z0-9.-]+html","[a-zA-Z0-9.-/]+[a-z0-9/-]+"]
    robos = ["[a-zA-Z.-_?]+[0-9]+","[a-zA-Z.-/_]+xml"]

    if str(content) == str("strs_data"):
        return strs_data

    elif str(content) == str("sitemaps"):
        return sitemaps

    elif str(content) == str("robos"):
        return robos
    
