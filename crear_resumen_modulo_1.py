from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether,
)


OUT = Path("output/pdf/modulo-1-guia-de-repaso.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2E6E9E")
PALE = colors.HexColor("#EAF2F8")
LIGHT = colors.HexColor("#F7F9FB")
TEXT = colors.HexColor("#25313C")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=28, leading=33, alignment=TA_CENTER, textColor=NAVY, spaceAfter=14,
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=13, leading=19, alignment=TA_CENTER, textColor=TEXT,
))
styles.add(ParagraphStyle(
    name="H1Custom", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=20, leading=24, textColor=NAVY, spaceBefore=0, spaceAfter=10,
))
styles.add(ParagraphStyle(
    name="H2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=12, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="BodyCustom", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.4, leading=14, textColor=TEXT, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="CodeCustom", parent=styles["Code"], fontName="Courier",
    fontSize=8.2, leading=11.5, backColor=LIGHT, borderColor=colors.HexColor("#DCE4EA"),
    borderWidth=0.5, borderPadding=7, spaceBefore=4, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Tip", parent=styles["BodyText"], fontName="Helvetica-Oblique",
    fontSize=9, leading=13, textColor=TEXT, backColor=PALE, borderColor=colors.HexColor("#BDD4E5"),
    borderWidth=0.5, borderPadding=7, spaceBefore=6, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="TableHeader", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=9.2, leading=12, textColor=colors.white,
))


def p(text, style="BodyCustom"):
    return Paragraph(text, styles[style])


def code(text):
    return p(text.replace("\n", "<br/>"), "CodeCustom")


def table(headers, rows, widths=None):
    data = [[p(h, "TableHeader") for h in headers]]
    for row in rows:
        data.append([p(str(cell), "BodyCustom") for cell in row])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D4DCE3")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CAD7E1"))
    canvas.line(doc.leftMargin, 1.35 * cm, A4[0] - doc.rightMargin, 1.35 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#607080"))
    canvas.drawString(doc.leftMargin, 0.88 * cm, "Data Analysis con Python - Modulo 1")
    canvas.drawRightString(A4[0] - doc.rightMargin, 0.88 * cm, f"Pagina {doc.page}")
    canvas.restoreState()


story = []
story.extend([
    Spacer(1, 4.0 * cm),
    p("GUIA DE REPASO", "CoverSub"),
    p("Modulo 1", "CoverTitle"),
    p("Data Analysis con Python<br/>Clases 1 a 4", "CoverSub"),
    Spacer(1, 0.8 * cm),
    p("Una ayuda memoria para repasar fundamentos de Python, control de flujo, funciones, manejo de errores, list comprehensions y limpieza de strings.", "CoverSub"),
    Spacer(1, 2.1 * cm),
    p("Como usar esta guia", "H2Custom"),
    p("Lee primero la idea principal de cada clase. Usa las tablas para recordar la funcion de cada comando y los bloques de codigo como modelos para adaptar en los ejercicios.", "BodyCustom"),
    PageBreak(),
])

# Clase 1
story.extend([
    p("Clase 1 - Introduccion al analisis de datos y Python", "H1Custom"),
    p("El analisis de datos transforma informacion cruda en respuestas concretas. El flujo habitual es obtener los datos, limpiarlos y transformarlos, analizarlos y comunicar los resultados.", "BodyCustom"),
    p("Entorno de trabajo", "H2Custom"),
    p("Jupyter Notebook permite trabajar por celdas: ejecutas una parte del codigo, ves el resultado y continuas. El atajo mas usado es <b>Shift + Enter</b>: ejecuta la celda actual y pasa a la siguiente.", "BodyCustom"),
    code('print("Hola, mundo del analisis de datos")'),
    p("Git y GitHub", "H2Custom"),
    p("Git guarda el historial de cambios en tu computadora. GitHub aloja ese historial en internet. El flujo basico consiste en preparar los cambios, crear un commit y subirlo.", "BodyCustom"),
    table(["Comando", "Para que sirve"], [
        ["git status", "Muestra los archivos modificados y si hay cambios pendientes."],
        ["git add archivo", "Prepara un archivo para incluirlo en el proximo commit."],
        ["git commit -m \"mensaje\"", "Guarda una version local identificada por un mensaje."],
        ["git push", "Sube los commits locales al repositorio remoto."],
        ["git clone URL", "Descarga una copia local de un repositorio existente."],
    ], [5.1*cm, 10.6*cm]),
    code('git add modulo-1-python/clase-01/practica/notebook.ipynb\ngit commit -m "Resuelve practica de la clase 1"\ngit push'),
    p("Variables y tipos de datos", "H2Custom"),
    code('nombre = "Ana"\ncantidad = 42\nprecio = 15990.50\nes_premium = True'),
    table(["Tipo", "Que representa", "Ejemplo"], [
        ["str", "Texto", '"Notebook"'],
        ["int", "Numero entero", "42"],
        ["float", "Numero con decimales", "15990.50"],
        ["bool", "Verdadero o falso", "True / False"],
    ], [2.5*cm, 7.0*cm, 6.2*cm]),
    p("Comandos y modelos utiles", "H2Custom"),
    table(["Elemento", "Funcion"], [
        ["print()", "Muestra un resultado en pantalla."],
        ["type(valor)", "Indica el tipo de dato de una variable."],
        ["int(), float(), str()", "Convierten un valor a entero, decimal o texto."],
        ["f\"...{variable}...\"", "Inserta valores dentro de un texto."],
        [":,.2f", "Muestra miles separados y dos decimales."],
    ], [5.0*cm, 10.7*cm]),
    code('precio_texto = "1500"\nprecio = int(precio_texto)\nprint(f"Precio final: ${precio:,.2f}")'),
    p("Recorda: los datos externos pueden llegar como texto. Antes de calcular, revisa su tipo y conviertelos si hace falta.", "Tip"),
    PageBreak(),
])

# Clase 2
story.extend([
    p("Clase 2 - Control de flujo y estructuras de datos", "H1Custom"),
    p("Esta clase permite que el programa tome decisiones, recorra colecciones de datos y acumule resultados. Es la base para analizar muchas filas sin repetir codigo manualmente.", "BodyCustom"),
    p("Condicionales", "H2Custom"),
    code('if monto < 1000:\n    categoria = "micro"\nelif monto < 100000:\n    categoria = "importante"\nelse:\n    categoria = "alto valor"'),
    table(["Palabra", "Funcion"], [
        ["if", "Ejecuta un bloque si la condicion es verdadera."],
        ["elif", "Prueba otra condicion si las anteriores fueron falsas."],
        ["else", "Define el caso restante."],
        ["and / or / not", "Combina o niega condiciones."],
    ], [4.0*cm, 11.7*cm]),
    p("Bucles y acumuladores", "H2Custom"),
    code('total = 0\nfor venta in ventas:\n    total += venta\n\npromedio = total / len(ventas)'),
    table(["Elemento", "Funcion"], [
        ["for", "Recorre cada elemento de una coleccion."],
        ["while", "Repite mientras una condicion sea verdadera."],
        ["range(5)", "Genera 0, 1, 2, 3 y 4."],
        ["break", "Sale del bucle inmediatamente."],
        ["continue", "Salta al inicio de la siguiente vuelta."],
        ["+=", "Suma y guarda el nuevo valor en una variable."],
    ], [4.0*cm, 11.7*cm]),
    p("Listas", "H2Custom"),
    code('productos = ["notebook", "mouse", "teclado"]\nproductos.append("monitor")\nprimer_producto = productos[0]\nultimo_producto = productos[-1]'),
    table(["Herramienta", "Funcion"], [
        ["lista[indice]", "Accede a un elemento; el primer indice es 0."],
        [".append(valor)", "Agrega al final."],
        [".insert(posicion, valor)", "Inserta en una posicion."],
        [".remove(valor) / .pop()", "Elimina un elemento."],
        ["len(), sum(), min(), max(), sorted()", "Cuentan, calculan u ordenan listas."],
    ], [6.1*cm, 9.6*cm]),
    p("Diccionarios", "H2Custom"),
    code('cliente = {"nombre": "Ana", "pais": "AR"}\nprint(cliente["nombre"])\ntelefono = cliente.get("telefono", "no registrado")'),
    p("Un diccionario guarda pares clave-valor. Usa <b>.get(clave, valor_por_defecto)</b> cuando la clave podria no existir: evita un <b>KeyError</b>.", "BodyCustom"),
    code('for clave, valor in cliente.items():\n    print(f"{clave}: {valor}")'),
    p("Recorda: inicializa los acumuladores antes del bucle; las lineas indentadas se ejecutan en cada vuelta.", "Tip"),
    PageBreak(),
])

# Clase 3
story.extend([
    p("Clase 3 - Funciones y errores", "H1Custom"),
    p("Las funciones evitan repetir logica y hacen que el codigo sea mas facil de modificar. El manejo de errores permite procesar datos imperfectos sin detener todo el programa.", "BodyCustom"),
    p("Funciones", "H2Custom"),
    code('def calcular_precio_final(precio, tasa_impuesto=0.19):\n    return precio * (1 + tasa_impuesto)\n\ntotal = calcular_precio_final(320000)'),
    table(["Elemento", "Funcion"], [
        ["def", "Define una funcion."],
        ["parametros", "Datos que la funcion recibe para trabajar."],
        ["valor=...", "Define un parametro con valor por defecto."],
        ["return", "Devuelve el resultado de la funcion."],
        ["pass", "Marcador temporal: no ejecuta ninguna accion."],
    ], [4.3*cm, 11.4*cm]),
    p("Una funcion puede devolver varios valores. Se reciben en el mismo orden.", "BodyCustom"),
    code('def calcular_orden(precio, cantidad, descuento=0):\n    subtotal = precio * cantidad\n    monto_descuento = subtotal * descuento\n    return subtotal, monto_descuento, subtotal - monto_descuento\n\nsubtotal, descuento, total = calcular_orden(8500, 5, 0.10)'),
    p("Manejo de errores", "H2Custom"),
    code('def convertir_temperatura(valor):\n    try:\n        return float(valor)\n    except ValueError:\n        return None'),
    table(["Concepto", "Funcion"], [
        ["try", "Intenta ejecutar un bloque que podria fallar."],
        ["except", "Indica que hacer cuando ocurre una excepcion."],
        ["raise", "Lanza manualmente un error con un mensaje."],
        ["else", "Se ejecuta si no hubo error en try."],
        ["finally", "Se ejecuta siempre."],
    ], [4.0*cm, 11.7*cm]),
    table(["Error", "Caso tipico"], [
        ["ValueError", 'float("N/A") o una conversion invalida.'],
        ["KeyError", "Una clave no existe en un diccionario."],
        ["TypeError", "Se combinan tipos incompatibles."],
        ["ZeroDivisionError", "Se divide por cero."],
        ["IndexError", "Se intenta usar una posicion inexistente."],
    ], [5.0*cm, 10.7*cm]),
    p("Diseno modular", "H2Custom"),
    p("Una funcion deberia tener una sola responsabilidad: validar, calcular, agrupar o coordinar. Una funcion principal puede llamar a las pequenas para armar un pipeline claro.", "BodyCustom"),
    p("Recorda: las variables creadas dentro de una funcion son locales. Para usarlas afuera, devuelve el resultado con return.", "Tip"),
    PageBreak(),
])

# Clase 4
story.extend([
    p("Clase 4 - List comprehensions y limpieza de strings", "H1Custom"),
    p("Una list comprehension crea una lista nueva transformando o filtrando los elementos de otra. La limpieza de strings prepara texto sucio para que pueda analizarse o convertirse a numero.", "BodyCustom"),
    p("Sintaxis de list comprehensions", "H2Custom"),
    code('[expresion for elemento in lista]\n[expresion for elemento in lista if condicion]'),
    code('precios_con_iva = [precio * 1.19 for precio in precios]\nprecios_altos = [precio for precio in precios if precio > 20000]'),
    table(["Parte", "Pregunta que responde"], [
        ["expresion", "Que quiero guardar en la lista nueva?"],
        ["for elemento in lista", "Que lista voy a recorrer?"],
        ["if condicion", "Que elementos deben entrar?"],
    ], [5.5*cm, 10.2*cm]),
    p("Usa una comprehension cuando la operacion es corta y se entiende de un vistazo. Si hay muchas condiciones o decisiones, un bucle for tradicional suele ser mas legible.", "Tip"),
    p("Metodos de limpieza de texto", "H2Custom"),
    table(["Metodo", "Funcion", "Ejemplo"], [
        [".strip()", "Quita espacios al inicio y al final.", '"  Ana  ".strip() -> "Ana"'],
        [".replace(a, b)", "Reemplaza un fragmento de texto.", '"$1,200".replace("$", "")'],
        [".lower()", "Convierte a minusculas.", '"ANA".lower() -> "ana"'],
        [".capitalize()", "Primera letra en mayuscula.", '"mUEBLES".capitalize() -> "Muebles"'],
        [".title()", "Primera letra de cada palabra en mayuscula.", '"ana torres".title()'],
    ], [3.5*cm, 6.0*cm, 6.2*cm]),
    p("Limpiar y convertir precios", "H2Custom"),
    code('def limpiar_precio_usa(valor):\n    texto = valor.strip().replace("$", "").replace(",", "")\n    try:\n        return float(texto)\n    except ValueError:\n        return None'),
    p("Para el formato estadounidense, la coma separa miles y se elimina; el punto se conserva porque es decimal. Antes de limpiar precios, confirma siempre el formato de origen.", "BodyCustom"),
    code('precios_procesados = [limpiar_precio_usa(p) for p in precios_crudos]\nprecios_validos = [p for p in precios_procesados if p is not None]'),
    p("Ejemplo de limpieza de emails", "H2Custom"),
    code('emails_limpios = [email.strip().lower() for email in emails_crudos]\nemails_validos = [email for email in emails_limpios if email != "" and "@" in email]'),
    p("Recorda: no filtres usando solo if precio, porque un valor 0.0 es valido. Para descartar conversiones fallidas usa if precio is not None.", "Tip"),
    PageBreak(),
])

# Repaso final
story.extend([
    p("Repaso final del Modulo 1", "H1Custom"),
    p("Este modulo construye la base para trabajar con datos antes de usar librerias como pandas. Primero se guarda y convierte informacion; luego se decide, recorre, valida, agrupa y limpia.", "BodyCustom"),
    p("Mapa de decisiones rapido", "H2Custom"),
    table(["Si necesitas...", "Usa..."], [
        ["Guardar un dato", "Una variable."],
        ["Ver el tipo de un dato", "type()."],
        ["Convertir texto a numero", "int() o float()."],
        ["Mostrar datos dentro de un texto", "f-strings."],
        ["Tomar una decision", "if / elif / else."],
        ["Recorrer datos", "for."],
        ["Guardar varios elementos", "Una lista []."],
        ["Guardar campos con nombre", "Un diccionario {}."],
        ["Evitar que una conversion detenga el programa", "try / except."],
        ["Reutilizar una operacion", "Una funcion con def."],
        ["Crear una lista transformada o filtrada", "List comprehension."],
        ["Limpiar texto", "strip(), replace(), lower(), title()."],
    ], [7.4*cm, 8.3*cm]),
    p("Checklist antes de dar por terminado un ejercicio", "H2Custom"),
    p("1. Ejecuta la celda y lee el resultado.<br/>2. Comprueba que los nombres de las variables sean claros.<br/>3. Revisa la indentacion dentro de if, for, while, try y funciones.<br/>4. Si usas datos externos, verifica tipos y valores faltantes.<br/>5. Guarda el notebook con Ctrl + S.<br/>6. Registra el avance en Git con git add, git commit y git push.", "BodyCustom"),
    p("Modelo de cierre de practica", "H2Custom"),
    code('git status\ngit add modulo-1-python/clase-XX/practica/notebook.ipynb\ngit commit -m "Resuelve practica de la clase XX"\ngit push'),
    Spacer(1, 0.6*cm),
    p("Fin de la guia. Usa los ejemplos como referencia, pero intenta primero resolver cada consigna con tus propias palabras y despues compara tu idea con el modelo.", "Tip"),
])

doc = SimpleDocTemplate(
    str(OUT), pagesize=A4, rightMargin=1.55*cm, leftMargin=1.55*cm,
    topMargin=1.55*cm, bottomMargin=1.75*cm,
    title="Modulo 1 - Guia de repaso",
    author="Codex",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT.resolve())
