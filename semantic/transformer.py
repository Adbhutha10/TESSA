from lark import Transformer, v_args
from tessa_ast.nodes import (
    SimulationNode, CellNode, DivideRuleNode, MigrateRuleNode,
    DieRuleNode, AttackRuleNode, ConditionNode
)

@v_args(inline=True)
class TESSATransformer(Transformer):
    
    def start(self, *cell_defs):
        return SimulationNode(cells=list(cell_defs))
    
    def cell_def(self, name, *rules):
        return CellNode(name=str(name), rules=list(rules))
    
    def divide_rule(self, time, unit):
        return DivideRuleNode(time=float(time), unit=str(unit))
    
    def migrate_rule(self, target):
        return MigrateRuleNode(target=str(target))
    
    def die_rule(self, condition):
        return DieRuleNode(condition=condition)
    
    def attack_rule(self, target, condition):
        return AttackRuleNode(target=str(target), condition=condition)
    
    def condition(self, attribute, operator, value):
        return ConditionNode(attribute=str(attribute), operator=str(operator), value=float(value))
    
    # Primitives mapping
    def NUMBER(self, n):
        return float(n)
    
    def CNAME(self, s):
        return str(s)
    
    def TIME_UNIT(self, s):
        return str(s)
