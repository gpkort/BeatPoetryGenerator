import bs4

HAPPY_LINKS_URL = 'http://mockurl.com/links/happy'
EMPTY_LINKS_URL = 'http://mockurl.com/links/empty'
NOPOEM_LINKS_URL = 'http://mockurl.com/links/no_poems'
MIXED_LINKS_URL = 'http://mockurl.com/links/mixed_poems'
NO_CONTENT_URL = 'http://mockurl.com/no_content'
BAD_CONTENT_URL = 'http://mockurl.com/bad_content'

HAPPY_POEM_URL = 'http://mockurl.com/happy_tag'
BAD_DIV_POEM_URL = 'http://mockurl.com/bad_div'
EMPTY_DIV_POEM_URL = 'http://mockurl.com/empty_div'
NO_TEXT_DIV_POEM_URL = 'http://mockurl.com/notext_div'

BAD_CONTENT = "dnnncadnhdfb"

UTF16_STRING_LIST = ["#ÑÑÖ#"]
UTF8_STRING_LIST = ["##"]

HAPPY_RAW_STRING_LIST = ["Here is one line!", "     has tabs. ", "join this line w- ",
                         "ith this one. ", "Next join this one ", "with this one.", "no ending"]

HAPPY_CLEAN_STRING_LIST = ["Here is one line!", "has tabs.", "join this line with this one.",
                           "Next join this one with this one.", "no ending"]

EMPTY_POEM_TAGS = "<html><title>list of tags</title><body><div " + \
                  "style='padding-left:14px;padding-top:20px;font-family:Arial;font-size:13px;'/></body></html> "

NO_TEXT_POEM_TAGS = "<html><title>list of tags</title><body><div " + \
                    "style='padding-left:14px;padding-top:20px;font-family:Arial;font-size:13px;'><B></B><br><H1/><br><B" + \
                    "/><br></div></body></html> "

BAD_DIV_POEM_TAGS = "<html><title>list of tags</title><body><div " + \
                    "style='padding-left:14px;padding-top:20px;font-family:Arial;font-size:14px;'>America I've given you " + \
                    "all and now I'm nothing. <br>America two dollars and twentyseven cents January <br>        17, " + \
                    "1956. <br>I can't stand my own mind. <br>America when will we end the human war? <br>Go fuck " + \
                    "yourself with your atom bomb. <br></div></body></html> "

HAPPY_POEM_TAGS = "<html><title>list of tags</title><body><div " + \
                  "style='padding-left:14px;padding-top:20px;font-family:Arial;font-size:13px;'>America I've given you " + \
                  "all and now I'm nothing. <br>America two dollars and twentyseven cents January <br>        17, " + \
                  "1956. <br>I can't stand my own mind. <br>America when will we end the human war? <br>Go fuck " + \
                  "yourself with your atom bomb. <br></div></body></html> "

GOOD_POET_LINKS = "<html><title>list of links</title><body>" + \
                  "<a href='/poets/allen_ginsberg/poems/8350'>When The Light Appears</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8361'>First Party At Ken Kesey's With Hell's Angels</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8362'>Wild Orphan</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8363'>Hum Bom!</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8364'>Cosmopolitan Greetings</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8365'>Sphincter</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8376'>CIA Dope Calypso</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8377'>In The Baggage Room At Greyhound</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8378'>Psalm IV</a>" + \
                  "<a href='/poets/allen_ginsberg/poems/8379'>Crossing Nation</a>" + \
                  "</body></html>"

EMPTY_LINKS = "<html><title>list of links</title><body></body></html>"
NO_POET_LINKS = "<html><title>list of links</title><body>" + \
                "<a href='blah'>When The Light Appears</a>" + \
                "<a href='blah'>First Party At Ken Kesey's With Hell's Angels</a>" + \
                "</body></html>"

MIXED_POET_LINKS = "<html><title>list of links</title><body>" + \
                   "<a href='blah'>When The Light Appears</a>" + \
                   "<a href='blah'>First Party At Ken Kesey's With Hell's Angels</a>" + \
                   "<a href='/poets/allen_ginsberg/poems/8378'>Psalm IV</a>" + \
                   "<a href='/poets/allen_ginsberg/poems/8379'>Crossing Nation</a>" + \
                   "</body></html>"
