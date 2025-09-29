from PIL import Image, ImageDraw

FOURK_WIDTH = 3840
MANIM_UNITS = FOURK_WIDTH/14

def make_grid(image_a_path, image_b_path, n, m, rows, cols, output_path="output.png", 
              buffer=10, target_width = None, scale = None):
    """
    Create a grid PNG with images A and B repeated n and m times respectively.

    Parameters:
        image_a_path (str): Path to PNG file A.
        image_b_path (str): Path to PNG file B.
        n (int): Number of times to place image A.
        m (int): Number of times to place image B.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        buffer (int): Pixel spacing between images.
        output_path (str): Path to save the output PNG.
    """

    # Open images and ensure RGBA (to preserve transparency)
    img_a = Image.open(image_a_path).convert("RGBA")
    img_b = Image.open(image_b_path).convert("RGBA")

    # Resize B to have same width as A
    wa, ha = img_a.size  
    wb, hb = img_b.size 
    hb = int(hb * wa/wb) # new height
    img_b = img_b.resize((wa, hb), Image.LANCZOS)

    w = wa
    h = max(ha, hb)

    # Compute final canvas size
    canvas_w = cols * w + (cols - 1) * buffer
    canvas_h = rows * h + (rows - 1) * buffer

    # Create transparent canvas
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    # Build sequence of images
    sequence = [img_a] * n + [img_b] * m
    total_cells = rows * cols

    if len(sequence) > total_cells:
        print(f"Warning: Grid has {total_cells} slots, but {len(sequence)} images given. Extra images will be ignored.")
        sequence = sequence[:total_cells]
    elif len(sequence) < total_cells:
        print(f"Warning: Grid has {total_cells} slots, but only {len(sequence)} images given. Remaining slots will stay empty.")

    # Paste images onto canvas
    for idx, img in enumerate(sequence):
        row = idx // cols
        col = idx % cols
        x = col * (w + buffer)
        y = row * (h + buffer)
        canvas.alpha_composite(img, (x, y))

    if target_width is None:
        if scale is None:
            target_width = canvas_w
            target_height = canvas_h
        else: 
            target_width = int(scale * canvas_w)
            target_height = int(scale * canvas_h)
    else:
        scale = target_width / canvas_w
        target_height = int(canvas_h * scale)

    canvas_resized = canvas.resize((target_width, target_height), Image.LANCZOS)

    # Save
    canvas_resized.save(output_path)
    print(f"Grid saved to {output_path}")


# Example usage
if __name__ == "__main__":
    # make_grid("assets/rod.png", "assets/red_x.png", 501, 499, 40, 25, target_width=int(3*MANIM_UNITS), output_path="assets/rod_501.png")
    # make_grid("assets/rod.png", "assets/red_x.png", 51, 49, 10, 10, target_width=int(3*MANIM_UNITS), output_path="assets/rod_51.png")
    # make_grid("assets/steve_angel.png", "assets/steve_angel.png", 1200, 0, 30, 40, target_width=int(7.5*MANIM_UNITS), output_path="assets/steve_1200.png")
    # make_grid("assets/steve_angel.png", "assets/steve_angel.png", 100, 0, 10, 10, target_width=int(2.7*MANIM_UNITS), output_path="assets/steve_100.png")
    # make_grid("assets/steve_angel.png", "assets/steve_angel.png", 192, 0, 12, 16, target_width=int(2.7*MANIM_UNITS), output_path="assets/steve_192.png")
    make_grid("assets/steve.png", "assets/steve.png", 48, 0, 6, 8, target_width=int(2.7*MANIM_UNITS), output_path="assets/steve_48.png")

# # Load your base image
# img = Image.open("assets/steve_angel.png")

# # Settings
# cols = 100
# rows = 25
# spacing = 25  # pixels between images

# w, h = img.size
# canvas_w = cols * w + (cols - 1) * spacing
# canvas_h = rows * h + (rows - 1) * spacing

# # Create blank canvas (white background)
# canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

# # Paste images in grid
# for r in range(rows):
#     for c in range(cols):
#         x = c * (w + spacing)
#         y = r * (h + spacing)
#         canvas.paste(img, (x, y), mask=img)  # mask keeps transparency

# target_width = 3750
# scale = target_width / canvas_w
# target_height = int(canvas_h * scale)

# canvas_resized = canvas.resize((target_width, target_height), Image.LANCZOS)

# canvas_resized.save("assets/steve_angel_grid.png")