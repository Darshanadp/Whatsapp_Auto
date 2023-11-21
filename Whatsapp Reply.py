import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time

# Specify the path to the Chrome webdriver
webdriver_path = 'C:\webdrivers\chromedriver.exe'

print(webdriver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(webdriver_path)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
time.sleep(60)  # Wait for the user to scan the QR code or complete authentication

# Define the group and direct chats where you want to reply
global group_chats

group_chats = 'Your Whatsapp Group Name'

# Function to find and reply to messages in a chat
def reply_to_messages(chat_name):
    search_box = driver.find_element("xpath",'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    # search_box.clear()
    search_box.send_keys(chat_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

def replyabs(msg_enter, msg_appear):
    message_box = driver.find_element("xpath",msg_enter)
    # Fetch all the messages in the chat
    messages = driver.find_elements("xpath",msg_appear)

    for message in messages:
        sampleany = ["birthday","b'day","bday", "birth day", "returns of the day", "return of the day"]
        sample2any = ["happiest", "happy"]
        samplemust = ["darshana"]

        humanlan1 = ["mchn", "machan", "machn", "mchan", "mcn"]
        humanlan2 = ["kollo", "komlo","kolla"]
        humanlan3 = ["saho", "bro", "brother"]
        humanlan4 = ["lokka", "bosa"]
        humanlan5 = ["sudda", "cudda", "suda"]
        sufix = ""
        
        if all(word1 in message.text.lower() for word1 in samplemust) and any(word2 in message.text.lower() for word2 in sampleany) and any(word3 in message.text.lower() for word3 in sample2any):
            if any(word4 in message.text.lower() for word4 in humanlan2):
                sufix = " kollo"
            elif any(word5 in message.text.lower() for word5 in humanlan1):
                sufix = " machn"
            elif any(word6 in message.text.lower() for word6 in humanlan3):
                sufix = " brother"
            elif any(word7 in message.text.lower() for word7 in humanlan4):
                sufix = " lokka"
            elif any(word8 in message.text.lower() for word8 in humanlan5):
                sufix = " sudda"
            else:
                sufix = ""
            greetings = ['Thank you for the wishes..!', 'Thank you...!!', 'Thanks for the bday wishes..!!']
            addgreetings = random.choice(greetings)
            passgreetings = addgreetings + sufix
            message_box.click()
            message_box.send_keys(passgreetings)
            message_box.send_keys(Keys.ENTER)
            time.sleep(1)
            reply_to_messages(group_chats)
            time.sleep(1)

msg_appear = str(input("Enter Xpath for the left side message appear : "))
msg_enter = str(input("Enter Xpath for the msg typing field : "))
time.sleep(2)

reply_to_messages(group_chats)

while True:
    replyabs(msg_enter, msg_appear)
    time.sleep(5)

# Close the browser
driver.quit()
