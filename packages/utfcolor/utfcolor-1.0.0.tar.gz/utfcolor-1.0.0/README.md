# UTF-Color

## What is UTF-Color?

UTF-Color is an esoterical encoding for text. It can be used to convert any text into an image and any UTF-Color encoded image can be decoded back into text.
Decoding is not available yet.

## What is the purpose of this project?

There is no real purpose, it should be seen as an art project.

## Usage

Installation:
```
pip install utfcolor
```

As a package:
```
>>> import utfcolor
>>> utfcolor.txtToImg(text="test", encoding="utf-color", scale=30)
```

From the command line:
```
python3 -m utfcolor %PathToTextfile% [options]
```

## Parameters

Parameter 			    | Flag 	| Description
------------------------|-------|------------
Text input           	| `-t`	| Input text directly.
File input           	| `-f`	| Input text from a textfile.
Output path           	| `-o`	| Path of output file. Uses the current time as default.
Encoding               	| `-e`	| Encoding that shoould be used for the image. Choices include `utf-color`, `utf-colorv2`, `utf-colorv3`, `rng-utf-color`, and standard encodings like `utf-8` or `latin1`. Default value is `utf-color`.
Scale                  	| `-s`	| Upscaling of the resulting image. The width and height of the resulting image will be multiplied with the given value. Default value is 0.

## Explanation and Examples

### utf-color

The first version of UTF-Color is an 8-Bit encoding. In this version each pixel in the image represents three characters in the text. The resulting image is hardly readable (for humans).
Example:
```
python3 -m utfcolor -t "test." -s 300
```

![utf-color](./examples/utf-color.png)

The text "test." encoded with utf-color. The HEX-code of the two pixels can be decoded into text (take a look at the codepage of [utfcolorv1](./utfcolorv1.py)).

### utf-colorv2

The second version of UTF-Color is a 24-Bit encoding. Every character from the text is represented by one pixel in the image. The image is easily readable.
The color-codes were chosen to make the image as colorful as possible.
Example:
```
python3 -m utfcolor -t "test." -s 200 -e "utf-colorv2"
```

![utf-colorv2](./examples/utf-colorv2.png)

The text "test." encoded with utf-colorv2. The pixels of the image can be decoded into text (read from top to bottom and left to right).

### utf-colorv3

The third version of UTF-Color is also a 24-Bit encoding. It is very similar to version two, but the color-codes are different, the resulting image should look less random now.
Example:

```
python3 -m utfcolor -f examples/lorem-ipsum.txt -s 10 -e utf-colorv3
```

![utf-colorv3](./examples/utf-colorv3.png)

1000 words of lorem ipsum encoded with utf-colorv3.

### rng-utf-color

The fourth version of UTF-Color is also a 24-Bit encoding and very similar to version 2 and 3. The color-codes will be chosen randomly. To avoid a too random looking image, the supported characters are sorted into three groups: letters, numbers and special. A starting point for each group gets chosen randomly, but the color-codes of the characters in that group will be relative to each other (i.e. all letters might look greenish while all numbers look redish).