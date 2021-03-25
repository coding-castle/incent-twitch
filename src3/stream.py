from streamlink import Streamlink
import subprocess
import time
import os
import glob
from pathlib import Path
import cv2


def get_stream_url(streamer):
    s = Streamlink()
    url = "https://twitch.tv/" + streamer
    streams = s.streams(url)
    if streams == {}:
        return ""
    stream = streams["best"]
    fd = stream.open()
    stream_url = fd.writer.stream.url
    fd.close()
    return stream_url


def clean_dir(dir_name):
    files = glob.glob(dir_name + '/**/*.jpg', recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def ensure_dir(dir_name):
    Path(dir_name).mkdir(parents=True, exist_ok=True)


def filter_black_images(dir_name):
    files = glob.glob(dir_name + '/**/*.jpg', recursive=True)
    for file in files:
        os.remove(file)
        # image = cv2.imread(file, 0)
        # if cv2.countNonZero(image) == 0:
        #     print("Image is black")
        # else:
        #     continue

def watch_stream(stream_url, streamer):
    clean_dir(streamer)
    ensure_dir(streamer)
    process = subprocess.Popen(['ffmpeg', '-i', stream_url, '-r', '1/10', '-f', 'image2', streamer + '/output_%05d.jpg'])
    return process
    

# os.system("mkdir " + name)
# process = subprocess.Popen(['ffmpeg', '-i', stream_url, '-r', '1/10', '-f', 'image2', name + '/output_%05d.jpg'])
# time.sleep(60)
# process.kill()

# out, err = (
#     ffmpeg
#     .input(stream_url)
#     .filter('select', 'gte(n,{})'.format(1))
#     .output('output.jpg', vframes=1, format='image2', vcodec='mjpeg')
#     .overwrite_output()
#     .run(capture_stdout=True)
# )

# ffmpeg -i https://video-weaver.fra02.hls.ttvnw.net/v1/playlist/CoQEMtjRNNtYOritJEr40QCAbBRu2rGljAhclH9YJAZXTuqmm8QVwc4TSO0QKA4FJqql-sz5CblTcWJFu4TB6GeC30Yowz_haKMi0pUPRwmlpSZFs69tTNPz9dRP6TnYHnjz9Q0EC-WN8edH7mvN5nQ9YtmGzb7W7SYs5P_et3wJMjtqEqGrZXxVKTDPgoynH3v6prpBNv6Nk9JOMrMxxyOjTZBtms3yoe4c4bAgmX5PG9qpvYstAwoRjRdB2Y5DI3JbXeoMTylk756-HVbCoY0yup3nD_GEiNN9Ze1ZY_bmPQ6-7NlUeMkK1KIzqGdBdPFNQi_PpG6lIHy0q1vrNls_j9edxVs0o2Wu-Zk6V5eP_T4mTeBJS7JvtBTCmeEqhTLEslAFLMBVXVMfq2snl3hvj4E19OlGFbXtaQt8VXB67W40_jQOZafUPAKF2kICkR64okPlz9E7TkSwvor2oqsAIuOX-PA5nCU4IP5rc6Q8IX0qoBWC_ldIuofzaw8z5FQaKZrdpSl0JP4C2ZVsakQASMZul9BUpF7zJCGfaJERQMAbojfXtihC3XANjTHltgAA-us0cIE19awYR-v775GBvBZt0IDRW7qOBM-V0ZwisJ1u1Ej9TuGxJ9yUo3aUx9oMbss3NlsV2Mqps1WS2ychH984CitbNasYBU9zzDOOzbSKfS_eEhCF6UszQCrZTyzVSa1FkoMlGgwS8JzXbODblCrTYB8.m3u8 -r 0.5 -f image2 output_%05d.jpg
# with open("output.mp4", "wb") as of:
#     shutil.copyfileobj(fd, of)
