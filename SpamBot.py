import pyautogui
import time


print("WARNING! 💀")
print("This tool is developed for educational purposes only. If misused, the developers are not responsible.")
print("Copyright © GhostXtbh")
msg = input("Enter the message you want to send: ")
n = input("How many times you want to send the message? : ")

print("Get Ready!")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Fire in the hole!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')