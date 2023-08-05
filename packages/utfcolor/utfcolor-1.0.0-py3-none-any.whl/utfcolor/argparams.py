import argparse

def parseArgs() -> dict:
    parser = argparse.ArgumentParser(description="Convert any text to an image.")

    parser.add_argument(
    "-f",
    "--file",
    type=str,
    help="Input text file path.")

    parser.add_argument(
    "-t",
    "--text",
    type=str,
    help="Directly input text for encoding.")

    parser.add_argument(
    "-e",
    "--encoding",
    type=str,
    default="utf-color",
    help="Encoding to use.")

    parser.add_argument(
    "-o",
    "--output",
    type=str,
    default="",
    help="Name of the output file.")

    parser.add_argument(
    "-s",
    "--scale",
    type=int,
    default=0,
    help="Upscaling of the resulting image.")

    parser.add_argument(
    "-pc",
    "--performancecounter",
    action='store_true', 
    default=False,
    help="Count the seconds until the image is created.")

    arguments = parser.parse_args()

    return {
        "file": arguments.file,
        "text": arguments.text,
        "encoding": arguments.encoding,
        "output": arguments.output,
        "scale": arguments.scale,
        "performancecounter": arguments.performancecounter
    }