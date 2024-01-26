import pandas as pd
import urllib.request
import re
from pytube import YouTube

html = urllib.request.urlopen('https://www.youtube.com/')
def find_yt_link(title,artist,index):

    html2 = urllib.request.urlopen("https://www.youtube.com/results?search_query="+title.replace(" ", "+")+artist.replace(" ", "+"))
    # print(html2.read().decode())
    video_ids = re.findall(r"watch\?v=(\S{11})", html2.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[index])

    yt = YouTube("https://www.youtube.com/watch?v=" + video_ids[index])
    try:
        #can set resolution, unfortunately not highier than 720.
        video = yt.streams.get_by_resolution("144p")
        #where we download
        video.download(r'C:\Name\Youtube_Downloaded_Videos\Dobre_Rapsy_playlist')
        print("Download complete.")
    except AttributeError as e:
        find_yt_link(title, artist, index+1)



# from where we download (csv file, in exel, you can easily find website that will allow you to do that to your spotify playlist
#
excelFile_location = 'C:\\Users\\Name\\Downloads\\dobre_rapsy.csv'
df_track = pd.read_csv(excelFile_location)
# df_track.info()
print(len(df_track))
print(df_track['Track Name'])
count=0
for item in df_track['Track Name']:
    #useful when errors happen
    if count>-1:
        track = str(item)
        print(track)
        artist = str(df_track.loc[count,"Artist Name(s)"])
        print(artist)
        find_yt_link(track, artist,0)
        count += 1
    else:
        count += 1




