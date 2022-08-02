from abstract_for_video import *
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip
import os


class GetTikTok(GetVideoFrom):
    """Сlass accesses the tiktok api. Download video and save as mp4 file"""

    @classmethod
    def download_by_url(cls, url):
        """Download TikTok video by url"""
        api = TikTokApi()

        try:
            video = api.video(url=url)
        except:
            raise ConnectionError('Something go wrong, check url')

        video_data = video.bytes()
        cls.save_video_to_file(video_data)

    @staticmethod
    def save_video_to_file(video):
        """Save TikTok video into mp4 file"""
        with open("some_video.mp4", "wb") as out_file:
            out_file.write(video)


class VideoToGif:
    """Class takes an mp4 video from the current directory,
    converts it to a gif file and returns the path to this file"""
    GIF_COUNT = 1

    @classmethod
    def convert_to_gif(cls):
        """Limit video fps, convert video to GIF and save into file"""

        try:
            video_clip = VideoFileClip("some_video.mp4").set_fps(20)  # fps limit for smaller file size
        except IOError:
            raise IOError('Something go wrong, check file name')

        video_clip.write_gif(f"TikTok-example-{cls.GIF_COUNT}.gif")

    @classmethod
    def path_return(cls):
        """Return abs path to GIF file"""
        cls.convert_to_gif()
        path = os.path.abspath(f"TikTok-example-{cls.GIF_COUNT}.gif")
        cls.GIF_COUNT += 1
        return path


some_tiktok = 'https://www.tiktok.com/@notjasonprt1/video/7065459675273415982'
GetTikTok.download_by_url(some_tiktok)
print(VideoToGif.path_return())

some_tiktok = 'https://www.tiktok.com/@artemmihas_1/video/7103035022675922182'
GetTikTok.download_by_url(some_tiktok)
print(VideoToGif.path_return())

