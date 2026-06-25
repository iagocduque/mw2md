===============================
Markdown to MediaWiki Converter
===============================
.. image:: /images/mw2md.png
   :alt: Banner
This software, written in *Python* using the "re" (regex) library, will handle documents' source-codes using either **Markdown** or **MediaWiki** markup languages and convert them based on changing regular expressions (commands) to highlight text.

Content
=======
1. `Planning <#planning>`_

 * `Functional Requirements <#functional-requirements>`_
 * `Non-functional Requirements <#non-functional-requirements>`_

2. `Markup languages <#markup-languages>`_

 * `MediaWiki <#mediawiki>`_
 * `Markdown <#markdown>`_

3. `Use of AI <#use-of-ai>`_
4. `License <#license>`_
5. `Contributing <#contributing>`_

 * `To-do <#to-do>`_
 * `Impossible <#impossible>`_

6. `Copyright <#copyright>`_


Planning
========
Functional Requirements
-----------------------
.. code-block :: mediawiki

  <blockquote>This file will be translated from MEDIAWIKI to MARKDOWN.</blockquote>
  {{quote|This file will be translated from MEDIAWIKI to MARKDOWN.}}
  [[File:image.png|thumb|Sample image.]]
  [[File:image.png|Sample image.]]
  [[File:image.png]]
  = Heading h1a =
  =Heading h1b=
  == Heading h2a ==
  ==Heading h2b==
  === Heading h3 ===
  ==== Heading h4 ====
  ===== Heading h5 =====
  ====== Heading h6 ======
  '''''Boltalic'''''
  '''Bold'''
  ''Italic''
  ...
.. code-block ::

  root@ubuntu:/home/user/Documents# ./-md.py test.wiki
  > This file will be translated from MEDIAWIKI to MARKDOWN.
  
  > This file will be translated from MEDIAWIKI to MARKDOWN.
  
  ![](/image.png "Sample image.")
  ![Sample image.](/image.png)
  ![](/image.png)
  # Heading h1a
  Heading h1b
  ===========
  ## Heading h2a
  Heading h2b
  -----------
  ### Heading h3
  #### Heading h4
  ##### Heading h5
  ###### Heading h6
  ___Boltalic___
  __Bold__
  _Italic_
  ...

The docs should be converted based on their source-code. A text in MediaWiki must be converted to Markdown and vice-versa. The way it converts will pick up patterns (regular expressions) present in both markup languages and change them to another one. For example, the ``[Sample Text](http://website.io)``, used to mark external links in MediaWiki, must be changed to ``[http://website.io Sample Text]``, the equivalent of the same to Markdown.

The comparison table below is to have an idea how the strings are marked:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Markdown
     - Meaning
     - Mediawiki
   * - ``#``
     - Heading h1 (common)
     - ``= =``
   * - ``====`` (under text)
     - Heading h1 (alternate)
     - ``= =``
   * - ``##``
     - Heading h2 (common)
     - ``== ==``
   * - ``----``  (under text)
     - Heading h2 (alternate)
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
   * - ``[Sample Text](http://website.io)``
     - External link
     - ``[http://website.io Sample Text]``
   * - ``![](/image.png)``
     - Image (no alt-text)
     - ``[[File:image.png]]``
   * - ``![Text](/image.png)``
     - Image (with alt-text)
     - ``[[File:image.png|Text]]``
   * - ``![](/image.png "Text")`` (cursor hover)
     - Image (thunbnail)
     - ``[[File:image.png|thumb|Text]]`` (below image)

As an exception treated, the software will only open and read text-based files. Images, videos, audios, compiled programs (``.exe``, ``.msi``, ``.AppImage``, ``.x86_64``, etc.), compressed files (``.rar``, ``.zip``, ``.7z``, ``.apk``, ``.tar.gz``, ``.deb``, ``.rpm``, etc.), program parts (``.dll``, etc.) and others **will not be opened.**

Considering the program is, for a while, for a shell (MS-DOS, Bash, etc.). A terminal should be opened based on the directory (folder) the program and the input text file is in, using the ``mw2md -wiki file.md`` args to convert.

Check the comments inside the ".py" files' source-codes (not yet compiled) for further info.


Non-functional Requirements
---------------------------
.. code-block :: markdown

  > This file will be translated from MEDIAWIKI to MARKDOWN.
  
  ![](/image.png "Sample image.")
  ![Sample image.](/image.png)
  ![](/image.png)
  # Heading h1a
  Heading h1b
  ===========
  ## Heading h2a
  Heading h2b
  -----------
  ### Heading h3
  #### Heading h4
  ##### Heading h5
  ###### Heading h6
  ___Boltalic 1___, __*Boltalic 2*__, *__Boltalic 3__*, _**Boltalic 4**_, **_Boltalic 5_** and ***Boltalic 6***
  __Bold 1__ and _*Bold 2*_
  _Italic 1_ and *Italic 2*
  ...
.. code-block ::

  root@ubuntu:/home/superuser/Documents# ./-wiki.py test.md
  {{quote|This file will be translated from MEDIAWIKI to MARKDOWN.}}
  [[File:image.png|thumb|Sample image.]]
  [[File:image.png|Sample image.]]
  [[File:image.png]]
  = Heading h1a =
  =Heading h1b=
  == Heading h2a ==
  ==Heading h2b==
  === Heading h3 ===
  ==== Heading h4 ====
  ===== Heading h5 =====
  ====== Heading h6 ======
  '''''Boltalic 1''''', '''''Boltalic 2''''', '''''Boltalic 3''''', '''''Boltalic 4''''', '''''Boltalic 5''''' and '''''Boltalic 6'''''
  '''Bold 1''' and '''Bold 2'''
  ''Italic 1'' and ''Italic 2''
  ...
Because it is still just a model, for a while, it will run in the form of a shell command. I plan in the future to make it either:
 * A software for Windows, Linux and, if possible, macOS by using Python's user interface libraries like *PySimpleGUI* or *tkInter*;
 * An application for Android and iOS;
 * A website by using HTML, JavaScript and Cascading Style Sheets.

 
Markup languages
================
MediaWiki
---------
.. image:: /images/mediawiki.svg
   :alt: MediaWiki's logo

This is the markup language used in multiple Wiki websites like `Wikipedia <http://en.wikipedia.org>`_, `FANDOM <http://fandom.com>`_, `wiki.gg <http://wiki.gg>`_, `Miraheze <http://miraheze.org>`_ and many others. The latter three are the main wiki hosters.

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
   * - `Windows' Flash parodies <https://web.archive.org/web/20221127022502/https://crappygames.miraheze.org/wiki/Windows'_Flash_parodies>`_
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
.. image:: /images/markdown.svg
   :alt: Markdown's logo

This is another markup language to create rich text by simply using a Notepad. It is used in GitHub (and other code versioning websites) for documents like README, CONTRIBUTING, LICENSE, CHANGELOG, MISSING, etc.

I like this markup language. It's easier to write text using Markdown than MediaWiki. In fact, the former can also be used as an alternative for those that didn't like the latter. One individual I used to follow online, in particular, would go as far as `developing an entire "wiki" (website) <https://gitlab.com/supremesonicbrazil/ytpbr-wiki>`_ using various document types and programming languages, including Markdown for page editing. All that because `he didn't like MediaWiki <https://youtu.be/BomasKTDs0M?t=430>`_.

I suddenly knew about this wiki when I was off the internet (due to pressures of my college, and life in general). For those asking, yes, I used to make *YouTube Poops*. So I created a page about myself there. For further information, you may want to have a look at the page I wrote below (NOTE: Because it uses *Google Translate*, the page has **LOTS** of gibberish and inconsistencies):

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
     
Use of AI
=========
  *"Question. Are the .py programs AI-generated? Did you tell to ChatGPT to generate them and you just copy-pasted (plagiarized) the final source-code?"*
Well... yes and no. Please read before overreacting.

No because, if you observe the source-codes of the .py programs, you may notice a lot of aspects that shows amateurism, something that AI wouldn't do. If you tell to a chatbot to generate a Python program that does this, it will obviously look way superior.

And yes because I didn't know to use the "re" library. I tried to develop the software by using Python's proper operations for strings, like ``.replace()``, ``.join()``, ``.strip()``, etc. But they would make the source-code look huge, and several patterns (eg.: ``[Sample Text](http://website.io)`` for external links in Markdown) are impossible to handle using the ``.replace()`` operation. It would be possible with the ``[Sample Text](http://website.io)`` isolated string in a variable, changed to ``[http://website.io Sample Text]``, but it is just a string in a huge text stored.

.. image:: /images/deepseek.svg
   :alt: DeepSeek's logo

So I had to rely on a chatbot to learn how to use the "re". I picked up DeepSeek. Yes, **that** Chinese chatbot that shaked the market, going as far as making NVIDIA `lose more than half a trillion USD in market value <https://www.forbes.com/sites/dereksaul/2025/01/27/biggest-market-loss-in-history-nvidia-stock-sheds-nearly-600-billion-as-deepseek-shakes-ai-darling/>`_.

My decision to use DeepSeek is because, I dunno, I found it superior compared to ChatGPT, Google's Gemini, Copilot or Claude. The former's results from the written prompts say closer to what I think than the latter three.


License
=======
.. image:: /images/gplv3.svg
   :alt: GNU General Public License v3.0's logo
This software is open-source by using Free Software Foundation's *GNU General Public License*, particularly the version 3.0.

This means you can reverse-engineer this software for studying purposes, modify or custom based on your own taste or improve the source-code (fixing bugs and glitches) and sending pull requests for me to put all improvements on the official one.

That being said, a limitation provided by the chosen license. Every fork of this repository on GitHub should also be "GPL-v3" license, being this one of the limitations of the said license. Deliberately the same one used by the Linux kernel; only this suggesting that every Linux distro known to man also uses the GPL license. And, unlike other licenses like *MIT*, this project cannot be forked for profit.

You may want to read the GPL-v3 under the License tab of this repo.


Contributing
============
As stated, this software is incomplete. There are lots of markup fields to be covered.

If you would like to contribute to this project, you should fork this repository and make your own improvements to the source-codes. If the improvements are good enough, they shall be eligible for a pull request and the changes will be put in the official "root" repository. Similar procedure used by *Early Access* videogames on Steam, where the developers uses gamers to debug and polish the game.

Or, if you'd like, download one of the ".py" files (either *-md* or *-wiki*) and test them in a random text file. The ".py" files should be executed in your operating system's shell.

 *Question. Why did you put a "contributing" section inside the README? You can create a separate "CONTRIBUTING.rst" file and a new tab is created.*
Why? Because the "new tabs" for special files (other than README) still do not exist for GitHub's Android/iOS apps. They only exist, for mobile, when accessing the same's website in mobile browsers. Which is a complete absurd, because GitHub is owned, as a subsidiary, by the trillion-dollar valuable Microsoft now.


To-do
-----
* Tables and sheets;
* More detailing of media (images, audios, videos, etc.);
* Blockquotes inside blockquotes ``>>`` for MediaWiki;
* re.sub **not** grabbing inside blockcodes (avoid ``def __init__`` becoming ``def '''init'''``);
* Output exporting inside code (no bash/Terminal's ``>`` function);
* Possibly... support for reStructuredText?


Impossible
----------
* ``<nowiki></nowiki>`` equivalent for Markdown;
* Mermaid diagrams for MediaWiki.


Copyright
=========
Copyright © 2026, Iago C. Duque. All rights reserved.
