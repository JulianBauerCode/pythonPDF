#http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/#whoCFCPh3TAks368.99

# #Insert single Strings
#  from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.units import cm, mm, inch, pica
# pdf = Canvas("test001.pdf")
# pdf.setFont("Courier", 12)
# pdf.setStrokeColorRGB(1, 0, 0)
# pdf.drawString(300, 300, "CLASSIFIED")
# pdf.drawString(2 * inch, inch, "For Your Eyes Only")
# pdf.showPage()
# pdf.save()


#Insert line after line
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, mm, inch, pica
pdf = Canvas("test002.pdf")
rhyme = pdf.beginText(inch * 1, inch * 10)
rhyme.textLine('Humpty Dumpty sat on a wall.')
rhyme.textLine('Humpty Dumpty had a great fall.')
rhyme.textLine('All the king’s horses and all the king’s men')
rhyme.textLine('couldn’t put Humpty together again.')
pdf.drawText(rhyme)
pdf.showPage()
pdf.save()




