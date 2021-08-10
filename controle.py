from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_projeto"
)

def funcao_principal():
    linha1 = formulario.lineEdit_2.text()
    linha2 = formulario.lineEdit_3.text()
    linha3 = formulario.lineEdit_4.text()
    linha4 = formulario.lineEdit_5.text()

    print("Cliente:",linha1)
    print("Telefone",linha2)
    print("Produto:",linha3)
    print("Preco",linha4)


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastro (cliente,telefone,produto,preco) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4))
    cursor.execute(comando_SQL,dados)
    banco.commit()


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()


