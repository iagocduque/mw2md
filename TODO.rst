=====
To-do
=====
As stated on the README, this software is incomplete. There are lots of markup fields to be covered.

If you would like to contribute to this project, you should fork this repository and make your own improvements to the source-codes. If the improvements are good enough, they shall be eligible for a pull request and the changes will be put in the official "root" repository.

Or, if you'd like, download one of the ".py" files (either *toMarkdown* or *toMediawiki*) and test them in a random text file. The ".py" files should be executed in your operating system's shell.


Enumerate lists
---------------
.. image:: /images/enumlists.png
   :alt: Incorrectly converted enumerate lists.
The way numbered lists in Markdown are written on the source-code is using number to number. A loop function in Python exists that replaces the numbers for the ``'# '`` markup used in MediaWiki. Same for vice-versa. However, there are issues:

* The counter should return to 1 when the list is broken by a random text out of either the ``[0-9]. (.+?)\n`` (normal item) or the ``'  [0-9]. (.+?)\n'`` (subitem, indented) patterns.
* Enumerate subitems are incorrectly rendered as ``"'#[0-9]. '``, with only the final ``#`` hashtag on the right being replaced. They should be replaced as the ``'  [0-9]. (.+?)\n'`` pattern.

The syntax for bulleted lists (excluding subitems) are the same in both. In *toMediawiki.py*'s case, a flag was added to avoid incorrectly rendering the ``*`` asterisk as ``''`` two single-quotes, as if it was a marking of italic.


Different h1 and h2 formatting
------------------------------
Markdown has an alternate method of marking h1 and h2 headers, looking just like the from h1, h2 and h3 headings in the reStructuredText (.rst) markup language, used in the README of this repo and this file. It uses a filling of the "=" character for h1 or the "-" for h2 in a line break below the text to be marked, based on the length of said text. For example, if the text has 10 characters, 10 = or - symbols will be used.


Exporting
---------
.. image:: /images/exporting.png
   :alt: Procedure of the ">" command in Bash.
There should be a command inside the .py source codes that exports the output. A command in bash (Linux Terminal) exists that exports the arguments outputs to another file: ``commands > output.txt``. The ">" writes the outputs inside the file. The equivalent for *Windows PowerShell* (same for cmd and MS-DOS) is unknown.

But there is a problem: bash's ">" replaces the output file if it already exists. There should be an exception inside the ".py" source-code that throws/raises an error if the output file already exists.


reStructuredText
----------------
.. image:: /images/restructuredtext.svg
   :alt: reStructuredText's logo
While looking randomly at GitHub for projects identical to this very one, I found that some have a README in the .rst format. I looked at them.

Suddenly discovered a new markup lang called reStructuredText. It is less common and is older than Markdown, appearing somewhere in 2001.

