import requests
import mechanicalsoup
import metaData_scraper
def trial_1():
    url = "https://library.osu.edu/dc/users/sign_in"

    browser = mechanicalsoup.StatefulBrowser()
    login_page = browser.open(url)
    login_form = browser.select_form('form[action="/dc/users/sign_in?locale=en"]')
    browser["user[email]"] = "xu.3579@osu.edu"
    browser["user[password]"] = "x&Nm!4F,?DA@*yk9HY"
    response = browser.submit_selected()
    if response.status_code == 200:
        print("login success")
        print(len(response.text))
        metaData_scraper.main(browser)
    else:
        print("Login fail!")
    
    
def trial_0():
    url = 'https://library.osu.edu/dc/users/sign_in'
    login_data = {}
    login_data["user[email]"] = "xu.3579@osu.edu"
    login_data["user[password]"] = "x&Nm!4F,?DA@*yk9HY"
    login_data["authenticity_token"] = "mRaO+j/GNWnE9GtINiuQwWK/PKk/WOmn0ItWEBazp9GhO/GzvhpTjzTJXV1OI/+epxCrf6PaZaTJmW6wo2Vjxw=="
    #print(login_data)
    session = requests.session()

    r = session.post(url, data=login_data)
    print(r.text)

def main():
    trial_1()
    
if __name__ == "__main__":
    main()
