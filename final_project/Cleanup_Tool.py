import maya.cmds as cmds
import maya.mel as mel
def display(obj):
    """This function freezes transformations, centers the pivot,
    deletes the history and lastly delete unused texturenodes"""
    maya.cmds.FreezeTransformations()
    maya.cmds.CenterPivot()
    maya.cmds.DeleteHistory()
    mel.eval('MLdeleteUnused;')
    selection = cmds.ls(sl=True);
"""this variable is what is being selected"""    
selection = maya.cmds.ls(sl=True);
"""this runs the function and tells it to run on the selection"""
display(selection[0])