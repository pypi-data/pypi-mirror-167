from typing import List
from formant.protos.model.v1 import navigation_pb2
from formant.sdk.agent.v1.localization.utils import validate_type, get_ros_module
from .transform import Transform


class Map:
    @classmethod
    def from_ros(cls, map):
        nav_msgs = get_ros_module("nav_msgs.msg")
        validate_type(map, nav_msgs.OccupancyGrid)
        return cls(
            map.info.resolution,
            map.info.width,
            map.info.height,
            origin=Transform.from_ros_pose(map.info.origin),
            occupancy_grid_data=map.data,
        )

    def __init__(
        self,
        resolution: float,
        width: float,
        height: float,
        origin: Transform = Transform(),
        transform_to_world: Transform = Transform(),
        url: str = None,
        raw_data: bytes = None,
        occupancy_grid_data: List[int] = None,
    ):
        self.resolution = resolution
        self.width = width
        self.height = height
        self.origin = origin
        self.transform_to_world = transform_to_world
        self.url = url
        self.raw_data = raw_data
        self.occupancy_grid_data = occupancy_grid_data

    def to_proto(self):
        map = navigation_pb2.Map(
            resolution=self.resolution,
            width=self.width,
            height=self.height,
            origin=self.origin.to_proto(),
            world_to_local=self.transform_to_world.to_proto(),
            url=self.url,
            raw=self.raw_data,
        )
        if self.occupancy_grid_data is not None:
            map.occupancy_grid.data.extend(self.occupancy_grid_data)
        return map
