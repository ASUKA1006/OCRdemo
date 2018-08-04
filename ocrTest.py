from PIL import Image
import sys

import pyocr
import pyocr.builders
from difflib import SequenceMatcher


def MatchingRate ():
    
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[2]
    print("Will use lang '%s'" % (lang))

    txt = tool.image_to_string(
        Image.open('PNGfile'),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )


    print (txt)


    g_txt = tool.image_to_string(
        Image.open('PNGfile'),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )

    print(g_txt)


    if (txt == g_txt):
        print ("Matching!")
    else:
        print ("!!!!!!oops, it doesn't match!!!!!!")

    matching =  SequenceMatcher(None, txt, g_txt).ratio()
    print()
    print ("Matching rate is " + str(matching*100) + " %")


def main():
    MatchingRate()


if __name__ == "__main__":
    main()
