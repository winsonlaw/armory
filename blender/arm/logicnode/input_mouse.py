import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class MouseNode(Node, ArmLogicTreeNode):
    '''Mouse node'''
    bl_idname = 'LNMergedMouseNode'
    bl_label = 'Mouse'
    bl_icon = 'NONE'
    property0: EnumProperty(
        items = [('Down', 'Down', 'Down'),
                 ('Started', 'Started', 'Started'),
                 ('Released', 'Released', 'Released'),
                 ('Moved', 'Moved', 'Moved')],
        name='', default='Down')
    property1: EnumProperty(
        items = [('left', 'left', 'left'),
                 ('right', 'right', 'right'),
                 ('middle', 'middle', 'middle')],
        name='', default='left')
    
    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.outputs.new('NodeSocketBool', 'State')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
        layout.prop(self, 'property1')

add_node(MouseNode, category='Input')
