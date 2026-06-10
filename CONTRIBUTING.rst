============
Contributing
============
If you would like to contribute to this project, you should fork this repository and make your own improvements to the source-codes. If the improvements are good enough, they shall be eligible for a pull request and the changes will be put in the official "root" repository.

Or, if you'd like, download one of the ".py" files (either toMarkdown or toMediawiki) and test them in a random text file. The ".py" files should be executed in your operating system's shell.


To-do
=====
As stated on the README, this software is incomplete. There are lots of markup fields to be covered.


Windows and macOS
-----------------
The program is not yet tested on these operating systems. So, the situation has yet to be known if the program works correctly on both.


Enumerate lists
---------------
The way numbered lists in Markdown are written on the source-code is using number to number. There should be a loop function in Python that replaces the numbers for the "# " markup used in MediaWiki. Same for vice-versa.


Different h1 and h2 formatting
------------------------------
Just like the from h1, h2 and h3 headings in the reStructured Text (.rst) markup language, used in the README of this repo and this file, Markdown also has an alternate method of marking h1 and h2 headers. It uses a filling of the "=" character for h1 or the "-" for h2 in a line break below the text to be marked, based on the length of said text. For example, if the text has 10 characters, 10 = or - symbols will be used.


Exporting
---------
.. image:: /images/exporting.png
   :alt: Procedure of the ">" command in Bash.
There should be a command inside the .py source codes that exports the output. A command in bash (Linux Terminal) exists that exports the arguments outputs to another file: ``commands > output.txt``. The ">" writes the outputs inside the file. The equivalent for *Windows PowerShell* (same for cmd and MS-DOS) is unknown.

But there is a problem: bash's ">" replaces the output file if it already exists. There should be an exception inside the ".py" source-code that throws/raises an error if the output file already exists.
