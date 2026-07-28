class WaterJugProblem():
    def dfs(self, jug1, jug2, path=[]):
        if (jug1, jug2) in self.visited:
            return False
        
        self.visited.add((jug1, jug2))
        path.append((jug1, jug2))

        if jug1 == self.target or jug2 == self.target:
            print("Target reached!")
            print("Path to solution:", path)
            return True

        operations = [
            (self.jug1_capacity, jug2),  # Fill jug1
            (jug1, self.jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (min(jug1 + jug2, self.jug1_capacity), jug2 - (min(jug1 + jug2, self.jug1_capacity) - jug1)),  # Pour jug2 into jug1
            (jug1 - (min(jug1 + jug2, self.jug2_capacity) - jug2), min(jug1 + jug2, self.jug2_capacity))  # Pour jug1 into jug2
        ]

        for op in operations:
            if self.dfs(op[0], op[1], path[:]):
                return True

        return False
p = WaterJugProblem(4, 3, 2)
if not p.dfs(0, 0): print("Target cannot be reached!")


