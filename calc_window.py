# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(670, 630)
        self.labelCalc = QtWidgets.QLabel(AppWindow)
        self.labelCalc.setGeometry(QtCore.QRect(70, 10, 591, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelCalc.setFont(font)
        self.labelCalc.setTextFormat(QtCore.Qt.RichText)
        self.labelCalc.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCalc.setWordWrap(True)
        self.labelCalc.setObjectName("labelCalc")
        self.tabWidget = QtWidgets.QTabWidget(AppWindow)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 670, 540))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_params = QtWidgets.QWidget()
        self.tab_params.setObjectName("tab_params")
        self.frame_params = QtWidgets.QGroupBox(self.tab_params)
        self.frame_params.setEnabled(True)
        self.frame_params.setGeometry(QtCore.QRect(10, 10, 320, 170))
        self.frame_params.setObjectName("frame_params")
        self.check_trl = QtWidgets.QCheckBox(self.frame_params)
        self.check_trl.setGeometry(QtCore.QRect(20, 20, 231, 17))
        self.check_trl.setObjectName("check_trl")
        self.check_trl.setChecked(True)
        self.check_mrl = QtWidgets.QCheckBox(self.frame_params)
        self.check_mrl.setGeometry(QtCore.QRect(20, 50, 231, 17))
        self.check_mrl.setObjectName("check_mrl")
        self.check_mrl.setChecked(True)
        self.check_erl = QtWidgets.QCheckBox(self.frame_params)
        self.check_erl.setGeometry(QtCore.QRect(20, 80, 231, 17))
        self.check_erl.setObjectName("check_erl")
        self.check_erl.setChecked(True)
        self.check_orl = QtWidgets.QCheckBox(self.frame_params)
        self.check_orl.setGeometry(QtCore.QRect(20, 110, 231, 17))
        self.check_orl.setObjectName("check_orl")
        self.check_orl.setChecked(True)
        self.check_crl = QtWidgets.QCheckBox(self.frame_params)
        self.check_crl.setGeometry(QtCore.QRect(20, 140, 231, 17))
        self.check_crl.setObjectName("check_crl")
        self.check_crl.setChecked(True)
        self.frame_types = QtWidgets.QGroupBox(self.tab_params)
        self.frame_types.setGeometry(QtCore.QRect(350, 10, 280, 110))
        self.frame_types.setObjectName("frame_types")
        self.radio_hard = QtWidgets.QRadioButton(self.frame_types)
        self.radio_hard.setGeometry(QtCore.QRect(10, 20, 211, 17))
        self.radio_hard.setObjectName("radio_hard")
        self.radio_hard.setChecked(True)
        self.radio_soft = QtWidgets.QRadioButton(self.frame_types)
        self.radio_soft.setGeometry(QtCore.QRect(10, 50, 261, 17))
        self.radio_soft.setObjectName("radio_soft")
        self.radio_both = QtWidgets.QRadioButton(self.frame_types)
        self.radio_both.setGeometry(QtCore.QRect(10, 80, 261, 16))
        self.radio_both.setAutoRepeat(False)
        self.radio_both.setObjectName("radio_both")
        self.btn_set_params = QtWidgets.QPushButton(self.tab_params)
        self.btn_set_params.setGeometry(QtCore.QRect(400, 140, 180, 30))
        self.btn_set_params.setObjectName("btn_set_params")
        self.frame_graph = QtWidgets.QFrame(self.tab_params)
        self.frame_graph.setGeometry(QtCore.QRect(340, 210, 320, 300))
        self.frame_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph.setObjectName("frame_graph")
        self.frame_results = QtWidgets.QFrame(self.tab_params)
        self.frame_results.setEnabled(False)
        self.frame_results.setGeometry(QtCore.QRect(10, 210, 320, 300))
        self.frame_results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_results.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_results.setObjectName("frame_results")
        self.label_ugt = QtWidgets.QLabel(self.frame_results)
        self.label_ugt.setGeometry(QtCore.QRect(10, 100, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ugt.setFont(font)
        self.label_ugt.setObjectName("label_ugt")
        self.label_ugt0 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt0.setEnabled(False)
        self.label_ugt0.setGeometry(QtCore.QRect(60, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt0.setFont(font)
        self.label_ugt0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt0.setObjectName("label_ugt0")
        self.label_ugt1 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt1.setEnabled(False)
        self.label_ugt1.setGeometry(QtCore.QRect(88, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt1.setFont(font)
        self.label_ugt1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt1.setObjectName("label_ugt1")
        self.label_ugt2 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt2.setEnabled(False)
        self.label_ugt2.setGeometry(QtCore.QRect(114, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt2.setFont(font)
        self.label_ugt2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt2.setObjectName("label_ugt2")
        self.label_ugt3 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt3.setEnabled(False)
        self.label_ugt3.setGeometry(QtCore.QRect(141, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt3.setFont(font)
        self.label_ugt3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt3.setObjectName("label_ugt3")
        self.label_ugt4 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt4.setEnabled(False)
        self.label_ugt4.setGeometry(QtCore.QRect(165, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt4.setFont(font)
        self.label_ugt4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt4.setObjectName("label_ugt4")
        self.label_ugt5 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt5.setEnabled(False)
        self.label_ugt5.setGeometry(QtCore.QRect(193, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt5.setFont(font)
        self.label_ugt5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt5.setObjectName("label_ugt5")
        self.label_ugt6 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt6.setEnabled(False)
        self.label_ugt6.setGeometry(QtCore.QRect(220, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt6.setFont(font)
        self.label_ugt6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt6.setObjectName("label_ugt6")
        self.label_ugt7 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt7.setEnabled(False)
        self.label_ugt7.setGeometry(QtCore.QRect(246, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt7.setFont(font)
        self.label_ugt7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt7.setObjectName("label_ugt7")
        self.label_ugt8 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt8.setEnabled(False)
        self.label_ugt8.setGeometry(QtCore.QRect(272, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt8.setFont(font)
        self.label_ugt8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt8.setObjectName("label_ugt8")
        self.label_ugt9 = QtWidgets.QLabel(self.frame_results)
        self.label_ugt9.setEnabled(False)
        self.label_ugt9.setGeometry(QtCore.QRect(300, 100, 10, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ugt9.setFont(font)
        self.label_ugt9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ugt9.setObjectName("label_ugt9")
        self.ugtSlider = QtWidgets.QSlider(self.frame_results)
        self.ugtSlider.setEnabled(True)
        self.ugtSlider.setGeometry(QtCore.QRect(60, 120, 250, 22))
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
        self.trl.setGeometry(QtCore.QRect(35, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trl.setFont(font)
        self.trl.setObjectName("trl")
        self.label_trl_result = QtWidgets.QLabel(self.frame_results)
        self.label_trl_result.setGeometry(QtCore.QRect(40, 220, 20, 25))
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
        self.mrl.setGeometry(QtCore.QRect(95, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mrl.setFont(font)
        self.mrl.setObjectName("mrl")
        self.label_mrl_result = QtWidgets.QLabel(self.frame_results)
        self.label_mrl_result.setGeometry(QtCore.QRect(100, 220, 20, 25))
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
        self.erl.setGeometry(QtCore.QRect(155, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.erl.setFont(font)
        self.erl.setObjectName("erl")
        self.label_erl_result = QtWidgets.QLabel(self.frame_results)
        self.label_erl_result.setGeometry(QtCore.QRect(160, 220, 20, 25))
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
        self.orl.setGeometry(QtCore.QRect(215, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orl.setFont(font)
        self.orl.setObjectName("orl")
        self.label_orl_result = QtWidgets.QLabel(self.frame_results)
        self.label_orl_result.setGeometry(QtCore.QRect(220, 220, 20, 25))
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
        self.crl.setGeometry(QtCore.QRect(275, 200, 30, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crl.setFont(font)
        self.crl.setObjectName("crl")
        self.label_crl_result = QtWidgets.QLabel(self.frame_results)
        self.label_crl_result.setGeometry(QtCore.QRect(280, 220, 20, 25))
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
        self.labelProject = QtWidgets.QLabel(self.frame_results)
        self.labelProject.setGeometry(QtCore.QRect(10, 10, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelProject.setFont(font)
        self.labelProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelProject.setObjectName("labelProject")
        self.label_project_num = QtWidgets.QLabel(self.frame_results)
        self.label_project_num.setGeometry(QtCore.QRect(165, 10, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_project_num.setFont(font)
        self.label_project_num.setText("")
        self.label_project_num.setObjectName("label_project_num")
        self.line_horizontal = QtWidgets.QFrame(self.tab_params)
        self.line_horizontal.setGeometry(QtCore.QRect(10, 190, 650, 20))
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line_horizontal")
        self.line_vertical = QtWidgets.QFrame(self.tab_params)
        self.line_vertical.setGeometry(QtCore.QRect(335, 200, 2, 330))
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_vertical")
        self.tabWidget.addTab(self.tab_params, "")
        self.tab_calc = QtWidgets.QWidget()
        self.tab_calc.setObjectName("tab_calc")
        self.tab_calc.setEnabled(False)
        self.frame_calc_params = QtWidgets.QFrame(self.tab_calc)
        self.frame_calc_params.setGeometry(QtCore.QRect(5, 5, 650, 140))
        self.frame_calc_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calc_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calc_params.setObjectName("frame_calc_params")
        self.label_calc_params = QtWidgets.QLabel(self.tab_calc)
        self.label_calc_params.setGeometry(QtCore.QRect(220, 5, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_calc_params.setFont(font)
        self.label_calc_params.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calc_params.setObjectName("label_calc_params")
        self.widget = QtWidgets.QWidget(self.frame_calc_params)
        self.widget.setGeometry(QtCore.QRect(40, 30, 213, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_calc_trl = QtWidgets.QCheckBox(self.widget)
        self.check_calc_trl.setObjectName("check_calc_trl")
        self.verticalLayout.addWidget(self.check_calc_trl)
        self.check_calc_mrl = QtWidgets.QCheckBox(self.widget)
        self.check_calc_mrl.setObjectName("check_calc_mrl")
        self.verticalLayout.addWidget(self.check_calc_mrl)
        self.check_calc_erl = QtWidgets.QCheckBox(self.widget)
        self.check_calc_erl.setObjectName("check_calc_erl")
        self.verticalLayout.addWidget(self.check_calc_erl)
        self.check_calc_orl = QtWidgets.QCheckBox(self.widget)
        self.check_calc_orl.setObjectName("check_calc_orl")
        self.verticalLayout.addWidget(self.check_calc_orl)
        self.check_calc_crl = QtWidgets.QCheckBox(self.widget)
        self.check_calc_crl.setObjectName("check_calc_crl")
        self.verticalLayout.addWidget(self.check_calc_crl)
        self.widget1 = QtWidgets.QWidget(self.frame_calc_params)
        self.widget1.setGeometry(QtCore.QRect(370, 50, 225, 65))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_calc_hard = QtWidgets.QRadioButton(self.widget1)
        self.radio_calc_hard.setObjectName("radio_calc_hard")
        self.verticalLayout_2.addWidget(self.radio_calc_hard)
        self.radio_calc_soft = QtWidgets.QRadioButton(self.widget1)
        self.radio_calc_soft.setObjectName("radio_calc_soft")
        self.verticalLayout_2.addWidget(self.radio_calc_soft)
        self.radio_calc_both = QtWidgets.QRadioButton(self.widget1)
        self.radio_calc_both.setAutoRepeat(False)
        self.radio_calc_both.setObjectName("radio_calc_both")
        self.verticalLayout_2.addWidget(self.radio_calc_both)
        self.btn_calculate = QtWidgets.QPushButton(self.tab_calc)
        self.btn_calculate.setGeometry(QtCore.QRect(240, 470, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setObjectName("btn_calculate")
        self.line = QtWidgets.QFrame(self.tab_calc)
        self.line.setGeometry(QtCore.QRect(0, 160, 670, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_questions = QtWidgets.QFrame(self.tab_calc)
        self.frame_questions.setGeometry(QtCore.QRect(5, 167, 650, 295))
        self.frame_questions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questions.setObjectName("frame_questions")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_questions)
        self.treeWidget.setGeometry(QtCore.QRect(5, 5, 640, 285))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.tabWidget.addTab(self.tab_calc, "")
        self.tabWidget.raise_()
        self.labelCalc.raise_()

        self.retranslateUi(AppWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "Form"))
        self.labelCalc.setText(_translate("AppWindow", "Калькулятор уровня готовности технологий для оценки зрелости инновационного продукта/технологии к внедрению в ОАО «РЖД»"))
        self.frame_params.setTitle(_translate("AppWindow", "Параметры оценки"))
        self.check_trl.setText(_translate("AppWindow", "Технологическая готовность (TRL)"))
        self.check_mrl.setText(_translate("AppWindow", "Производственная готовность (MRL)"))
        self.check_erl.setText(_translate("AppWindow", "Инженерная готовность (ERL)"))
        self.check_orl.setText(_translate("AppWindow", "Организационная готовность (ORL)"))
        self.check_crl.setText(_translate("AppWindow", "Коммерческая готовность (СRL)"))
        self.frame_types.setTitle(_translate("AppWindow", "Тип проекта"))
        self.radio_hard.setText(_translate("AppWindow", "Разработка оборудования"))
        self.radio_soft.setText(_translate("AppWindow", "Разработка программного обеспечения"))
        self.radio_both.setText(_translate("AppWindow", "Разработка оборудования и ПО"))
        self.btn_set_params.setText(_translate("AppWindow", "Установить параметры"))
        self.label_ugt2.setText(_translate("AppWindow", "2"))
        self.label_ugt3.setText(_translate("AppWindow", "3"))
        self.label_orl_result.setText(_translate("AppWindow", "0"))
        self.orl.setText(_translate("AppWindow", "ORL"))
        self.label_trl_result.setText(_translate("AppWindow", "0"))
        self.label_ugt4.setText(_translate("AppWindow", "4"))
        self.crl.setText(_translate("AppWindow", "CRL"))
        self.trl.setText(_translate("AppWindow", "TRL"))
        self.label_crl_result.setText(_translate("AppWindow", "0"))
        self.label_ugt.setText(_translate("AppWindow", "УГТ"))
        self.label_ugt7.setText(_translate("AppWindow", "7"))
        self.label_mrl_result.setText(_translate("AppWindow", "0"))
        self.label_ugt0.setText(_translate("AppWindow", "0"))
        self.label_erl_result.setText(_translate("AppWindow", "0"))
        self.label_ugt8.setText(_translate("AppWindow", "8"))
        self.mrl.setText(_translate("AppWindow", "MRL"))
        self.labelProject.setText(_translate("AppWindow", "Номер проекта"))
        self.label_ugt6.setText(_translate("AppWindow", "6"))
        self.label_ugt1.setText(_translate("AppWindow", "1"))
        self.erl.setText(_translate("AppWindow", "ERL"))
        self.label_ugt9.setText(_translate("AppWindow", "9"))
        self.label_ugt5.setText(_translate("AppWindow", "5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_params), _translate("AppWindow", "Параметры"))
        self.label_calc_params.setText(_translate("AppWindow", "Подтвержденные параметры"))
        self.check_calc_trl.setText(_translate("AppWindow", "Технологическая готовность (TRL)"))
        self.check_calc_mrl.setText(_translate("AppWindow", "Производственная готовность (MRL)"))
        self.check_calc_erl.setText(_translate("AppWindow", "Инженерная готовность (ERL)"))
        self.check_calc_orl.setText(_translate("AppWindow", "Организационная готовность (ORL)"))
        self.check_calc_crl.setText(_translate("AppWindow", "Коммерческая готовность (СRL)"))
        self.radio_calc_hard.setText(_translate("AppWindow", "Разработка оборудования"))
        self.radio_calc_soft.setText(_translate("AppWindow", "Разработка программного обеспечения"))
        self.radio_calc_both.setText(_translate("AppWindow", "Разработка оборудования и ПО"))
        self.btn_calculate.setText(_translate("AppWindow", "Рассчитать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calc), _translate("AppWindow", "Калькулятор"))
