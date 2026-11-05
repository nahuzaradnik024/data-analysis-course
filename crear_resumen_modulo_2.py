from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

OUT = Path("output/pdf/modulo-2-guia-de-repaso.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2E6E9E")
PALE = colors.HexColor("#EAF2F8")
LIGHT = colors.HexColor("#F7F9FB")
TEXT = colors.HexColor("#25313C")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=28, leading=33, alignment=TA_CENTER, textColor=NAVY, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontName="Helvetica", fontSize=13, leading=19, alignment=TA_CENTER, textColor=TEXT))
styles.add(ParagraphStyle(name="H1Custom", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=10))
styles.add(ParagraphStyle(name="H2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=14, textColor=TEXT, spaceAfter=5))
styles.add(ParagraphStyle(name="CodeCustom", parent=styles["Code"], fontName="Courier", fontSize=8.2, leading=11.5, backColor=LIGHT, borderColor=colors.HexColor("#DCE4EA"), borderWidth=.5, borderPadding=7, spaceBefore=4, spaceAfter=8))
styles.add(ParagraphStyle(name="Tip", parent=styles["BodyText"], fontName="Helvetica-Oblique", fontSize=9, leading=13, textColor=TEXT, backColor=PALE, borderColor=colors.HexColor("#BDD4E5"), borderWidth=.5, borderPadding=7, spaceBefore=6, spaceAfter=8))
styles.add(ParagraphStyle(name="TableHeader", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.2, leading=12, textColor=colors.white))

def p(text, style="BodyCustom"):
    return Paragraph(text, styles[style])

def code(text):
    return p(text.replace("\n", "<br/>"), "CodeCustom")

def table(headers, rows, widths=None):
    data = [[p(h, "TableHeader") for h in headers]]
    data += [[p(str(cell), "BodyCustom") for cell in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), .35, colors.HexColor("#D4DCE3")),
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
    canvas.drawString(doc.leftMargin, .88 * cm, "Data Analysis con Python - Modulo 2")
    canvas.drawRightString(A4[0] - doc.rightMargin, .88 * cm, f"Pagina {doc.page}")
    canvas.restoreState()

story = [
    Spacer(1, 4*cm), p("GUIA DE REPASO", "CoverSub"), p("Modulo 2", "CoverTitle"),
    p("Extraccion de datos<br/>Clases 5 a 8", "CoverSub"), Spacer(1, .8*cm),
    p("Una ayuda memoria para trabajar con Pandas, archivos CSV, SQL, SQLite y exploracion inicial de datos.", "CoverSub"),
    Spacer(1, 2.1*cm), p("Como usar esta guia", "H2Custom"),
    p("Cada clase resume la idea principal, los comandos que vas a usar y ejemplos breves para adaptar en ejercicios. El objetivo es tener una referencia rapida antes de consultar documentacion.", "BodyCustom"), PageBreak(),

    p("Clase 5 - Introduccion a Pandas", "H1Custom"),
    p("Pandas es una libreria para trabajar con datos tabulares: filas y columnas, como una planilla. Permite responder preguntas sobre una tabla sin programar bucles manuales para cada operacion.", "BodyCustom"),
    p("Preparar Pandas", "H2Custom"),
    code('pip install pandas\n\nimport pandas as pd'),
    table(["Comando", "Funcion"], [
        ["pip install pandas", "Instala Pandas si el entorno no lo trae incluido."],
        ["import pandas as pd", "Importa la libreria con el alias estandar pd."],
        ["pd.Series([...])", "Crea una columna individual con indice."],
        ["pd.DataFrame([...])", "Crea una tabla a partir de filas o diccionarios."],
    ], [5.2*cm, 10.5*cm]),
    p("Series y operaciones vectorizadas", "H2Custom"),
    code('precios = pd.Series([12000, 8500, 34000])\nprecios_con_iva = precios * 1.19'),
    p("La multiplicacion se aplica a cada elemento de la Series. Esto evita escribir un for para transformaciones simples sobre una columna.", "BodyCustom"),
    p("DataFrames y archivos CSV", "H2Custom"),
    code('df = pd.read_csv("ventas.csv")\nprint(df.head())'),
    table(["Elemento", "Funcion"], [
        ["df.shape", "Devuelve una tupla: cantidad de filas y columnas."],
        ["df.columns", "Muestra los nombres de las columnas."],
        ["df.dtypes", "Muestra el tipo de dato de cada columna."],
        ["df.head(n)", "Muestra las primeras n filas."],
        ['df["precio"]', "Selecciona una columna y devuelve una Series."],
        ['df[["producto", "precio"]]', "Selecciona varias columnas."],
        ["df.iloc[0:3]", "Selecciona filas por posicion."],
    ], [6.3*cm, 9.4*cm]),
    p("Recorda: si pd.read_csv() no encuentra el archivo, revisa la ruta. Si no esta en la misma carpeta, indica la ruta correcta.", "Tip"), PageBreak(),

    p("Clase 6 - Introduccion a SQL", "H1Custom"),
    p("SQL es un lenguaje para consultar datos directamente en una base de datos. En lugar de descargar todo, pedis solo las columnas y filas que necesitas.", "BodyCustom"),
    p("Consulta basica", "H2Custom"),
    code("SELECT * FROM productos;\n\nSELECT nombre, precio FROM productos;"),
    table(["Clausula", "Funcion"], [
        ["SELECT", "Indica las columnas que queres obtener."],
        ["*", "Representa todas las columnas."],
        ["FROM", "Indica la tabla de origen."],
        [";", "Cierra la instruccion SQL."],
    ], [4.0*cm, 11.7*cm]),
    p("Filtrar y limitar", "H2Custom"),
    code("SELECT * FROM productos WHERE categoria = 'tech';\n\nSELECT * FROM productos WHERE categoria = 'tech' AND precio > 50000;\n\nSELECT * FROM productos LIMIT 3;"),
    table(["Elemento", "Funcion"], [
        ["WHERE", "Filtra filas segun una condicion."],
        ["AND / OR", "Combina condiciones."],
        ["=, !=, >, <, >=, <=", "Compara valores. En SQL igualdad se escribe con un solo =."],
        ["LIMIT", "Restringe la cantidad de filas devueltas."],
    ], [5.0*cm, 10.7*cm]),
    p("Tablas relacionadas y JOIN", "H2Custom"),
    code("SELECT clientes.nombre, pedidos.producto, pedidos.monto\nFROM pedidos\nJOIN clientes ON pedidos.cliente_id = clientes.id;"),
    p("Las bases relacionales separan la informacion en tablas para no duplicarla. Una clave, como id o cliente_id, conecta las filas. JOIN combina datos de tablas relacionadas a partir de esa clave.", "BodyCustom"),
    p("Orden tipico de una consulta: SELECT, FROM, JOIN, WHERE, LIMIT.", "Tip"), PageBreak(),

    p("Clase 7 - SQLite con Python", "H1Custom"),
    p("SQLite guarda una base de datos en un archivo local. Python puede conectarse a ella y Pandas puede traer el resultado de una consulta SQL directo a un DataFrame.", "BodyCustom"),
    p("Flujo de trabajo", "H2Custom"),
    code('import sqlite3\nimport pandas as pd\n\nconexion = sqlite3.connect("ventas.db")\ndf = pd.read_sql("SELECT * FROM productos", conexion)\nconexion.close()'),
    table(["Comando", "Funcion"], [
        ["import sqlite3", "Importa el modulo incluido en Python para SQLite."],
        ['sqlite3.connect("archivo.db")', "Abre una base existente o crea el archivo si no existe."],
        ["conexion.cursor()", "Crea un cursor para ejecutar SQL manualmente."],
        ["cursor.execute(sql)", "Ejecuta instrucciones SQL como CREATE o INSERT."],
        ["conexion.commit()", "Confirma los cambios realizados en la base."],
        ["pd.read_sql(sql, conexion)", "Ejecuta una consulta y devuelve su resultado como DataFrame."],
        ["conexion.close()", "Cierra la conexion al terminar."],
    ], [6.4*cm, 9.3*cm]),
    p("Crear una tabla y consultar", "H2Custom"),
    code('cursor.execute("""\nCREATE TABLE IF NOT EXISTS productos (\n    id INTEGER PRIMARY KEY,\n    nombre TEXT,\n    precio REAL\n)\n""")\nconexion.commit()'),
    code('df_tech = pd.read_sql(\n    "SELECT * FROM productos WHERE categoria = \'tech\'",\n    conexion\n)'),
    p("Explorar una base que ya existe", "H2Custom"),
    code('sql_tablas = "SELECT name FROM sqlite_master WHERE type=\'table\'"\ntablas = pd.read_sql(sql_tablas, conexion)\nestructura = pd.read_sql("PRAGMA table_info(productos)", conexion)'),
    p("Recorda: mientras uses la conexion podés hacer varias consultas. Cerrala solo cuando terminaste de leer o modificar la base.", "Tip"), PageBreak(),

    p("Clase 8 - Exploracion inicial de datos", "H1Custom"),
    p("Antes de sacar conclusiones, hay que conocer el dataset: tamaño, columnas, tipos, valores faltantes, rangos numericos y categorias. Esta etapa se llama EDA: Exploratory Data Analysis.", "BodyCustom"),
    p("Inspeccion inicial de un DataFrame", "H2Custom"),
    code("print(df.shape)\nprint(df.head())\nprint(df.tail())\ndf.info()\ndf.describe()"),
    table(["Herramienta", "Para que sirve"], [
        ["df.shape", "Cantidad de filas y columnas."],
        ["df.head(n)", "Muestra las primeras n filas."],
        ["df.tail(n)", "Muestra las ultimas n filas."],
        ["df.info()", "Muestra estructura, valores no nulos y tipos de datos."],
        ["df.describe()", "Calcula estadisticas de columnas numericas."],
        ['df["categoria"].value_counts()', "Cuenta cada categoria."],
        ["value_counts(normalize=True)", "Devuelve proporciones por categoria."],
    ], [6.4*cm, 9.3*cm]),
    p("Estadisticas descriptivas", "H2Custom"),
    p("describe() resume count, mean, std, min, cuartiles 25%, 50% y 75%, y max. Sirve para detectar rapidamente valores inesperados, por ejemplo una edad maxima imposible.", "BodyCustom"),
    p("Primeros graficos", "H2Custom"),
    code("import matplotlib.pyplot as plt\n\ndf['categoria'].value_counts().plot(kind='bar')\nplt.title('Productos por categoria')\nplt.xlabel('Categoria')\nplt.ylabel('Cantidad')\nplt.show()"),
    table(["Grafico", "Cuando usarlo"], [
        ["Barras: plot(kind='bar')", "Comparar cantidades entre categorias."],
        ["Histograma: plot(kind='hist')", "Ver como se distribuye una variable numerica."],
        ["plt.title(), xlabel(), ylabel()", "Agregar contexto para que el grafico se entienda solo."],
        ["plt.show()", "Mostrar el grafico."],
    ], [6.4*cm, 9.3*cm]),
    p("Recorda: explora primero y analiza despues. head(), tail(), info() y describe() suelen ser las primeras lineas de cualquier notebook con un dataset nuevo.", "Tip"), PageBreak(),

    p("Repaso final del Modulo 2", "H1Custom"),
    p("El Modulo 2 enseña distintas formas de obtener y conocer datos. Empezas con archivos CSV, avanzas a consultas SQL y SQLite, y terminas explorando lo que recibiste antes de analizarlo en profundidad.", "BodyCustom"),
    p("Mapa de decisiones rapido", "H2Custom"),
    table(["Si necesitas...", "Usa..."], [
        ["Cargar una tabla desde un CSV", 'pd.read_csv("archivo.csv")'],
        ["Crear una tabla desde diccionarios", "pd.DataFrame(lista_de_diccionarios)"],
        ["Ver columnas y tipos", "df.columns, df.dtypes o df.info()"],
        ["Seleccionar una columna", 'df["columna"]'],
        ["Seleccionar filas por posicion", "df.iloc[...]"],
        ["Pedir datos a una base", "SELECT ... FROM ..."],
        ["Filtrar en SQL", "WHERE condicion"],
        ["Unir tablas relacionadas", "JOIN ... ON ..."],
        ["Conectar Python a SQLite", 'sqlite3.connect("archivo.db")'],
        ["Traer SQL a Pandas", "pd.read_sql(sql, conexion)"],
        ["Explorar tamaño y muestra", "shape, head(), tail()"],
        ["Resumir numeros y categorias", "describe() y value_counts()"],
        ["Crear un grafico basico", "plot(kind=...) y plt.show()"],
    ], [7.0*cm, 8.7*cm]),
    p("Checklist cuando recibis datos nuevos", "H2Custom"),
    p("1. Identifica de donde vienen: CSV, base de datos u otra fuente.<br/>2. Carga solo lo necesario.<br/>3. Revisa shape, head(), tail() e info().<br/>4. Confirma nombres y tipos de columnas.<br/>5. Busca valores faltantes o rangos extraños con describe().<br/>6. Cuenta categorias con value_counts().<br/>7. Cierra la conexion SQLite al terminar.", "BodyCustom"),
    p("Fin de la guia. Usa estos modelos como punto de partida y adapta los nombres de archivos, tablas y columnas a cada ejercicio.", "Tip"),
]

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=1.55*cm, leftMargin=1.55*cm, topMargin=1.55*cm, bottomMargin=1.75*cm, title="Modulo 2 - Guia de repaso", author="Codex")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT.resolve())
