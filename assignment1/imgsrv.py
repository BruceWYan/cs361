import time

# Number of images (change this to the actual number of images you have)
num_images = 3

while True:
    # Sleep for 1 second
    time.sleep(1)

    # Open the file image-service.txt in read mode
    with open("image-service.txt", "r") as file:
        # Read the content of the file and convert it to an integer (assuming the file contains a number)
        try:
            content = int(file.read().strip())
        except ValueError:
            content = None

    if isinstance(content, int):  #isinstance - checks if the object (content) is an instance of certain data type (int)
        # Calculate the index based on the modulus operation
        num = content % 3 + 1
        # Construct the path to the image file
        image_path = f"/nfs/stak/users/yanbr/cs361/assignment1/cs361/{num}.jpg"
        time.sleep(2)
        # Open the file image-service.txt in write mode
        with open("image-service.txt", "w") as file:
            # Write the image path to the file
            file.write(image_path)

# The script will continue running in an infinite loop with a 1-second delay