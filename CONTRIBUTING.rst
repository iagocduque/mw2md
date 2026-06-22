=====
To-do
=====
As stated on the README tab, this software is incomplete. There are lots of markup fields to be covered.

If you would like to contribute to this project, you should fork this repository and make your own improvements to the source-codes. If the improvements are good enough, they shall be eligible for a pull request and the changes will be put in the official "root" repository. Similar procedure used by *Early Access* videogames on Steam, where the developers uses gamers to debug and polish the game.

Or, if you'd like, download one of the ".py" files (either *toMarkdown* or *toMediawiki*) and test them in a random text file. The ".py" files should be executed in your operating system's shell.


Exporting
---------
.. image:: /images/exporting.png
   :alt: Procedure of the ">" command in Bash.
There should be a command inside the .py source codes that exports the output. A command in bash (Linux Terminal) exists that exports the arguments outputs to another file: ``commands > output.txt``. The ">" writes the outputs inside the file. The equivalent for *Windows PowerShell* (same for cmd and MS-DOS) is unknown.

But there is a problem: bash's ">" replaces the output file if it already exists. There should be an exception inside the ".py" source-code that throws/raises an error if the output file already exists.

Other
-----
* Tables and sheets;
* More detailing of media (images, audios, videos, etc.);
* re.sub **not** grabbing inside blockcodes (avoid ``def __init__`` becoming ``def '''init'''``).
