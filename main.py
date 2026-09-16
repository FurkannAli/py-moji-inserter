import sys, json
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtGui import QCursor

from window import Ui_Form
from inserter import paste_character
import window

class EmojiInserter(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.is_pasting = False

        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.ui.gridLayout.setSpacing(4)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool            
        )

        self.ui.gridLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.data_path = Path(__file__).parent / "assets" / "data.json"
        self.dataset = self.load_data()
        self.current_category = "kaomoji"

        self.ui.pushButton_Kao.clicked.connect(lambda: self.switch_category("kaomoji"))
        self.ui.pushButton_Emo.clicked.connect(lambda: self.switch_category("emoji"))
        self.ui.pushButton_Sym.clicked.connect(lambda: self.switch_category("symbol"))
        self.ui.lineEdit.textChanged.connect(self.filter_items)

        self.move_to_cursor()

        self.switch_category("kaomoji")

    def load_data(self):
        if self.data_path.exists():
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"kaomoji": [], "emoji": [], "symbols": []}

    def move_to_cursor(self):
        cursor_pos = QCursor.pos()
        self.move(cursor_pos)

    def switch_category(self, category: str):
        self.current_category = category
        self.ui.lineEdit.clear()
        self.populate_grid(self.dataset.get(category, []))

    #oh my goshhh bruhhh 
    def populate_grid(self, items: list):
        while self.ui.gridLayout.count():
            item = self.ui.gridLayout.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        is_kaomoji = self.current_category == "kaomoji"
        columns = 3 if is_kaomoji else 6

        for c in range(self.ui.gridLayout.columnCount()):
            self.ui.gridLayout.setColumnStretch(c, 0)
        for c in range(columns):
            self.ui.gridLayout.setColumnStretch(c, 1)

        for idx, entry in enumerate(items):
            char = entry["char"]
            btn = QPushButton(char)
            btn.setFixedHeight(38)

            btn.setMinimumWidth(0)
            btn.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)

            btn.clicked.connect(lambda _, text=char: self.handle_selection(text))

            row = idx // columns
            col = idx % columns
            self.ui.gridLayout.addWidget(btn, row, col)

    def filter_items(self, query: str):
        query = query.strip().lower()
        if not query:
            self.populate_grid(self.dataset.get(self.current_category, []))
            return

        filtered = []
        for entry in self.dataset.get(self.current_category, []):
            if query in entry["char"].lower() or any(query in kw for kw in entry["keywords"]):
                filtered.append(entry)

        self.populate_grid(filtered)

    def handle_selection(self, text: str):
        self.is_pasting = True
        self.hide()
        QTimer.singleShot(20, lambda: self._finish_paste(text))
        #paste_character(text)
        #QApplication.quit()

    def _finish_paste(self, text: str):
        paste_character(text)
        self.show()
        self.raise_()
        self.activateWindow()
        self.is_pasting = False

    def changeEvent(self, event):
        if event.type() == event.Type.ActivationChange and not self.isActiveWindow():
            if not self.is_pasting:
                self.hide()
                QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmojiInserter()
    window.show()
    sys.exit(app.exec())