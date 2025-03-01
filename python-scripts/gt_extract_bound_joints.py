"""
GT Extract Bound Joints - Extract or Transfer bound joints
github.com/TrevisanGMW/gt-tools - 2022-06-22

0.0.1 - 2022-06-22
Core function

0.0.2 - 2022-07-14
Added GUI

Todo:
    Add Transfer functions
    Create checkboxes for settings
    Write help menu

"""
from maya import OpenMayaUI as OpenMayaUI
import maya.cmds as cmds
import logging
import sys

try:
    from shiboken2 import wrapInstance
except ImportError:
    from shiboken import wrapInstance

try:
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import QWidget
except ImportError:
    from PySide.QtGui import QIcon, QWidget

# Logging Setup
logging.basicConfig()
logger = logging.getLogger("gt_extract_bound_joints")
logger.setLevel(logging.INFO)

# Script Name
script_name = "GT - Extract Bound Joints"

# Version
script_version = "0.0.2"

# Settings
extract_joints_settings = {'filter_non_existent': True,
                           'include_mesh': True,
                           }


# Function for the "Run Code" button
def run_output_code(out):
    try:
        exec(out)
    except Exception as e:
        cmds.warning("Something is wrong with your code!")
        cmds.warning(e)


# Main Window ============================================================================
def build_gui_extract_bound_joints():
    window_name = "build_gui_extract_bound_joints"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    # Main GUI Start Here =================================================================================
    window_gui_extract_bound_joints = cmds.window(window_name, title=script_name + '  (v' + script_version + ')',
                                                  titleBar=True, mnb=False, mxb=False, sizeable=True)

    cmds.window(window_name, e=True, s=True, wh=[1, 1])

    content_main = cmds.columnLayout(adj=True)

    # Title
    title_bgc_color = (.4, .4, .4)
    cmds.separator(h=10, style='none')  # Empty Space
    cmds.rowColumnLayout(nc=1, cw=[(1, 500)], cs=[(1, 10)], p=content_main)  # Window Size Adjustment
    cmds.rowColumnLayout(nc=3, cw=[(1, 10), (2, 425), (3, 50)], cs=[(1, 10), (2, 0), (3, 0)],
                         p=content_main)  # Title Column
    cmds.text(" ", bgc=title_bgc_color)  # Tiny Empty Green Space
    cmds.text(script_name, bgc=title_bgc_color, fn="boldLabelFont", align="left")
    cmds.button(l="Help", bgc=title_bgc_color, c=lambda x: build_gui_help_extract_bound_joints())
    cmds.separator(h=10, style='none', p=content_main)  # Empty Space

    # Body ====================
    cmds.rowColumnLayout(nc=1, cw=[(1, 500)], cs=[(1, 10)], p=content_main)
    cmds.rowColumnLayout(nc=1, cw=[(1, 500)], cs=[(1, 10)])
    cmds.rowColumnLayout(nc=1, cw=[(1, 470)], cs=[(1, 0)])
    cmds.separator(h=10, style='none')  # Empty Space
    cmds.button(l="Extract Bound Joints", bgc=(.6, .6, .6), c=lambda x: _btn_extract_python_curve_shape())
    cmds.separator(h=10, style='none', p=content_main)  # Empty Space
    cmds.separator(h=10, p=content_main)

    # Bottom ====================
    cmds.rowColumnLayout(nc=1, cw=[(1, 490)], cs=[(1, 10)], p=content_main)
    cmds.text(label='Output - Selection Command:')
    output_python = cmds.scrollField(editable=True, wordWrap=True)
    cmds.separator(h=10, style='none')  # Empty Space
    cmds.button(l="Run Code", c=lambda x: run_output_code(cmds.scrollField(output_python, query=True, text=True)))
    cmds.separator(h=10, style='none')  # Empty Space

    def _btn_extract_python_curve_shape():
        selection = cmds.ls(selection=True) or []

        if len(selection) == 0:
            cmds.warning('Nothing selected. Please select a bound mesh and try again.')
            return

        valid_nodes = []
        for sel in selection:
            shapes = cmds.listRelatives(sel, shapes=True, children=False) or []
            if shapes:
                if cmds.objectType(shapes[0]) == 'mesh' or cmds.objectType(shapes[0]) == 'nurbsSurface':
                    valid_nodes.append(sel)

        commands = []
        for transform in valid_nodes:
            message = '# Joint influences found in "' + transform + '":'
            message += '\nbound_list = '
            bound_joints = get_bound_joints(transform)

            if extract_joints_settings.get('include_mesh'):
                bound_joints.insert(0, transform)

            message += str(bound_joints)

            if extract_joints_settings.get('filter_non_existent'):
                message += '\nbound_list = [jnt for jnt in bound_list if cmds.objExists(jnt)]'

            message += '\ncmds.select(bound_list)'

            commands.append(message)

        cmds.scrollField(output_python, edit=True, wordWrap=True, text='', sl=True)
        command = ''
        for cmd in commands:
            command += cmd + '\n\n'

        print('#' * 80)
        print(command)
        print('#' * 80)

        cmds.scrollField(output_python, edit=True, wordWrap=True, text=command, sl=True)
        cmds.scrollField(output_python, e=True, ip=1, it='')  # Bring Back to the Top
        cmds.setFocus(output_python)

    # Show and Lock Window
    cmds.showWindow(window_gui_extract_bound_joints)
    cmds.window(window_name, e=True, s=False)

    # Set Window Icon
    qw = OpenMayaUI.MQtUtil.findWindow(window_name)
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(':/smoothSkin.png')
    widget.setWindowIcon(icon)

    # Main GUI Ends Here =================================================================================


# Creates Help GUI
def build_gui_help_extract_bound_joints():
    window_name = "build_gui_help_extract_bound_joints"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    cmds.window(window_name, title=script_name + " Help", mnb=False, mxb=False, s=True)
    cmds.window(window_name, e=True, s=True, wh=[1, 1])

    cmds.columnLayout("main_column", p=window_name)

    # Title Text
    cmds.separator(h=12, style='none')  # Empty Space
    cmds.rowColumnLayout(nc=1, cw=[(1, 310)], cs=[(1, 10)], p="main_column")  # Window Size Adjustment
    cmds.rowColumnLayout(nc=1, cw=[(1, 300)], cs=[(1, 10)], p="main_column")  # Title Column
    cmds.text(script_name + " Help", bgc=[.4, .4, .4], fn="boldLabelFont", align="center")
    cmds.separator(h=10, style='none', p="main_column")  # Empty Space

    # Body ====================
    cmds.rowColumnLayout(nc=1, cw=[(1, 300)], cs=[(1, 10)], p="main_column")
    cmds.text(l='This script generates the Python code necessary to select\nall joints influencing a skinCluster node',
              align="left")
    cmds.separator(h=10, style='none')  # Empty Space
    cmds.text(l='"Extract Bound Joints" button:', align="left", fn="boldLabelFont")
    cmds.text(l='Outputs the python code necessary to reselect the joints', align="left")
    cmds.text(l='inside the "Output Python Curve" box.', align="left")
    cmds.separator(h=15, style='none')  # Empty Space
    cmds.text(l='Run Code:', align="left", fn="boldLabelFont")
    cmds.text(l='Attempts to run the code (or anything written) inside ', align="left")
    cmds.text(l='"Output Python Curve" box', align="left")
    cmds.separator(h=15, style='none')  # Empty Space
    cmds.rowColumnLayout(nc=2, cw=[(1, 140), (2, 140)], cs=[(1, 10), (2, 0)], p="main_column")
    cmds.text('Guilherme Trevisan  ')
    cmds.text(l='<a href="mailto:trevisangmw@gmail.com">TrevisanGMW@gmail.com</a>', hl=True, highlightColor=[1, 1, 1])
    cmds.rowColumnLayout(nc=2, cw=[(1, 140), (2, 140)], cs=[(1, 10), (2, 0)], p="main_column")
    cmds.separator(h=15, style='none')  # Empty Space
    cmds.text(l='<a href="https://github.com/TrevisanGMW">Github</a>', hl=True, highlightColor=[1, 1, 1])
    cmds.separator(h=7, style='none')  # Empty Space

    # Close Button
    cmds.rowColumnLayout(nc=1, cw=[(1, 300)], cs=[(1, 10)], p="main_column")
    cmds.separator(h=10, style='none')
    cmds.button(l='OK', h=30, c=lambda args: close_help_gui())
    cmds.separator(h=8, style='none')

    # Show and Lock Window
    cmds.showWindow(window_name)
    cmds.window(window_name, e=True, s=False)

    # Set Window Icon
    qw = OpenMayaUI.MQtUtil.findWindow(window_name)
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(':/question.png')
    widget.setWindowIcon(icon)

    def close_help_gui():
        if cmds.window(window_name, exists=True):
            cmds.deleteUI(window_name, window=True)


def get_bound_joints(obj):
    """
    Gets a list of joints bound to the skin cluster of the object
    Args:
        obj: Name of the object to extract joints from (must contain a skinCluster node)

    Returns:
        joints (list): List of joints bound to this object
    """
    if not cmds.objExists(obj):
        logger.warning('Object "' + obj + '" was not found in the scene.')
        return

    history = cmds.listHistory(obj) or []
    skin_clusters = cmds.ls(history, type='skinCluster') or []

    if len(skin_clusters) != 0:
        skin_cluster = skin_clusters[0]
    else:
        logger.debug('history: ', str(history))
        logger.debug('skin_clusters: ', str(skin_clusters))
        logger.warning('Object "' + obj + "\" doesn't seem to be bound to any joints.")
        return

    connections = cmds.listConnections(skin_cluster + '.influenceColor') or []
    joints = []
    for obj in connections:
        if cmds.objectType(obj) == 'joint':
            joints.append(obj)
    return joints


if __name__ == '__main__':
    build_gui_extract_bound_joints()
