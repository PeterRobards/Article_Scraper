#!/usr/bin/env python3
"""Program designed to extract text content from a handful of popular websites"""
# -*- coding: utf-8 -*-
#
# Web Scraping Program designed to extract text content from a handful of popular websites
# Created by Peter Robards -- Version 1.1
#
##########################################################################################

import sys
import requests
import tldextract
from bs4 import BeautifulSoup

# method to extract the top level domain from a given url - requires tldextract library
def extract_domain(url):
    """Extracts the top level domain from a given url - requires tldextract library"""
    ext = tldextract.extract(url)
    domain = ext.domain
    return domain


# Method to save output to a specified file
def output_to_file(file_name, text):
    """Saves output to a specified file"""
    with open(file_name, "w") as out_file:
        # write the new line to output file
        out_file.write(text)

    print(f"\nThe results have been saved to: {file_name} ")


# Method to set web scraping variables based on the target website
#  website_list = ["arstechnica", "bleepingcomputer", "vice", "wired"]
def set_scraper_variables(domain, website_list):
    """set which elements to extract content from based on the target website"""

    if domain == website_list[0]:

        title_wrapper = "h1"
        title_attr = "itemprop"
        title_attr_name = "headline"
        content_wrapper = "div"
        content_attr = "itemprop"
        content_attr_name = "articleBody"
        target_wrapper = "p"

    elif domain == website_list[1]:

        title_wrapper = "div"
        title_attr = "class"
        title_attr_name = "article_section"
        content_wrapper = "div"
        content_attr = "class"
        content_attr_name = "articleBody"
        target_wrapper = "p"

    elif domain == website_list[2]:

        title_wrapper = "h1"
        title_attr = "class"
        title_attr_name = "smart-header__hed smart-header__hed--size-2"
        content_wrapper = "div"
        content_attr = "class"
        content_attr_name = "article__body-components"
        target_wrapper = "p"

    elif domain == website_list[3]:

        title_wrapper = "h1"
        title_attr = "class"
        title_attr_name = "content-header__row content-header__hed"
        content_wrapper = "div"
        content_attr = "class"
        content_attr_name = "article__chunks"
        target_wrapper = "p"

    else:
        print("\nERROR -> Domain: {domain} is not a valid entry.")
        print("\nValid entries include: ")
        print(f"{website_list}")
        sys.exit("\nPlease check URL and retry - thank you!\n")

    return (
        title_wrapper,
        title_attr,
        title_attr_name,
        content_wrapper,
        content_attr,
        content_attr_name,
        target_wrapper,
    )


# Method to remove unwanted content from specific websites
def remove_unwanted_content(domain, soup_object):
    """Remove unwanted content collected from non-standard websites"""
    if domain == "bleepingcomputer":
        # Remove unwanted content from soup object
        soup_object.find("div", {"class": "cz-related-article-wrapp"}).decompose()

    return soup_object


# Method to extract title text from supported websites
def get_title(website, soup, title_wrapper, title_attr, title_attr_name):
    """Extracts title text from supported website"""
    # Code to extract title from SomeWebsite.com
    # Check if website is the single edge cases
    # if it is use the customized method, else use the default method
    if website == "bleepingcomputer":
        title = (
            soup.find(title_wrapper, attrs={title_attr: title_attr_name})
            .find("h1")
            .text
        )
    else:
        title = soup.find(title_wrapper, attrs={title_attr: title_attr_name}).text

    return title


# Method to extract the text content from supported websites
def get_text(soup, content_wrapper, content_attr, content_attr_name, target_wrapper):
    """Extracts the text content from supported websites"""
    content_text = ""
    target = soup.find(content_wrapper, {content_attr: content_attr_name}).findAll(
        target_wrapper
    )

    for element in target:
        content_text += "\n\n" + "".join(element.findAll(text=True)) + " "

    return content_text


# Method to extract content title and full targeted text from supported websites
def get_content(url, website, site_list):
    """Extracts content title and full targeted text from supported websites"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # set scraper variables based on name of target website
    (
        title_wrapper,
        title_attr,
        title_attr_name,
        content_wrapper,
        content_attr,
        content_attr_name,
        target_wrapper,
    ) = set_scraper_variables(website, site_list)

    title = get_title(website, soup, title_wrapper, title_attr, title_attr_name)

    # Remove unwanted content from soup object for a few select websites
    soup = remove_unwanted_content(website, soup)

    content_text = get_text(
        soup, content_wrapper, content_attr, content_attr_name, target_wrapper
    )

    return title, content_text


##########################################################################################


def main():
    """Main() method for program"""
    target = input("\nPlease enter the url of webpage you wish to scrape: ")

    supported_sites = ["arstechnica", "bleepingcomputer", "vice", "wired"]
    # extract domain from url
    website = extract_domain(target)
    if website not in supported_sites:
        print(f"\nERROR -> Website: {website} is not a valid entry.")
        print("\nValid entries include: ")
        print(f"{supported_sites}")
        sys.exit(1)

    # print out the HTML content of the page, formatted nicely,
    # using the prettify method on the BeautifulSoup object
    # print(soup.prettify())

    title, article = get_content(target, website, supported_sites)

    while True:
        choice = input("\nWould you like to save article to file? [Yes or No] : ")

        if choice[0].lower() == "y":
            outfile = input("\nPlease enter path for output file\n\t:")
            output_text = title + ". \n\n" + article + " \n\nSource: " + target
            output_to_file(outfile, output_text)
            break
        if choice[0].lower() == "n":
            print("\nTITLE:\n")
            print(title)
            print("\nText:")
            print(article)
            break

        print(f"\nERROR - your response {choice} is invalid!\n")
        print('\nPlease type either "Yes" or "No"!\n')

    print("\nJob Done!\n")


##########################################################################################

if __name__ == "__main__":

    main()
