# gen-a-card
A greeting card generator using NVIDIA's StyleGAN2-ADA and Transfer Learning.

## Overview
`gen-a-card` is a desktop application that enables users to generate simple greeting cards using neural networks. Users can select from 4 categories, customize the design with text, and save the final result as an image. The application is powered by NVIDIA's StyleGAN2-ADA, which was fine-tuned using transfer learning techniques.

## Features
- **Category Selection:** Choose from four categories: Flowers, Landscapes, Butterflies, or Dogs.
- **Customizable Seed:** Generate a specific image by providing a custom seed value or let the app choose one randomly.
- **Text Overlay:** Add personalized text to the generated image.
- **Save and Load:** Save the completed greeting card to your local disk or load a previously generated image for editing.
- **Responsive UI:** The app remains responsive during image generation, ensuring a smooth user experience.

## How It Works
1. **Image Generation:**
   - The app uses pre-trained StyleGAN2-ADA models, fine-tuned for each category (Flowers, Landscapes, Butterflies, and Dogs).
   - Users can specify a random seed to control the generated output.

2. **Adding Text:**
   - Once an image is generated, users can input their desired text and choose from a variety of font styles.
   - The text is overlaid on the image, creating a personalized greeting card.

3. **Saving the Card:**
   - Users can save the final design to their local storage as an image file.

## Installation
To run `gen-a-card`, you need Python installed on your system. Follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/gen-a-card.git
   cd gen-a-card
   ```

2. **Install Dependencies:**
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```

## Dependencies
- Python 3.8+
- CustomTkinter: For creating the user interface.
- StyleGAN2-ADA: For image generation.
- Other Python libraries listed in `requirements.txt`.

## Usage
1. Launch the application by running `python main.py`.
2. Select a category (Flowers, Landscapes, Butterflies, or Dogs).
3. Optionally, enter a seed value or leave it blank for a random image.
4. Click "Generate" to create an image.
5. Add your personalized text, select a font.
6. Save the final design or generate a new card.

## Example Output
![Example Card](examples/example_cards.png)

## Future Improvements
- **Enhanced Image Quality:** Further fine-tuning of StyleGAN2-ADA parameters and training on improved datasets.
- **Additional Categories:** Adding more categories for greater variety.
- **Web Version:** Extending the application to a web-based platform.
- **Batch Generation:** Allowing users to generate multiple cards at once.

## Acknowledgments
This project was created as part of a learning experience in generative adversarial networks (GANs). Special thanks to NVIDIA for providing StyleGAN2-ADA and the open-source community for tools and resources.

