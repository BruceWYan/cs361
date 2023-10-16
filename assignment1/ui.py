import time

while True:
    print("Options:")
    print("1 - Generate new image")
    print("2 - Exit")
    
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        # Open prng-service.txt in write mode and write "run"
        with open("prng-service.txt", "w") as prng_file:
            prng_file.write("run")
        
        print("Generating image...")
        
        # Sleep for 5 seconds
        time.sleep(5)
        
        # Read pseudo random number from prng-service.txt
        with open("prng-service.txt", "r") as prng_file:
            pseudo_random_number = prng_file.read().strip()
        
        # Open image-service.txt in write mode and write the pseudo random number
        with open("image-service.txt", "w") as image_file:
            image_file.write(pseudo_random_number)
        
        # Sleep for 5 seconds
        time.sleep(5)
        
        # Read and output image-service.txt
        with open("image-service.txt", "r") as image_file:
            image_data = image_file.read()
            print("Image Data:", image_data)
    
    elif user_input == "2":
        print("Exiting...")
        break
    
    else:
        print("Unknown option. Please choose 1 to generate a new image or 2 to exit.")