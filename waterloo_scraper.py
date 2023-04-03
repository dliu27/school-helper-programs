from bs4 import BeautifulSoup
import requests
import time
import webbrowser

def main():
    """
    main scrapes the Waterloo booking website every second and if there are spots available, opens the link to the page in the browser.
    
    """
    while (True):
        url = "https://warrior.uwaterloo.ca/program/getprogramdetails?courseid=aaa1e996-2b04-49c9-b6bb-6b8a37b9d1d8&semesterid=875edabf-1182-42a8-b187-157092f2d1c9"
        page_to_scrape = requests.get(url)

        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

        test = soup.findAll('p', attrs={"class": "card-text text-right"})
        small = [p.find('small') for p in test]

        if small[0].contents[0] != "No Spots Available":
            print("Go Book!")
            print(small[0].contents[0])
            webbrowser.open(url, new=2)
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
