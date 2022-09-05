import heapq
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Video:
    content: str
    likes: int = 0
    dislikes: int = 0
    views: int = 0

    def __len__(self) -> int:
        return len(self.content)


class VideoSharingPlatform:
    _videos: Dict[int, Video]
    _available_ids: List[int]

    def __init__(self):
        self._videos = {}
        self._available_ids = []
        self._max_id = 0

    def _pick_id(self) -> int:
        if self._available_ids:
            return heapq.heappop(self._available_ids)

        video_id = self._max_id
        self._max_id += 1

        return video_id

    def upload(self, video: str) -> int:
        video_id = self._pick_id()

        self._videos[video_id] = Video(video)

        return video_id

    def remove(self, videoId: int) -> None:
        if videoId not in self._videos:
            return

        self._videos.pop(videoId)
        heapq.heappush(self._available_ids, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self._videos:
            return "-1"

        video = self._videos[videoId]
        video.views += 1

        return (
            video.content[min(startMinute, len(video)) : min(endMinute + 1, len(video))]
            or "-1"
        )

    def like(self, videoId: int) -> None:
        if videoId not in self._videos:
            return

        self._videos[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId not in self._videos:
            return

        self._videos[videoId].dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self._videos:
            return [-1]

        video = self._videos[videoId]

        return [video.likes, video.dislikes]

    def getViews(self, videoId: int) -> int:
        if videoId not in self._videos:
            return -1

        video = self._videos[videoId]

        return video.views


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
