import time
import random
while True:
    # Sleep for 1 second
    time.sleep(2)

    # Open the file prng-service.txt in write mode
    with open("prng-service.txt", "r+") as file:
        # Read the content of the file
        content = file.read()

        # Check if the line in the file is "run"
        if "run" in content:
            # Generate a random number
            random_number = random.randint(0,1000000000) # Change the range as needed
            # Replace "run" with the random number in the content
            content = content.replace("run", str(random_number))

            # Move the file cursor to the beginning and truncate the file
            file.seek(0)
            file.truncate()

            # Write the updated content back to the file
            file.write(content)