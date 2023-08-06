import collections
import math

from .isosm_config import NOT_ALL_FLAGS, FLIPPED_VERTICALLY_FLAG, FLIPPED_HORIZONTALLY_FLAG, SCROLL_STEP
from ... import _hub
from ... import event
from ...compo import vscreen as core

EngineEvTypes = event.EngineEvTypes

# --------------------------------------------
# optimization
_gl_halftile_w = _gl_halftile_h = None
_buffer_relx = dict()
_buffer_rely = dict()


def relative_x(x, y):
    """Return the relative x position of this tile, ignoring offset."""
    try:
        return _buffer_relx[x][y]
    except KeyError:
        if x not in _buffer_relx:
            _buffer_relx[x] = dict()
        _buffer_relx[x][y] = int(x * _gl_halftile_w - y * _gl_halftile_w)
        return _buffer_relx[x][y]


def relative_y(x, y):
    """Return the relative y position of this tile, ignoring offset."""
    try:
        return _buffer_rely[x][y]
    except KeyError:
        if x not in _buffer_rely:
            _buffer_rely[x] = dict()
        _buffer_rely[x][y] = int(y * _gl_halftile_h + x * _gl_halftile_h)
        return _buffer_rely[x][y]


def rel_set_info(halftile_w, halftile_h):
    global _gl_halftile_w, _gl_halftile_h, _buffer_relx, _buffer_rely
    _gl_halftile_w = float(halftile_w)
    _gl_halftile_h = float(halftile_h)
    _buffer_relx.clear()
    _buffer_rely.clear()


# ----------------------------------------------


class IsometricMapViewer(event.EventReceiver):
    MEGAOPTIM = False
    MOUSEMOTION_CONST = None
    SOLID_COLOR = 'navyblue'
    FLOORS = {}
    FLOOR_MAN_OFFSET = {
        0: (1617 + 305, 240 - 128),  # what offset one needs to apply so the floor img is aligned, map 0 (city.png)
        1: (522 + 300, 100 - 92)
    }

    def __init__(self, isometric_map, screen, postfx=None, cursor=None,
                 left_scroll_key=None, right_scroll_key=None, up_scroll_key=None, down_scroll_key=None):
        super().__init__()

        self.MOUSEMOTION_CONST = _hub.pygame.MOUSEMOTION
        self.animated_wallpaper = False
        self.block_wallpaper = False

        self.isometric_map = isometric_map
        self.FLOORS = {
            0: _hub.pygame.image.load('assets/city.png'),
            1: _hub.pygame.image.load('assets/casino.png')
        }
        self.manoffset = self.FLOOR_MAN_OFFSET[0]
        self.scrollable_floor = self.FLOORS[0]

        self.scrollable_floor.set_colorkey((255, 0, 255))

        self.screen = screen
        self.mid = (
            self.screen.get_width() // 2, self.screen.get_height() // 2
        )
        # self.prevx = float('NaN')
        # self.prevy = float('NaN')

        self.floor_rect = _hub.pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())

        if isometric_map.wallpaper:
            self.screen_rect = self.screen.get_rect()
            wp_width, wp_height = self.isometric_map.wallpaper.get_size()
            self.wp_temp_rect = _hub.pygame.Rect(0, 0, wp_width, wp_height)
            self.wp_grid_w = self.screen_rect.w // wp_width + 1
            self.wp_grid_h = self.screen_rect.h // wp_height + 1

        # The focus is defined by map coordinates, so a lot of the back and forth between screen and map coords
        # can be cut.
        self._focus_x = 0
        self._focus_y = 0
        self._focused_object_x0 = 0
        self._focused_object_y0 = 0
        self._focused_object = None

        self.phase = 0

        self.tile_width = isometric_map.tile_width
        self.tile_height = isometric_map.tile_height

        self.half_tile_width = isometric_map.tile_width // 2
        self.half_tile_height = isometric_map.tile_height // 2
        rel_set_info(
            self.half_tile_width, self.half_tile_height
        )
        self.visible_area = None
        self._init_visible_area_init(self.screen)

        # _mouse_tile contains the actual tile the mouse is hovering over. However, in most cases what we really want
        # is the location of the mouse cursor. Time to make a property!
        self._mouse_tile = (-1, -1)
        self.postfx = postfx
        self.cursor = cursor
        self.left_scroll_key = left_scroll_key
        self.right_scroll_key = right_scroll_key
        self.up_scroll_key = up_scroll_key
        self.down_scroll_key = down_scroll_key
        self.debug_sprite = None
        self.lastmousepos = None

        # util for the drawing of tiles
        self.line_cache = list()
        self.objgroup_contents = dict()
        self.objgroup_modified_mappos = dict()
        self._camera_updated_this_frame = False

    def _check_mouse_scroll(self, screen_area, mouse_x, mouse_y):
        # Check for map scrolling, depending on mouse position.
        if not self._camera_updated_this_frame:
            if mouse_x < 20:
                dx = -SCROLL_STEP
            elif mouse_x > (screen_area.right - 20):
                dx = +SCROLL_STEP
            else:
                dx = 0

            if mouse_y < 20:
                dy = -SCROLL_STEP
            elif mouse_y > (screen_area.bottom - 20):
                dy = +SCROLL_STEP
            else:
                dy = 0

            if dx or dy:
                self._update_camera(dx, dy)

    def _get_horizontal_line(self, x0, y0, line_number):
        x = x0 + line_number // 2
        y = y0 + (line_number + 1) // 2

        _, py = self.screen_coords(x, y)
        if py > self.visible_area.bottom:
            return None

        mylist = list()
        while self.screen_coords(x, y)[0] < self.visible_area.right:
            if self.isometric_map.on_the_map(x, y):
                mylist.append((x, y))
            x += 1
            y -= 1
        return mylist

    def _init_visible_area_init(self, scr):
        # The visible area describes the region of the map we need to draw
        w, h = scr.get_size()
        # below: x, y do not matter actually
        self.visible_area = _hub.pygame.Rect(0, 0, w + self.half_tile_width, h + 4 * self.tile_height)

    def _model_depth(self, model):
        return relative_y(model.x, model.y)

    def _update_camera(self, dx, dy):
        # If the mouse and the arrow keys conflict, only one of them should win.
        if self._camera_updated_this_frame:
            return
        self._focus_x, self._focus_y = self.isometric_map.clamp_pos([self._focus_x + dx, self._focus_y + dy])

    def _paint_all(self):
        # TODO idea 1 optimize such as the ground layer is blit as one single image, we just move a rect to cut
        # properly from the very large image stored in memory

        #
        # TOM REMARK: but i cannot use this optimization right now, it makes
        # the floor "wiggle" compared to buildings or portals :(

        # TODO maybe?
        #  idea 2 optimize such as if player+cursor are not moving, all graphic elements are saved onto a "texture"
        #  and we just blit this texture instead of computing new stuff

        # Prep the screen.
        wpok = False
        if not self.block_wallpaper:
            if self.isometric_map.wallpaper is not None:
                self.fill_wallpaper()
                wpok = True
        if not wpok:
            self.screen.fill(self.SOLID_COLOR)

        # Check the map scrolling.
        self._camera_updated_this_frame = False
        if self._focused_object:
            if self._focused_object.x != self._focused_object_x0 or self._focused_object.y != self._focused_object_y0:
                self.focus(self._focused_object.x, self._focused_object.y)
                self._focused_object_x0 = self._focused_object.x
                self._focused_object_y0 = self._focused_object.y

        # Disabling mouse scrolling because the right and bottom edges of the screen don't seem to be working.
        #     if self.lastmousepos:
        #         self._check_mouse_scroll(self.visible_area, *self.lastmousepos)

        # ------------------------------------- check this out <<<
        # --- OPTIM blit large image for the ground level (1/3)---
        if self.MEGAOPTIM:
            # a = relative_x(self._focused_object.x, self._focused_object.y)
            # b = relative_y(self._focused_object.x, self._focused_object.y)  # - self.mid[0],  self._focused_object.y-self.mid[1]
            a, b = self.screen_offset()
            self.floor_rect.topleft = self.manoffset[0] - a, self.manoffset[1] - b
        # ------------------------------------- check this out <<<
        # --- OPTIM blit large image for the ground level (2/3)---
            self.screen.blit(self.scrollable_floor, (0, 0), area=self.floor_rect)

        # Record all of the objectgroup contents for display when their tile comes up
        # Also, clamp all object positions. If this is an infinite scrolling map, objects can move off one side to the
        # map to the other. However, in their data, we want the objects to stay within the bounds of the map.
        for k, v in self.isometric_map.objectgroups.items():
            self.objgroup_contents[k] = collections.defaultdict(list)
            for ob in v.contents:
                ob.x, ob.y = self.isometric_map.clamp_pos((ob.x, ob.y))
                sx, sy = self.screen_coords(ob.x, ob.y, v.offsetx, v.offsety)
                mx, my = self.map_x(sx, sy, return_int=False), self.map_y(sx, sy, return_int=False)
                obkey = self.isometric_map.clamp_pos_int((mx, my))
                self.objgroup_contents[k][obkey].append(ob)
                # Also save the mofidied map pos, which will come in handy later.
                self.objgroup_modified_mappos[ob] = (mx, my)

        x, y = self.map_x(0, 0) - 2, self.map_y(0, 0) - 1
        x0, y0 = x, y
        painting_tiles = True
        line_number = 1

        while painting_tiles:
            # In order to allow smooth sub-tile movement of stuff, we have
            # to draw everything in a particular order.
            nuline = self._get_horizontal_line(x0, y0, line_number)
            self.line_cache.append(nuline)
            current_y_offset = self.isometric_map.layers[0].offsety
            current_line = len(self.line_cache) - 1

            for layer_num, layer in enumerate(self.isometric_map.layers):
                # ------------------------------------- check this out <<<
                # --- OPTIM blit large image for the ground level (3/3)---
                if self.MEGAOPTIM:
                    if layer_num == 0:
                        continue

                if current_line >= 0:
                    if current_line > 1 and layer in self.objgroup_contents and self.line_cache[current_line - 1]:
                        # After drawing the terrain last time, draw any objects in the previous cell.
                        for x, y in self.line_cache[current_line - 1]:
                            if self.cursor:
                                if self.cursor.layer_name == layer.name and x == self.cursor.x and y == self.cursor.y:
                                    self.cursor.render(self)

                            ox, oy = x % self.isometric_map.width, y % self.isometric_map.height
                            if (ox, oy) in self.objgroup_contents[layer]:
                                self.objgroup_contents[layer][(ox, oy)].sort(key=self._model_depth)
                                for ob in self.objgroup_contents[layer][(ox, oy)]:
                                    # The following bit of math makes sure that the clamped object positions will
                                    # print at the correct screen positions. Otherwise, if the player/focus is on the
                                    # other side of the map seam, this object will be printed in the wrong position.
                                    mmx, mmy = self.objgroup_modified_mappos[ob]
                                    fx = x + math.modf(mmx)[0]
                                    fy = y + math.modf(mmy)[0]
                                    sx, sy = self.screen_coords(
                                        fx, fy,
                                        self.isometric_map.objectgroups[layer].offsetx,
                                        self.isometric_map.objectgroups[layer].offsety
                                    )
                                    ob(self.screen, sx, sy, self.isometric_map)

                    if self.line_cache[current_line]:
                        for x, y in self.line_cache[current_line]:
                            gid = layer[x, y]
                            tile_id = gid & NOT_ALL_FLAGS
                            if tile_id > 0:
                                my_tile = self.isometric_map.tilesets[tile_id]

                                # Note that x,y refer to IsometricMapObject coordinates, and so 0,0 points at the
                                # top of the "ground" level of a tile. So, we adjust sy before sending the coords
                                # to the printer, so it is pointing at the bottom corner of the tile instead.
                                sx, sy = self.screen_coords(x, y)
                                my_tile.paint_tile(
                                    self.screen, sx, sy + layer.offsety + self.isometric_map.tile_height,
                                                     gid & FLIPPED_HORIZONTALLY_FLAG,
                                                     gid & FLIPPED_VERTICALLY_FLAG)

                    elif self.line_cache[current_line] is None:  # and layer == self.isometric_map.layers[-1]:
                        painting_tiles = False
                else:
                    break
                if layer.offsety < current_y_offset:
                    current_line -= 1
                    current_y_offset = layer.offsety
            line_number += 1

        self.phase = (self.phase + 1) % 640

        del self.line_cache[:]
        self.objgroup_contents.clear()
        self.objgroup_modified_mappos.clear()

    def fill_wallpaper(self):
        for x in range(-1, self.wp_grid_w):
            self.wp_temp_rect.x = self.screen_rect.x + x * self.wp_temp_rect.w
            for y in range(-1, self.wp_grid_h):
                self.wp_temp_rect.y = self.screen_rect.y + y * self.wp_temp_rect.h
                if self.animated_wallpaper:
                    self.wp_temp_rect.y += self.phase

                self.screen.blit(self.isometric_map.wallpaper, self.wp_temp_rect)

    def focus(self, x, y):
        """Move the camera to point at the requested map tile. x,y can be ints or floats."""
        self._focus_x, self._focus_y = self.isometric_map.clamp_pos((x, y))

        # self.floor_rect.x = a
        # self.floor_rect.y = b

    def map_x(self, sx, sy, return_int=True):
        """Return the map x row for the given screen coordinates."""
        x_off, y_off = self.screen_offset()

        # We're going to use the relative coordinates of the tiles instead of the screen coordinates.
        rx = sx - x_off
        ry = sy - y_off

        # Calculate the x position of map_x tile 0 at ry.
        ox = float(-ry * self.half_tile_width) / float(self.half_tile_height)

        # Now that we have that x origin, we can determine this screen position's x coordinate by dividing by the
        # tile width. Fantastic.
        if return_int:
            # Because of the way Python handles division, we need to apply a little nudge right here.
            if rx - ox < 0:
                ox += self.tile_width
            return int(math.floor((rx - ox) / self.tile_width))
        else:
            return (rx - ox) / self.tile_width

    def map_y(self, sx, sy, return_int=True):
        """Return the map y row for the given screen coordinates."""
        x_off, y_off = self.screen_offset()

        # We're going to use the relative coordinates of the tiles instead of the screen coordinates.
        rx = sx - x_off
        ry = sy - y_off

        oy = float(rx * self.half_tile_height) / float(self.half_tile_width)

        # Now that we have that x origin, we can determine this screen position's x coordinate by dividing by the
        # tile width. Fantastic.
        if return_int:
            # Because of the way Python handles division, we need to apply a little nudge right here.
            if ry - oy < 0:
                oy += self.tile_height
            return int(math.floor((ry - oy) / self.tile_height))
        else:
            return (ry - oy) / self.tile_height

    @property
    def mouse_tile(self):
        if self.cursor:
            return self.cursor.x, self.cursor.y
        else:
            return self._mouse_tile

    def proc_event(self, ev, source=None):
        if ev.type == EngineEvTypes.PAINT:
            self._paint_all()

        elif ev.type == self.MOUSEMOTION_CONST:
            mouse_x, mouse_y = core.proj_to_vscreen(ev.pos)
            self.lastmousepos = (mouse_x, mouse_y)
            self._mouse_tile = (self.map_x(mouse_x, mouse_y), self.map_y(mouse_x, mouse_y))
            if self.cursor:
                self.cursor.update(self, ev)

    def screen_coords(self, x, y, extra_x_offset=0, extra_y_offset=0):
        x_off, y_off = self.screen_offset()
        return relative_x(x, y) + x_off + extra_x_offset, relative_y(x, y) + y_off + extra_y_offset

    def screen_offset(self):
        return self.mid[0] - relative_x(self._focus_x, self._focus_y), \
               self.mid[1] - relative_y(self._focus_x, self._focus_y)

    def set_focused_object(self, fo):
        if fo:
            self._focused_object = fo
            self.focus(fo.x, fo.y)
        else:
            self._focused_object = None

    def switch_map(self, isometric_map):
        # ---------- MEGAOPTIM
        if self.MEGAOPTIM:
            if isometric_map.mapname == 'city':
                self.scrollable_floor = self.FLOORS[0]
                self.manoffset = self.FLOOR_MAN_OFFSET[0]
            elif isometric_map.mapname == 'casino':
                self.scrollable_floor = self.FLOORS[1]
                self.manoffset = self.FLOOR_MAN_OFFSET[1]

        self.isometric_map = isometric_map
        self.tile_width = isometric_map.tile_width
        self.tile_height = isometric_map.tile_height

        self.half_tile_width = isometric_map.tile_width // 2
        self.half_tile_height = isometric_map.tile_height // 2
        rel_set_info(
            self.half_tile_width, self.half_tile_height
        )

        if self._focused_object:
            fo = self._focused_object
            self.focus(fo.x, fo.y)
        else:
            self._focus_x = 0
            self._focus_y = 0
