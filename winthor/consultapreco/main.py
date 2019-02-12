import sys
import cx_Oracle
import platform
import locale
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL,'')
else:
    locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

def buscaDadosOracle(sql,dic):
    if platform.system() == 'Windows':
        ##con = cx_Oracle.connect("user/senha@sid")
        con = cx_Oracle.connect("tns/senha@user")
    else:
        ##dsn_tns = cx_Oracle.makedsn(host='192.168.0.203',port='1521',sid='WINT')
        ##con = cx_Oracle.connect(user='Suporte', password='SuP_468_t', dsn=dsn_tns)
        dsn_tns = cx_Oracle.makedsn(host='ip',port='1521',sid='sid')
        con = cx_Oracle.connect(user='user', password='pass', dsn=dsn_tns)
    setattr(con, 'current_schema', 'schema')
    cur = con.cursor()
    cur.prepare(sql)
    cur.execute(None, dic)
    res = cur.fetchall()
    cur.close()
    #con.close()
    return res

def dadosProduto(codauxiliar):
    sql = '''
        SELECT
                TO_CHAR(PCEMBALAGEM.CODAUXILIAR) CODAUXILIAR
                ,PCPRODUT.CODPROD
                ,PCPRODUT.DESCRICAO
                --,PCEMBALAGEM.EMBALAGEM
                --,PCEMBALAGEM.PERMITEVENDAATACADO
                ,NVL(PCEMBALAGEM.QTMINIMAATACADO,0) QTMINIMAATACADO
                ,PCEMBALAGEM.PVENDA --VAREJO
                ,PCEMBALAGEM.PVENDAATAC --ATACADO
            FROM
                WR.PCEMBALAGEM, WR.PCPRODUT
            WHERE
                PCEMBALAGEM.CODPROD = PCPRODUT.CODPROD       
                AND PCEMBALAGEM.CODFILIAL = 2
                AND NVL(PCEMBALAGEM.PVENDA,0) > 0
                --AND PCEMBALAGEM.QTMINIMAATACADO > 0
                AND PCEMBALAGEM.CODAUXILIAR = :CODAUXILIAR
            ORDER BY 
                PCEMBALAGEM.CODPROD, PCEMBALAGEM.CODAUXILIAR, PCEMBALAGEM.CODFILIAL
    '''
    res = buscaDadosOracle(sql,{'CODAUXILIAR': codauxiliar})
    #print(res)
    return res
#dadosProduto('789603089253022')


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.janela()

    def janela(self):
        self.setWindowTitle("Consulta Preço")
        self.resize(320,240)
        self.showFullScreen()
        self.layout = QGridLayout()
        self.label1 = QLabel("1", self)
        self.label2 = QLabel("2", self)
        self.label3 = QLabel("3", self)
        self.label4 = QLabel("4", self)
        #self.tela2()
        self.tela1()

    def tela1(self):
        self.label1 = QLabel("Test", self)
        self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label1.setAlignment(Qt.AlignCenter)
        #self.label.setStyleSheet("QLabel {background-color: white;}")
        pixmap = QPixmap('logowr.png')
        self.label1.setPixmap(pixmap)

        self.label2 = QLabel("Passe o código\ndo produto", self)
        self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label2.setAlignment(Qt.AlignCenter)
        font = QFont('Serif', 30, QFont.Normal)
        self.label2.setFont(font)
        self.label2.setStyleSheet("QLabel {background-color: white;}")

        self.codEdit = QLineEdit('',self)
        self.codEdit.setFocus()
        
        self.codEdit.returnPressed.connect(self.onClick)

        #self.layout = QGridLayout()
        #self.layout.setSpacing(10)
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.label2, 1, 0)
        self.layout.addWidget(self.codEdit, 2, 0)

        self.setLayout(self.layout)

    def tela2(self):
        #print(self.codEdit.text())
        try:
            cod = int(self.codEdit.text())
            res = dadosProduto(self.codEdit.text())
        except:
            res = []


        if res == []:
            self.label1 = QLabel('', self)
            self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.label1.setAlignment(Qt.AlignLeft)
            font = QFont('Serif', 15, QFont.Normal)
            self.label1.setFont(font)
            #self.label.setStyleSheet("QLabel {background-color: white;}")

            self.label2 = QLabel('Produto não\nencontrado', self)
            self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.label2.setAlignment(Qt.AlignCenter)
            font = QFont('Serif', 30, QFont.Normal)
            self.label2.setFont(font)
            #self.label2.setStyleSheet("QLabel {background-color: white;}")
        
        else:

            texto = '\n'
            if len(str(res[0][2])) > 25:
                texto = texto + str(res[0][2])[0:25] + '\n' + str(res[0][2])[25:len(str(res[0][2]))]
            else:
                texto = texto + str(res[0][2])
            
            self.label1 = QLabel(texto, self)
            self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.label1.setAlignment(Qt.AlignLeft)
            font = QFont('Serif', 16, QFont.Normal)
            self.label1.setFont(font)
            #self.label.setStyleSheet("QLabel {background-color: white;}")

            self.label2 = QLabel(locale.currency(res[0][4],grouping=True), self)
            self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.label2.setAlignment(Qt.AlignCenter)
            font = QFont('Serif', 30, QFont.Normal)
            self.label2.setFont(font)
            #self.label2.setStyleSheet("QLabel {background-color: white;}")

            if int(res[0][3]) > 0:

                self.label3 = QLabel(str(res[0][3]) + " ou mais", self)
                self.label3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.label3.setAlignment(Qt.AlignLeft)
                font = QFont('Serif', 15, QFont.Normal)
                self.label3.setFont(font)
                self.label3.setStyleSheet("QLabel {color: red;}")

                self.label4 = QLabel(locale.currency(res[0][5],grouping=True), self)
                self.label4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.label4.setAlignment(Qt.AlignCenter)
                font = QFont('Serif', 30, QFont.Bold)
                self.label4.setFont(font)
                #self.label4.setStyleSheet("QLabel {background-color: white;}")

        #self.layout = QGridLayout()
        self.layout.setRowStretch(1, 1)
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.label2, 1, 0)
        self.layout.addWidget(self.label3, 2, 0)
        self.layout.addWidget(self.label4, 3, 0)

        self.setLayout(self.layout)

    @pyqtSlot()
    def onClick(self):
        self.layout.removeWidget(self.label1)
        self.layout.removeWidget(self.label2)
        self.layout.removeWidget(self.label3)
        self.layout.removeWidget(self.label4)
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        self.label4.hide()
        self.codEdit.hide()
        self.tela2()
        loop = QEventLoop()
        QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        self.layout.removeWidget(self.label1)
        self.layout.removeWidget(self.label2)
        self.layout.removeWidget(self.label3)
        self.layout.removeWidget(self.label4)
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        self.label4.hide()
        self.codEdit.hide()       
        self.tela1()



if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Window()
    app.show()

sys.exit(root.exec_())
