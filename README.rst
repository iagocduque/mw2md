===============================
Markdown to MediaWiki Converter
===============================
.. image:: /mw2md.png
   :alt: Banner
This software, written in *Python* using several libraries, will handle documents' source-codes using either **Markdown** or **MediaWiki** markup languages and convert them based on changing the commands to highlight text.

Planning
========

Functional Requirements
-----------------------
.. image:: /toMarkdown.png
   :alt: A model on how the "toMarkdown" command should work.
The software must convert documents based on their source-code. A text in MediaWiki must be converted to Markdown and vice-versa. The way it converts will pick up regular expressions present in both markup languages and change them to another one. For example, the ``== Heading h1 ==``, used to mark *h1* headers in MediaWiki, must be changed to ``# Heading h1``, the equivalent of the same to Markdown.

As an exception treated, the software will only open and read text-based files. Images, videos, audios, compiled programs (``*.exe``, ``.msi``, ``.AppImage``, ``.x86_64``, etc.), compressed files (``*.rar``, ``.zip``, ``.7z``, ``.apk``, ``.tar.gz``, ``.deb``, ``.rpm``, etc.), program parts (``*.dll``, etc.) and others **will not be opened.**

Non-functional Requirements
---------------------------
.. image:: /toMediawiki.png
   :alt: A model on how the "toMediawiki" command should work.

Because it is still just a model, the software, for a while, will run in the form of a shell (MS-DOS, Bash, etc.)'s command. I plan in the future to make it either:
 * A software for Windows, macOS and Linux by using Python's user interface libraries like *PySimpleGUI* or *tkInter*;
 * An application for Android and iOS;
 * A website by using HTML, JavaScript and Cascading Style Sheets.
 
Markup languages
================

MediaWiki
---------
.. image:: /mediawiki.svg
   :alt: MediaWiki's logo

This is the markup language used in multiple Wiki websites like `Wikipedia <http://en.wikipedia.org>`_, `FANDOM <http://fandom.com>`_, `wiki.gg <http://wiki.gg>`_, `Miraheze <http://miraheze.org>`_ and many others. The three latter websites are the main wiki hosters.

Okay, how can I basically describe the MediaWiki. It was used on various wikis I was a contributor, such as `Qualitipedia <http://newqualitipedia.telepedia.net>`_ (at the time when it was hosted by Miraheze) and `The Dubbing Database <http://dubdb.fandom.com>`_. I don't know why, but I preferred editing on the source-code than the visual editor. All of my contributions on these wikis were sometime before 2023, these dates being before I started my Computer Science B.Sc. college.

Here is my "wikiography" (pages I have created or updated), the best I can remember:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Page
     - Wiki
     - Status
     - Username
     - Hosting
   * - `Dan the Man <https://web.archive.org/web/20221023221013/https://awesomegames.miraheze.org/wiki/Dan_the_Man>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Dangerous Dungeons <https://web.archive.org/web/20221212210516/https://awesomegames.miraheze.org/wiki/Dangerous_Dungeons_and_Super_Dangerous_Dungeons>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Disgaea: Hour of Darkness <https://web.archive.org/web/20221212211540/https://awesomegames.miraheze.org/wiki/Disgaea:_Hour_of_Darkness>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Mother 3 <https://web.archive.org/web/20230112171734/https://awesomegames.miraheze.org/wiki/Mother_3>`_
     - Awesome Games Wiki (deleted wiki)
     - Updated
     - *GRAND-DUCHY*
     - Miraheze
   * - `Super Cat Tales 2 <https://web.archive.org/web/20221213005944/https://awesomegames.miraheze.org/wiki/Super_Cat_Tales_2>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Super Dangerous Dungeons <https://web.archive.org/web/20221212210516/https://awesomegames.miraheze.org/wiki/Dangerous_Dungeons_and_Super_Dangerous_Dungeons>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `The King of Fighters '97 <https://web.archive.org/web/20210513130401/https://awesomegames.miraheze.org/wiki/The_King_of_Fighters_%2797>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `The King of Fighters '98 <https://web.archive.org/web/20210513050231/https://awesomegames.miraheze.org/wiki/The_King_of_Fighters_%2798>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `The King of Fighters 2002 <https://web.archive.org/web/20210511190421/https://awesomegames.miraheze.org/wiki/The_King_of_Fighters_2002>`_
     - Awesome Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Beat Street <https://web.archive.org/web/20210515180856/https://crappygames.miraheze.org/wiki/Beat_Street>`_
     - Crappy Games Wiki (deleted wiki)
     - Deleted by staff
     - *GRAND-DUCHY*
     - Miraheze
   * - `Head Boxing <https://web.archive.org/web/20210302141620/https://crappygames.miraheze.org/wiki/Head_Boxing>`_
     - Crappy Games Wiki (deleted wiki)
     - Deleted by staff
     - *GRAND-DUCHY*
     - Miraheze
   * - `Schnappi - 3 Fun Games <https://web.archive.org/web/20221011175837/https://crappygames.miraheze.org/wiki/Schnappi_-_3_Fun_Games>`_
     - Crappy Games Wiki (deleted wiki)
     - Updated
     - *GRAND-DUCHY*
     - Miraheze
   * - `The King of Fighters 2001 <https://web.archive.org/web/20220727051040/https://crappygames.miraheze.org/wiki/The_King_of_Fighters_2001>`_
     - Crappy Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - Windows Flash parodies (not found in archive.org)
     - Crappy Games Wiki (deleted wiki)
     - Created
     - *GRAND-DUCHY*
     - Miraheze
   * - `Attack on Titan (Brazilian Portuguese) <https://dubdb.fandom.com/wiki/Attack_on_Titan_(Brazilian_Portuguese)>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `Dado Atrasado <https://dubdb.fandom.com/wiki/Dado_Atrasado>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `Death Note (Brazilian Portuguese) <https://dubdb.fandom.com/wiki/Death_Note_(Brazilian_Portuguese)>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `My Hero Academia (Brazilian Portuguese) <https://dubdb.fandom.com/wiki/My_Hero_Academia_(Brazilian_Portuguese)>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `Resident Evil 4 (Remake) <https://dubdb.fandom.com/wiki/Resident_Evil_4_(Remake)>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `サルゲッチュ <https://dubdb.fandom.com/wiki/サルゲッチュ>`_
     - The Dubbing Database
     - Created
     - *StuDionysius*
     - FANDOM
   * - `Disgaea: Hour of Darkness <https://logos.fandom.com/wiki/Disgaea:_Hour_of_Darkness>`_
     - Logopedia
     - Created
     - *StuDionysius*
     - FANDOM

Markdown
--------
.. image:: /markdown.svg
   :alt: Markdown's logo

This is the markup language used in GitHub (and other code versioning websites) for documents like README, CONTRIBUTING, LICENSE, etc.

I liked this markup language. It's easier to write text using Markdown than MediaWiki. In fact, the former can also be used as an alternative for those that didn't like the latter. One individual I used to follow online, in particular, would go as far as `developing an entire "wiki" (website) <https://gitlab.com/supremesonicbrazil/ytpbr-wiki>`_ using various document types and programming languages, including Markdown for page editing. All that because `he didn't like MediaWiki <https://youtu.be/BomasKTDs0M?t=430>`_.

I suddenly knew about this wiki when I was off the internet (due to pressures of my college, and life in general). For those asking, yes, I used to make *YouTube Poops*. So I created a page about myself there. For further information, you may want to have a look at the page I wrote below (NOTE: Because it uses *Google Translate*, the page has **LOTS** of gibberish and inconsistensies):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Page
     - Wiki
     - Status
     - Username
     - Hosting
   * - `ULTIMEGANIUS <https://ytpbr-wiki.translate.goog/pessoas/ULTIMEGANIUS/?_x_tr_sl=pt&_x_tr_tl=en&_x_tr_hl=pt-BR&_x_tr_pto=wapp>`_
     - Catálogo YTPBR
     - Created
     - *iagocduque*
     - GitLab

Comparison table
----------------
.. list-table::
   :header-rows: 1
   :widths: auto

   * - Markdown
     - Meaning
     - Mediawiki
   * - ``#``
     - Heading h1
     - ``= =``
   * - ``##``
     - Heading h2
     - ``== ==``
   * - ``###``
     - Heading h3
     - ``=== ===``
   * - ``####``
     - Heading h4
     - ``==== ====``
   * - ``#####``
     - Heading h5
     - ``===== =====``
   * - ``######``
     - Heading h6
     - ``====== ======``
   * - ``__ __``
     - Bold
     - ``''' '''``
   * - ``_ _``
     - Italic
     - ``'' ''``
   * - ``~ ~``
     - Strikethrough
     - ``<s> </s>``
   * - ``<u> </u>``
     - Underlining
     - ``<u> </u>``
   * - ``` ```
     - In-line code
     - ``<code> </code>``
   * - ``````` ```````
     - Blockcode
     - ``<pre> </pre>``
   * - ``[GitHub](http://github.com)``
     - External link
     - ``[http://github.com GitHub]``
     
License
=======
.. image:: /gplv3.svg
   :alt: GNU General Public License v3.0's logo
This software is open-source by using Free Software Foundation's *GNU General Public License*, particularly the version 3.0.

This means you can reverse-engineer this software for studying purposes, modify or custom based on your own taste or improve the source-code (fixing bugs and glitches) and sending pull requests for me to put all improvements on the official one. The latter of the three said things is a similar procedure used by *Early Access* videogames on Steam, where the developers uses gamers to debug and polish the game.

Every fork of this repository on GitHub should also be of the GPL-v3 license, being this one of the limitations of the. It is deliberately the same license used by the Linux kernel; only this suggests that every Linux distro known to man also uses the GPL license.

Copyright
=========
Copyright © 2026, Iago C. Duque. All rights reserved.
