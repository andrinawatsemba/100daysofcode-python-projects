from PIL import Image

def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"Image saved at {output_path}")
    except Exception as e:
        print("Error:", e)

def convert_image(input_path, output_path, format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=format)
            print(f"Image converted and saved at {output_path}")
    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Resize Image")
    print("2. Convert Image Format")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        input_path = input("Enter image path: ")
        output_path = input("Enter output path: ")
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        resize_image(input_path, output_path, width, height)

    elif choice == "2":
        input_path = input("Enter image path: ")
        output_path = input("Enter output path (with extension, e.g. output.png): ")
        format = output_path.split(".")[-1].upper()
        convert_image(input_path, output_path, format)

    else:
        print("Invalid choice.")



