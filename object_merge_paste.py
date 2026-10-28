import hou


def report(message):
    hou.ui.setStatusMessage(message, severity=hou.severityType.Error)


def find_network_editor(kwargs):
    for pane in (
        hou.ui.paneTabUnderCursor(),
        kwargs.get("pane"),
        hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor),
    ):
        if isinstance(pane, hou.NetworkEditor):
            return pane
    return None


def main(kwargs):
    pane = find_network_editor(kwargs)
    if pane is None:
        return report("Paste Object Merge: no Network Editor is open.")

    parent = pane.pwd()
    if parent.childTypeCategory() != hou.sopNodeTypeCategory():
        return report("Paste Object Merge: run this inside a SOP network.")

    sources = [hou.node(p) for p in hou.ui.getTextFromClipboard().split()]
    sources = [n for n in sources if n is not None]
    if not sources:
        return report("Paste Object Merge: copy one or more SOP nodes first.")

    # Hotkey places at cursor; shelf click uses the center of the visible area.
    position = (pane.cursorPosition() if pane.isUnderCursor()
                else pane.visibleBounds().center())

    with hou.undos.group("Paste Object Merge"):
        for i, source in enumerate(sources):
            merge = parent.createNode("object_merge", "merge_" + source.name())
            merge.parm("objpath1").set(source.path())
            merge.setPosition(position + hou.Vector2(i * 2, 0))
            merge.setSelected(True, clear_all_selected=(i == 0))


main(kwargs)
