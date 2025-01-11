import threading
import traceback

from model.image_model import ImageModel

class MainPresenter:
    def __init__(self, view):
        self.view = view
        self.model = ImageModel()

    def get_categories(self):
        return self.model.network_paths.keys()

    def get_fonts(self):
        return self.model.get_fonts()

    def generate_image(self, category, seed):
        try:
            if seed is not None:
                seed = int(seed)
            self.view.show_loading()
            threading.Thread(target=self._generate_image_thread, args=(category, seed)).start()
        except ValueError:
            self.view.show_error("Enter correct seed (decimal number).")

    def _generate_image_thread(self, category, seed):
        try:
            image_path = self.model.generate_image(category, seed)
            self.view.show_image(image_path)
            self.view.update_open_menu()
        except Exception as e:
            self.view.show_error(f"Failed to generate image: {e}")
            print(traceback.format_exc())
        finally:
            self.view.hide_loading()

    def add_text_to_image(self, text, font_name):
        try:
            font_path = self.model.get_fonts().get(font_name, "arial.ttf")
            image_path = self.model.add_text_to_image(text, font_path, self.model.generated_image_path)
            self.view.show_image(image_path)
        except Exception as e:
            self.view.show_error(f"Failed to add text to image: {e}")
            print(traceback.format_exc())

    def get_generated_files(self):
        return self.model.get_generated_files()

    def open_image(self, filename):
        try:
            image_path = f'out/{filename}'
            self.view.show_image(image_path)
            self.model.generated_image_path = image_path
        except Exception as e:
            self.view.show_error(f"Failed to load image: {e}")

    def save_image(self, file_path):
        try:
            self.model.save_image(file_path)
        except Exception as e:
            self.view.show_error(f"Failed to save image: {e}")

    def get_base_path(self):
        return self.model.base_path
