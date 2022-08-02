import pytube

link = "https://youtu.be/s3HuIRD5sUY?t=14199"
yt = pytube.YouTube(link)
print("Title:", yt.title)
print("Author:", yt.author)
print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
print("Number of views:", yt.views)
print("Length of video:", yt.length, "seconds")
yt.streams.get_highest_resolution().download()
print("Video successfullly downloaded from", link)
