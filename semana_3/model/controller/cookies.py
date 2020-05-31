import web
from datetime import date
from datetime import datetime

class Cookies:
  def GET(self, name):
    try:
      cookie = web.cookies()
      visit = "0"
      dateHoy = date.today() 
      now = datetime.now()
      Hora = now.strftime("   %H:%M:%S")

      #cookies visit
      if cookie.get("Visit"):
        visit = int(cookie.get("Visit"))
        visit += 1
        web.setcookie("Visit", str(visit),expires = "",  domain = None)
      else:
        web.setcookie("Visit", str(1), expires = "", domain = None)
      
      #cookies name
      if name:
        web.setcookie("Name", name, expires = "", domain=None)
      else:
        name = "Anonimo"
        web.setcookie("Name", name, expires = "", domain=None)
      
      #cookies date
      if cookie.get("Date"):
        web.setcookie("Date", dateHoy, expires="", domain=None)
      else:
        web.setcookie("Date", dateHoy, expires="", domain=None)

      #cookie Hour
      if cookie.get("Hour"):
        web.setcookie("Hour", Hora, expires="", domain=None)
      else:
        web.setcookie("Hour", Hora, expires="", domain=None)
      

      return "Hola " + str(name) + "\nEres la visita numero " + str(visit) + "\nHoy es: "+ str(dateHoy) +  str(Hora)
    
    except Exception as e:
      return "error "+str(e.args)