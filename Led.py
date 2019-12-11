import RPi.GPIO as GPIO             
import time                        
GPIO.cleanup()                    
led_pin = 37                       
motion_pin = 35                    
def init():
  GPIO.setmode(GPIO.BOARD)         
  GPIO.setwarnings(False)   
  GPIO.setup(led_pin,GPIO.OUT)                              
  GPIO.setup(motion_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  
  print("-----------------------------------------------------------------------")  

def main():
  while True:
    value=GPIO.input(motion_pin)  
    if value!=0:                             
      GPIO.output(led_pin,GPIO.HIGH)                
      time.sleep(2)        
      print ("LED on")                           
      
    else:
      GPIO.output(led_pin,GPIO.LOW)                
      time.sleep(2)       
      print ("LED off")                         

init()
main()
GPIO.cleanup()