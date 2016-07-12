import asyncio

from PyQt5 import QtCore
from PyQt5.QtWidgets import QToolBar

class _ToolBar(QToolBar):
    def __init__(self, icon_1, icon_2, parent=None):
        super().__init__(parent)

        self._red_icon = icon_1
        self._green_icon = icon_2

        self.speak_action = self.addAction(self._red_icon, 'speak')
        self.speak_action.triggered.connect(self._change_icon)

    async def _change_to_red(self):
        await asyncio.sleep(3)
        self.speak_action.setIcon(self._red_icon)

    @QtCore.pyqtSlot()
    def _change_icon(self):
        self.speak_action.setIcon(self._green_icon)
        asyncio.ensure_future(self._change_to_red())


def _send_speech_command(messager):
    """
    returns a function which calls the `send_command` function
    that is passed in
    """
    def inner():
        messager.send_command('record')
    return inner

def add_speech_button(main_window, messager):


    status_bar = main_window.status_bar

    # NOTE: in the future, we'd add our own icons
    tool_bar = _ToolBar(status_bar._red_icon,
                        status_bar._green_icon,
                        parent=main_window)

    main_window.addToolBar(QtCore.Qt.LeftToolBarArea, tool_bar)
    # FIXME
    speech_triggered_slot = _send_speech_command(messager)
    tool_bar.speak_action.triggered.connect(speech_triggered_slot)
