from PySide6.QtWidgets import QApplication, QDialog


def set_dialog_height(dialog: QDialog) -> None:
    screen = dialog.screen() or QApplication.primaryScreen()
    if screen is None:
        raise RuntimeError("Не удалось определить экран для диалогового окна.")

    height = round(screen.availableGeometry().height() * 0.95)
    dialog.setMinimumHeight(height)
    dialog.resize(dialog.width(), height)
