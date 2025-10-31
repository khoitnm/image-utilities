import configparser
from pathlib import Path
from PIL import Image, ImageDraw


def parse_rgba(color_str):
    """Convert 'R,G,B,A' string into a tuple of 4 integers"""
    parts = [int(x.strip()) for x in color_str.split(",")]
    if len(parts) == 3:  # If alpha not provided, default to 255
        parts.append(255)
    return tuple(parts)


def generate_grid(config_file="config.ini"):
    """Generate a grid image based on settings from config_file"""

    # --- Load configuration ---
    config = configparser.ConfigParser()
    config.read(config_file)

    square_size = int(config["Grid"].get("square_size", 64))
    columns = int(config["Grid"].get("columns", 5))
    rows = int(config["Grid"].get("rows", 8))
    square_color = parse_rgba(config["Grid"].get("square_color", "52,152,219,255"))
    background_color = parse_rgba(config["Grid"].get("background_color", "255,255,255,0"))
    output_file = config["Grid"].get("output_file", "output/grid.png")

    # --- Prepare output folder ---
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # --- Compute image size ---
    width = columns * square_size
    height = rows * square_size

    # --- Create image ---
    image = Image.new("RGBA", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # --- Draw squares ---
    for row in range(rows):
        for col in range(columns):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255), fill=square_color)

    # --- Save image ---
    image.save(output_path, format="PNG")

    # --- Print absolute path ---
    abs_path = output_path.resolve()
    print(f"✅ Grid image saved at:\n{abs_path}")
    print(f"   ({columns}x{rows} squares, {square_size}px each)")


# --- Call the function if script is run directly ---
if __name__ == "__main__":
    generate_grid()
