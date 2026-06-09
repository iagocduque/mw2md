#!/usr/bin/env python3
# ^ This element will allow the ./toMediawiki.py program run directly on the Terminal, without needing the preceding "python3".
import sys
# ^ Importing this library is necessary to use and open a wanted file to convert. By using only the filename, the same should be on the same folder the program is. If it is in another folder, the absolute directory (path) should be specified.
import re
# ^ This will replace patterns and regular expressions if they match. The following command will be used: re.sub(r"([^.$]+?)",r"\1",text).


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


# ↓ NOTE: Since Python reads from left to right and from up to down, to avoid incorrect rendering, the codes will run from the highest to the lowest of characters' amount. "Bolditalic" first, italic last. Heading h6 first, heading h1 last.

# ↓ Heading h6 formatting
if "######" in text: # ←  Will only be done if the specified string exists in text
 text=re.sub(r"###### ([^.$]+?)\n",r"====== \1 ======\n",text)
 
# ↓ Heading h5 formatting
if "#####" in text:
 text=re.sub(r"##### ([^.$]+?)\n",r"===== \1 =====\n",text)
 
# ↓ Heading h4 formatting
if "####" in text:
 text=re.sub(r"#### ([^.$]+?)\n",r"==== \1 ====\n",text)

# ↓ Heading h3 formatting
if "###" in text:
 text=re.sub(r"### ([^.$]+?)\n",r"=== \1 ===\n",text)

# ↓ Heading h2 formatting
# ↓ NOTE: For a while, only the usual "## " formatting will be used. The " \n-" alternative will be handled later. Same for the heading h1, that uses " \n=" as an alternative.
if "##" in text:
 text=re.sub(r"## ([^.$]+?)\n",r"== \1 ==\n",text)

# ↓ Heading h1 formatting
if "#" in text:
 text=re.sub(r"# ([^.$]+?)\n",r"= \1 =\n",text)
 
# ↓ Bold and italic formatting
if "___" in text:
 text=re.sub(r"___([^.$]+?)___",r"'''''\1'''''",text)
# ↓ NOTE: The way the re library works, the "*" in the pattern to be grabbed must be written as "\*" to avoid confusions. Putting simply an "*" will throw an exception.
if "__*" and "*__" in text:
 text=re.sub(r"__\*([^.$]+?)\*__",r"'''''\1'''''",text)
 text=re.sub(r"\*__([^.$]+?)__\*",r"'''''\1'''''",text)
if "_**" and "**_" in text:
 text=re.sub(r"_\*\*([^.$]+?)\*\*_",r"'''''\1'''''",text)
 text=re.sub(r"\*\*_([^.$]+?)_\*\*",r"'''''\1'''''",text)
if "***" in text:
 text=re.sub(r"\*\*\*([^.$]+?)\*\*\*",r"'''''\1'''''",text)

# ↓ Bold formatting
if "__" in text:
 text=re.sub(r"__([^.$]+?)__",r"'''\1'''",text)
if "_*" in text and "*_" in text:
 text=re.sub(r"_\*([^.$]+?)\*_",r"'''\1'''",text)
 text=re.sub(r"\*_([^.$]+?)_\*",r"'''\1'''",text)
if "**" in text:
 text=re.sub(r"\*\*([^.$]+?)\*\*",r"'''\1'''",text)

# ↓ Italic formatting
if "_" in text:
 text=re.sub(r"_([^.$]+?)_",r"''\1''",text)
if "*" in text:
 text=re.sub(r"\*([^.$]+?)\*",r"''\1''",text)

# ↓ Striked through text
if "~" in text:
 text=re.sub(r"~([^.$]+?)~",r"<s>\1</s>",text)

# ↓ Blockcode field (copyable on GitHub-flavored formatting)
if "```" in text:
 text=re.sub(r"```([^.$]+?)```",r"<pre>\1</pre>",text)

# ↓ Quotes field
if ">" in text:
 text=re.sub(r"> (.+?)\n\n",r"{{quote|\1}}\n",text) # ← Space after the ">"
 text=re.sub(r"> (.+?)\n\n",r"{{quote|\1}}\n",text)

# ↓ Inline code field
if "`" in text:
 text=re.sub(r"<code>([^.$]+?)</code>",r"`\1`",text)

# ↓ Images
if "![" in text and "](" in text:
 text=re.sub(r"!\[(.*?)\]\(/(.*?)\)", r"[[File:\2|\1]]",text)

# ↓ External link
if "http" in text:
 text=re.sub(r"\[(.*?)\]\((.*?)\)", r"[\2 \1]",text)


print(f"\n{text}")
