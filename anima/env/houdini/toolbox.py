# -*- coding: utf-8 -*-
# Copyright (c) 2012-2018, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

from anima.ui.lib import QtCore, QtWidgets


def ui():
    """returns the widget to Houdini
    """
    root_widget = QtWidgets.QWidget()
    tlb = ToolboxLayout()
    root_widget.setLayout(tlb)
    return root_widget


def add_button(label, layout, callback, tooltip=''):
    """A wrapper for button creation

    :param label: The label of the button
    :param layout: The layout that the button is going to be placed under.
    :param callback: The callable that will be called when the button is
      clicked.
    :param str tooltip: Optional tooltip for the button
    :return:
    """
    # button
    button = QtWidgets.QPushButton()
    button.setText(label)
    layout.addWidget(button)

    button.setToolTip(tooltip)

    # Signal
    QtCore.QObject.connect(
        button,
        QtCore.SIGNAL("clicked()"),
        callback
    )

    return button


class ToolboxLayout(QtWidgets.QVBoxLayout):
    """The toolbox
    """

    def __init__(self, *args, **kwargs):
        super(ToolboxLayout, self).__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        """add tools
        """
        # create the main tab layout
        main_tab_widget = QtWidgets.QTabWidget(self.widget())
        self.addWidget(main_tab_widget)

        # add the General Tab
        general_tab_widget = QtWidgets.QWidget(self.widget())
        general_tab_vertical_layout = QtWidgets.QVBoxLayout()
        general_tab_widget.setLayout(general_tab_vertical_layout)

        main_tab_widget.addTab(general_tab_widget, 'Generic')

        # Create tools for general tab

        # -------------------------------------------------------------------
        # Version Creator
        add_button(
            'Version Creator',
            general_tab_vertical_layout,
            GenericTools.version_creator,
            GenericTools.version_creator.__doc__
        )

        add_button(
            'Browse $HIP',
            general_tab_vertical_layout,
            GenericTools.browse_hip,
            GenericTools.browse_hip.__doc__
        )

        # Copy Path
        add_button(
            'Copy Node Path',
            general_tab_vertical_layout,
            GenericTools.copy_node_path,
            GenericTools.copy_node_path.__doc__
        )

        # Range from shot
        add_button(
            'Range From Shot',
            general_tab_vertical_layout,
            GenericTools.range_from_shot,
            GenericTools.range_from_shot.__doc__
        )

        # -------------------------------------------------------------------
        # Add the stretcher
        general_tab_vertical_layout.addStretch()


class GenericTools(object):
    """Generic Tools
    """

    @classmethod
    def version_creator(cls):
        """version creator
        """
        from anima.ui.scripts import houdini
        houdini.version_creator()

    @classmethod
    def browse_hip(cls):
        """browse HIP folder
        """
        from anima.utils import open_browser_in_location
        import os
        hip = os.environ.get('HIP')
        if hip:
            open_browser_in_location(hip)

    @classmethod
    def copy_node_path(cls):
        """copies path to clipboard
        """
        import hou
        node = hou.selectedNodes()[0]
        hou.ui.copyTextToClipboard(node.path())

    @classmethod
    def range_from_shot(cls):
        """sets the playback range from the related shot item
        """
        from anima.env import houdini
        h = houdini.Houdini()
        v = h.get_current_version()
        if not v:
            print('no v, returning!')
            return

        from stalker import Shot
        if not v.task.parent or not isinstance(v.task.parent, Shot):
            return

        shot = v.task.parent
        h.set_frame_range(shot.cut_in, shot.cut_out)