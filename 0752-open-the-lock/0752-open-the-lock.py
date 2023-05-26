class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
 
        queue = deque()
        visited = set(deadends)
        queue.append(('0000', 0))

        while queue:
            state, turns = queue.popleft()

            if state == target:
                return turns

            if state in visited:
                continue

            visited.add(state)

            for i in range(4):
                digit = int(state[i])

                # Rotate digit clockwise
                next_state_cw = state[:i] + str((digit + 1) % 10) + state[i + 1:]
                queue.append((next_state_cw, turns + 1))

 
                next_state_ccw = state[:i] + str((digit - 1) % 10) + state[i + 1:]
                queue.append((next_state_ccw, turns + 1))

        return -1

