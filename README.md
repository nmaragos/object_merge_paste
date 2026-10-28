# Object Merge Paste for Houdini

A small Houdini shelf tool that creates an **Object Merge** SOP from copied SOP nodes.

## Install

1. In Houdini, add a **New Tool** in a shelf of your choice.
2. Name the tool `Object Merge Paste`, or however you like.
3. On the **Script** tab, set the language to **Python** and paste the contents of the accompanying Python script.
4. On the **Hotkeys** tab, assign a shortcut in the **Network Editor** context—for example, `Ctrl+Shift+V`.
5. Save the tool.

## Usage

1. Select one or more SOP nodes (such as a Null) and press `Ctrl+C` to copy.
2. Enter the target SOP network.
3. Position the mouse cursor where the new nodes should appear.
4. Paste by pressing the shortcut assigned or clicking the tool button in the shelf.

The tool creates one Object Merge per copied node and sets each node's **Object 1** path automatically.

## Notes

- Run the tool inside a SOP network; it will not create Object Merge nodes in OBJ, LOP, or other contexts.
- The source nodes may be in another geometry network.
