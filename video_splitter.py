__author__ = "the_pythonist"
"""I felt like mentioning here that $NANO is going to shock the world. Looking forward to that point in time with faith.
I might be wrong, but let's see what God makes happen"""

from moviepy.editor import *

def video_split(video_name, split_at, out_name):
    """ :video_name - File name of the video to be splitted.
    :split_at - Length for each splitted video created.
    :out_name - Name to append to every outputed splitted video. NOTE: this is used as first part of output files,
    the second part have numbers attached to them, e.g [out_name]_0, [out_name]_1, [out_name]_2"""
        
    full_vid = VideoFileClip(video_name)   # Load the video to be splitted

    duration = full_vid.duration # what is video duration

    file_name_count = 0 # Counter that will be appended to file_name of splitted videos

    """We set starting split position at 0."""
    split_position = 0


    """Then, we loop through the video duration as long as split_position
    is less than duration.
    :split_position is updated every time we split the video at :split_at"""
    while split_position < duration:

        try:

            """:if statement to spot when :split_position is at the point of the video where selecting up to 120 seconds
            next become unfeasible (i.e, when the last clip to be selected is less than 120 seconds). It then
            raises a KeyError exception that executes the :except block which comes later. 
            N.B: There's no particular reason for choosing :KeyError except, you can as well use other excepts, just
            choose wisely ;-)"""
            if (duration - split_position) < split_at:
                raise KeyError

            """A sub video is created every 2 minutes until :split_position exceeds
            duration
            """
            sub_video = full_vid.subclip(split_position, split_position+split_at)
            """:split_position updates to next 2 minutes (120 secs)"""
            split_position += split_at

            """Write each :sub_video file"""
            sub_video.write_videofile(f"{out_name}_{file_name_count}.mp4", codec="libx264")
            file_name_count += 1 # increment by 1 to produce new :sub_video file names


        except KeyError:
            """An OSError is what is raised if MoviePy is unable to get a subclip
            for the video range specified.
            At some point in our :while loop, we expect that the last :sub_video
            group might not be up to 120 seconds. Hence, the need for the
            try-expect statement to look out for that point"""


            """# splits video from last split_position up to the end
            of the OG video file (:full_vid)"""
            sub_video = full_vid.subclip(split_position, )

            sub_video.write_videofile(f"{out_name}_{file_name_count}.mp4", codec="libx264")
            
            split_position += split_at # so we can breakout of loop and not have an infinite loop


video_split("nicos.mp4", 120, "Nicos")
