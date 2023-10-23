# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Adw.Flap()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Adw.Flap()')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_child(child=vbox)

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        # Botão que abre e fecha o Flap.
        flap_Toggle_button = Gtk.ToggleButton.new()
        flap_Toggle_button.set_icon_name(icon_name='sidebar-show-right-rtl-symbolic')
        flap_Toggle_button.connect('clicked', self.on_flap_button_toggled)
        headerbar.pack_start(child=flap_Toggle_button)

        self.adw_flap = Adw.Flap.new()
        self.adw_flap.set_reveal_flap(reveal_flap=False)
        self.adw_flap.set_locked(locked=True)

        vbox.append(child=self.adw_flap)

        stack = Gtk.Stack.new()
        self.adw_flap.set_content(content=stack)

        # Página 1
        box_page_1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_1, name='page1', title='Page 1')

        label_page_1 = Gtk.Label.new(str='Page 1')
        label_page_1.set_halign(align=Gtk.Align.CENTER)
        label_page_1.set_valign(align=Gtk.Align.CENTER)
        label_page_1.set_hexpand(expand=True)
        label_page_1.set_vexpand(expand=True)
        box_page_1.append(child=label_page_1)

        # Página 2
        box_page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_2, name='Page 1', title='Page 2')

        label_page_2 = Gtk.Label.new(str='Page 2')
        label_page_2.set_halign(align=Gtk.Align.CENTER)
        label_page_2.set_valign(align=Gtk.Align.CENTER)
        label_page_2.set_hexpand(expand=True)
        label_page_2.set_vexpand(expand=True)
        box_page_2.append(child=label_page_2)

        # StackSidebar gerencia a troca entre os stack.
        stack_sidebar = Gtk.StackSidebar.new()
        stack_sidebar.set_stack(stack=stack)
        self.adw_flap.set_flap(flap=stack_sidebar)

    def on_flap_button_toggled(self, widget):
        self.adw_flap.set_reveal_flap(not self.adw_flap.get_reveal_flap())


class Application(Adw.Application):

    def __init__(self):
        super().__init__(application_id='io.example.xomrkob',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)