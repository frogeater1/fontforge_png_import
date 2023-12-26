import os, fontforge

myfont = fontforge.activeFont()
folder_path = "C:\\Users\shiwa\\Desktop\\testimgs"
for filename in os.listdir(folder_path):
    if filename.endswith(".PNG"):
        char_code_int = ord(filename[0])
        char_code_hex = hex(char_code_int)[2:]
        fontforge.logWarning(char_code_hex)
        glyph = myfont.createChar(char_code_int, "uni" + char_code_hex)
        layer = glyph.foreground
        if layer.isEmpty():
            try:
                glyph.importOutlines(os.path.join(folder_path, filename))
            except:
                fontforge.logWarning(os.path.join(folder_path, filename)+" failed")
            else:
                glyph.autoTrace()
                fontforge.logWarning(filename[0] + " import success")
