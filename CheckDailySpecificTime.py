import os
import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox
from appdirs import user_data_dir
from datetime import datetime, date, time, timezone, timedelta
import function as fun

print('\nPlease wait a while...')

app_name = 'MakeScript'
date = datetime.now(timezone.utc)
year = date.timetuple()[0] - 2000 #*ex) 24 = 2024 - 2000
month = date.timetuple()[1]
day = date.timetuple()[2]
if month - 6 <= 0 :
    sem = f'S{year}A'
    data_dir = user_data_dir(app_name)
else:
    sem = f'S{year}B'
    data_dir = user_data_dir(app_name)
stime_file_path = os.path.join(data_dir, '.' + sem + 'stime.txt')

#*get SAST
timezone_sa = timezone(timedelta(hours=2))
date_sa = datetime.now(timezone_sa)

text_list = []
with open(stime_file_path, mode='r') as f:
    lines = f.readlines()
    for i, row in enumerate(lines):
        row_tmp = row.rstrip('\n')
        row_scm = re.split(',', row_tmp) #*split with comma
        script_name = row_scm[0]
        block_id = row_scm[1]
        stime = row_scm[2]
        stime_sub = re.split('_', stime) #*split with under bar
        utc = stime_sub[0]
        if utc == 'UTC':
            start_tar = stime_sub[1]
            start_tar_scl = re.split(':', start_tar) #*split with colon
            start_hour = start_tar_scl[0]
            start_min = start_tar_scl[1]
            end_tar = stime_sub[2]
            end_tar_scl = re.split(':', end_tar) #*split with colon
            end_hour = end_tar_scl[0]
            end_min = end_tar_scl[1]
            date_tar = stime_sub[3]
            date_tar_ssl = re.split('/', date_tar) #*split with slash
            day_tar = date_tar_ssl[0]
            month_tar = date_tar_ssl[1]
            year_tar = date_tar_ssl[2]

            if int(month) == int(month_tar):
                if int(day) == int(day_tar):
                    if int(start_hour) > 12:
                        utc_datetime_start = datetime(int(year_tar), int(month_tar), int(day_tar), int(start_hour), int(start_min))
                        if int(end_hour) >= int(start_hour):
                            utc_datetime_end = datetime(int(year_tar), int(month_tar), int(day_tar), int(end_hour), int(end_min))
                        elif int(end_hour) < int(start_hour):
                            utc_datetime_end = datetime(int(year_tar), int(month_tar), int(day_tar) + 1, int(end_hour), int(end_min))
                        sast_start = fun.utc2sast(utc_datetime_start)
                        sast_end = fun.utc2sast(utc_datetime_end)
                        row_new = script_name + ', ' + block_id + ', ' + str(sast_start.date()) +' '+ str(sast_start.time()) + ' - ' + str(sast_end.date()) +' '+ str(sast_end.time()) + ' (SAST)\n'
                        text_list.append(row_new)
                    else:
                        pass
                elif int(day) == int(day_tar) - 1:
                    if int(start_hour) < 12:
                        utc_datetime_start = datetime(int(year_tar), int(month_tar), int(day_tar), int(start_hour), int(start_min))
                        utc_datetime_end = datetime(int(year_tar), int(month_tar), int(day_tar), int(end_hour), int(end_min))
                        sast_start = fun.utc2sast(utc_datetime_start)
                        sast_end = fun.utc2sast(utc_datetime_end)
                        row_new = script_name + ', ' + block_id + ', ' + str(sast_start.date()) +' '+ str(sast_start.time()) + ' - ' + str(sast_end.date()) +' '+ str(sast_end.time()) + ' (SAST)\n'
                        text_list.append(row_new)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

text = "Today's spesific time targets list:\n\n"
for i in text_list:
    text += i

def close_program():
    print('\nQuit CheckDailySpecificTime.py.\nSee you tomorrow!')
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()

messagebox_window = tk.Toplevel(root)
messagebox_window.geometry("600x300")

messagebox_window.protocol("WM_DELETE_WINDOW", close_program)

message_label = ttk.Label(messagebox_window, text=text, wraplength=580)
message_label.pack(pady=20, padx=10)

root.mainloop()




