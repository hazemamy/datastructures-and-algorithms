## Arrays
- Data structure for storing elements.
- Access: O(1)
- Insertion: O(n)
- Deletion: O(n)

## Linked Lists
- Collection of nodes.
- Access: O(n)
- Insertion at beginning: O(1)
- Deletion at beginning: O(1)

## Stacks
- Follows Last-In-First-Out (LIFO).
- Push: O(1)
- Pop: O(1)

## Queues
- Follows First-In-First-Out (FIFO).
- Enqueue: O(1)
- Dequeue: O(1)

## Trees
- Hierarchical data structure.
- Various types with varying complexities.
- Binary Search Tree (BST) Operations:
  - Search/Insert/Delete: O(h), where h is the height (log n in a balanced tree).

## Hash Tables
- Key-value pairs storage.
- Average Case:
  - Access (search/insert/delete): O(1)
- Worst Case (if collisions are not handled):
  - Access: O(n)

## Graphs
- Complex structures with variable complexities.
- Graph traversal depends on the algorithm (e.g., BFS, DFS).

## Heaps
- Tree-like structures for priority queues.
- Insertion: O(log n)
- Extraction (min/max): O(log n)

## Trie
- Tree-like structure for efficient string storage.
- Search/Insert/Delete: O(m), where m is the length of the string.

## Linked HashMap
- Combines linked list and hash map.
- Access: O(1)
- Insertion/Deletion: O(1)

## Disjoint Set (Union-Find)
- Used for tracking connected components.
- Union/Find: O(α(n)), where α(n) is the inverse Ackermann function (almost O(1) in practice).
