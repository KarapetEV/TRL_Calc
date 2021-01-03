# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.setFixedSize(770, 840)
        self.frame_title = QtWidgets.QFrame(AppWindow)
        self.frame_title.setGeometry(QtCore.QRect(0, 0, 770, 90))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.logo = QtWidgets.QLabel(self.frame_title)
        self.logo.setGeometry(QtCore.QRect(5, 10, 95, 70))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.labelCalc = QtWidgets.QLabel(self.frame_title)
        self.labelCalc.setGeometry(QtCore.QRect(100, 0, 670, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelCalc.setFont(font)
        self.labelCalc.setTextFormat(QtCore.Qt.RichText)
        self.labelCalc.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCalc.setWordWrap(True)
        self.labelCalc.setObjectName("labelCalc")
        #---------------------------------------------
        self.frame_manual = QtWidgets.QFrame(AppWindow)
        self.frame_manual.setGeometry(QtCore.QRect(0, 90, 770, 90))
        self.frame_manual.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_manual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_manual.setObjectName('frame_manual')
        self.labelManual = QtWidgets.QLabel(self.frame_manual)
        self.labelManual.setGeometry(QtCore.QRect(10, 5, 750, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(25)
        self.labelManual.setFont(font)
        self.labelManual.setTextFormat(QtCore.Qt.RichText)
        self.labelManual.setAlignment(QtCore.Qt.AlignLeft)
        self.labelManual.setWordWrap(True)
        self.labelManual.setObjectName('labelManual')
        #-----------------------Создание вкладок---------------------------
        self.tabWidget = QtWidgets.QTabWidget(AppWindow)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 180, 770, 750))
        self.tabWidget.setObjectName("tabWidget")
        # -----------------------Вкладка калькулятора---------------------------
        self.tab_calc = QtWidgets.QWidget()
        self.tab_calc.setObjectName("tab_calc")
        self.tabWidget.addTab(self.tab_calc, "")
        self.frame_params = QtWidgets.QFrame(self.tab_calc)
        self.frame_params.setGeometry(QtCore.QRect(0, 0, 770, 180))
        self.frame_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_params.setObjectName('frame_params')
        self.group_params = QtWidgets.QGroupBox(self.frame_params)
        self.group_params.setEnabled(True)
        self.group_params.setGeometry(QtCore.QRect(10, 10, 340, 170))
        self.group_params.setObjectName("frame_params")
        self.check_trl = QtWidgets.QCheckBox(self.group_params)
        self.check_trl.setGeometry(QtCore.QRect(20, 25, 240, 17))
        self.check_trl.setObjectName("check_trl")
        self.check_trl.setChecked(True)
        self.check_mrl = QtWidgets.QCheckBox(self.group_params)
        self.check_mrl.setGeometry(QtCore.QRect(20, 55, 240, 17))
        self.check_mrl.setObjectName("check_mrl")
        self.check_mrl.setChecked(False)
        self.check_erl = QtWidgets.QCheckBox(self.group_params)
        self.check_erl.setGeometry(QtCore.QRect(20, 85, 240, 17))
        self.check_erl.setObjectName("check_erl")
        self.check_erl.setChecked(False)
        self.check_orl = QtWidgets.QCheckBox(self.group_params)
        self.check_orl.setGeometry(QtCore.QRect(20, 115, 240, 17))
        self.check_orl.setObjectName("check_orl")
        self.check_orl.setChecked(False)
        self.check_crl = QtWidgets.QCheckBox(self.group_params)
        self.check_crl.setGeometry(QtCore.QRect(20, 145, 240, 17))
        self.check_crl.setObjectName("check_crl")
        self.check_crl.setChecked(False)
        self.group_types = QtWidgets.QGroupBox(self.frame_params)
        self.group_types.setGeometry(QtCore.QRect(400, 10, 330, 110))
        self.group_types.setObjectName("frame_types")
        self.radio_hard = QtWidgets.QRadioButton(self.group_types)
        self.radio_hard.setGeometry(QtCore.QRect(10, 25, 211, 17))
        self.radio_hard.setObjectName("radio_hard")
        self.radio_hard.setChecked(True)
        self.radio_soft = QtWidgets.QRadioButton(self.group_types)
        self.radio_soft.setGeometry(QtCore.QRect(10, 55, 261, 17))
        self.radio_soft.setObjectName("radio_soft")
        self.radio_both = QtWidgets.QRadioButton(self.group_types)
        self.radio_both.setGeometry(QtCore.QRect(10, 85, 261, 17))
        self.radio_both.setAutoRepeat(False)
        self.radio_both.setObjectName("radio_both")
        self.btn_set_params = QtWidgets.QPushButton(self.frame_params)
        self.btn_set_params.setGeometry(QtCore.QRect(475, 140, 200, 40))
        self.btn_set_params.setObjectName("btn_set_params")
        self.frame_tasks = QtWidgets.QFrame(self.tab_calc)
        self.frame_tasks.setGeometry(QtCore.QRect(0, 180, 770, 463))
        self.frame_tasks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tasks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tasks.setObjectName("frame_tasks")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_tasks)
        self.treeWidget.setGeometry(QtCore.QRect(5, 5, 755, 390))
        self.treeWidget.setObjectName("treeWidget")
        self.btn_calculate = QtWidgets.QPushButton(self.frame_tasks)
        self.btn_calculate.setGeometry(QtCore.QRect(102, 405, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setObjectName("btn_calculate")
        self.btn_calculate.setEnabled(False)
        self.btn_reset_tasks = QtWidgets.QPushButton(self.frame_tasks)
        self.btn_reset_tasks.setGeometry(QtCore.QRect(486, 405, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_reset_tasks.setFont(font)
        self.btn_reset_tasks.setObjectName("btn_reset_tasks")
        self.btn_reset_tasks.setEnabled(False)
        #----------------------Вкладка результатов-----------------------------
        self.tab_results = QtWidgets.QWidget()
        self.tab_results.setObjectName("tab_results")
        self.tabWidget.addTab(self.tab_results, "")
        self.frame_results = QtWidgets.QFrame(self.tab_results)
        self.frame_results.setEnabled(False)
        self.frame_results.setGeometry(QtCore.QRect(0, 0, 383, 260))
        self.frame_results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_results.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_results.setObjectName("frame_results")
        self.labelProject = QtWidgets.QLabel(self.frame_results)
        self.labelProject.setGeometry(QtCore.QRect(10, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelProject.setFont(font)
        self.labelProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelProject.setObjectName("labelProject")
        self.label_project_num = QtWidgets.QLabel(self.frame_results)
        self.label_project_num.setGeometry(QtCore.QRect(180, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_project_num.setFont(font)
        self.label_project_num.setText("14.576.21.0123")
        self.label_project_num.setObjectName("label_project_num")
        self.label_expert = QtWidgets.QLabel(self.frame_results)
        self.label_expert.setGeometry(QtCore.QRect(10, 60, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_expert.setFont(font)
        self.label_expert.setText("Эксперт:")
        self.label_expert.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_expert.setObjectName("label_expert")
        self.label_expert_name = QtWidgets.QLabel(self.frame_results)
        self.label_expert_name.setGeometry(QtCore.QRect(100, 60, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_expert_name.setFont(font)
        self.label_expert_name.setText("Иванов И.И.")
        self.label_expert_name.setWordWrap(True)
        self.label_expert_name.setObjectName("label_project_num")
        self.label_ugt = QtWidgets.QLabel(self.frame_results)
        self.label_ugt.setGeometry(QtCore.QRect(10, 120, 60, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ugt.setFont(font)
        self.label_ugt.setObjectName("label_ugt")
        self.label_ugt0 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt0.setEnabled(False)
        self.label_ugt0.setGeometry(QtCore.QRect(86, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt0.setFont(font)
        self.label_ugt0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt0.setObjectName("label_ugt0")
        self.label_ugt1 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt1.setEnabled(False)
        self.label_ugt1.setGeometry(QtCore.QRect(116, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt1.setFont(font)
        self.label_ugt1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt1.setObjectName("label_ugt1")
        self.label_ugt2 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt2.setEnabled(False)
        self.label_ugt2.setGeometry(QtCore.QRect(142, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt2.setFont(font)
        self.label_ugt2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt2.setObjectName("label_ugt2")
        self.label_ugt3 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt3.setEnabled(False)
        self.label_ugt3.setGeometry(QtCore.QRect(169, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt3.setFont(font)
        self.label_ugt3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt3.setObjectName("label_ugt3")
        self.label_ugt4 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt4.setEnabled(False)
        self.label_ugt4.setGeometry(QtCore.QRect(193, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt4.setFont(font)
        self.label_ugt4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt4.setObjectName("label_ugt4")
        self.label_ugt5 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt5.setEnabled(False)
        self.label_ugt5.setGeometry(QtCore.QRect(221, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt5.setFont(font)
        self.label_ugt5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt5.setObjectName("label_ugt5")
        self.label_ugt6 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt6.setEnabled(False)
        self.label_ugt6.setGeometry(QtCore.QRect(248, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt6.setFont(font)
        self.label_ugt6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt6.setObjectName("label_ugt6")
        self.label_ugt7 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt7.setEnabled(False)
        self.label_ugt7.setGeometry(QtCore.QRect(274, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt7.setFont(font)
        self.label_ugt7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt7.setObjectName("label_ugt7")
        self.label_ugt8 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt8.setEnabled(False)
        self.label_ugt8.setGeometry(QtCore.QRect(300, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt8.setFont(font)
        self.label_ugt8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt8.setObjectName("label_ugt8")
        self.label_ugt9 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt9.setEnabled(False)
        self.label_ugt9.setGeometry(QtCore.QRect(328, 120, 15, 23))
        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt9.setFont(font)
        self.label_ugt9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt9.setObjectName("label_ugt9")
        self.ugtSlider = QtWidgets.QSlider(self.frame_results)
        self.ugtSlider.setEnabled(False)
        self.ugtSlider.setGeometry(QtCore.QRect(90, 147, 250, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ugtSlider.setFont(font)
        self.ugtSlider.setTabletTracking(False)
        self.ugtSlider.setAutoFillBackground(False)
        self.ugtSlider.setMaximum(9)
        self.ugtSlider.setPageStep(10)
        self.ugtSlider.setProperty("value", 0)
        self.ugtSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ugtSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ugtSlider.setTickInterval(0)
        self.ugtSlider.setObjectName("ugtSlider")
        self.trl = QtWidgets.QLabel(self.frame_results)
        self.trl.setGeometry(QtCore.QRect(70, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trl.setFont(font)
        self.trl.setObjectName("trl")
        self.label_trl_result = QtWidgets.QLabel(self.frame_results)
        self.label_trl_result.setGeometry(QtCore.QRect(68, 220, 32, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_trl_result.setFont(font)
        self.label_trl_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_trl_result.setLineWidth(2)
        self.label_trl_result.setMidLineWidth(1)
        self.label_trl_result.setTextFormat(QtCore.Qt.PlainText)
        self.label_trl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trl_result.setObjectName("label_trl_result")
        self.mrl = QtWidgets.QLabel(self.frame_results)
        self.mrl.setGeometry(QtCore.QRect(130, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mrl.setFont(font)
        self.mrl.setObjectName("mrl")
        self.label_mrl_result = QtWidgets.QLabel(self.frame_results)
        self.label_mrl_result.setGeometry(QtCore.QRect(128, 220, 32, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_mrl_result.setFont(font)
        self.label_mrl_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_mrl_result.setLineWidth(2)
        self.label_mrl_result.setMidLineWidth(1)
        self.label_mrl_result.setTextFormat(QtCore.Qt.PlainText)
        self.label_mrl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mrl_result.setObjectName("label_mrl_result")
        self.erl = QtWidgets.QLabel(self.frame_results)
        self.erl.setGeometry(QtCore.QRect(190, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.erl.setFont(font)
        self.erl.setObjectName("erl")
        self.label_erl_result = QtWidgets.QLabel(self.frame_results)
        self.label_erl_result.setGeometry(QtCore.QRect(188, 220, 32, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_erl_result.setFont(font)
        self.label_erl_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_erl_result.setLineWidth(2)
        self.label_erl_result.setMidLineWidth(1)
        self.label_erl_result.setTextFormat(QtCore.Qt.PlainText)
        self.label_erl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erl_result.setObjectName("label_erl_result")
        self.orl = QtWidgets.QLabel(self.frame_results)
        self.orl.setGeometry(QtCore.QRect(250, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orl.setFont(font)
        self.orl.setObjectName("orl")
        self.label_orl_result = QtWidgets.QLabel(self.frame_results)
        self.label_orl_result.setGeometry(QtCore.QRect(248, 220, 32, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_orl_result.setFont(font)
        self.label_orl_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_orl_result.setLineWidth(2)
        self.label_orl_result.setMidLineWidth(1)
        self.label_orl_result.setTextFormat(QtCore.Qt.PlainText)
        self.label_orl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_orl_result.setObjectName("label_orl_result")
        self.crl = QtWidgets.QLabel(self.frame_results)
        self.crl.setGeometry(QtCore.QRect(310, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crl.setFont(font)
        self.crl.setObjectName("crl")
        self.label_crl_result = QtWidgets.QLabel(self.frame_results)
        self.label_crl_result.setGeometry(QtCore.QRect(308, 220, 32, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_crl_result.setFont(font)
        self.label_crl_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_crl_result.setLineWidth(2)
        self.label_crl_result.setMidLineWidth(1)
        self.label_crl_result.setTextFormat(QtCore.Qt.PlainText)
        self.label_crl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_crl_result.setObjectName("label_crl_result")
        self.line_vertical = QtWidgets.QFrame(self.tab_results)
        self.line_vertical.setGeometry(QtCore.QRect(385, 0, 2, 260))
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_vertical")
        self.frame_graph = QtWidgets.QFrame(self.tab_results)
        self.frame_graph.setGeometry(QtCore.QRect(387, 0, 383, 260))
        self.frame_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph.setObjectName("frame_graph")
        self.save_graph_btn = QtWidgets.QPushButton(self.frame_graph)
        self.save_graph_btn.setStyleSheet('background: #f3f3f3;')
        self.save_graph_btn.setGeometry(QtCore.QRect(350, 220, 30, 30))
        self.save_graph_btn.setContentsMargins(0, 0, 0, 0)
        self.save_graph_btn.setIcon(QtGui.QIcon('.\img\\save_icon2.png'))
        self.save_graph_btn.setIconSize(QtCore.QSize(30, 30))
        self.save_graph_btn.setToolTip("Сохранить график")
        self.save_graph_btn.setEnabled(False)
        self.lay = QtWidgets.QVBoxLayout(self.frame_graph)
        self.lay.setContentsMargins(0, 0, 30, 0)
        self.line_horizontal = QtWidgets.QFrame(self.tab_results)
        self.line_horizontal.setGeometry(QtCore.QRect(0, 262, 770, 2))
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line_horizontal")
        #-----------------------Frame_TPRL_results----------------------
        self.frame_tprl_results = QtWidgets.QFrame(self.tab_results)
        self.frame_tprl_results.setGeometry(QtCore.QRect(5, 266, 755, 380))
        self.frame_tprl_results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tprl_results.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tprl_results.setObjectName('frame_tprl_results')
        # -----------------------Table_TPRL_results----------------------
        self.table_tprl_results = QtWidgets.QTableWidget(self.frame_tprl_results)
        self.table_tprl_results.setGeometry(QtCore.QRect(0, 0, 755, 370))
        self.table_tprl_results.setObjectName('table_tprl_results')
        self.table_tprl_results.horizontalHeader().setVisible(False)
        self.table_tprl_results.verticalHeader().setVisible(False)
        #----------------------TPRL_Text_results-----------------------
        # self.text_tprl = QtWidgets.QTextEdit(self.frame_tprl_results)
        # self.text_tprl.setGeometry(QtCore.QRect(5, 5, 720, 55))
        # self.text_tprl.setStyleSheet('''background-color: #f3f3f3;
        #                                 font-size: 17px;
        #                                 border: 0;
        #                                 border-bottom: 1px solid red''')
        #
        # self.text_tprl.setReadOnly(True)
        # self.text_tprl.setObjectName('text_tprl')
        # #----------------------other_text_results------------------------
        # self.text_other = QtWidgets.QTextEdit(self.frame_tprl_results)
        # self.text_other.setGeometry(QtCore.QRect(60, 60, 700, 300))
        # self.text_other.setStyleSheet('''background-color: #f3f3f3;
        #                                         font-size: 16px;
        #                                         border: 0;''')
        #
        # self.text_other.setReadOnly(True)
        # self.text_other.setObjectName('text_other')
        #
        #-----------------------------------------------------------
        # self.frame_check_params = QtWidgets.QFrame(self.tab_results)
        # self.frame_check_params.setGeometry(QtCore.QRect(0, 0, 770, 140))
        # self.frame_check_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_check_params.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_check_params.setObjectName("frame_check_params")
        # self.group_check_params = QtWidgets.QGroupBox(self.tab_results)
        # self.group_check_params.setEnabled(True)
        # self.group_check_params.setGeometry(QtCore.QRect(10, 10, 750, 130))
        # self.group_check_params.setObjectName("group_check_params")
        # self.res_check_trl = QtWidgets.QCheckBox(self.group_check_params)
        # self.res_check_trl.setGeometry(QtCore.QRect(50, 20, 240, 17))
        # self.res_check_trl.setObjectName("res_check_trl")
        # self.res_check_mrl = QtWidgets.QCheckBox(self.group_check_params)
        # self.res_check_mrl.setGeometry(QtCore.QRect(50, 50, 240, 17))
        # self.res_check_mrl.setObjectName("check_mrl")
        # self.res_check_erl = QtWidgets.QCheckBox(self.group_check_params)
        # self.res_check_erl.setGeometry(QtCore.QRect(50, 80, 240, 17))
        # self.res_check_erl.setObjectName("res_check_erl")
        # self.res_check_orl = QtWidgets.QCheckBox(self.group_check_params)
        # self.res_check_orl.setGeometry(QtCore.QRect(400, 20, 240, 17))
        # self.res_check_orl.setObjectName("res_check_orl")
        # self.res_check_crl = QtWidgets.QCheckBox(self.group_check_params)
        # self.res_check_crl.setGeometry(QtCore.QRect(400, 50, 240, 17))
        # self.res_check_crl.setObjectName("res_check_crl")
        #-----------------------------------------------------------
        # self.label_calc_params = QtWidgets.QLabel(self.frame_check_params)
        # self.label_calc_params.setGeometry(QtCore.QRect(220, 5, 250, 20))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.label_calc_params.setFont(font)
        # self.label_calc_params.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_calc_params.setObjectName("label_calc_params")

        # self.widget = QtWidgets.QWidget(self.frame_calc_params)
        # self.widget.setGeometry(QtCore.QRect(40, 30, 240, 110))
        # self.widget.setObjectName("widget")
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.check_calc_trl = QtWidgets.QCheckBox(self.widget)
        # self.check_calc_trl.setObjectName("check_calc_trl")
        # self.verticalLayout.addWidget(self.check_calc_trl)
        # self.check_calc_mrl = QtWidgets.QCheckBox(self.widget)
        # self.check_calc_mrl.setObjectName("check_calc_mrl")
        # self.verticalLayout.addWidget(self.check_calc_mrl)
        # self.check_calc_erl = QtWidgets.QCheckBox(self.widget)
        # self.check_calc_erl.setObjectName("check_calc_erl")
        # self.verticalLayout.addWidget(self.check_calc_erl)
        # self.check_calc_orl = QtWidgets.QCheckBox(self.widget)
        # self.check_calc_orl.setObjectName("check_calc_orl")
        # self.verticalLayout.addWidget(self.check_calc_orl)
        # self.check_calc_crl = QtWidgets.QCheckBox(self.widget)
        # self.check_calc_crl.setObjectName("check_calc_crl")
        # self.verticalLayout.addWidget(self.check_calc_crl)
        # self.widget1 = QtWidgets.QWidget(self.frame_calc_params)
        # self.widget1.setGeometry(QtCore.QRect(420, 50, 275, 65))
        # self.widget1.setObjectName("frame_calc_params")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        # self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.radio_calc_hard = QtWidgets.QRadioButton(self.widget1)
        # self.radio_calc_hard.setObjectName("radio_calc_hard")
        # self.verticalLayout_2.addWidget(self.radio_calc_hard)
        # self.radio_calc_soft = QtWidgets.QRadioButton(self.widget1)
        # self.radio_calc_soft.setObjectName("radio_calc_soft")
        # self.verticalLayout_2.addWidget(self.radio_calc_soft)
        # self.radio_calc_both = QtWidgets.QRadioButton(self.widget1)
        # self.radio_calc_both.setAutoRepeat(False)
        # self.radio_calc_both.setObjectName("radio_calc_both")
        # self.verticalLayout_2.addWidget(self.radio_calc_both)

        # self.line = QtWidgets.QFrame(self.tab_results)
        # self.line.setGeometry(QtCore.QRect(0, 160, 770, 2))
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")

        self.tabWidget.raise_()
        self.labelCalc.raise_()

        self.retranslateUi(AppWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "Form"))
        self.labelCalc.setText(_translate("AppWindow", "Расчёт уровня зрелости инновационного продукта/технологии к внедрению в ОАО «РЖД»"))
        self.labelManual.setText(_translate("AppWindow", "Инструкция! Для расчета уровня зрелости инновационного проекта/технологии к внедрению в ОАО «РЖД» необходимо выбрать параметры оценки, по которым производится расчет и нажать кнопку «Установить параметры». В открывшемся поле необходимо отметить те задачи, которые были выполнены в полном объеме на каждом уровне. Результат рассчитывается нажатием кнопки «Расчитать» и представлен в отдельной вкладке «Результаты». Уровень зрелости результата проекта считается достигнутым, если все задачи, относящиеся к различным унифицированным параметрам, отмечены. Общая оценка зрелости проекта принимается равным минимальному достигнутому уровню зрелости по отдельному выбранному параметру.   "))
        self.group_params.setTitle(_translate("AppWindow", "Параметры оценки"))
        self.check_trl.setText(_translate("AppWindow", "Технологическая готовность (TRL)"))
        self.check_mrl.setText(_translate("AppWindow", "Производственная готовность (MRL)"))
        self.check_erl.setText(_translate("AppWindow", "Инженерная готовность (ERL)"))
        self.check_orl.setText(_translate("AppWindow", "Организационная готовность (ORL)"))
        self.check_crl.setText(_translate("AppWindow", "Коммерческая готовность (СRL)"))
        self.group_types.setTitle(_translate("AppWindow", "Тип проекта"))
        self.radio_hard.setText(_translate("AppWindow", "Разработка оборудования"))
        self.radio_soft.setText(_translate("AppWindow", "Разработка программного обеспечения"))
        self.radio_both.setText(_translate("AppWindow", "Разработка оборудования и ПО"))
        self.btn_set_params.setText(_translate("AppWindow", "Установить параметры"))
        self.labelProject.setText(_translate("AppWindow", "Номер проекта:"))
        self.label_ugt.setText(_translate("AppWindow", "TPRL"))
        self.label_ugt0.setText(_translate("AppWindow", "0"))
        self.label_ugt1.setText(_translate("AppWindow", "1"))
        self.label_ugt2.setText(_translate("AppWindow", "2"))
        self.label_ugt3.setText(_translate("AppWindow", "3"))
        self.label_ugt4.setText(_translate("AppWindow", "4"))
        self.label_ugt5.setText(_translate("AppWindow", "5"))
        self.label_ugt6.setText(_translate("AppWindow", "6"))
        self.label_ugt7.setText(_translate("AppWindow", "7"))
        self.label_ugt8.setText(_translate("AppWindow", "8"))
        self.label_ugt9.setText(_translate("AppWindow", "9"))
        self.trl.setText(_translate("AppWindow", "TRL"))
        self.label_trl_result.setText(_translate("AppWindow", "0"))
        self.mrl.setText(_translate("AppWindow", "MRL"))
        self.label_mrl_result.setText(_translate("AppWindow", "0"))
        self.erl.setText(_translate("AppWindow", "ERL"))
        self.label_erl_result.setText(_translate("AppWindow", "0"))
        self.orl.setText(_translate("AppWindow", "ORL"))
        self.label_orl_result.setText(_translate("AppWindow", "0"))
        self.crl.setText(_translate("AppWindow", "CRL"))
        self.label_crl_result.setText(_translate("AppWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calc), _translate("AppWindow", "Калькулятор"))
        self.treeWidget.headerItem().setText(0, _translate("AppWindow", "Параметр"))
        self.treeWidget.headerItem().setText(1, _translate("AppWindow", "Задачи"))
        # self.label_calc_params.setText(_translate("AppWindow", "Подтвержденные параметры"))
        # self.res_check_trl.setText(_translate("AppWindow", "Технологическая готовность (TRL)"))
        # self.res_check_mrl.setText(_translate("AppWindow", "Производственная готовность (MRL)"))
        # self.res_check_erl.setText(_translate("AppWindow", "Инженерная готовность (ERL)"))
        # self.res_check_orl.setText(_translate("AppWindow", "Организационная готовность (ORL)"))
        # self.res_check_crl.setText(_translate("AppWindow", "Коммерческая готовность (СRL)"))
        # self.radio_calc_hard.setText(_translate("AppWindow", "Разработка оборудования"))
        # self.radio_calc_soft.setText(_translate("AppWindow", "Разработка программного обеспечения"))
        # self.radio_calc_both.setText(_translate("AppWindow", "Разработка оборудования и ПО"))
        self.btn_calculate.setText(_translate("AppWindow", "Рассчитать"))
        self.btn_reset_tasks.setText(_translate("AppWindow", "Сбросить задачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_results), _translate("AppWindow", "Результат"))
