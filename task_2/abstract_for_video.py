from abc import ABC, abstractmethod


class GetVideoFrom(ABC):
    """Abstract class that implements methods for working with a video file from different services"""

    @classmethod
    @abstractmethod
    def download_by_url(cls, url):
        """Abstract API video download method by url """
        pass

    @staticmethod
    @abstractmethod
    def save_video_to_file(video):
        """Abstract method to save video to file"""
        pass
