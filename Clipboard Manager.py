import pyperclip as pc

#copy text
pc.copy("Vijay")

#paste text
copiedtext = pc.paste()

# Doesn't return until non-empty text is on the clipboard.
pyperclip.waitForPaste()  

#waits for new text in clipboard, n is time to wait, it is not necessary
pc.waitForNewPaste(n)    

print(copiedtext)
