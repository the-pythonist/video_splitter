# video_splitter
Split your videos into smaller sections (lengths) with ease :-)


#### Motivation for this video splitter program.
So at the point of writing this code, I was learning the German language. Part of my learning resource is the "Nicos weg" series by Deutsche Welle (DW), available here: https://learngerman.dw.com/de/nicos-weg/c-36519687. A compiled video of all the sections of the A1 serie can be found on YouTube here: https://www.youtube.com/watch?v=4-eDoThe6qo.

Because I wanted to learn on the go using bite-sized learning, I intended to have the entire video compilation in bits of about 2 minutes length. This would mean that I have the luxury to go over the series in bits of 2 minutes which I could repeat (while walking, cooking, doing chores etc.) until I have a grasp on the words, grammar and context; before moving on to the next 2 minutes. P.S: You might consider a 'bite-sized' approach if you happen to be a German learner.

To this end, I decided to write a program that took the compiled video available here: https://www.youtube.com/watch?v=4-eDoThe6qo; and splits the video into sub videos of 2 minutes length. Und jetzt, learning made easy :-). This meant a total number of 52 sub videos.

#### How can you use this program?
Good news is that you can apply this program I've written to any video for which you might want to split.

#### What you need?
You only need the following to conveniently use the program:
- Knowledge of the video you would like to split.
- Knowledge of the minutes you want for each sub video (i.e, At what times do you want to split your video).
- Python installed from here: https://www.python.org/downloads/
- After successfull install of Python, install MoviePy (https://pypi.org/project/moviepy/)
  - Simply fire up your command prompt (cmd.exe) and type in: pip install moviepy

#### The Process
I made use of the MoviePy library available here: https://pypi.org/project/moviepy/. You can find the documentation here: https://zulko.github.io/moviepy/. 


![image](https://user-images.githubusercontent.com/68852419/147521840-12179e72-d19f-4247-99d9-dd98e4d300d8.png)

The above image is a screen shot of the 'progress report' MoviePy offers while it works on your video.
###### You only need to call the video_split function and put in two parameters: video_name and intended length for the splitted videos.


#### The Result
###### Und jetzt habe ich mehrere kleines Video vom Ganzen Video vom Nicos Weg (And now I have several smaller videos from the entire Nicos Weg video compilation).


#### How this program can be made better?
So this video in mention by Deutsche Welle is already originally designed in bits here: (https://learngerman.dw.com/de/nicos-weg/c-36519687). The only problem is that having to download each of the video files seperately is a pain, hence the invention for this Python code. This code/program can be made much better though, read on.
- The MoviePy library includes means to split videos at certain points. These points could be identified by specific characteristics such as points of increased video loudness, points of black screen, points in which a certain soundtrack is used etc. Using these calculatively, one could with a better version of a video splitter - that goes beyond just splitting at consistent times - to splitting the video based on these aforementioned video characteristics that could help identify if a video section (e.g as applicable to the Nicos Weg series) has ended and if one is beginning.

- This program could have included a GUI interface that abstracts the code. 
##### P.S: You could probably also employ some web interaction with Python to automatically download all the video sections on the DW site. A story for another though, haha.


#### Why didn't I do a sophisticated version?
Time. As a Master's degree student in Cybersecurity, I probably don't have that luxury of time. And afterall, this program worked for me as is. 
Probably a factor to was no 'ginger' (that's pidgin). Anyways, moving forward .....

###### If you are a Python developer and feel you can implement the above; please feel free to fork or I'll happily make you a Manager.


#### And voilà, das ist alle. viele Erfolg und mach's gut. (And there, that is all. Much success and take care :-D )

If you need to contact me, here you go: gadawesome@gmail.com.
