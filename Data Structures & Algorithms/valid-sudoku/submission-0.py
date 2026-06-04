class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_len = {}
        hash_breadth = {}
        hash_3_3 = {}

        for i in range(0,9):
            hash_len[i] = board[i]
            for j in range(0,9):
                hash_breadth.setdefault(j, []).append(board[i][j])
                block_num = ((i//3)*3) + (j//3)
                hash_3_3.setdefault(block_num, []).append(board[i][j])

        print(hash_breadth)

        return self._def_validate_hash(hash_len) and self._def_validate_hash(hash_breadth) and self._def_validate_hash(hash_3_3)

    def _def_validate_hash(self, hash_m: Dict):
        for key, value in hash_m.items():
            if key < 0 or key >= 9:
                return False
            seen = []
            for v in value:
                if v != ".":
                    if v in seen:
                        return False
                    seen.append(v)
        return True

