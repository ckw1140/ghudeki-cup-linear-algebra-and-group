from PIL import Image

data_path = "../data/ghudeki-cup-linear-algebra-and-group/book-cover.jpg"
save_path = "../data/ghudeki-cup-linear-algebra-and-group/"

def main():
    img = Image.open(data_path)

    img_width, img_height = img.size

    num_piece_width = 50
    num_piece_height = 29
    unit_width = img_width / num_piece_width
    unit_height = img_height / num_piece_height

    for i in range(num_piece_width):
        for j in range(num_piece_height):
            bound = (
                i * unit_width,
                j * unit_height,
                (i + 1) * unit_width,
                (j + 1) * unit_height,
            )
            cropped_img = img.crop(bound)

            file_name = f"{i}-{j}.jpg"
            cropped_img.save(save_path + file_name)


if __name__ == "__main__":
    main()