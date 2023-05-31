# Decision Tree

## Why use Decision Trees?

- Decision Trees usually mimic human thinking ability while making a decision, so it is easy to understand
- the logic behind the decision tree can be easily understood because it shows a tree-like structure.

![](Illustrasion/decision-tree-classification-algorithm.png)

## Key words

- **Root Node:** Root node is from where the decision tree starts. It represents the entire dataset, which further after getting a leaf node.
- **Leaf Node:** Leaf nodes are the dinal output node, and the tree cannot be divided(segregated) further after getting a leaf node.
- **Splitting:** Splitting is the process of dividing the decision node/root into sub-nodes according to the given conditions.
- **Brach/Sub tree:** A tree formed by splitting the tree.
- **Pruning:** Pruning is the process of removing the unwanted branches from the tree.
- **Parent/Child node:** The root node of the tree is called node, and other nodes are called the child nodes.

## Algorithm work

In a decision tree, for predicting the class of the given dataset, the algorithm starts from the root node of the tree. Alforithm compares the values of root attribute with the record (real dataset) attribute and based on the comparison, follows the brach and jumps to the next node.

**For the next node**, the algorithm again compare the attribute value with the other sub-nodes and move further. It continues the process until it reaches the leaf node ò the . the complete process can be better understood using the algorithm.

- **Step 1:** Begin the tree with the root node, says S, which contains the complete dataset.
- **Step 2:** Find the best  attribute in the dataset using **Attribute Selection Measure (ASM)**.
- **Step 3:** Divide the S into subsets that contains possible values for the best attributes - thuoc tinh. 
- 
