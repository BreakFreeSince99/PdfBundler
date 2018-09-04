from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "This is Page 1 of Kumar"
SubTitle = "pannekoek"
Name = "pannekoek"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',40)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, Title)
    canvas.setFont('Times-Bold',20)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-135, SubTitle)
    canvas.setFont('Times-Italic',15)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-158, Name)
    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    pass
    
def go(x):
    doc = SimpleDocTemplate(x)
    Story = [Spacer(1,2*inch)]
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

