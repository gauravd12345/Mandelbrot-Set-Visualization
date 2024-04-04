import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# Change max iterations to get more precise values of the mandelbrot set
max_iter = 128

# Change width to alter the pixel densty
width = 1024
height = width

# Use these values to alternate the center and scale repsectively
center = -0.1 - 0.875j
scale = 0.1 / width


def mandelbrot_set(scale):
    # Creating numpy arrays for real, imaginary, and color values for each point
        real_numbers = np.zeros(width * width)
        imag_numbers = np.zeros(width * width)
        colors = np.zeros(width * width)

        index = 0
        for x in range(width):
            for y in range(height):

                # Getting the real and imaginary numbers based on x, y values
                rl = x - width // 2
                ig = (y - height // 2) * 1j

                # Getting the complex number and its mandelbrot result 
                c = center + (rl + ig) * scale
                mandelbrot_result = mandelbrot_function(c)

                # Checking if the result is bounded
                real_numbers[index] = c.conjugate().real
                imag_numbers[index] = c.conjugate().imag
                colors[index] = (mandelbrot_result / max_iter)
                    
                index += 1

        # Plotting the mandelbrot set graph
        fig, axes = plt.subplots(1, 1, figsize=(10, 7))
        plt.scatter(real_numbers, imag_numbers, c = colors, cmap=cm.get_cmap("twilight_shifted"), marker=",", s=1)
        plt.gca().set_aspect("equal")
        plt.axis("off")
        plt.tight_layout()
        plt.show()


def main():
    mandelbrot_set(scale)


# Returns the no. of iterations before diverging/converging 
def mandelbrot_function(c):
    z = 0
    for i in range(max_iter):
        z = z ** 2 + c
        
        if((z * z.conjugate()).real > 4):
            return i
        
    return max_iter




if __name__ == "__main__":
    main()
