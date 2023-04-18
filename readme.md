# image2prime: ASCII Prime Generator

This project generates a prime number by converting an input image into a number. The generated number is then used to find the nearest prime number.

## Explanation

In this program, we aim to generate a prime number from an input image using the surface area of digits and a probabilistic primality test. The process is divided into two main steps:

1. **Determining the surface area of each digit**: The digit_surface_area.py script is responsible for calculating the surface area (in terms of black pixels) of each digit from 0 to 9. It does this by drawing each digit on an image and then counting the number of black pixels in the respective images. Once the surface area is calculated for all the digits, they are sorted in decreasing order to create a list of digit intensities, which represents the drawn surface area coverage of each digit.
2. **Converting an input image into a prime number**: The main.py script is responsible for the following tasks:
   1. Converting the input image into a number by mapping the grayscale color value of each pixel to a respective digit from the sorted list of digit intensities.
   2. Applying the Miller-Rabin primality test (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) to probabilistically determine the first prime number (to a degree of certainty). This test is an efficient algorithm for verifying the primality of large numbers with a certain level of accuracy.

By combining these steps, the program generates a porential prime number from the input image, effectively transforming visual information into a unique mathematical representation. (To-do: Add a deterministic primality test to verify the generated prime number.)

## Requirements

- Python 3.x
- NumPy
- Pillow (PIL)

## Files

`digit_surface_area.py`: Creates an image for each digit, counts the black pixels in the image, and sorts the digits based on the pixel count.

`main.py`: Converts an input image to a number using the sorted list of digits, finds the nearest prime number, and constructs a 2D grid representing the prime number.

## Usage

Install the required packages if you haven't already:

```bash
pip install numpy Pillow
```

Update the following variables in main.py with your own input image and desired output shape:

```python
input_image = "twitter.png"
output_shape = (30, 30)
```

Run the main.py script:

```bash
python main.py
```

This will generate the prime number and print the 2D grid representation of the prime number.
The resulting grid is also saved as a text file res.txt in the current directory.
