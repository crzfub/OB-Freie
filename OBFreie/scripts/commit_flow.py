import subprocess
import os


def convert_font(input_path, output_dir):
    command = ["fonttools", "ttx", input_path, "-d", output_dir]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully converted {input_path} to {output_dir}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e}")
        print(e.stderr)


def main():
    # List of Fonts - add OBNL-Fonts once created
    fonts = [
        "OBFreie-Light.otf",
        "OBFreie-Regular.otf",
        "OBFreie-Bold.otf",
        "OBNLFreie-Light.otf",
        "OBNLFreie-Regular.otf",
        "OBNLFreie-Bold.otf",
    ]
    input_dir = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/otf"
    output_dir = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for font in fonts:
        input_path = os.path.join(input_dir, font)
        convert_font(input_path, output_dir)


if __name__ == "__main__":
    main()
