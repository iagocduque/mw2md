#!/usr/bin/env python3
# ^ This element will allow the ./-wiki.py program run directly on the Terminal, without needing the preceding "python3".
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


# ↓ Alternate h1 and h2 formattings
# ↓ NOTE: Since Python reads from left to right and from up to down, to avoid incorrect rendering, the codes will run from the highest to the lowest of characters' amount. "Bolditalic" first, italic last. Heading h6 first, heading h1 last.
def h1h2towiki(txt):
 pattern=re.compile(r"^(.*?)\s*\n(=+|-+)\s*$",re.MULTILINE)
 def repl(match):
  header=match.group(1).strip()
  chars=match.group(2)
  if all(c=="=" for c in chars):
   lv=1
  else:
   lv=2
  return f"{'='*(lv)}{header}{'='*(lv)}"
 return pattern.sub(repl,txt)
text=h1h2towiki(text)

# ↓ Heading h6 formatting
text=re.sub(r"###### (.+?)\n",r"====== \1 ======\n",text)
 
# ↓ Heading h5 formatting
text=re.sub(r"##### (.+?)\n",r"===== \1 =====\n",text)
 
# ↓ Heading h4 formatting
text=re.sub(r"#### (.+?)\n",r"==== \1 ====\n",text)

# ↓ Heading h3 formatting
text=re.sub(r"### (.+?)\n",r"=== \1 ===\n",text)

# ↓ Heading h2 formatting
text=re.sub(r"## (.+?)\n",r"== \1 ==\n",text)

# ↓ Heading h1 formatting
text=re.sub(r"# (.+?)\n",r"= \1 =\n",text)

# ↓ Enumerate sub-items
# ↓ NOTE: Numbers/digits from 0 to 9 are grabbed using re's "(\d+)".
text=re.sub(r"\n   (\d+). (.+?)",r"\n## \2",text)

# ↓ Enumerate lists
text=re.sub(r"\n(\d+). (.+?)",r"\n# \2",text)
 
# ↓ Bulleted sub-items
# ↓ NOTE: The way the re library works, the "*" in the pattern to be grabbed must be written as "\*" to avoid confusions. Putting simply an "*" will throw an exception.
text=re.sub(r"  \* (.+?)\n",r"** \1\n",text)

# ↓ Bold and italic formatting
text=re.sub(r"___(.+?)___",r"'''''\1'''''",text)
text=re.sub(r"__\*(.+?)\*__",r"'''''\1'''''",text)
text=re.sub(r"\*__(.+?)__\*",r"'''''\1'''''",text)
text=re.sub(r"_\*\*(.+?)\*\*_",r"'''''\1'''''",text)
text=re.sub(r"\*\*_(.+?)_\*\*",r"'''''\1'''''",text)
text=re.sub(r"\*\*\*(.+?)\*\*\*",r"'''''\1'''''",text)

# ↓ Bold formatting
text=re.sub(r"__(.+?)__",r"'''\1'''",text)
text=re.sub(r"_\*(.+?)\*_",r"'''\1'''",text)
text=re.sub(r"\*_(.+?)_\*",r"'''\1'''",text)
text=re.sub(r"\*\*(.+?)\*\*",r"'''\1'''",text)

# ↓ Italic formatting
text=re.sub(r"_(.+?)_",r"''\1''",text)
text=re.sub(r"\*(.+?)\*",r"''\1''",text)

# ↓ Quotes field
text=re.sub(r"> (.+?)\n\n",r"{{quote|\1}}\n",text)

# ↓ Striked through text
text=re.sub(r"~(.+?)~",r"<s>\1</s>",text)

# ↓ Blockcode field with syntax highlight
text=re.sub(r"```(.+?)\n([^.$]+?)\n```",r'<syntaxhighlight lang="\1">\n\2\n</syntaxhighlight>',text,flags=re.MULTILINE)

# ↓ Normal blockcode field
text=re.sub(r"```\n([^.$]+?)\n```",r"<pre>\n\1\n</pre>",text,flags=re.MULTILINE)

# ↓ Inline code field
text=re.sub(r"`(.+?)`",r"<code>\1</code>",text)

# ↓ Images
text=re.sub(r'!\[(.*?)\]\(/(.*?) \"(.*?)\"\)', r"[[File:\2|thumb|\3]]",text)
text=re.sub(r"!\[(.*?)\]\(/(.*?)\)", r"[[File:\2|\1]]",text)
text=re.sub(r"!\[\]\(/(.*?)\)", r"[[File:\1]]",text)

# ↓ External link
text=re.sub(r"\[(.*?)\]\((.*?)\)", r"[\2 \1]",text)


print(text)
