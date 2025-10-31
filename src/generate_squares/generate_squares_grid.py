import configparser
from pathlib import Path
from PIL import Image, ImageDraw, __version__ as pillow_version

print(f"Using Pillow {pillow_version}")

# --- Load configuration ---
config = configparser.ConfigParser()
config.read("config.ini")

# Read settings
square_size = int(config["Grid"].get("square_size", 64))
columns = int(config["Grid"].get("columns", 5))
rows = int(config["Grid"].get("rows", 8))
square_color = config["Grid"].get("square_color", "#3498db")
background_color = config["Grid"].get("background_color", "#ffffff")
output_file = config["Grid"].get("output_file", "grid.png")

# --- Prepare output folder ---
output_path = Path(output_file)
output_path.parent.mkdir(parents=True, exist_ok=True)

# --- Compute image size ---
width = columns * square_size
height = rows * square_size

# --- Create image ---
# Decide mode based on background transparency
if background_color.lower() in ["none"]:
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
else:
    image = Image.new("RGBA", (width, height), background_color)
draw = ImageDraw.Draw(image)

# --- Draw squares ---
for row in range(rows):
    for col in range(columns):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        draw.rectangle([x1, y1, x2, y2], outline="black", fill=square_color)

# --- Save image ---
image.save(output_path, format="PNG")

# --- Print absolute path ---
abs_path = output_path.resolve()
print(f"✅ Grid image saved at:\n{abs_path}")
print(f"   ({columns}x{rows} squares, {square_size}px each)")
