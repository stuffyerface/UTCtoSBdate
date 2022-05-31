from datetime import datetime,timezone
import math
SKYBLOCK_YEAR_114 = 1610718900
SKYBLOCK_YEAR_LENGTH = 446400
SKYBLOCK_MONTH_LENGTH = 37200
SKYBLOCK_DAY_LENGTH = 1200
SKYBLOCK_HOUR_LENGTH = 50
SKYBLOCK_10MIN_LENGTH = 8.34

UTCtime = 1653930755887 ## Timestamp from SB item nbt

def currentdate():
  ogDate = int(datetime(2021, 1, 15, 13, 55).timestamp())
  #print(ogDate)
  testDate = int(UTCtime/1000)
  #print(testDate)
  timesince = math.floor(testDate - ogDate)
  #print(timesince)
  #timesince = now.total_seconds()
  sbyear = 114
  sbmonth = 0
  sbday = 0
  sbhour = 0
  sbminute = 0
  while(timesince >= SKYBLOCK_YEAR_LENGTH):
    timesince -= SKYBLOCK_YEAR_LENGTH
    sbyear += 1
  while(timesince >= SKYBLOCK_MONTH_LENGTH):
    timesince -= SKYBLOCK_MONTH_LENGTH
    sbmonth += 1
  while(timesince >= SKYBLOCK_DAY_LENGTH):
    timesince -= SKYBLOCK_DAY_LENGTH
    sbday +=1
  while(timesince >= SKYBLOCK_HOUR_LENGTH):
    timesince -= SKYBLOCK_HOUR_LENGTH
    sbhour +=1
  while(timesince >= SKYBLOCK_10MIN_LENGTH):
    timesince -= SKYBLOCK_10MIN_LENGTH
    sbminute += 10
  return [sbyear, sbmonth, sbday, sbhour, sbminute]

current_date = currentdate()
#print(current_date)
sbmonths = ["Early Spring", "Spring", "Late Spring", "Early Summer", "Summer", "Late Summer", "Early Autumn", "Autumn", "Late Autumn", "Early Winter", "Winter", "Later Winter"]

sbdays = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th",  "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"] 
dN = "am"
sbmonth = sbmonths[current_date[1]]
sbday = sbdays[current_date[2]]

if (current_date[3] > 11):
    sbhour = current_date[3] - 12
    dN= "pm"
elif(current_date[3] == 0):
    sbhour = 12
else:
    sbhour = current_date[3]
if (current_date[4] == 0):
    sbmin = "00"
else:
    sbmin = current_date[4]
    
print(f"{sbmonth} {sbday} at {sbhour}:{sbmin}{dN}")
