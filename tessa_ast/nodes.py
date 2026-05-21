from dataclasses import dataclass, field
from typing import List, Union

@dataclass
class RuleNode:
    """Base class for all rules."""
    pass

@dataclass
class ConditionNode:
    attribute: str
    operator: str
    value: float

@dataclass
class DivideRuleNode(RuleNode):
    time: float
    unit: str

@dataclass
class MigrateRuleNode(RuleNode):
    target: str

@dataclass
class DieRuleNode(RuleNode):
    condition: ConditionNode

@dataclass
class AttackRuleNode(RuleNode):
    target: str
    condition: ConditionNode

@dataclass
class CellNode:
    name: str
    rules: List[RuleNode] = field(default_factory=list)

@dataclass
class SimulationNode:
    cells: List[CellNode] = field(default_factory=list)
