from pico2d import get_canvas_width, get_time, load_image
from pathlib import Path
import game_world


class Ball:
    image = None
    speed = 400.0  # Pixels per second.

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image(str(Path(__file__).with_name('ball21x21.png')))
        self.x, self.y = x, y
        self.direction = direction
        self.last_updated_at = get_time()

    def update(self):
        now = get_time()
        self.x += self.direction * self.speed * max(0.0, now - self.last_updated_at)
        self.last_updated_at = now
        if self.x < -11 or self.x > get_canvas_width() + 11:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
