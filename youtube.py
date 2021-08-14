from pytube import YouTube

link = input("Enter link to download: ")
file = YouTube(link)

print("Title: ", file.title)
print("Lenght: ", int(file.length / 60), ":", file.length % 60)

ext = input("Audio or video: ")
if ext == "Audio" :
    print("Generating list of streams...")
    print("\n")
    print(file.streams.filter(only_audio=True))
    print("\n")
if ext == "Video" :
    print("Generating list of streams....")
    print("\n")
    print(file.streams.filter(only_video=True))
    print("\n")
tag = input("Select a stream to download by tag: ")
if tag == "stop" :
    print("Closing...")
    exit()
    print("Program closed successfully!")

ys = file.streams.get_by_itag(tag)
print("Size of selected stream: ", round(ys.filesize / 1000000, 2), "MBs")
finish = input("Press 1 to download, 2 to exit: ")
if finish == "1":
    print("Downloading...")
    ys.download()
    print("Download finished!")
if finish == "2":
    print("Closing...")
    exit()
    print("Program closed successfully!")
