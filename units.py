import define
import copy

class pazzle:
    """ 15パズルの問題自体を表すクラス """

    def __init__(self):
        """ クラス変数の宣言、インスタント作成時に一度のみ実行される """
        self.state = define.init_state
        self.all_move_type = ["up", "down", "left", "right"]
        self.solution = []

    def goal_test(self, state):
        """ 与えられた状態が最終状態ならば真、そうでなければ偽を返す関数 """
        goal_state = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, None]]
        return state == goal_state

    def actions(self, state):
        """ 与えられた状態で実行可能な全ての行為を返す関数 """
        action = self.all_move_type.copy()
        pos_row = [not all(i) for i in state].index(True)
        pos_col = [not i for i in state[pos_row]].index(True)
        if pos_row == 0:
            action.remove("up")
        elif pos_row == 3:
            action.remove("down")
        if pos_col == 0:
            action.remove("left")
        elif pos_col == 3:
            action.remove("right")
        return action

    def result(self, state, action):
        """ 与えられた状態で与えられた行動を実行して得られる状態を返す関数 """
        move_dict = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

        # 場所を交換するための関数内関数
        def swap_position():
            st = copy.deepcopy(state)
            pos_row = [not all(i) for i in state].index(True)
            pos_col = [not i for i in state[pos_row]].index(True)
            st[pos_row][pos_col] = st[pos_row + move_dict[action][0]][pos_col + move_dict[action][1]]
            st[pos_row + move_dict[action][0]][pos_col + move_dict[action][1]] = None
            return st

        return copy.deepcopy(swap_position())

    def cost(self):
        return 1


class Node:
    def __init__(self, state=define.init_state, parent_node=None, action=None, cost=0):
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.cost = cost

    def movement_log(self):
        if self.parent_node is None:
            return []
        return [self.action] + self.parent_node.movement_log()


def child_node(probrem, parent, action):
    return Node(probrem.result(parent.state, action), parent, action, parent.cost + probrem.cost())
