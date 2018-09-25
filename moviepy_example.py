# Import everything needed to edit video clips
import sys
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

print 'len:', len(sys.argv)
print 'video name', sys.argv[1]
print 'start:', sys.argv[2]
print 'end:', sys.argv[3]
videoName = sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("Downloads/mjRH6T.mp4").subclip(start,end)
logo=ImageClip("Downloads/textlogo.jpg").set_duration(clip.duration).resize(height=50).margin(right=8, top=8, opacity=0).set_pos(("right","top"))
rev_clip = clip

clip=CompositeVideoClip([clip, logo])
rev_clip=CompositeVideoClip([rev_clip, logo])

clip=speedx.speedx(clip, final_duration=(end - start) + 20)
rev_clip=speedx.speedx(rev_clip, final_duration=(end - start) + 20)

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(0.1)
clip = clip.without_audio()


# Say that you want it to appear 10s at the center of the screen
_txt=TextClip("www.tactification.com", fontsize=70, color='white')
_txt=_txt.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt], size=clip.size)

_rev_txt=TextClip("reverse replay", fontsize=70, color='white')
_rev_txt=_rev_txt.set_position('center').set_duration(1)
rev_txt = CompositeVideoClip( [_rev_txt], size=rev_clip.size)

rev_clip=time_mirror.time_mirror(rev_clip)
final = concatenate_videoclips([txt, clip, rev_txt, rev_clip])
# Overlay the text clip on the first video clip

# Write the result to a file (many options available !)
final.write_videofile("Downloads/finalpost31.mp4", fps=60)
