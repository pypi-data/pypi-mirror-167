# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: MIT


from functools import lru_cache
from typing import List, Union
from pyvis.network import Network # see also https://visjs.org/
from pathlib import Path
import webbrowser
from collections import deque


class TreeNode:
    def __init__(self, val: Union[float, int, str] = None, shape: str = "ellipse", color: str = None, **options):
        self.val = val
        self.children = []
        self.grandchildren = []
        self.shape = shape
        self.color = color
        self.options = options

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class tree(object):
    def __init__(self, data: List[Union[float, int, str]] = [], *args, **kwargs):
        """
        https://en.wikipedia.org/wiki/Binary_tree#Arrays
        "Binary trees can also be stored in breadth-first order as an implicit data structure in arrays"
        """
        super().__init__(*args, **kwargs)
        self.treetype = 'Tree'
        self.root = None
        
    def __repr__(self) -> str:
        if self.root:
            return f"TreeNode({self.root.val})"

    def tree_traversals_summary(self):
      self.root = TreeNode('Tree Traversals')
      node_DFS = TreeNode('Depth-First Search\n(DFS)')
      node_BFS = TreeNode('Breadth-First Search\n(BFS)')
      node_BFS_iteration = TreeNode('BFS\nIteration w/ queue')
      node_BFS.children.extend([node_BFS_iteration,])
      node_preorder = TreeNode('Preorder')
      node_inorder = TreeNode('Inorder')
      node_postorder = TreeNode('Postorder')
      node_preorder_iteration = TreeNode('Preorder\nIteration w/ stack')
      node_preorder_recursion = TreeNode('Preorder\nRecursion')
      node_preorder_morris = TreeNode('Preorder\nMorris')
      node_inorder_iteration = TreeNode('Inorder\nIteration w/ stack')
      node_inorder_recursion = TreeNode('Inorder\nRecursion')
      node_inorder_morris = TreeNode('Inorder\nMorris')
      node_postorder_iteration = TreeNode('Postorder\nIteration w/ stack')
      node_postorder_recursion = TreeNode('Postorder\nRecursion')
      node_postorder_morris = TreeNode('Postorder\nMorris')
      node_preorder.children.extend([node_preorder_iteration, node_preorder_recursion, node_preorder_morris])
      node_inorder.children.extend([node_inorder_iteration, node_inorder_recursion, node_inorder_morris])
      node_postorder.children.extend([node_postorder_iteration, node_postorder_recursion, node_postorder_morris])
      node_DFS.children.extend([node_preorder, node_inorder, node_postorder])
      self.root.children.extend([node_DFS, node_BFS])
      self.show(heading='Tree Traversals')

    def disjoint_set(self):
      self.quick_find = TreeNode('Quick Find', shape='text')
      self.quick_union = TreeNode('Quick Union', shape='text')
      self.union_by_rank = TreeNode('Union by Rank', shape='text')
      self.path_compression = TreeNode('Path Compression', shape='text')
      self.optimized = TreeNode('Optimized (Path Compression + Union by Rank)', shape='text')
      self.quick_find.children.append(self.quick_union)
      self.quick_union.children.append(self.union_by_rank)
      self.union_by_rank.children.append(self.path_compression)
      self.path_compression.children.append(self.optimized)
      self.root = self.quick_find
      self.show(heading="Disjoint Set (Union-Find) Data Structure")

    def binary_tree_traversal(self):
      self.root = TreeNode('Binary Tree Traversal', shape='text')
      self.DFS = TreeNode('DFS', shape='text')
      self.BFS = TreeNode('BFS', shape='text')
      self.BFS_levelorder = TreeNode('Level Order', shape='text')
      self.BFS_uses = TreeNode('Usage: Guaranteed to find a solution within specific levels in a chess game', shape='text')
      self.BFS_recursion = TreeNode('Recursion [Easy]', shape='text')
      self.BFS_recursion_details = TreeNode("""\
def DFS(curr, level = 0):
    if curr:
        if len(res) == level:
            res.append([])
        res[level].append(curr.val)
        DFS(curr.left, level+1)
        DFS(curr.right, level+1)
res = []
DFS(root)
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.BFS_iteration = TreeNode('Iteration [Medium]', shape='text')
      self.BFS_iteration_details = TreeNode("""\
res = []
if not root:
    return res
else:
    queue = [root]
level = 0
while queue:
    res.append([])
    n = len(queue)
    for i in range(n):
        curr = queue.pop()
        res[level].append(curr.val)
        if curr.left:
            queue.insert(0, curr.left)
        if curr.right:
            queue.insert(0, curr.right)
    level += 1
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.BFS_recursion_complexity = TreeNode("""\
Time Complexity: O(|V|+|E|)
Space Complexity: O(|V|+|E|)""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'}, color='#FFA500')
      self.BFS_iteration_complexity = TreeNode("""\
Time Complexity: O(|V|+|E|)
Space Complexity: O(|V|)""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'}, color='#FFA500')
      self.BFS.children.append(self.BFS_levelorder)
      self.BFS_levelorder.children.append(self.BFS_uses)
      self.BFS_uses.children.append(self.BFS_recursion)
      self.BFS_uses.children.append(self.BFS_iteration)
      self.BFS_recursion.children.append(self.BFS_recursion_details)
      self.BFS_iteration.children.append(self.BFS_iteration_details)
      self.BFS_recursion_details.children.append(self.BFS_recursion_complexity)
      self.BFS_iteration_details.children.append(self.BFS_iteration_complexity)
      self.preorder = TreeNode('Preorder (*Root* -> Left Subtree -> Right Subtree)', shape='text')
      self.preorder_uses = TreeNode('Usage: Copy of the tree', shape='text')
      self.inorder = TreeNode('Inorder (Left Subtree -> *Root* -> Right Subtree)', shape='text')
      self.inorder_uses = TreeNode('Usage: Nodes of BST in non-decreasing order', shape='text')
      self.inorder_recursion = TreeNode('Recursion [Easy]', shape='text')
      self.inorder_recursion_details = TreeNode("""\
def DFS(curr):
    if curr:
        DFS(curr.left)
        res.append(curr.val)
        DFS(curr.right)
res = []
DFS(root)
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.inorder_iteration = TreeNode('Iteration [Medium]', shape='text')
      self.inorder_iteration_details = TreeNode("""\
res = []
curr, stack = root, []
while True:
    if curr:
        stack.append(curr)
        curr = curr.left
    elif stack:
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    else:
        break
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.O_of_n_complexity = TreeNode("""\
Time Complexity: O(n)
Space Complexity: O(n)""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'}, color='#FFA500')
      self.preorder_recursion = TreeNode('Recursion [Easy]', shape='text')
      self.preorder_recursion_details = TreeNode("""\
def DFS(curr):
    if curr:
        res.append(curr.val)
        DFS(curr.left)
        DFS(curr.right)
res = []
DFS(root)
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.preorder_iteration = TreeNode('Iteration [Medium]', shape='text')
      self.preorder_iteration_details = TreeNode("""\
res = []
if root:
    stack = [root,]
else:
    return res
while True:
    if stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    else:
        break
return res""", shape='box', font={'face': 'Monospace', 'align': 'left', 'size': '22'})
      self.root.children.append(self.DFS)
      self.root.children.append(self.BFS)
      self.DFS.children.append(self.preorder)
      self.DFS.children.append(self.inorder)
      self.preorder.children.append(self.preorder_uses)
      self.inorder.children.append(self.inorder_uses)
      self.inorder_uses.children.append(self.inorder_recursion)
      self.inorder_recursion.children.append(self.inorder_recursion_details)
      self.inorder_uses.children.append(self.inorder_iteration)
      self.inorder_iteration.children.append(self.inorder_iteration_details)
      self.preorder_uses.children.append(self.preorder_recursion)
      self.preorder_recursion.children.append(self.preorder_recursion_details)
      self.preorder_uses.children.append(self.preorder_iteration)
      self.preorder_iteration.children.append(self.preorder_iteration_details)
      self.inorder_recursion_details.children.append(self.O_of_n_complexity)
      self.inorder_iteration_details.children.append(self.O_of_n_complexity)
      self.preorder_recursion_details.children.append(self.O_of_n_complexity)
      self.preorder_iteration_details.children.append(self.O_of_n_complexity)
      self.show(heading='Tree Traversal', nodeDistance=500, height='90%', levelSeparation=300)

    def validate_IP_address(self):
      self.root = TreeNode('IP string', shape = 'text')
      level1_three_dots = TreeNode('Contains 3 dots', shape='text')
      level1_seven_colons = TreeNode('Contains 7 colons', shape='text')
      level1_neither = TreeNode('Otherwise, return \"Neither\"', shape='text')
      level2_ip4_validate = TreeNode('Validate each \"IPv4\" chunk', shape='text')
      level3_ip4_valid = TreeNode('Valid, return \"IPv4\"', shape='text')
      level3_ip4_invalid = TreeNode('Invalid, return \"Neither\"', shape='text')
      level2_ip6_validate = TreeNode('Validate each \"IPv6\" chunk', shape='text')
      level3_ip6_valid = TreeNode('Valid, return \"IPv6\"', shape='text')
      level3_ip6_invalid = TreeNode('Invalid, return \"Neither\"', shape='text')
      level2_ip4_validate.children.extend([level3_ip4_valid, level3_ip4_invalid])
      level2_ip6_validate.children.extend([level3_ip6_valid, level3_ip6_invalid])
      level1_three_dots.children.extend([level2_ip4_validate])
      level1_seven_colons.children.extend([level2_ip6_validate])
      self.root.children.extend([level1_three_dots, level1_seven_colons, level1_neither])
      self.show(heading='Validate IP Address')

    def decode_ways(self, s: str = "11106") -> int:
      """
      The original question: https://leetcode.com/problems/decode-ways/
      """
      def decode(start: int = 0, parent: TreeNode = None, msg: str = ''):
        nonlocal count, success
        if start == len(s): # reach the end
          curr_node = TreeNode(val=f"Successful\n\"{msg}\"", color='lightgreen')
          parent.children.append(curr_node)
          success += 1
        else:
          making_progress = False
          # try to decode single digit
          if int(s[start]) != 0:
            curr_node = TreeNode(val=f"#{count}. \"{s[start]}\"=\"{chr(64+int(s[start]))}\";\nleft=\"{s[start+1:]}\"")
            count += 1
            parent.children.append(curr_node)
            decode(start+1, curr_node, msg+chr(64+int(s[start])))
            making_progress = True
          # try to decode two digits
          if s[start] != '0' and start < len(s)-1: # allows 2 digit
            if int(s[start:start+2]) <= 26:
              curr_node = TreeNode(val=f"#{count}. \"{s[start:start+2]}\"=\"{chr(64+int(s[start:start+2]))}\";\nleft=\"{s[start+2:]}\"")
              count += 1
              parent.children.append(curr_node)
              decode(start+2, curr_node, msg+chr(64+int(s[start:start+2])))
              making_progress = True
          # not making progress
          if not making_progress:
            curr_node = TreeNode(val=f"Unsuccessful", color='orange')
            parent.children.append(curr_node)
      success = 0
      count = 0
      self.root = TreeNode(val=f"#{count}. left=\"{s}\"")
      count += 1
      decode(0, self.root)
      self.show(heading=f'DFS Search Tree to Decode \"{s}\" Into Letters (Result: {success} Successful Ways)')

    def word_break_DFS(self, s: str = "catsandog", wordDict: List[str] = ["cats", "dog", "sand", "and", "cat"]) -> bool:
      """
      The original question: https://leetcode.com/problems/word-break/
      """
      def is_breakable_DFS(start: int = 0, parent: TreeNode = None):
        nonlocal count
        if start == n:
          curr_node = TreeNode(val=f"#{count}. True", color='lightgreen')
          parent.children.append(curr_node)
          return True
        for end in range(start, n):
            substring = s[start:end+1]
            curr_node = TreeNode(val=f"#{count}. {substring}")
            count += 1
            parent.children.append(curr_node)
            if s[start:end+1] in wordset and is_breakable_DFS(end+1, parent=curr_node):
              return True
        return False
      n = len(s)
      wordset = set(wordDict)
      count = 0
      self.root = TreeNode(val=f"#{count}. {s}")
      count += 1
      res = is_breakable_DFS(start = 0, parent = self.root)
      self.show(heading='DFS Search Space for Word Break')
      return res

    def word_break_BFS(self, s: str = "catsandog", wordDict: List[str] = ["cats", "dog", "sand", "and", "cat"]) -> bool:
      """
      https://leetcode.com/problems/word-break/
      """
      count = 0
      self.root = TreeNode(val=f"#{count}.")
      count += 1
      n = len(s)
      word_set = set(wordDict)
      start_idx_queue = deque()
      start_idx_visited = set()
      start_idx_queue.append((0, self.root))
      res = False
      while start_idx_queue:
        (start, parent_node) = start_idx_queue.popleft()
        if start in start_idx_visited:
          continue
        for end in range(start, n):
          if s[start:end+1] in word_set:
            curr_node = TreeNode(val=f"#{count}. {s[start:end+1]}")
            count += 1
            parent_node.children.append(curr_node)
            start_idx_queue.append((end+1, curr_node))
            if end == n-1:
              leaf_node = TreeNode(val=f"#{count}. True", color='lightgreen')
              curr_node.children.append(leaf_node)
              res = True
              break
        start_idx_visited.add(start)
      self.show(heading='BFS Search Space for Word Break')
      return res

    def Fibonacci_numbers(self, n=5, a=[0, 1], symbol="F", heading="Fibonacci Numbers", distinct=False):
      self.Fibonacci_numbers_generalized(n=n, a=a, symbol=symbol, heading=heading, distinct=distinct)

    def Lucas_numbers(self, n=5, a=[2, 1], symbol="L", heading="Lucas Numbers", distinct=False):
      self.Fibonacci_numbers_generalized(n=n, a=a, symbol=symbol, heading=heading, distinct=distinct)
    
    def Tribonacci_numbers(self, n=5, a=[0, 1, 1], symbol="F", heading="Tribonacci Numbers", distinct=False):
      self.Fibonacci_numbers_generalized(n=n, a=a, symbol=symbol, heading=heading, distinct=distinct)

    def Fibonacci_numbers_generalized(self, n=6, a=[0, 0, 0, 1], symbol="F", heading="Fibonacci Numbers Generalized", distinct=False):
      order = len(a)
      def fib_generalized(n, order=order):
        F = a[:order]
        if n < order:
          return F[n]
        else:
          for i in range(order, n+1):
            F_i = sum(F)
            F[:] = F[1:] + [F_i]
          return F_i
      if distinct:
        child_nodes = [TreeNode(val=f"{symbol}{child_i}={fib_generalized(n=child_i)}") for child_i in range(order)]
        hidden_edges_set = set()
        for child_i in range(order-1, 0, -1):
          child_nodes[child_i].children.append(child_nodes[child_i-1])
          for grandchild_i in range(child_i-1, -1, -1):
            hidden_edges_set.add((id(child_nodes[child_i]), id(child_nodes[grandchild_i])))
        if n >= order:
          for i in range(order, n+1):
            parent_node = TreeNode(val=f"{symbol}{i}={fib_generalized(n=i)}")
            parent_node.children.append(child_nodes[order-1])
            for j in range(order-2, -1, -1):
              parent_node.grandchildren.append(child_nodes[j])
            child_nodes[:] = child_nodes[1:] + [parent_node]
          self.root = parent_node
          self.show(heading=f'Computation Space for {heading} (order={order}), Distinct (n={n})', direction="RL", edge_smooth_type = "curvedCCW", hidden_edges_set = hidden_edges_set)
        else:
          print(f"n={n} should be >= order={order}")
      else:
        self.root = TreeNode(val=f"{symbol}{n}={fib_generalized(n=n)}")
        queue = [(self.root,n),]
        while queue:
          (curr_node, curr_n) = queue.pop()
          for i in range(1, order+1):
            child_n = curr_n - i
            if child_n >= 0:
              child_node = TreeNode(val=f"{symbol}{child_n}={fib_generalized(n=child_n)}")
              curr_node.children.append(child_node)
              if child_n > (order-1):
                queue.append((child_node, child_n))
        self.show(heading=f'{heading} (order={order}) (n={n})')

    def climbing_stairs(self, n_steps = 8):
      ways = 0
      steps_count = 0
      self.root = TreeNode(val=f"#{steps_count}", color='lightgray')
      queue = [(self.root, steps_count)]
      while queue:
        (curr_node, curr_step_count) = queue.pop()
        if curr_step_count == n_steps:
          ways += 1
        else:
          if n_steps - curr_step_count >= 1:
            new_node = TreeNode(val=f"#{curr_step_count+1}", color='lightgreen')
            curr_node.children.append(new_node)
            queue.append((new_node, curr_step_count+1))
          if n_steps - curr_step_count >= 2:
            new_node = TreeNode(val=f"#{curr_step_count+2}")
            curr_node.children.append(new_node)
            queue.append((new_node, curr_step_count+2))
      self.show(heading=f"{ways} different ways to climb a staircase with {n_steps} steps to reach the top")
    
    def coin_change(self, coins = [3, 5], amount = 12):
      def fewest_number_of_coins_to_make_up_amount(amount: int) -> int:
          dp = [float('inf')] * (amount + 1)
          dp[0] = 0
          for coin in coins:
              for x in range(coin, amount + 1):
                  dp[x] = min(dp[x], dp[x - coin] + 1)
          return dp[amount] if dp[amount] != float('inf') else -1 
      self.root = TreeNode(val=f"amount left = ¢{amount};\nF(¢{amount}) = min. # of coins\nto make up ¢{amount} = {fewest_number_of_coins_to_make_up_amount(amount = amount)}")
      queue = [(self.root, amount)]
      while queue:
        (curr_node, amount_left) = queue.pop()
        if amount_left > 0:
          for coin in coins:
            if amount_left - coin >= 0:
                if amount_left - coin == 0:
                  new_node = TreeNode(val=f"used 1 ¢{coin};\namount left = ¢0;\nF(¢0) = {fewest_number_of_coins_to_make_up_amount(amount = 0)}, we are done!", color='lightgreen')
                  curr_node.children.append(new_node)
                else:
                  min_number = fewest_number_of_coins_to_make_up_amount(amount = amount_left - coin)
                  if min_number < 0:
                    new_node = TreeNode(val=f"used 1 ¢{coin};\namount left = ¢{amount_left - coin};\nF(¢{amount_left - coin}) = min. # of coins\nto make up ¢{amount_left - coin} = {min_number}", color='orange')
                  else:
                    new_node = TreeNode(val=f"used 1 ¢{coin};\namount left = ¢{amount_left - coin};\nF(¢{amount_left - coin}) = min. # of coins\nto make up ¢{amount_left - coin} = {min_number}")
                    queue.append((new_node, amount_left - coin))
                  curr_node.children.append(new_node)
      self.show(heading=f"Recursive space to find the minimal # of coins to make up amount = ¢{amount} with coin denominations of {[f'¢{coin}' for coin in coins]}; The answer is # of the edges of the shortest path to fully make up the amount; F(amount) = min([F(amount - coin) for coin in coins]) + 1")

    def remove_invalid_parenthese(self, s: str = '()())a)b()))'):
      """
      https://leetcode.com/problems/remove-invalid-parentheses/
      """
      def DFS(s='', pair=('(', ')'), anomaly_scan_left_range=0, removal_scan_left_range=0, depth=0, parent: TreeNode = None):
        # phase 1: scanning for anomaly
        stack_size = 0
        for index_i in range(anomaly_scan_left_range, len(s)):
            if s[index_i] == pair[0]:
                stack_size += 1
            elif s[index_i] == pair[1]:
                stack_size -= 1
                if stack_size == -1:
                    break
        if stack_size < 0:
            # phase 2: scanning for removal
            for index_j in range(removal_scan_left_range, index_i+1):
                if s[index_j] == pair[1]:
                    if index_j == removal_scan_left_range or s[index_j-1] != pair[1]:
                        new_s = s[:index_j] + s[(index_j+1):len(s)]
                        # add the node - start
                        if pair[0] == '(':
                          curr_node = TreeNode(val=new_s)
                        else:
                          curr_node = TreeNode(val=new_s[::-1])
                        parent.children.append(curr_node)
                        # add the node - end
                        DFS(s=new_s, pair=pair, anomaly_scan_left_range=index_i, removal_scan_left_range=index_j, depth=depth+1, parent=curr_node)
        elif stack_size > 0:
            # phase 3: reverse scanning
            DFS(s=s[::-1], pair=(')', '('), depth=depth, parent=parent)
        else:
          if pair[0] == '(':
              res.append(s)
          else:
              res.append(s[::-1])
      res = []
      self.root = TreeNode(val=s)
      DFS(s=s, pair=('(', ')'), depth=0, parent=self.root)
      self.show(heading='DFS Search Space for Removing Invalid Parentheses')
      return res

    def show(self, width='100%', height='60%', filename: str = 'output.html', heading: str = None, direction: str = "UD", edge_smooth_type: str = False, hidden_edges_set: set = set(), nodeDistance: int = 150, levelSeparation: int = 300, configure: bool = True):
        if not self.root:
            return
        def dfs_add_child(parent, level=0):
          if parent.children:
            for child in parent.children:
              if child.color:
                g.add_node(n_id=id(child), label=child.val, shape=child.shape, color=child.color, level=level+1, title=f"child node of Node({parent.val}), level={level+1}", **child.options)
              else:
                g.add_node(n_id=id(child), label=child.val, shape=child.shape,                    level=level+1, title=f"child node of Node({parent.val}), level={level+1}", **child.options)
              if (id(parent), id(child)) in hidden_edges_set:
                g.add_edge(source=id(parent), to=id(child), hidden = True)
              else:
                g.add_edge(source=id(parent), to=id(child))
              dfs_add_child(child, level=level+1)
        def dfs_add_grandchildren_edge(parent):
          if parent.grandchildren:
            for grandchild in parent.grandchildren:
              if (id(parent), id(grandchild)) in hidden_edges_set:
                g.add_edge(source=id(parent), to=id(grandchild), hidden=True)
              else:
                g.add_edge(source=id(parent), to=id(grandchild))
          if parent.children:
            for child in parent.children:
              dfs_add_grandchildren_edge(child)
        g = Network(width=width, height=height)
        g.set_edge_smooth(smooth_type = edge_smooth_type)
        if self.root.color:
          g.add_node(n_id=id(self.root), label=self.root.val, shape=self.root.shape, color=self.root.color, level=0, title=f"root node of the tree, level=0", **self.root.options)
        else:
          g.add_node(n_id=id(self.root), label=self.root.val, shape=self.root.shape,                        level=0, title=f"root node of the tree, level=0", **self.root.options)
        dfs_add_child(parent=self.root)
        dfs_add_grandchildren_edge(parent=self.root)
        if not heading:
          g.heading = f"{self.treetype}"
        else:
          g.heading = heading
        options = """
var options = {
  "nodes": {
    "font": {
      "size": 20
    }
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true
      }
    },
    "color": {
      "inherit": true
    },"""
        if edge_smooth_type:
          options += f"""
    "smooth": {{
        "type": "{edge_smooth_type}",
        "forceDirection": "none"
        }}"""
        else:
          options += """
    "smooth": false"""
        options += """
  },
  "layout": {
    "hierarchical": {
      "enabled": true,"""
        options += f"""
      "levelSeparation": {levelSeparation},
      "direction": "{direction}","""
        options += """
      "sortMethod": "directed"
    }
  },
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0,
      "springConstant": 0.2,"""
        options += f"""
      "nodeDistance": {nodeDistance}"""
        options += """
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }"""
        if configure:
          options += """,
  "configure": {
      "enabled": true,
      "filter": "layout,physics" 
  }
}"""
        else:
          options += """
}"""
        g.set_options(options)
        full_filename = Path.cwd() / filename
        g.write_html(full_filename.as_posix())
        webbrowser.open(full_filename.as_uri(), new = 2)
        return g
