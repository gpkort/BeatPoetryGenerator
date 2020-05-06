HAPPY_LINKS_URL = 'http://mockurl.com/links/happy'
EMPTY_LINKS_URL = 'http://mockurl.com/links/empty'
NOPOEM_LINKS_URL = 'http://mockurl.com/links/no_poems'
MIXED_LINKS_URL = 'http://mockurl.com/links/mixed_poems'
NO_CONTENT_URL = 'http://mockurl.com/no_content'
BAD_CONTENT_URL = 'http://mockurl.com/bad_content'

BAD_CONTENT = "dnnncadnhdfb"

GOOD_POEM_LINKS = "<html><title>list of links</title><body>" +\
                  "<a href='/poets/allen_ginsberg/poems/8350'>When The Light Appears</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8361'>First Party At Ken Kesey's With Hell's Angels</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8362'>Wild Orphan</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8363'>Hum Bom!</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8364'>Cosmopolitan Greetings</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8365'>Sphincter</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8376'>CIA Dope Calypso</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8377'>In The Baggage Room At Greyhound</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8378'>Psalm IV</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8379'>Crossing Nation</a>" +\
                  "</body></html>"

EMPTY_LINKS = "<html><title>list of links</title><body></body></html>"
NO_POEM_LINKS = "<html><title>list of links</title><body>" +\
                  "<a href='blah'>When The Light Appears</a>" +\
                  "<a href='blah'>First Party At Ken Kesey's With Hell's Angels</a>" +\
                  "</body></html>"

MIXED_POEM_LINKS = "<html><title>list of links</title><body>" +\
                  "<a href='blah'>When The Light Appears</a>" +\
                  "<a href='blah'>First Party At Ken Kesey's With Hell's Angels</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8378'>Psalm IV</a>" +\
                  "<a href='/poets/allen_ginsberg/poems/8379'>Crossing Nation</a>" +\
                  "</body></html>"


GOOD_UGLY_LINKS = b'<html>\n<head>\n\t<title>Allen Ginsberg Poems and Poetry</title>\n\t<meta http-equiv="Description" ' \
        b'content="All of Allen Ginsberg Poems. Allen Ginsberg Poetry Collection from Famous Poets and ' \
        b'Poems.">\n\t<meta http-equiv="Keywords" content="Allen Ginsberg poems, poetry, poem, Allen Ginsberg ' \
        b'poetry">\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\t<LINK ' \
        b'href="/css/style.css" type="text/css" rel="STYLESHEET">\n</head>\n<body bgcolor="#ebebeb" topmargin="0" ' \
        b'bottommargin="0" leftmargin="0" rightmargin="0">\n\t<table width="826" cellpadding="0" align="center" ' \
        b'bgcolor="#FFFFFF">\n\t\t<tr>\n\t\t\t<td ' \
        b'style="padding-bottom:0px;padding-top:10px;padding-right:10px;padding-left:10px;">\n\t\t\t\t<div>\n\n<!-- ' \
        b'ValueClick Media POP-UNDER CODE for Famous Poets and Poems (0.25 hour) -->\n<script ' \
        b'src="//cdn.fastclick.net/js/adcodes/pubcode.min.js"></script><script type="text/javascript">document.write(' \
        b'\'<scr\' + \'ipt type="text/javascript">(function () {try{VCM.media.render({sid:53785,media_id:2,' \
        b'media_type:2,version:"1.2",pfc:900000});} catch(e){}}());</scr\' + \'ipt>\');</script>\n<!-- ValueClick ' \
        b'Media POP-UNDER CODE for Famous Poets and Poems -->\n\n<table height="28" width="100%" ' \
        b'bgcolor="#E1EEED">\n\t<tr>\n\t\t<td align="center"><b>Famous Poets and Poems:&nbsp;</b> <a href="/" ' \
        b'style="color:#000000;">Home</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/poets.html" ' \
        b'style="color:#000000;">Poets</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/month_poem.html" ' \
        b'style="color:#000000;">Poem of the Month</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/month_poet.html" ' \
        b'style="color:#000000;">Poet of the Month</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/top_poems.html" ' \
        b'style="color:#000000;">Top 50 Poems</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/poets_quotes.html" ' \
        b'style="color:#000000;">Famous Quotes</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="/love_poems.html" ' \
        b'style="color:#000000;">Famous Love Poems</a></td>\n\t</tr>\n</table>\n</div>\t\t\t\t<div ' \
        b'align="center"></div>\n\t\t\t\t<br>\n\t\t\t\t<table width="100%">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><a ' \
        b'href="/"><img src="/images/_logo.gif" border="0" alt="Back to main page"></a></td>\n\t\t\t\t\t\t<td ' \
        b'style="padding-bottom:2px;padding-right:16px;" align="right" valign="bottom">Search for: <input type="text" ' \
        b'class="input" style="width:96px;" id="what" onkeydown="if(event.keyCode==13){' \
        b'self.parent.location=\'/search/1/\'+document.getElementById(\'where\').value+\'/\'+escape(' \
        b'document.getElementById(\'what\').value);}"><img src="/images/_spacer.gif" width="6"><select ' \
        b'style="font-size:11px;width:87px;" id="where" class="input"><option value="poems">Poems</option><option ' \
        b'value="poets">Poets</option></select><img src="/images/_spacer.gif" width="9"><input style="width:67px;" ' \
        b'type="button" class="blueBtn" value="Search" ' \
        b'onclick="self.parent.location=\'/search/1/\'+document.getElementById(\'where\').value+\'/\'+escape(' \
        b'document.getElementById(\'what\').value);"></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t<td height=10 ' \
        b'align="center" colspan="2">\n\n\n<br>\n<!-- Conversant Media 728x90 LEADERBOARD CODE for Famous Poets and ' \
        b'Poems -->\n<script type="text/javascript">var vclk_options = {sid:53785,media_type:5,' \
        b'version:"1.4"};</script><script class="vclk_pub_code" type="text/javascript" ' \
        b'src="//cdn.fastclick.net/js/adcodes/pubcode.min.js?sid=53785&media_type=5&version=1.4&exc=1"></script' \
        b'><noscript><a href="//media.fastclick.net/w/click.here?sid=53785&m=1&c=1" target="_blank"><img ' \
        b'src="//media.fastclick.net/w/get.media?sid=53785&tp=5&d=s&c=1&vcm_acv=1.4" width="728" height="90" ' \
        b'border="1"></a></noscript>\n<!-- Conversant Media 728x90 LEADERBOARD CODE for Famous Poets and Poems ' \
        b'-->\n<br>\n</td>\n</tr>\n\t\t\t\t</table>\n\t\t\t\t<table cellpadding="0"><tr><td ' \
        b'style="padding-right:4px;" valign="bottom"><img src="/images/_sl.gif"></td><td><a href="/" ' \
        b'style="color:#0060EA;font-size:10px;">FamousPoetsAndPoems.com</a> <span ' \
        b'style="color:#3C605B;font-size:10px;font-weight:bold;">/</span> <a href="/poets.html" ' \
        b'style="color:#0060EA;font-size:10px;">Poets</a> <span ' \
        b'style="color:#3C605B;font-size:10px;font-weight:bold;">/ </span><a href="/poets/allen_ginsberg" ' \
        b'style="color:#0060EA;font-size:10px;">Allen Ginsberg</a> <span ' \
        b'style="color:#3C605B;font-size:10px;font-weight:bold;">/ Poems</span></td></tr></table>\n\t\t\t\t<table ' \
        b'cellpadding="0" width="100%">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td ' \
        b'height="7"></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td height="6" ' \
        b'bgcolor="#66908A"></td>\n\t\t\t\t\t</tr>\n\t\t\t\t</table>\n\t\t\t\t<table cellpadding="0" ' \
        b'width="100%">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td bgcolor="#F7F4F3" width="150" style="padding: 5px 5px 50px ' \
        b'5px;" valign="top">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<table cellpadding="0" width="100%" height="23" ' \
        b'style="border-width:1px; border-style:solid; border-color:#B1ACB4;">\n\t\t\t\t\t\t\t\t<tr><td ' \
        b'background="/images/_bg_menu.gif" valign="bottom">\n\t\t\t\t\t\t\t\t\t<table cellpadding="0" ' \
        b'height="19">\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-left:9px;padding-right:6px;"><img ' \
        b'src="/images/_dot_menu.gif"></td>\n\t\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:1px;"><a ' \
        b'href="/poets/allen_ginsberg/biography" ' \
        b'class="a_menu">Biography</a></td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t' \
        b'</td></tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t<table cellpadding="0" ' \
        b'height="2"><tr><td></td></tr></table>\n\t\t\t\t\t\t\t<table cellpadding="0" width="100%" height="23" ' \
        b'style="border-width:1px; border-style:solid; border-color:#B1ACB4;">\n\t\t\t\t\t\t\t\t<tr><td ' \
        b'background="/images/_bg_menu.gif" valign="bottom">\n\t\t\t\t\t\t\t\t\t<table cellpadding="0" ' \
        b'height="19">\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-left:9px;padding-right:6px;"><img ' \
        b'src="/images/_dot_menu.gif"></td>\n\t\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:1px;"><a ' \
        b'href="/poets/allen_ginsberg/poems" class="a_menu">Poems</a></td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t' \
        b'\t\t</table>\n\t\t\t\t\t\t\t\t</td></tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<table ' \
        b'cellpadding="0" height="2"><tr><td></td></tr></table>\n\t\t\t\t\t\t\t<table cellpadding="0" width="100%" ' \
        b'height="23" style="border-width:1px; border-style:solid; border-color:#B1ACB4;">\n\t\t\t\t\t\t\t\t<tr><td ' \
        b'background="/images/_bg_menu.gif" valign="bottom">\n\t\t\t\t\t\t\t\t\t<table cellpadding="0" ' \
        b'height="19">\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-left:9px;padding-right:6px;"><img ' \
        b'src="/images/_dot_menu.gif"></td>\n\t\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:1px;"><a ' \
        b'href="/poets/allen_ginsberg/quotes" class="a_menu">Quotes</a></td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t' \
        b'\t\t\t</table>\n\t\t\t\t\t\t\t\t</td></tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<table ' \
        b'cellpadding="0" height="2"><tr><td></td></tr></table>\n\t\t\t\t\t\t\t<table cellpadding="0" width="100%" ' \
        b'height="23" style="border-width:1px; border-style:solid; border-color:#B1ACB4;">\n\t\t\t\t\t\t\t\t<tr><td ' \
        b'background="/images/_bg_menu.gif" valign="bottom">\n\t\t\t\t\t\t\t\t\t<table cellpadding="0" ' \
        b'height="19">\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-left:9px;padding-right:6px;"><img ' \
        b'src="/images/_dot_menu.gif"></td>\n\t\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:1px;"><a ' \
        b'href="/poets/allen_ginsberg/books" class="a_menu">Books</a></td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t' \
        b'\t\t</table>\n\t\t\t\t\t\t\t\t</td></tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<table ' \
        b'cellpadding="0" height="19"><tr><td></td></tr></table>\n\t\t\t\t\t\t\t\n<table cellpadding="0" ' \
        b'align="center" style="border-width:1px; border-color:#D4C8B5; border-style:solid;" width="150">\n<tr>\n<td ' \
        b'background="/images/_bg_tb.gif" style="padding-left:9px;padding-top:5px;" valign="top" height="20"><span ' \
        b'style="font-weight:bold; color:#3C605B;">Popular Poets</span></td>\n</tr>\n<tr>\n<td bgcolor="#FFFFFF" ' \
        b'align="center" height="1" style="padding-top:1px;"><img src="/images/_spacer_g.gif" width="130" ' \
        b'height="1"></td>\n</tr>\n<tr>\n<td style="padding-left:9px;padding-bottom:10px;padding-top:5px;" ' \
        b'bgcolor="#FFFFFF">\n<a href="/poets/langston_hughes">Langston Hughes</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/shel_silverstein">Shel Silverstein</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/pablo_neruda">Pablo Neruda</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/maya_angelou">Maya Angelou</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/edgar_allan_poe">Edgar Allan Poe</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/robert_frost">Robert Frost</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/emily_dickinson">Emily Dickinson</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/elizabeth_barrett_browning">Elizabeth Barrett Browning</a><br><img ' \
        b'src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/e__e__cummings">E. E. Cummings</a><br><img ' \
        b'src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/walt_whitman">Walt Whitman</a><br><img ' \
        b'src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/william_wordsworth">William ' \
        b'Wordsworth</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/allen_ginsberg">Allen ' \
        b'Ginsberg</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/sylvia_plath">Sylvia ' \
        b'Plath</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a href="/poets/jack_prelutsky">Jack ' \
        b'Prelutsky</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a ' \
        b'href="/poets/william_butler_yeats">William Butler Yeats</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/thomas_hardy">Thomas Hardy</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/robert_hayden">Robert Hayden</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/amy_lowell">Amy Lowell</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/oscar_wilde">Oscar Wilde</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets/theodore_roethke">Theodore Roethke</a><br><img src="/images/_spacer.gif" ' \
        b'height="10"><br>\n<a href="/poets.html"><b>All Poets</b></a>&nbsp;&nbsp;<img ' \
        b'src="/images/_ar.gif"></div>\n</td>\n</tr>\n</table>\n<br>\n<table cellpadding="0" align="center" ' \
        b'style="border-width:1px; border-color:#D4C8B5; border-style:solid;" width="150">\n<tr>\n<td ' \
        b'bgcolor="#FFFFFF" style="padding-bottom:10px;padding-top:10px;padding-left:9px;">\nSee also:<br><img ' \
        b'src="/images/_spacer.gif" height="3"><br>\n<a href="/poets_by_nationality.html">Poets by ' \
        b'Nationality</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a ' \
        b'href="/poets_african_american.html">African American Poets</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets_women.html">Women Poets</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/thematic_poems.html">Thematic Poems</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/thematic_quotes.html">Thematic Quotes</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n<a href="/poets_contemporary.html">Contemporary Poets</a><br><img ' \
        b'src="/images/_spacer.gif" height="2"><br>\n<a href="/poets_nobel_prize.html">Nobel Prize Poets</a><br><img ' \
        b'src="/images/_spacer.gif" height="2"><br>\n<a href="/country/America/American_poets.html">American ' \
        b'Poets</a><br><img src="/images/_spacer.gif" height="2"><br>\n<a ' \
        b'href="/country/England/English_poets.html">English Poets</a><br><img src="/images/_spacer.gif" ' \
        b'height="2"><br>\n</td>\n</tr>\n</table>\t\t\t\t\t\t\t\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td bgcolor="#FFFFFF" ' \
        b'width="456" valign="top">\n\n\t\t\t\t\t\t<table cellpadding="0" width="435"><tr><td>\n\t\t\t\t\t\t<table ' \
        b'cellpadding="0">\n\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td colspan="2" ' \
        b'height="10"></td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-right:18px;padding-left:18px;"><img src="/images/_per.gif"></td>\n\t\t\t\t\t\t\t\t<td ' \
        b'valign="top" style="padding-top:22px;">\n\t\t\t\t\t\t\t\t<table height="22" ' \
        b'cellpadding="0">\n\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t<td width="3" ' \
        b'bgcolor="#D4C8B5"></td>\n\t\t\t\t\t\t\t\t\t\t<td ' \
        b'style="padding-left:8px;font-size:19px;color:#3C605B;font-family:Times New Roman;">Allen Ginsberg ' \
        b'Poems</td>\n\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n' \
        b'\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</td><td style="padding-top:20px;" align="right"><a ' \
        b'href="/poets/allen_ginsberg">Back to Poet Page</a></td></tr></table>\n\t\t\t\t\t\t<div align="left" ' \
        b'style="padding-left:10px;padding-top:6px;"><script type="text/javascript"><!--\rgoogle_ad_client = ' \
        b'"pub-0841760908627326";\r/* 336x280, created 12/14/09 */\rgoogle_ad_slot = "7548858617";\rgoogle_ad_width = ' \
        b'336;\rgoogle_ad_height = 280;\r//-->\r</script>\r<script ' \
        b'type="text/javascript"\rsrc="//pagead2.googlesyndication.com/pagead/show_ads.js">\r</script></div>\n\t\t\t' \
        b'\t\t\t<div style="padding-bottom:13px;padding-top:12px;padding-left:10px;">\n\t\t\t\t\t\t<table ' \
        b'cellpadding="0" width="436" style="border-width:1px; border-style:solid; border-color:#D4C8B5;" ' \
        b'background="/images/_t_bg.gif">\n\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td height="22" ' \
        b'style="padding-left:15px;"><b>Sort by:</b>&nbsp;\n\t\t\t\t\t\t\t\tViews |\n\t\t\t\t\t\t\t\t<a ' \
        b'href="/poets/allen_ginsberg/apoems">Alphabetically</td>\n\t\t\t\t\t\t\t\t<td height="22" align="right" ' \
        b'style="padding-right:9px;">Total Poems: ' \
        b'40</td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<table cellpadding="0" ' \
        b'width="436" align="center">\n\t\t\t\t\t\t<tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">1</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8315">Howl</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">2</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8318">America</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">3</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8320">A Supermarket In ' \
        b'California</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">4</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8322">Homework</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">5</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8325">An Eastern ' \
        b'Ballad</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">6</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8327">A Western ' \
        b'Ballad</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">7</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8329">Sunflower ' \
        b'Sutra</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">8</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8331">Song</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">9</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8333">Please ' \
        b'Master</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">10</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8335">Death & Fame</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">11</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8337">The Lion For ' \
        b'Real</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">12</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8340">Refrain</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">13</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8342">Kissass</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">14</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8344">Haiku (Never ' \
        b'Published)</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">15</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8346">A Desolation</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">16</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8348">Five ' \
        b'A.M.</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">17</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8349">Father Death Blues ' \
        b'(Don\'t Grow Old, Part V)</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">18</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8350">In Back Of The Real</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">19</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8351">Feb. 29, ' \
        b'1958</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">20</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8352">Footnote To ' \
        b'Howl</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">21</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8355">September On ' \
        b'Jessore Road</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">22</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8356">Making The Lion For All It\'s Got -- A Ballad</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">23</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8358">When The Light ' \
        b'Appears</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">24</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8360">First Party At Ken Kesey\'s With Hell\'s ' \
        b'Angels</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">25</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8362">Wild Orphan</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">26</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8365">Hum ' \
        b'Bom!</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">27</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8367">Cosmopolitan ' \
        b'Greetings</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">28</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8369">Sphincter</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">29</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8371">CIA Dope ' \
        b'Calypso</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">30</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8374">In The Baggage Room At Greyhound</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">31</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8376">Psalm ' \
        b'IV</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">32</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8378">Crossing ' \
        b'Nation</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">33</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8381">War Profit Litany</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">34</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8382">Those ' \
        b'Two</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">35</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8386">Nagasaki ' \
        b'Days</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">36</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8388">Plutonian ' \
        b'Ode</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" align="right">37</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8390">Transcription Of ' \
        b'Organ Music</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">38</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8391">An Asphodel</a></td></tr><tr><td ' \
        b'style="padding-left:3px;padding-bottom:5px;" width="26" align="right">39</td><td ' \
        b'style="padding-left:7px;padding-bottom:5px;"><a href="/poets/allen_ginsberg/poems/8392">136 Syllables At ' \
        b'Rocky Mountain Dharma Center</a></td></tr><tr><td style="padding-left:3px;padding-bottom:5px;" width="26" ' \
        b'align="right">40</td><td style="padding-left:7px;padding-bottom:5px;"><a ' \
        b'href="/poets/allen_ginsberg/poems/8393">Fourth Floor, Dawn, Up All Night Writing ' \
        b'Letters</a></td></tr>\t\t\t\t\t\t</table>\n\t\t\t\t\t\t<div align="left" ' \
        b'style="padding-left:46px;padding-top:6px;"></div>\n\t\t\t\t\t\t<div align="left" ' \
        b'style="padding-left:10px;padding-top:20px;"><img src="/images/_ln.gif" width="436" ' \
        b'height="2"></div>\n\t\t\t\t\t\t<div style="padding-top:8px;" align="center">\n\t\t\t\t\t\t\t<b>View  Allen ' \
        b'Ginsberg:</b>&nbsp;\n\t\t\t\t\t\t\t<a href="/poets/allen_ginsberg/poems">Poems</a> | \n\t\t\t\t\t\t\t<a ' \
        b'href="/poets/allen_ginsberg/quotes">Quotes</a> |\t\t\t\t\t\t\t<a ' \
        b'href="/poets/allen_ginsberg/biography">Biography</a> |\n\t\t\t\t\t\t\t<a ' \
        b'href="/poets/allen_ginsberg/books">Books</a>\n\t\t\t\t\t\t\t<br><br><!-- Conversant Media 300x250 Medium ' \
        b'Rectangle CODE for Famous Poets and Poems -->\r<script type="text/javascript">var vclk_options = {' \
        b'sid:53785,media_id:6,media_type:8,version:"1.4"};</script><script class="vclk_pub_code" ' \
        b'type="text/javascript" src="//cdn.fastclick.net/js/adcodes/pubcode.min.js?sid=53785&media_id=6&media_type=8' \
        b'&version=1.4&exc=1"></script><noscript><a href="//media.fastclick.net/w/click.here?sid=53785&m=6&c=1" ' \
        b'target="_blank"><img src="//media.fastclick.net/w/get.media?sid=53785&m=6&tp=8&d=s&c=1&vcm_acv=1.4" ' \
        b'width="300" height="250" border="1"></a></noscript>\r<!-- Conversant Media 300x250 Medium Rectangle CODE ' \
        b'for Famous Poets and Poems -->\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td bgcolor="#F7F4F3" ' \
        b'width="176" valign="top" align="center" style="padding-top:8px;padding-bottom:40px;"><!-- Conversant Media ' \
        b'160x600 WIDE SKYSCRAPER CODE for Famous Poets and Poems -->\n<script type="text/javascript">var ' \
        b'vclk_options = {sid:53785,media_type:7,version:"1.4"};</script><script class="vclk_pub_code" ' \
        b'type="text/javascript" src="//cdn.fastclick.net/js/adcodes/pubcode.min.js?sid=53785&media_type=7&version=1' \
        b'.4&exc=1"></script><noscript><a href="//media.fastclick.net/w/click.here?sid=53785&m=3&c=1" ' \
        b'target="_blank"><img src="//media.fastclick.net/w/get.media?sid=53785&tp=7&d=s&c=1&vcm_acv=1.4" width="160" ' \
        b'height="600" border="1"></a></noscript>\n<!-- Conversant Media 160x600 WIDE SKYSCRAPER CODE for Famous ' \
        b'Poets and Poems --></td>\n\t\t\t\t\t</tr>\n\t\t\t\t</table>\n\t\t\t\t<table cellpadding="0" ' \
        b'height="10"><tr><td></td></tr></table>\n\t\t\t\t<table cellpadding="0" height="3" width="100%" ' \
        b'bgcolor="#66908A"><tr><td></td></tr></table>\n\t\t\t\t<table cellpadding="0" ' \
        b'height="1"><tr><td></td></tr></table>\n\t\t\t\t<table cellpadding="0" height="3" width="100%" ' \
        b'bgcolor="#E1EEED">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td style="padding-top:7px;">\n\t\t\t\t\t\t\t<table ' \
        b'width="615" height="18" align="center" bgcolor="#FFFFFF">\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t<td ' \
        b'align="center"><a href="/" style="font-size:10px;">Home</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/about_project.html" style="font-size:10px;">About Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/privacy_policy.html" style="font-size:10px;">Privacy ' \
        b'Policy</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href="/copyright_notice.html" ' \
        b'style="font-size:10px;">Copyright Notice</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/links_poetry.html" style="font-size:10px;">Links</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/link_to_us.html" style="font-size:10px;">Link to Us</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/tell_a_friend.html" style="font-size:10px;">Tell a Friend</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a ' \
        b'href="/contact_us.html" style="font-size:10px;">Contact ' \
        b'Us</a></td>\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t<div align="center" ' \
        b'style="color:#577D77;font-size:11px;padding-bottom:22px;padding-top:8px;">Copyright &copy; 2006 - 2010 ' \
        b'Famous Poets And Poems . com. All Rights Reserved.<br>The Poems and Quotes on this site are the property of ' \
        b'their respective authors. All information has been<br>reproduced here for educational and informational ' \
        b'purposes.</div>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t</table>\n\t\t\t</td>\n\t\t\t<td ' \
        b'bgcolor="#ebebeb" valign="top"><img ' \
        b'src="/images/shadow.gif"></td>\n\t\t</tr>\n\t</table>\n\n</body>\n</html> '
