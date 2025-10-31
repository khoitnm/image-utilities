import configparser
from PIL import Image, ImageDraw, __version__ as pillow_version

print(f"Using Pillow {pillow_version}")

# --- Load configuration ---
config = configparser.ConfigParser()
config.read("config.ini")

# Read settings
square_size = int(config["Grid"].get("square_size", 64))
columns = int(config["Grid"].get("columns", 5))
rows = int(config["Grid"].get("rows", 8))
output_file = config["Grid"].get("output_file", "grid.png")

# --- Compute image size ---
width = columns * square_size
height = rows * square_size

# --- Create transparent image (RGBA mode) ---
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # fully transparent
draw = ImageDraw.Draw(image)

# --- Draw grid squares with black outlines only ---
for row in range(rows):
    for col in range(columns):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        # No fill, only outline
        draw.rectangle([x1, y1, x2, y2], outline="black", width=1)

# --- Save as PNG (keeps transparency) ---
image.save(output_file, format="PNG")

print(f"✅ Transparent grid saved as '{output_file}' ({columns}x{rows}, {square_size}px each)")
