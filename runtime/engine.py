import random
from runtime.environment import Environment
from runtime.cell_actor import CellActor

class SimulationEngine:
    def __init__(self, simulation_node, width=50, height=50):
        self.simulation_node = simulation_node
        self.env = Environment(width, height)
        self.cells = []
        self.tick_count = 0
        self.next_id = 1
        
        # Spawn initial "seed" cells in the center of the grid
        self._spawn_initial_cells()

    def _spawn_initial_cells(self):
        center_x = self.env.width // 2
        center_y = self.env.height // 2
        
        for cell_node in self.simulation_node.cells:
            # Spawn 1 of each defined cell type near the center
            x = center_x + random.randint(-2, 2)
            y = center_y + random.randint(-2, 2)
            self.spawn_cell(cell_node, x, y)
            print(f"[INIT] Spawned {cell_node.name} at ({x}, {y})")

    def spawn_cell(self, cell_node, x, y):
        if self.env.is_within_bounds(x, y):
            new_cell = CellActor(self.next_id, x, y, cell_node)
            self.cells.append(new_cell)
            self.next_id += 1

    def tick(self):
        """Advances the simulation by one unit of time."""
        self.tick_count += 1
        print(f"\n--- Tick {self.tick_count} ---")
        
        dead_cells = set()
        new_cells_to_spawn = []

        # 1. Update all cells and collect their actions
        for cell in self.cells:
            if cell.id in dead_cells:
                continue
                
            actions = cell.update(self.env, self)
            
            # 2. Process actions
            for action in actions:
                act_type = action[0]
                
                if act_type == "DIE":
                    dead_cells.add(cell.id)
                    print(f"[DEATH] {cell.name}_{cell.id} died at ({cell.x}, {cell.y}).")
                    
                elif act_type == "DIVIDE":
                    # Spawn next to parent
                    dx, dy = random.choice([(-1,0), (1,0), (0,-1), (0,1)])
                    new_cells_to_spawn.append((cell.cell_node, cell.x + dx, cell.y + dy))
                    print(f"[DIVIDE] {cell.name}_{cell.id} divided at ({cell.x}, {cell.y}).")
                    
                elif act_type == "MOVE":
                    dx, dy = action[1], action[2]
                    new_x, new_y = cell.x + dx, cell.y + dy
                    if self.env.is_within_bounds(new_x, new_y):
                        cell.x = new_x
                        cell.y = new_y
                        # print(f"[MOVE] {cell.name}_{cell.id} moved to ({cell.x}, {cell.y}).")

                elif act_type == "ATTACK":
                    target_name = action[1]
                    print(f"[ATTACK] {cell.name}_{cell.id} attacked a {target_name}!")
                    # Simplification: Randomly kill a target cell to simulate the attack succeeding
                    targets = [c for c in self.cells if c.name == target_name and c.id not in dead_cells]
                    if targets:
                        victim = random.choice(targets)
                        dead_cells.add(victim.id)
                        print(f"        -> {victim.name}_{victim.id} was destroyed by the attack!")

        # 3. Remove dead cells
        self.cells = [c for c in self.cells if c.id not in dead_cells]

        # 4. Spawn new cells
        for cell_node, nx, ny in new_cells_to_spawn:
            self.spawn_cell(cell_node, nx, ny)
            
        print(f"Total Cells Alive: {len(self.cells)}")

    def run(self, max_ticks=10):
        print("\nStarting Simulation...")
        for _ in range(max_ticks):
            self.tick()
        print("\nSimulation Complete!")
