import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from WhatsApp_Responses import response 

#Mouse click
mouse = Controller()

class WhatsApp:
    
    #Starting Values
    def __init__(self, speed = .5, click_speed = .5):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
    
    #Navigate to the green dots for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        # except Exception as e:
            # print('Exception (nav_green_dot):', e)
        except:
            print("No new messages!!")
    
    #Navigate to the text box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 25, duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        # except Exception as e:
            # print('Exception (nav_input_box):', e)
        except:
            print("No new messages!!")
    
    #Navigate to the message we want to copy
    def nav_move_to_message(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-37, -71, duration = self.speed)
        # except Exception as e:
            # print('Exception (nav_input_box):', e)
        except:
            print("No new messages!!")
        
    #Copying the message
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)   
        pt.moveRel(40, -280, duration=self.speed)
        mouse.click(Button.left, 2)
        sleep(1)    
        # sleep(self.speed)
        self.message = pc.paste()
        print("The user said: ", self.message)
        
    #Sends the message to the user
    def send_message(self):
        try:
            if(self.message!=self.last_message):
                bot_response = response(self.message)
                print("You said: ", bot_response)
                pt.typewrite(bot_response, interval=.1)
                # Enter key 
                pt.typewrite('\n')
                self.last_message = self.message
            else:
                print("No new messages!\n")
        except:
            print("Send_message function did not work!!\n")
wa_bot = WhatsApp(speed = .7, click_speed=.8)
sleep(2)
while(1):
    # wa_bot.nav_green_dot()
    wa_bot.nav_input_box()
    wa_bot.nav_move_to_message()
    wa_bot.get_message()
    wa_bot.send_message()


