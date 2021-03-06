import bpy

from . import tree, categories, nodes, sockets, operators, handlers


addon_modules = [
    tree,
    sockets,
    nodes,
    categories,
    operators,
    handlers
]


def register():
    bpy.types.Scene.elements_nodes = {}
    for addon_module in addon_modules:
        addon_module.register()


def unregister():
    for addon_module in reversed(addon_modules):
        addon_module.unregister()
    del bpy.types.Scene.elements_nodes
