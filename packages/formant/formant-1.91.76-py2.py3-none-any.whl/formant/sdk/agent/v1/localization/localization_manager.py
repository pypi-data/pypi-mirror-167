import time
from threading import Lock
from typing import Dict, Optional
from formant.protos.model.v1 import navigation_pb2, datapoint_pb2
from formant.sdk.agent.v1.localization.types import (
    Odometry,
    Path,
    Goal,
    Map,
    PointCloud,
)

MIN_TIME_BETWEEN_MESSAGES = 0.2
DEFAULT_POINTCLOUD_NAME = "defualt"


class LocalizationManager:
    def __init__(self, stream_name: str, client):
        self._client = client
        self._stream_name = stream_name  # type: str
        self._last_sent_time = time.time()  # type: float
        self._lock = Lock()
        self._cached_odometry = None  # type: Optional[Odometry]
        self._cached_map = None  # type: Optional[Map]
        self._cached_point_clouds = {}  # type: Dict[str, PointCloud]
        self._cached_path = None  # type: Optional[Path]
        self._cached_goal = None  # type: Optional[Goal]

        self._tags = {}  # type: Dict

    def update_point_cloud(
        self, point_cloud: PointCloud, cloud_name=DEFAULT_POINTCLOUD_NAME
    ):
        with self._lock:
            self._cached_point_clouds[cloud_name] = point_cloud
        self._try_send_localization()

    def invalidate_pointcloud(self, cloud_name: str = DEFAULT_POINTCLOUD_NAME):
        with self._lock:
            del self._cached_point_clouds[cloud_name]
        self._try_send_localization()

    def update_odometry(self, odometry: Odometry):
        with self._lock:
            self._cached_odometry = odometry
        self._try_send_localization()

    def update_map(self, map: Map):
        with self._lock:
            self._cached_map = map
        self._try_send_localization()

    def update_path(self, path: Path):
        with self._lock:
            self._cached_path = path
        self._try_send_localization()

    def update_goal(self, goal: Goal):
        with self._lock:
            self._cached_goal = goal
        self._try_send_localization()

    def set_tags(self, tags: Dict):
        with self._lock:
            self._tags = tags

    def _try_send_localization(self):
        with self._lock:
            # Localization requires odometry
            if self._cached_odometry is None:
                return
            # Don't send messages too fast
            now = time.time()
            if now - self._last_sent_time < MIN_TIME_BETWEEN_MESSAGES:
                return
            self._last_sent_time = now

            map = self._cached_map
            odometry = self._cached_odometry
            path = self._cached_path
            goal = self._cached_goal
            point_clouds = self._cached_point_clouds
            tags = self._tags

        localization = navigation_pb2.Localization(
            map=protected_to_proto(map),
            odometry=protected_to_proto(odometry),
            path=protected_to_proto(path),
            goal=protected_to_proto(goal),
        )
        if len(point_clouds.keys()) != 0:
            del localization.point_clouds[:]
            localization.point_clouds.extend(
                [point_cloud.to_proto() for point_cloud in point_clouds.values()]
            )

        self._client.agent_stub.PostData(
            datapoint_pb2.Datapoint(
                stream=self._stream_name,
                localization=localization,
                tags=tags,
                timestamp=int(time.time() * 1000),
            )
        )


def protected_to_proto(obj):
    if obj is None:
        return None
    return obj.to_proto()
