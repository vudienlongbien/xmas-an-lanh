import datetime
import subprocess

now = datetime.datetime.now()
start = datetime.datetime(now.year,12,25,0,0,0)
end = datetime.datetime(now.year,12,26,0,0,0)
if start <= now <=end :
  subprocess.run(["figlet", "-f", "slant", 'Merry Xmas'])
  subprocess.run([
    "termux-notification",
    "--title", "🎄 Merry Christmas",
    "--content", "chuc mung Giang sinh tu idk.py!",
    "--sound",                              
    "--vibrate", "500,100,500",                           
  ])
elif now <= start:
  tgian_conlai = start - now
  ngay_conlai = tgian_conlai.days
  print(f"noooo chua den noel 🎄, con {ngay_conlai} ngay nua!")
else:
  print("het noel roi ban oi cho nam sau nhe :D")
