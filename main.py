from io import BytesIO
from json import loads
from struct import pack
from binascii import crc32
from urllib.request import urlopen
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth, getFont
crc = lambda data: crc32(data, 1051410793) # crc of 'cOMM'
def combine(pdf: bytes, png: bytes) -> bytes:
    return b"\x89PNG\r\n\x1a\n" + \
           pack('>I', len(pdf)) + \
           b'cOMM' + pdf        + \
           pack('>I', crc(pdf)) + \
           png[8:]
def get_png(url: str = "https://raw.githubusercontent.com/donno2048/snake/master/demo/qr.png") -> bytes:
    return urlopen(url).read()
def get_pdf() -> bytes:
    pdf = BytesIO()
    def link(canvas: Canvas, text: str, font: str, size: float, color: tuple, url: str, location: tuple) -> None:
        face = getFont(font).face
        width = stringWidth(text, font, size)
        height = (face.ascent - face.descent) / 1000 * size
        canvas.setFont(font, size)
        canvas.linkURL(url, (*location, location[0] + width, location[1] + height))
        canvas.setFillColorRGB(*color)
        canvas.setStrokeColorRGB(*color)
        canvas.drawString(*location, text)
        canvas.setLineWidth(.5)
        canvas.line(location[0], location[1] - height / 5, location[0] + width, location[1] - height / 5)
    c = Canvas(pdf, pagesize = letter)
    c.setFillColorRGB(.9, .9, .9)
    c.rect(-1, letter[1] - 120, letter[0] + 2, 121, fill = True)
    c.setFillColorRGB(.1, .2, .2)
    c.setFont("Helvetica-Bold", 35)
    c.drawString(30, letter[1] - 50, "ELISHA HOLLANDER")
    c.setFont("Helvetica", 15)
    c.drawString(30, letter[1] - 80, "  ".join("SOFTWARE ENGINEER"))
    section = (letter[0] / 2, (letter[1] - 120) / 3)
    margins = (section[0] / 8, 3 * section[0] / 4 + 20)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margins[0], 11 * section[1] / 4 - 20, " ".join("DETAILS"))
    c.drawString(margins[0], 7 * section[1] / 4, " ".join("EXPERIENCE"))
    c.drawString(margins[0], 3 * section[1] / 4, " ".join("EDUCATION"))
    c.drawString(margins[1], 11 * section[1] / 4 - 20, " ".join("PROFILE"))
    c.drawString(margins[1], 7 * section[1] / 4, " ".join("TRIVIA"))
    c.drawString(margins[1], 3 * section[1] / 4, " ".join("OPEN SOURCE"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margins[0], 7 * section[1] / 4 - 30, "VBA DEVELOPER")
    c.drawString(margins[0], 7 * section[1] / 4 - 90, "FULLSTACK DEVELOPER")
    c.drawString(margins[0], 3 * section[1] / 4 - 30, "COMPUTER ENGINEERING")
    c.drawString(margins[0], 3 * section[1] / 4 - 40, "BACHELOR'S DEGREE")
    c.drawString(margins[0], 3 * section[1] / 4 - 90, "THEORETICAL MATHEMATICS")
    c.drawString(margins[0], 3 * section[1] / 4 - 100, "BACHELOR'S DEGREE")
    c.drawString(margins[1], 7 * section[1] / 4 - 110, "I'M IN GITHUB'S DEVELOPERS PROGRAM")
    mail = "just4now666666@gmail.com"
    link(c, mail, "Helvetica", 8.5, (.1, .2, .2), "mailto:" + mail, (margins[0], 11 * section[1] / 4 - 50))
    link(c, "Personal website", "Helvetica", 8.5, (.1, .2, .2), "https://github.com/donno2048/portfolio", (margins[0], 11 * section[1] / 4 - 70))
    link(c, "I MADE THE SMALLEST SNAKE GAME EVER MADE", "Helvetica-Bold", 10, (.1, .2, .2), "https://github.com/donno2048/snake", (margins[1], 7 * section[1] / 4 - 30))
    link(c, "The Hackaday magazine published an article about it", "Helvetica", 8.5, (.1, .2, .2), "https://hackaday.com/?p=607892", (margins[1], 7 * section[1] / 4 - 50))
    link(c, "I MADE A WIN95 EMULATOR RUNNING ONLINE", "Helvetica-Bold", 10, (.1, .2, .2), "https://donno2048.github.io/win95", (margins[1], 7 * section[1] / 4 - 90))
    link(c, "PLEASE VIEW MY GITHUB ACCOUNT", "Helvetica-Bold", 10, (.1, .2, .2), "https://github.com/donno2048", (margins[1], 3 * section[1] / 4 - 30))
    link(c, "I OPTIMIZED SOME OF PYTHON'S SOURCE CODE", "Helvetica-Bold", 10, (.1, .2, .2), "https://github.com/python/cpython/pull/27102", (margins[1], 3 * section[1] / 4 - 60))
    link(c, "I FOUND A SECURITY VULNERABILITY IN SYMPY", "Helvetica-Bold", 10, (.1, .2, .2), "https://github.com/sympy/sympy-live/issues/192", (margins[1], 3 * section[1] / 4 - 80))
    link(c, "CV source code", "Helvetica", 5, (.1, .2, .2), "https://github.com/donno2048/CV", (letter[0] - 200, 20))
    c.setFont("Helvetica", 8.5)
    c.drawString(margins[0], 7 * section[1] / 4 - 40, "Immanuel")
    c.drawString(margins[0], 7 * section[1] / 4 - 50, "2020")
    c.drawString(margins[0], 7 * section[1] / 4 - 100, "Linnovate")
    c.drawString(margins[0], 7 * section[1] / 4 - 110, "2021")
    c.drawString(margins[1], 7 * section[1] / 4 - 60, "Change the file extension from .pdf to .png to see the program as a QR")
    c.drawString(margins[0], 3 * section[1] / 4 - 50, "Bar Ilan University")
    c.drawString(margins[0], 3 * section[1] / 4 - 60, "2019-2022")
    c.drawString(margins[0], 3 * section[1] / 4 - 110, "Bar Ilan University")
    c.drawString(margins[0], 3 * section[1] / 4 - 120, "2019-2022")
    c.drawString(margins[1], 3 * section[1] / 4 - 40, f"Where I host {loads(urlopen('https://api.github.com/users/donno2048').read())['public_repos']} projects in over than 20 programming languages")
    profile = """
    I'm a 19 year old developer from Israel.
    I have 5 years of experience and looking for a part time job.
    """
    p = Paragraph("<br />".join(map(lambda l: l.strip(), profile.split("\n"))), style = ParagraphStyle("Normal", fontName = "Helvetica", fontSize = 8.5, textColor = (.1, .2, .2)))
    p.drawOn(c, margins[1], 11 * section[1] / 4 - 30 - p.wrap(letter[0] - sum(margins), section[1] - 50)[1])
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(3 * section[0] / 4, 11 * section[1] / 4, 3 * section[0] / 4, section[1] / 4)
    c.line(margins[0], section[1], letter[0] - margins[0], section[1])
    c.line(margins[0], 2 * section[1], letter[0] - margins[0], 2 * section[1])
    c.save()
    return pdf.getvalue()
def main(out: str) -> None:
    open(out, "wb").write(combine(get_pdf(), get_png()))
main("cv.png")
