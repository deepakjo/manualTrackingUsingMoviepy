from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking

def track_coords(videoName, start, end, noObj):
    clip = VideoFileClip(videoName).subclip(start, end)
    trajectories_team = manual_tracking(clip, t1=start, t2='00:11:37.51', \
                                        fps=1, nobjects=noObj,
                                        savefile="track_t1.txt")

    a=list()
    b=list()
    for coords in trajectories_team:
        a.append(coords.xx.tolist()[0])
        b.append(coords.yy.tolist()[0])
        print a, b

    team_coords=zip(a,b)
    print 'team coordinates', team_coords
    clip.close()
    return team_coords
