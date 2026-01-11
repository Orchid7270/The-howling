'''
metrics.py
Handles logging of quantitative metrics of disk.
Logging of metrics turns this project from a visual demo.
into a measurable research system

'''
import csv
import os
import time

LOG_FILE = 'evaluation/motion_log.csv'

def init_logger():
    '''Initialize  the csv logger 
    
    1.Creates evaluation folder
    2.Write csv header only once
    
    '''
    os.makedirs('evaluation',exist_ok=True)

    if not os.path.exists(LOG_FILE):
      with open(LOG_FILE,'w',newline= '')as f:
         writer =csv.writer(f)
         writer.writerow([
            'timesstamp,brightness,motion_pixels,mode,fps'])

def log_metrics(brightness,motion_pixels,mode,fps):
   '''Append one row of metrics to the CSV file
   Logged every frame so we can:
   1.Analyse behaviour offline
   2.Plot trends
   3.Co-relate with observations
   '''
   with open(LOG_FILE,'a',newline = '')as f:
      writer = csv.writer(f)
      writer.writerow([
         time.strftime('%Y-%m-%d %H: %M: %S'),
                              round(brightness,2),
                              int(motion_pixels),
                              mode,
                              round(fps,2)       
                                     ])