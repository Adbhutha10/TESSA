import random
from tessa_ast.nodes import DivideRuleNode, MigrateRuleNode, DieRuleNode, AttackRuleNode

class CellActor:
    def __init__(self, id, x, y, cell_node):
        self.id = id
        self.x = x
        self.y = y
        self.cell_node = cell_node
        self.name = cell_node.name
        self.time_alive = 0.0

    def evaluate_condition(self, condition_node, env, engine):
        """Evaluates a ConditionNode against the environment or other cells."""
        # For simplicity, we currently only check global environment variables
        # Future enhancement: checking distance to nearest 'target' cell
        val = env.get_attribute(condition_node.attribute)
        
        # If attribute wasn't in environment, maybe it's 'distance'? 
        # (Very simplified logic for Phase 2)
        if condition_node.attribute == "distance":
            # Just mock a random distance for now to test the attack rule
            val = random.uniform(0, 10)

        target_val = condition_node.value

        if condition_node.operator == "<":
            return val < target_val
        elif condition_node.operator == ">":
            return val > target_val
        elif condition_node.operator == "==":
            return val == target_val
        return False

    def update(self, env, engine):
        """
        Called every simulation tick.
        Returns a list of 'actions' (intents) the cell wants to perform.
        """
        self.time_alive += 1.0
        actions = []

        for rule in self.cell_node.rules:
            if isinstance(rule, DieRuleNode):
                if self.evaluate_condition(rule.condition, env, engine):
                    actions.append(("DIE",))
                    return actions # Immediately stop processing if dead

            elif isinstance(rule, DivideRuleNode):
                # Assuming 1 tick = 1 hour for now
                if self.time_alive >= rule.time:
                    actions.append(("DIVIDE",))
                    self.time_alive = 0.0 # Reset timer

            elif isinstance(rule, MigrateRuleNode):
                # Random walk simplification
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                actions.append(("MOVE", dx, dy))

            elif isinstance(rule, AttackRuleNode):
                if self.evaluate_condition(rule.condition, env, engine):
                    actions.append(("ATTACK", rule.target))

        return actions
