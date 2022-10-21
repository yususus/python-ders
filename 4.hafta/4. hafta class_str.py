class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __str__(self):
        return "yazilan: .. " + self.metin


nesne = sinif("buraya ne yazarsa sonuna ekler")
print(nesne)