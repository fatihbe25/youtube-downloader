from pytube import YouTube

def Download(link,n):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred",n)
    print("Download is completed successfully" , n)


#link = input("Enter the YouTube video URL: ")
#Download(link)

file1 = open('list.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    Download(line,count)

