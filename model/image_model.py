import os
import random
import time

from PIL import Image, ImageDraw, ImageFont

from . import image_generator


class ImageModel:

    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.network_paths = {
            "Flowers": os.path.join(self.base_path, "networks", "flowers-network.pkl"),
            "Landscape": os.path.join(self.base_path, "networks", "landscape-network.pkl"),
            "Dogs": os.path.join(self.base_path, "networks", "dogs-network.pkl"),
            "Butterflies": os.path.join(self.base_path, "networks", "butterflies-network.pkl")
        }
        self.generated_image_path = None

    def get_fonts(self):
        import tkinter.font as tkfont
        font_dict = {font: font for font in tkfont.families()}
        return font_dict

    def generate_image(self, category, seed=None):
        network_pkl = self.network_paths[category]
        if seed is None:
            seed = random.randint(0, 10000)

        image_generator.generate_images(
            network_pkl=network_pkl,
            seeds=[seed],
            truncation_psi=1,
            noise_mode='const',
            outdir='out',
            class_idx=None,
            projected_w=None,
            class_name=category.lower()
        )
        self.generated_image_path = f'out/{category.lower()}_seed{seed:04d}.png'
        while not os.path.exists(self.generated_image_path):
            time.sleep(0.1)

        return self.generated_image_path

    def add_text_to_image(self, text, font_path, generated_image_path):
        image = Image.open(generated_image_path)
        resized_image = image.resize((512, 512))
        draw = ImageDraw.Draw(resized_image)

        text = text.replace("\\n", "\n")

        if '\n' in text:
            parts = text.split('\n')
            mid = len(parts) // 2
            text_upper = "\n".join(parts[:mid])
            text_lower = "\n".join(parts[mid:])
        else:
            words = text.split()
            mid = len(words) // 2
            if len(words) > 1:
                text_upper = " ".join(words[:mid])
                text_lower = " ".join(words[mid:])
            else:
                text_upper = text
                text_lower = ""

        # Function to find the maximum font size that fits the width
        def find_max_font_size(draw, text, width, font_path):
            if not text:
                return float("inf")
            fontsize = 1
            font = ImageFont.truetype(font_path, fontsize)
            while draw.textbbox((0, 0), text, font=font)[2] < width:
                fontsize += 1
                font = ImageFont.truetype(font_path, fontsize)
            return fontsize - 1

        max_font_size_upper = find_max_font_size(draw, text_upper, 512 - 20, font_path)
        max_font_size_lower = find_max_font_size(draw, text_lower, 512 - 20, font_path)
        font_size = min(max_font_size_upper, max_font_size_lower)

        font_upper = ImageFont.truetype(font_path, font_size)
        font_lower = ImageFont.truetype(font_path, font_size)

        upper_text_bbox = draw.textbbox((0, 0), text_upper, font=font_upper)
        lower_text_bbox = draw.textbbox((0, 0), text_lower, font=font_lower)
        upper_text_position = ((512 - upper_text_bbox[2]) // 2, 10)
        lower_text_position = ((512 - lower_text_bbox[2]) // 2, 512 - lower_text_bbox[3] - 10)

        outline_color = "black"
        fill_color = "white"

        def draw_text_with_outline(draw, position, text, font, outline_color, fill_color):
            x, y = position
            draw.text((x - 1, y - 1), text, font=font, fill=outline_color)
            draw.text((x + 1, y - 1), text, font=font, fill=outline_color)
            draw.text((x - 1, y + 1), text, font=font, fill=outline_color)
            draw.text((x + 1, y + 1), text, font=font, fill=outline_color)
            draw.text(position, text, font=font, fill=fill_color)

        draw_text_with_outline(draw, upper_text_position, text_upper, font_upper, outline_color, fill_color)
        draw_text_with_outline(draw, lower_text_position, text_lower, font_lower, outline_color, fill_color)

        output_path = "out/edited_image.png"
        resized_image.save(output_path)
        return output_path

    def save_image(self, file_path):
        image_path = "out/edited_image.png"
        if image_path:
            image = Image.open(image_path)
            image.save(file_path)
        else:
            raise Exception("No image to save.")

    def get_generated_files(self):
        return [f for f in os.listdir('out') if f.endswith('.png')]

