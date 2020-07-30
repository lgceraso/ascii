import os
import sys
import cv2
from PIL import Image

files = os.listdir()
if "imgs" not in files:
    os.system("mkdir imgs")

def check(video):
    cap = cv2.VideoCapture(video)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if width != 1280 and height != 720:
        print("-> Resolution: ERROR")
        os.system("ffmpeg -i {} -s 1280x720 out.mp4".format(video))
        os.system("mv out.mp4 {}".format(video))
    else:
        print("-> Resolution: PASS")
    if fps != 30:
        print("-> Frames: ERROR")
        os.system("ffmpeg -i {} -filter:v fps=fps=30 out.mp4".format(video))
        os.system("mv out.mp4 {}".format(video))
    else:
        print("-> Frames: PASS")

def concat(video):
    os.system("printf 'file check.mp4\nfile {}' > list.txt ".format(video))
    os.system("ffmpeg -f concat -i list.txt play.mp4")
    os.system("ffmpeg -i play.mp4 -vn aud.mp3")

def play(delay):
    os.system("st -f Hermit:pixelsize=5 -e python {}/run.py -play & sleep {} && mpv aud.mp3".format(path,delay))

def convert():
    cap = cv2.VideoCapture("play.mp4")
    os.chdir("imgs/")
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite('p'+str(i)+'.jpg',frame)
        i+=1
    os.chdir("..")

def ascii():
    imgs = os.listdir("imgs/")
    os.chdir("imgs")
    count = 0
    for c in imgs:
        if ".jpg" in c:
            img = Image.open("p{}.jpg".format(count))
            width, height = img.size
            aspect_ratio = height/width
            new_width = 500
            new_height = aspect_ratio * new_width * 0.5
            img = img.resize((new_width, int(new_height)))
            img = img.convert('L')
            pixels = img.getdata()
            chars = ["@","#","S","%","?","*","+",";",":",",","."]
            new_pixels = [chars[pixel//25] for pixel in pixels]
            new_pixels = ''.join(new_pixels)
            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)
            print(ascii_image)
            count +=1

video = sys.argv[1]
if ".mp4" in video:
    check(video)
elif ".mkv" in video:
    print("-> Invalid file format.")
    op = input("Do you wanna change it? [Y/N] ").lower()
    if op == "y":
        os.system("ffmpeg -i {} temp.mp4".format(video))
        video = video.split(".")
        os.system("mv temp.mp4 {}.mp4".format(video[0]))
        exit()
    else:
        exit()
elif "-play" in video:
    ascii()
    exit()
else:
    print("-> Specify the correct file format.")
    exit()

path = os.getcwd()

while True:
    os.system("clear")
    try:
        op = int(input("""-> Select an option:
[1] - Convert
[2] - Play
[3] - Exit
"""))
        os.system("clear")
        if op == 1:
            print("-> Loading...")
            concat(video)
            convert()
        elif op == 2:
            delay = float(input("-> How much delay? [Default = 0.5] "))
            play(delay)
        elif op == 3:
            break
        else:
            print("-> Invalid option")
            break
    except Exception as e:
        print(e)
