from pytube import YouTube


def download(link: str):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


if __name__ == "__main__":
    link_in = input("Enter the YouTube video URL: ")
    download(link_in)
