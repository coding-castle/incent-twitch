from stream import get_stream_url, watch_stream, filter_black_images, clean_dir
from text_detection import detect
import cv2
import time
from multiprocessing import Process
import threading
import os
import glob


processes = []
results = []

streamers = [
    "agurin"
]

def main(streamer):
    stream_url = get_stream_url(streamer)
    print(stream_url)
    if stream_url == "":
        return
    process = watch_stream(stream_url, streamer)
    print("waiting for the twitch screen")
    time.sleep(40)
    print("start listening...")
    for i in range(6):
        # do recognition
        files = glob.glob(streamer + '/**/*.jpg', recursive=True)
        for file in files:
            image = cv2.imread(file, 0)
            if cv2.countNonZero(image) == 0:
                print("Image is black")
                os.remove(file)
            else:
                matches = detect(file)
                if len(matches) > 0:
                    # wow found code, do smth
                    results.append(matches)
                os.remove(file)

        time.sleep(10)
    process.kill()
    print("done")

for streamer in streamers:
    p = Process(target=main, args=(streamer,))
    processes.append(p)
    p.start()

for t in processes:
    t.join()

print("actually done")
print(results)
#matches = detect("gtawiseguy/output_00007.jpg")
#matches = detect("example.png")
# print(matches)

