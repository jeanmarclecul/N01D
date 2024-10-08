def init():
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = 1024, 600

    # Colors
    global WHITE, BLACK, RED, BLUE, GREEN, YELLOW, CYAN, GREEN_MID, GREEN_LOW
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    GREEN_MID = (0, 155, 0)
    GREEN_LOW = (0, 55, 0)

    global paddles, balls, bricks
    paddles = []
    balls = []
    bricks = []

    global mouse_x, mouse_y, mouse_x_before, mouse_y_before
    mouse_x = 1
    mouse_y = 1
    mouse_x_before = 1
    mouse_y_before = 1
