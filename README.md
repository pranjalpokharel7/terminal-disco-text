# Terminal-Disco-Text
Rapidly color-changing text effect in terminal (plus audio) using python

# External Libraries/Modules (requires pip):

1) art (https://pypi.org/project/art/) - For ASCII-Art of Message
   Installation Command (Linux): 
      pip install art

2) playsound (https://pypi.org/project/playsound/) - For Audio
   Installation Command (Linux):
      pip install playsound
      
# Run Command:

  python3 main.py
 
# For Custom Message:

  Change the value of string message in main.py
  message = "Hello, World!"
 
# Notes:

  1) Major Bug: KeyBoard Interrupt (Ctrl+C) does not stop the audio from playing, although the text effect is interrupted. 
                Will fix this in the next update in which probably a different audio library/module will be preferred.
  
  2) The process will stop when the audio will stop (hence only a 10-second audio is used). Since keyboard interrupt
     will not stop the audio for now, it is advised not to use long audio (on the other hand if you are a developer
     and know a way around this, please leave a comment)
     
  3) Will only work on Linux-based distros for now.

  4) Please add \n (newline escape character) where necessary to prevent jumbling of texts (for custom messages). 
