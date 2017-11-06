This repo is a collection of all my small scripts.

<h2><b> tic_tac_toe.py</b></h2>
The classic game of tic-tac-toe which keeps a tally of your scores over multiple games.

Requires Python3.

Instructions:
Clone the file. Run <code>python tic_tac_toe.py</code> or <code>python3 tic_tac_toe.py</code>, whichever is applicable.


----------------------------
<h2><b> billboard_downloader.py</b></h2>
Downloads all songs listed in any supplied billboards url (top 100 by default), or all the songs listed in a file, in general.

Requirements:
Python
youtube-dl

Usage:
<code>git clone https://github.com/hundredrab/spock42 </code> 
python billboard_downloader/download.py {{ url or genre }}
</code>

{{ url or genre }} may be any url of the billboards website listing top songs, or one genre among 'pop', 'country', 'rock', or 'indie'.

<b>For</b> downloading all the songs from a file-list, run:
<code> python billboard_downloader/download.py file {{ filename }}

{{ filename }} should contain the name of a file which contains list of songs to be downloaded, separated by newlines.

The songs will be downloaded in a <code>music\_new</code> directory, inside <code>billboard\_downloader/</code>. Once downloaded, songs will not be re-downloaded, even if deleted, unless names are cleared in <code>downloaded.txt</code>. This allows users the freedom to move/delete music to another folder without going through the trouble of re-downloading.


----------------------------
<h2><b> Metadata_changer.py</b></h2>
Changes the artist, title, etc. Useful for songs downloaded using youtube-dl which do not have relevant metadata but contain verbose titles.

Usage
