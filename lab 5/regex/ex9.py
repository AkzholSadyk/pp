import re
def text_match(text):
   return re.sub(r" (\W) (IA-Z])", r"\1 \2", text)
a=input ()
print(text_match(a))