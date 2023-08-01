import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget, QComboBox, QHBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter, QLinearGradient, QBrush, QCursor
from PyQt5.QtCore import Qt

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 500)

        # Create the main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Set fancy stylesheet
        self.setStyleSheet('background-color: #2E4053;')

        # Create the task input field and "Add Task" button
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText('Enter your task...')
        self.task_input.setStyleSheet(
            'background-color: #485669; color: #E0E0E0; border: 2px solid #5B6F82; border-radius: 5px; padding: 10px; font-size: 14px;'
        )

        self.add_button = QPushButton('Add Task', objectName='addButton')
        self.add_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_button.clicked.connect(self.add_task)
        self.add_button.setStyleSheet(
            'background-color: #4CAF50; color: #E0E0E0; border-radius: 15px; padding: 10px 20px; font-size: 14px;'
        )

        # Create the task list
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.edit_task)
        self.task_list.setStyleSheet(
            'background-color: #485669; color: #E0E0E0; border: 2px solid #5B6F82; border-radius: 5px; padding: 10px; font-size: 14px;'
        )

        # Create a layout for the priority and status options
        priority_layout = QHBoxLayout()
        self.priority_label = QLabel('Priority:')
        self.priority_label.setStyleSheet('color: #E0E0E0; font-size: 14px;')
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(['High', 'Medium', 'Low'])
        self.priority_combo.setStyleSheet(
            'background-color: #485669; color: #E0E0E0; border: 2px solid #5B6F82; border-radius: 5px; padding: 5px; font-size: 14px;'
        )

        self.status_label = QLabel('Status:')
        self.status_label.setStyleSheet('color: #E0E0E0; font-size: 14px;')
        self.status_combo = QComboBox()
        self.status_combo.addItems(['Pending', 'Completed'])
        self.status_combo.setStyleSheet(
            'background-color: #485669; color: #E0E0E0; border: 2px solid #5B6F82; border-radius: 5px; padding: 5px; font-size: 14px;'
        )

        # Create "Update Task" button
        self.update_button = QPushButton('Update Task', objectName='updateButton')
        self.update_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_button.clicked.connect(self.update_task)
        self.update_button.setStyleSheet(
            'background-color: #1E90FF; color: #E0E0E0; border-radius: 15px; padding: 10px 20px; font-size: 14px;'
        )

        # Create "Delete Task" button
        self.delete_button = QPushButton('Delete Task', objectName='deleteButton')
        self.delete_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_button.setStyleSheet(
            'background-color: #FF4500; color: #E0E0E0; border-radius: 15px; padding: 10px 20px; font-size: 14px;'
        )

        # Add widgets to the layout
        layout.addWidget(self.task_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list)
        layout.addLayout(priority_layout)
        priority_layout.addWidget(self.priority_label)
        priority_layout.addWidget(self.priority_combo)
        priority_layout.addWidget(self.status_label)
        priority_layout.addWidget(self.status_combo)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

    def add_task(self):
        task = self.task_input.text()
        if task:
            priority = self.priority_combo.currentText()
            status = self.status_combo.currentText()
            self.task_list.addItem(f'{task} - Priority: {priority} - Status: {status}')
            self.task_input.clear()

    def edit_task(self, item):
        current_text = item.text()
        task, priority, status = self.get_task_details(current_text)
        self.task_input.setText(task)
        self.priority_combo.setCurrentText(priority)
        self.status_combo.setCurrentText(status)

    def update_task(self):
        selected_item = self.task_list.currentItem()
        if not selected_item:
            return

        current_text = selected_item.text()
        task, _, _ = self.get_task_details(current_text)
        new_task = self.task_input.text()
        if new_task:
            priority = self.priority_combo.currentText()
            status = self.status_combo.currentText()
            selected_item.setText(f'{new_task} - Priority: {priority} - Status: {status}')
            self.task_input.clear()

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if not selected_item:
            return

        confirm = QMessageBox.question(self, 'Delete Task', 'Are you sure you want to delete this task?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.task_list.takeItem(self.task_list.row(selected_item))

    def get_task_details(self, task_text):
        parts = task_text.split(' - ')
        task = parts[0]
        priority = parts[1].replace('Priority: ', '')
        status = parts[2].replace('Status: ', '')
        return task, priority, status

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())
