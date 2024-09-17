import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
from PyPDF2 import PdfMerger


class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_files = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Merger')
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('请选择要合并的PDF文件', self)
        layout.addWidget(self.label)

        self.select_button = QPushButton('选择PDF文件', self)
        self.select_button.clicked.connect(self.select_files)
        layout.addWidget(self.select_button)

        self.merge_button = QPushButton('合并PDF文件', self)
        self.merge_button.clicked.connect(self.merge_pdfs)
        layout.addWidget(self.merge_button)

        self.setLayout(layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, '选择PDF文件', '', 'PDF Files (*.pdf)')
        if files:
            self.selected_files = files
            self.label.setText(f'已选择 {len(files)} 个文件')

    def merge_pdfs(self):
        if not self.selected_files:
            QMessageBox.warning(self, '错误', '请先选择PDF文件')
            return

        # 选择保存的文件路径
        save_path, _ = QFileDialog.getSaveFileName(
            self, '保存合并后的PDF', '', 'PDF Files (*.pdf)')
        if not save_path:
            return

        if not save_path.endswith('.pdf'):
            save_path += '.pdf'

        try:
            # 创建一个 PdfMerger 对象
            merger = PdfMerger()

            # 将选择的 PDF 文件合并
            for pdf in self.selected_files:
                merger.append(pdf)

            # 将合并后的文件保存
            with open(save_path, 'wb') as output_pdf:
                merger.write(output_pdf)

            QMessageBox.information(self, '成功', f'PDF 文件已成功合并并保存到 {save_path}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'合并PDF文件时出错: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFMergerApp()
    ex.show()
    sys.exit(app.exec_())
