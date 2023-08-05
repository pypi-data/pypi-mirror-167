from time import perf_counter

from utfcolor.main import txtToImg
from utfcolor.argparams import parseArgs
import utfcolor.util as util


startTime = perf_counter()

args = parseArgs()

#get the text that will be converted into an image
text = args.pop("text")
if not text:
    with open(args.pop("file")) as f:
        text = f.read()

#start converting the text
txtToImg(text=text, encoding=args.pop("encoding"), outputFile=args.pop("output"), scale=args.pop("scale"))

if args.pop("performancecounter"):
    endTime = perf_counter()
    logger = util.getLogger("utfcolor", "INFO")
    logger.info(f'New Image created in {endTime - startTime: 0.2f} second(s).')