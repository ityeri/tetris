import tereen
from tereen.text_map import TextMap

from tetris.display_map import DisplayMap


class DisplayMapSurface(tereen.surface.BaseSurface):
    def __init__(self, display_map: DisplayMap, cell_width: int, cell_height: int):
        self.display_map: DisplayMap = display_map
        self.cell_width: int = cell_width
        self.cell_height: int = cell_height
        self.width = cell_width * display_map.width
        self.height = cell_height * display_map.height

    def render(self) -> TextMap:
        output_map = TextMap(self.width, self.height, ' ')

        for y in range(self.display_map.height * self.cell_height):
            for x in range(self.display_map.width * self.cell_width):
                pixel_type = self.display_map[x // self.cell_width, y // self.cell_height]
                if pixel_type is None:
                    char = " "
                else:
                    char = tereen.at_color(" ", back=pixel_type.color)

                output_map[x, y] = char

        return output_map