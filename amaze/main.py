import numpy as np
import imageio
import logging

TOOL_NAME = 'amaze'
LOG = logging.getLogger(TOOL_NAME)

# I'd like to build this a bit differently.
# I want it to roll for a total number of points, then spend the points on rooms
# and things in the rooms. For now we'll just get the basics working.
class Dungeon:
    """Contains all the details of a dungeon map."""

    def __init__(self, map_x=64, map_y=64, max_rooms=15, min_room_xy=5, max_room_xy=10):
        self.map_x = map_x
        self.map_y = map_y
        self.max_rooms = max_rooms
        self.min_room_xy = min_room_xy
        self.max_room_xy = max_room_xy
        self.rooms = []
        self.image_filename = 'test.png'
        self.map_array = np.zeros((self.map_x, self.map_y), dtype=np.uint8)
        self.image_array = None

    def create_room(self, x, y):
        self.rooms.append(np.ones((x,y), dtype=np.uint8))

    def place_room_at_xy(self, room, x, y):
        # needs error checking that room fits in full_map at x,y
        # can use ValueError it throws, or check validity before hand
        # with full_map.shape
        self.map_array[x:x + room.shape[0], y:y + room.shape[1]] = room

    # a function to convert map_array -> image_array, the full bitmap for imwrite
    # def map_to_image_array(self):

    def to_png(self):
        LOG.info(f"Saving {self.map_array.shape} map_array to {self.image_filename}.")
        imageio.imwrite(self.image_filename, self.map_array)


def _main():
    """Setup and start the dungeon create utility."""
    dungeon = Dungeon()
    dungeon.create_room(3,3)
    dungeon.place_room_at_xy(dungeon.rooms[0], 2, 2)
    dungeon.to_png()

if __name__ == "__main__":
    _main()

