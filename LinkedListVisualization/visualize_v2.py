import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def get_nodes(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return nodes

def update_graph(num, linked_list, ax):
    ax.clear()
    num_nodes = len(linked_list.get_nodes())
    
    # Adjust plot limits based on the number of nodes
    ax.set_xlim(0, max(15, 2 + num_nodes * 4))
    ax.set_ylim(0, 3)
    ax.axis('off')

    if num == 0:
        # Initial node creation
        x = 5
        rect = patches.FancyBboxPatch((x, 1), 2, 0.5, boxstyle="round,pad=0.1", edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        ax.text(x + 1, 1.25, 'Creating Node', ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(x + 1, 1, 'Value: ', ha='center', va='center', fontsize=10)
        ax.text(x + 1, 0.75, 'Next: ', ha='center', va='center', fontsize=10)
    else:
        # Update graph with existing nodes
        x = 1
        nodes = linked_list.get_nodes()
        for i, node in enumerate(nodes):
            # Draw node rectangle
            rect = patches.FancyBboxPatch((x, 1), 2, 0.5, boxstyle="round,pad=0.1", edgecolor='black', facecolor='lightblue')
            ax.add_patch(rect)
            # Add node value and address text with adjusted positions
            next_addr = hex(id(node.next)) if node.next else 'None'
            ax.text(x + 1, 1.25, f'Value: {node.value}', ha='center', va='center', fontsize=10)
            ax.text(x + 1, 1, f'Next: {next_addr}', ha='center', va='center', fontsize=10)
            # Draw arrow to next node
            if i < len(nodes) - 1:
                ax.annotate('', xy=(x + 3, 1.25), xytext=(x + 2, 1.25),
                            arrowprops=dict(arrowstyle='->', color='black'))
            x += 4

def animate(frame):
    if frame == 0:
        # Initial node creation
        update_graph(frame, linked_list, ax)
    elif frame <= len(values):
        # Add new node and update graph
        linked_list.append(values[frame - 1])
        update_graph(frame, linked_list, ax)

# Example data
values = [10, 20, 30, 40]
linked_list = LinkedList()

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=len(values) + 1, repeat=False, interval=1500)

plt.show()
