#!/usr/bin/env python3
# ^ This element will allow the ./-md.py program run directly on the Terminal, without needing the preceding "python3".
import sys
# ^ Importing this library is necessary to use and open a wanted file to convert. By using only the filename, the same should be on the same folder the program is. If it is in another folder, the absolute directory (path) should be specified.
import re
# ^ This will replace patterns and regular expressions if they match. The following command will be used: re.sub(r"(.+?)",r"\1",text).


if len(sys.argv)!=2: # ← Two items: Program's name and filename
 print("Unspecified file or bad input.")
 exit()

name=sys.argv[1] # ← The second file on the string is the filename
try: # ← Field to treat exceptions
 with open(name,'r',encoding='utf-8') as file: # ← Will open the text file and read the content inside
  text=file.read() # ← Will read and store the content in the variable
except: # ← If the file either does not exist, it's not text type or anything else happened
 print("File does not exist or the type is invalid.")
 exit()


# ↓ NOTE: Since Python reads from left to right and from up to down, to avoid incorrect rendering, the ccodes will run from the highest to the lowest of characters' amount. "Bolditalic" first, italic last. Heading h6 first, heading h1 last.

# ↓ Enumerate sub-items
if "##" in text: # ←  Will only be done if the specified string exists in text
 text=re.sub(r"\n##(.+?)",r"\n   1.\1",text)

# ↓ Enumerate lists
if "#" in text:
 text=re.sub(r"\n#(.+?)",r"\n1.\1",text)

# ↓ Heading h6 formatting
if "======" in text:
 text=re.sub(r"====== (.+?) ======",r"###### \1",text)
 text=re.sub(r"======(.+?)======",r"###### \1",text)
 
# ↓ Heading h5 formatting
if "=====" in text:
 text=re.sub(r"===== (.+?) =====",r"##### \1",text)
 text=re.sub(r"=====(.+?)=====",r"##### \1",text)
 
# ↓ Heading h4 formatting
if "====" in text:
 text=re.sub(r"==== (.+?) ====",r"#### \1",text)
 text=re.sub(r"====(.+?)====",r"#### \1",text)

# ↓ Heading h3 formatting
if "===" in text:
 text=re.sub(r"=== (.+?) ===",r"### \1",text)
 text=re.sub(r"===(.+?)===",r"### \1",text)

# ↓ Heading h2 formatting
if "==" in text:
 text=re.sub(r"== (.+?) ==",r"## \1",text)

# ↓ Heading h1 formatting
if "=" in text:
 text=re.sub(r"= (.+?) =",r"# \1",text)
 
# ↓ Alternate h1 and h2 formattings
def h1h2alt(txt):
 pattern=re.compile(r"^(=+)(.*?)\1$",re.MULTILINE)
 def subst(match):
  lvl=len(match.group(1))
  header=match.group(2).strip()
  if lvl==1:
   char='='
  elif lvl==2:
   char='-'
  else:
   char='=' if lvl%2==1 else '-'
  size=max(len(header),4)
  return f"{header}\n{char*size}"
 return pattern.sub(subst,txt)
if "==" in text or "=" in text:
 text=h1h2alt(text)

# ↓ Bold and italic formatting
if "'''''" in text:
 text=re.sub(r"'''''(.+?)'''''",r"___\1___",text)

# ↓ Bold formatting
if "'''" in text:
 text=re.sub(r"'''(.+?)'''",r"__\1__",text)

# ↓ Italic formatting
if "''" in text:
 text=re.sub(r"''(.+?)''",r"_\1_",text)

# ↓ Bulleted sub-items
# ↓ NOTE: The way the re library works, the "*" in the pattern to be grabbed must be written as "\*" to avoid confusions. Putting simply an "*" will throw an exception.
if "** " in text:
 text=re.sub(r"\n\*\* (.+?)",r"\n   * \1",text)

# ↓ Striked through text
if "<s>" in text and "</s>" in text:
 text=re.sub(r"<s>(.+?)</s>",r"~\1~",text)

# ↓ Blockcode field (copyable on GitHub-flavored formatting)
if "<pre>" in text and "</pre>" in text:
 text=re.sub(r"<pre>(.+?)</pre>",r"```\1```",text)

# ↓ Inline code field
if "<code>" in text and "</code>" in text:
 text=re.sub(r"<code>(.+?)</code>",r"`\1`",text)
 
# ↓ Quotes field
if "{{quote|" in text:
 text=re.sub(r"{{quote\|(.+?)}}\n",r">\1\n\n",text)
if "<blockquote>" in text and "</blockquote>" in text:
 text=re.sub(r"<blockquote>(.+?)</blockquote>\n",r">\1\n\n",text)

# ↓ External link
if "https" in text:
 text=re.sub(r'\[(https?://\S+?)\s+(.+?)\]', r'[\2](\1)',text)
if "http" in text:
 text=re.sub(r'\[(http?://\S+?)\s+(.+?)\]', r'[\2](\1)',text)
 
# ↓ Image file
if "[[File:" in text and "|" in text: # ← With an alt text
 text=re.sub(r"\[\[File?:(.+?)\|(.+?)\|(.+?)]]",r'![](/\1 "\3")',text)
 text=re.sub(r"\[\[File?:(.+?)\|(.+?)]]",r'![\2](/\1)',text)
if "[[File:" in text: # ← Without alt text
 text=re.sub(r"\[\[File?:(.+?)]]",r"![](/\1)",text)


print(text)
