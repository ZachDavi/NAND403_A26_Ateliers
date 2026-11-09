import maya.cmds as cmds


def run():
    object_selected = cmds.ls(selection=True, transforms=True, long=True)
    if not object_selected:
        cmds.warning("Sélectionne au moins un objet.")
        return

    cmds.undoInfo(openChunk=True)
    try:
        for obj in object_selected:
            cmds.xform(obj, centerPivots=True)
            cmds.makeIdentity(obj, apply=True, translate=True, rotate=True, scale=True, normal=False)
            cmds.delete(obj, constructionHistory=True)
        print("Nettoyage terminé sur {} objet(s).".format(len(object_selected)))
    finally:
        cmds.undoInfo(closeChunk=True)

run()