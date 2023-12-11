# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import analyser
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////


class SetupMainWindow:
  def __init__(self):
    super().__init__()
    # SETUP MAIN WINDOw
    # Load widgets from "gui\uis\main_window\ui_main.py"
    # ///////////////////////////////////////////////////////////////
    self.ui = UI_MainWindow()
    self.ui.setup_ui(self)

  # ADD LEFT MENUS
  # ///////////////////////////////////////////////////////////////
  add_left_menus = [
      {
          "btn_icon": "icon_home.svg",
          "btn_id": "btn_home",
          "btn_text": "Home",
          "btn_tooltip": "Home page",
          "show_top": True,
          "is_active": True
      },
      {
          "btn_icon": "icon_file.svg",
          "btn_id": "btn_internet_speed",
          "btn_text": "Analyse Internet Speed",
          "btn_tooltip": "Analyse your Network Performance",
          "show_top": True,
          "is_active": False,
      },
      {
          "btn_icon": "icon_signal.svg",
          "btn_id": "btn_dns",
          "btn_text": "Analyse DNS",
          "btn_tooltip": "Analyse any Site's DNS",
          "show_top": True,
          "is_active": False,
      },
      {
          "btn_icon": "icon_idle.svg",
          "btn_id": "btn_ping",
          "btn_text": "Analyse Response Time",
          "btn_tooltip": "Analyse Response Time",
          "show_top": True,
          "is_active": False,
      },
      {
          "btn_icon": "icon_folder.svg",
          "btn_id": "btn_loading_speed",
          "btn_text": "Analyse Loading Speed",
          "btn_tooltip": "Analyse Site Loading Speed",
          "show_top": True,
          "is_active": False,
      },
      {
          "btn_icon": "icon_settings.svg",
          "btn_id": "btn_settings",
          "btn_text": "Settings",
          "btn_tooltip": "Settings",
          "show_top": False,
          "is_active": False,
      }
  ]

  # ADD TITLE BAR MENUS
  # ///////////////////////////////////////////////////////////////
  add_title_bar_menus = [
      {
          "btn_icon": "icon_search.svg",
          "btn_id": "btn_search",
          "btn_tooltip": "Search",
          "is_active": False
      },
      {
          "btn_icon": "icon_settings.svg",
          "btn_id": "btn_top_settings",
          "btn_tooltip": "Top settings",
          "is_active": False
      }
  ]

  # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
  # Get sender() function when btn is clicked
  # ///////////////////////////////////////////////////////////////
  def setup_btns(self):
    if self.ui.title_bar.sender() != None:
      return self.ui.title_bar.sender()
    elif self.ui.left_menu.sender() != None:
      return self.ui.left_menu.sender()
    elif self.ui.left_column.sender() != None:
      return self.ui.left_column.sender()

  # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
  # ///////////////////////////////////////////////////////////////
  def setup_gui(self):
    # APP TITLE
    # ///////////////////////////////////////////////////////////////
    self.setWindowTitle(self.settings["app_name"])

    # REMOVE TITLE BAR
    # ///////////////////////////////////////////////////////////////
    if self.settings["custom_title_bar"]:
      self.setWindowFlag(Qt.FramelessWindowHint)
      self.setAttribute(Qt.WA_TranslucentBackground)

    # ADD GRIPS
    # ///////////////////////////////////////////////////////////////
    if self.settings["custom_title_bar"]:
      self.left_grip = PyGrips(self, "left", self.hide_grips)
      self.right_grip = PyGrips(self, "right", self.hide_grips)
      self.top_grip = PyGrips(self, "top", self.hide_grips)
      self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
      self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
      self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
      self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
      self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

    # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
    # ///////////////////////////////////////////////////////////////
    # ADD MENUS
    self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

    # SET SIGNALS
    self.ui.left_menu.clicked.connect(self.btn_clicked)
    self.ui.left_menu.released.connect(self.btn_released)

    # TITLE BAR / ADD EXTRA BUTTONS
    # ///////////////////////////////////////////////////////////////

    # ADD MENUS
    self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

    # SET SIGNALS
    self.ui.title_bar.clicked.connect(self.btn_clicked)
    self.ui.title_bar.released.connect(self.btn_released)

    # ADD Title
    if self.settings["custom_title_bar"]:
      self.ui.title_bar.set_title(self.settings["app_name"])
    else:
      self.ui.title_bar.set_title("Welcome to Web Analyser")

    # LEFT COLUMN SET SIGNALS
    # ///////////////////////////////////////////////////////////////
    self.ui.left_column.clicked.connect(self.btn_clicked)
    self.ui.left_column.released.connect(self.btn_released)

    # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
    # ///////////////////////////////////////////////////////////////
    MainFunctions.set_page(self, self.ui.load_pages.home)
    MainFunctions.set_left_column_menu(
        self,
        menu=self.ui.left_column.menus.menu_1,
        title="Settings Left Column",
        icon_path=Functions.set_svg_icon("icon_settings.svg")
    )
    MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

    # ///////////////////////////////////////////////////////////////
    # EXAMPLE CUSTOM WIDGETS
    # Here are added the custom widgets to pages and columns that
    # were created using Qt Designer.
    # This is just an example and should be deleted when creating
    # your application.
    #
    # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
    # You can access objects inside Qt Designer projects using
    # the objects below:
    #
    # <OBJECTS>
    # LEFT COLUMN: self.ui.left_column.menus
    # RIGHT COLUMN: self.ui.right_column
    # LOAD PAGES: self.ui.load_pages
    # </OBJECTS>
    # ///////////////////////////////////////////////////////////////

    # LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    settings = Settings()
    self.settings = settings.items

    # LOAD THEME COLOR
    # ///////////////////////////////////////////////////////////////
    themes = Themes()
    self.themes = themes.items
    self.ls_input = PyLineEdit(
        place_holder_text="Enter site name",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
    )
    self.ls_input.setMinimumHeight(40)
    self.ls_btn_submit = PyPushButton(
        text="Submit",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
        bg_color_hover=self.themes["app_color"]["dark_three"],
        bg_color_pressed=self.themes["app_color"]["dark_four"]
    )
    self.ls_btn_submit.setMinimumHeight(40)
    self.ls_btn_submit.setMaximumWidth(300)

    self.ls_table = PyTableWidget(
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        selection_color=self.themes["app_color"]["context_color"],
        bg_color=self.themes["app_color"]["bg_two"],
        header_horizontal_color=self.themes["app_color"]["dark_two"],
        header_vertical_color=self.themes["app_color"]["bg_three"],
        bottom_line_color=self.themes["app_color"]["bg_three"],
        grid_line_color=self.themes["app_color"]["bg_one"],
        scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
        scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        context_color=self.themes["app_color"]["context_color"]
    )
    self.ls_table.setColumnCount(2)
    self.ls_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.ls_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    self.ls_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    self.column_1 = QTableWidgetItem()
    self.column_1.setText("Site Name")

    self.column_2 = QTableWidgetItem()
    self.column_2.setText("Loading Speed (sec)")

    # Set column
    self.ls_table.setHorizontalHeaderItem(0, self.column_1)
    self.ls_table.setHorizontalHeaderItem(1, self.column_2)

    def ls_on_submit():
      sitename = self.ls_input.text()
      score, data = analyser.compare_load_times(sitename)
      for row in data:
        row_number = self.ls_table.rowCount()
        self.ls_table.insertRow(row_number)
        self.ls_table.setItem(
            row_number, 0, QTableWidgetItem(row[0]))
        self.ls_table.setItem(
            row_number, 1, QTableWidgetItem(str(row[1])))

      row_number = self.ls_table.rowCount()
      self.ls_table.insertRow(row_number)
      self.ls_table.setItem(
          row_number, 0, QTableWidgetItem('Score: '))
      self.ls_table.setItem(
          row_number, 1, QTableWidgetItem(str(score)))

      self.ls_input.setText("")
    self.ls_btn_submit.clicked.connect(ls_on_submit)

    self.ui.load_pages.ls_top_layout.addWidget(self.ls_input)
    self.ui.load_pages.ls_btn_layout.addWidget(self.ls_btn_submit)
    self.ui.load_pages.ls_main_layout.addWidget(self.ls_table)

    # RS Starts here
    # /////////////////////////////////////////////////////////////
    self.rs_input = PyLineEdit(
        place_holder_text="Enter site name",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
    )
    self.rs_input.setMinimumHeight(40)
    self.rs_btn_submit = PyPushButton(
        text="Submit",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
        bg_color_hover=self.themes["app_color"]["dark_three"],
        bg_color_pressed=self.themes["app_color"]["dark_four"]
    )
    self.rs_btn_submit.setMinimumHeight(40)
    self.rs_btn_submit.setMaximumWidth(300)

    self.rs_table = PyTableWidget(
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        selection_color=self.themes["app_color"]["context_color"],
        bg_color=self.themes["app_color"]["bg_two"],
        header_horizontal_color=self.themes["app_color"]["dark_two"],
        header_vertical_color=self.themes["app_color"]["bg_three"],
        bottom_line_color=self.themes["app_color"]["bg_three"],
        grid_line_color=self.themes["app_color"]["bg_one"],
        scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
        scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        context_color=self.themes["app_color"]["context_color"]
    )
    self.rs_table.setColumnCount(2)
    self.rs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.rs_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    self.rs_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    self.column_1 = QTableWidgetItem()
    self.column_1.setText("Site Name")

    self.column_2 = QTableWidgetItem()
    self.column_2.setText("Response Time (sec)")

    # Set column
    self.rs_table.setHorizontalHeaderItem(0, self.column_1)
    self.rs_table.setHorizontalHeaderItem(1, self.column_2)

    def rs_on_submit():
      sitename = self.rs_input.text()
      score, data = analyser.compare_ping(sitename)
      for row in data:
        row_number = self.rs_table.rowCount()
        self.rs_table.insertRow(row_number)
        self.rs_table.setItem(
            row_number, 0, QTableWidgetItem(row[0]))
        self.rs_table.setItem(
            row_number, 1, QTableWidgetItem(str(row[1])))

      row_number = self.rs_table.rowCount()
      self.rs_table.insertRow(row_number)
      self.rs_table.setItem(
          row_number, 0, QTableWidgetItem('Score: '))
      self.rs_table.setItem(
          row_number, 1, QTableWidgetItem(str(score)))

      self.rs_input.setText("")
    self.rs_btn_submit.clicked.connect(rs_on_submit)

    self.ui.load_pages.rs_top_layout.addWidget(self.rs_input)
    self.ui.load_pages.rs_btn_layout.addWidget(self.rs_btn_submit)
    self.ui.load_pages.rs_main_layout.addWidget(self.rs_table)

    self.st_btn_submit = PyPushButton(
        text="SpeedTest",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
        bg_color_hover=self.themes["app_color"]["dark_three"],
        bg_color_pressed=self.themes["app_color"]["dark_four"]
    )
    self.st_btn_submit.setMinimumHeight(40)
    self.st_btn_submit.setMaximumWidth(300)

    self.st_lable_download_speed = QLabel(f'Download Speed: _ Mbps')
    self.st_lable_upload_speed = QLabel(f'Upload Speed: _ Mbps')
    self.st_lable_ping = QLabel(f'Ping: _ ms')

    def on_st_btn_submit():
      download_speed, upload_speed, ping = analyser.get_internet_speed()
      self.st_lable_download_speed.setText(
          f'Download Speed: {download_speed} Mbps')
      self.st_lable_upload_speed.setText(f'Upload Speed: {upload_speed} Mbps')
      self.st_lable_ping.setText(f'Ping: {ping} ms')

    self.st_btn_submit.clicked.connect(on_st_btn_submit)
    self.ui.load_pages.st_top_layout.addWidget(self.st_btn_submit)
    self.ui.load_pages.st_top_layout.addWidget(self.st_lable_download_speed)
    self.ui.load_pages.st_top_layout.addWidget(self.st_lable_upload_speed)
    self.ui.load_pages.st_top_layout.addWidget(self.st_lable_ping)

    # DNS
    # ////////////////////////////////////////////////
    self.dns_btn_submit = PyPushButton(
        text="Get Info",
        radius=8,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["dark_one"],
        bg_color_hover=self.themes["app_color"]["dark_three"],
        bg_color_pressed=self.themes["app_color"]["dark_four"]
    )
    self.dns_btn_submit.setMinimumHeight(40)
    self.dns_btn_submit.setMaximumWidth(300)

    self.dns_sitename = PyLineEdit(place_holder_text="Enter domain name")
    self.dns_lable = QTextEdit()

    def on_dns_btn_submit():
      domain_name = self.dns_sitename.text()
      domain_info = analyser.get_domain_info(domain_name)
      print(domain_info)
      self.dns_lable.setText(str(domain_info))
      self.dns_sitename.setText("")

    self.dns_btn_submit.clicked.connect(on_dns_btn_submit)
    self.ui.load_pages.dns_top_layout.addWidget(self.dns_sitename)
    self.ui.load_pages.dns_top_layout.addWidget(self.dns_btn_submit)
    self.ui.load_pages.dns_main_layout.addWidget(self.dns_lable)

    # BTN 2
    # self.left_btn_2 = PyPushButton(
    #     text="Btn With Icon",
    #     radius=8,
    #     color=self.themes["app_color"]["text_foreground"],
    #     bg_color=self.themes["app_color"]["dark_one"],
    #     bg_color_hover=self.themes["app_color"]["dark_three"],
    #     bg_color_pressed=self.themes["app_color"]["dark_four"]
    # )
    # self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
    # self.left_btn_2.setIcon(self.icon)
    # self.left_btn_2.setMaximumHeight(40)
    # self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

  # RESIZE GRIPS AND CHANGE POSITION
  # Resize or change position when window is resized
  # ///////////////////////////////////////////////////////////////

  def resize_grips(self):
    if self.settings["custom_title_bar"]:
      self.left_grip.setGeometry(5, 10, 10, self.height())
      self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
      self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
      self.bottom_grip.setGeometry(
          5, self.height() - 15, self.width() - 10, 10)
      self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
      self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
      self.bottom_right_grip.setGeometry(
          self.width() - 20, self.height() - 20, 15, 15)
