
from PyQt5 import  uic,QtWidgets
from reportlab.pdfgen import canvas
import mysql.connector
import _sqlite3

banco = _sqlite3.connect('cadastro_produtos.db')
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco TEXT NOT NULL,
    categoria TEXT NOT NULL                
        
);
""")
print("Conectado com suscesso")


"""banco = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "",
    database= "cadastro_produtos"

)"""

def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id =dados_lidos[linha[0]]
    cursor.execute("DELETE FROM produtos WHERE id=" + str(valor_id))
    



def gerar_pdf():
    
    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    y=0
    pdf = canvas.Canvas("Cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos cadastrados")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PRECO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range (0, len(dados_lidos)):
     y = y + 50
     pdf.drawString(10,750 - y, str(dados_lidos[i][0]))   
     pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
     pdf.drawString(210,750 - y, str(dados_lidos[i][2]))   
     pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
     pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

     pdf.save()
     print("PDF FOI GERADO COM SUSCESSO ")
     
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""
    
    if formulario.radioButton.isChecked() :
        print("Categoria Eletronicos selecionada")
        categoria ="Eletronicos"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Informatica selecionada")
        
        categoria ="Alimentos"
    else :
        print("Categoria Alimentos selecionada")
        categoria ="Informatica"

    print("Codigo:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.conn.commit()

    formulario.lineEdit.seTText("")
    formulario.lineEdit_2.seTText("")
    formulario.lineEdit_3.seTText("")
    
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    #print(dados_lidos[0][0])

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QtWidgetItem(str(dados_lidos[i][j])))



app = QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)

formulario.show()
app.exec()


# criando a tabela

""" create table produtos (id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao VARCHAR(50),  
preco DOUBLE,
categoria VARCHAR(20),
PRIMARY KEY (id)
);  """

# inserindo registros na tabela

#INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (123,"impressora",500.00,"informatica"); 
