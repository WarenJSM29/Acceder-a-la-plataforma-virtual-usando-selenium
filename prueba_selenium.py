import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Le pedimos al usurio ingresar sus datos:
writeUserName = input("Usuario:")
writeUserPassword = input("Contraseña:")

time.sleep(1)

# Crear la variable para el reporte HTML
report_html = """
<html>
<head><title>Reporte de Acción</title></head>
<body>
<h1>Reporte de Acciones</h1>
"""

# Aqui creo una funcion para guardar capturas de pantallas y sobrescribir las ya existentes.
def screenshotForSelenium(strPath):
    file_path = strPath

    # Eliminar el archivo si ya existe
    if os.path.exists(file_path):
        os.remove(file_path)

    # Tomar la captura de pantalla
    driver.save_screenshot(file_path)

# Ruta al Edge WebDriver
service = Service('./edgedriver_win64/msedgedriver.exe')

# Configuración de las opciones de Edge
options = Options()

# Crear el driver de Edge
driver = webdriver.Edge(service=service, options=options)

# Abrir la página de inicio de sesión
driver.get('https://plataformavirtual.itla.edu.do/login/index.php')
report_html += "<p>Se accedio al Login del ITLA.</p>\n"

time.sleep(2)

# Esperar a que los campos estén disponibles
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'loginbtn')
    
    # Ingresar las credenciales
    username_field.send_keys(writeUserName)
    password_field.send_keys(writeUserPassword)
    
    time.sleep(2)
    
    # Captura de pantalla del Login:
    screenshotForSelenium('./capturas/01CapturaLogin.png')
    report_html += "<p>Captura de pantalla del Login tomada.</p>\n"

    # Hacer clic en el botón de login
    login_button.click()
    report_html += "<p>Se hizo clic en el botón de login.</p>\n"

    """ # Verificar si el login fue exitoso
    try:
        profile_element = driver.find_element(By.ID, 'profile')  # Verificar si la página de perfil está disponible
        print("¡Login exitoso!")
    except Exception as e:
        print(f"Error al verificar login: {e}") """
    
except Exception as e:
    print(f"Error al cargar la página o realizar el login: {e}")
    report_html += f"<p>Error al cargar la página o realizar el login: {e}</p>\n"

# 2 --------------------------------------------------------------------------------------------------------------------

# Vamos a la pagina principal:
driver.get('https://plataformavirtual.itla.edu.do/')
report_html += "<p>Se accedio a la pantalla principal.</p>\n"

time.sleep(2)

# Captura de pantalla de los cursos:
screenshotForSelenium('./capturas/02CapturaPaginaPrincipal.png')
report_html += "<p>Captura de pantalla de la Página Principal tomada.</p>\n"

# 3 --------------------------------------------------------------------------------------------------------------------

# Vamos a la pagina de Programacion 3:
driver.get('https://plataformavirtual.itla.edu.do/course/view.php?id=8791')
report_html += "<p>Se accedio al curso P3.</p>\n"

time.sleep(2)

# Captura de pantalla de los cursos:
screenshotForSelenium('./capturas/03CapturaCursoProgramacion3.png')
report_html += "<p>Captura de pantalla de P3 fue tomada.</p>\n"

# 4 --------------------------------------------------------------------------------------------------------------------

# Vamos a la pagina de Programacion 3:
driver.get('https://plataformavirtual.itla.edu.do/mod/assign/view.php?id=686211')
report_html += "<p>Se accedio a la tarea 4 de P3.</p>\n"

time.sleep(2)

# Captura de pantalla de la tarea 4:
screenshotForSelenium('./capturas/04CapturaCursoP3Tarea4.png')
report_html += "<p>Captura de pantalla de la tarea 4 de P3 fue tomada.</p>\n"

# 5 --------------------------------------------------------------------------------------------------------------------

# Vamos a la pagina de Programacion 3:
driver.get('https://plataformavirtual.itla.edu.do/login/logout.php?')
report_html += "<p>Se accedio a la pagina de cerrar sesion.</p>\n"

time.sleep(2)

# Captura de pantalla de cerrar sesion:
screenshotForSelenium('./capturas/05CapturaCerrarSesion.png')
report_html += "<p>Captura de pantalla de cerrar sesion fue tomada.</p>\n"

report_html += "<p>Se cerró el navegador.</p>\n"

# Finalizar y guardar el archivo HTML
report_html += """
</body>
</html>
"""

# Guardar el reporte en un archivo HTML
with open('reporte_acciones.html', 'w') as file:
    file.write(report_html)

print("El reporte de acciones ha sido guardado como 'reporte_acciones.html'.")
# 6 --------------------------------------------------------------------------------------------------------------------

# Cerrar el navegador cuando se termine -------------------------------------------------------------------------------
driver.quit()