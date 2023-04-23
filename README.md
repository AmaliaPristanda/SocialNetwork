# SocialNetwork

# Table of contents
1. [Challenge description](#cd)
2. [Social network representation](#repr)
3. [Algorithm](#alg)
3. [Test cases](#ts)

## Challenge description <a name="cd"></a>
Let's build a social network. 

In this social network, each user has friends.

A chain of friends between two users, user A and user B, is a sequence of users starting with A and ending with B, such that for each user in the chain, ua, the subsequent user, ua + 1, are friends.

Given a social network and two users, user A and user B, please write a function that computes the length of the shortest chain of friends between A and B.


## Social network representation <a name="repr"></a>
The social network is represented as an undirected graph (if user A is friends with user B, then automatically user B is friends with user A) with unweighted edges (all friendships have the same value, in this case 1). Each friendship relationship between two users is marked as a vertex.     
I chose this approach because it is easy to analyze and well-suited for larger social networks.
  
The graph is represented by a adjacency list as oposed to a adjacency matrix because it is more space efficient and it is faster to iterate over neighbours.  
  
I also considered that since the challenge it is to compute the length of the shortest chain of friends between A and B, the graph should have at least 2 nodes.

## Algorithm <a name="alg"></a>
In order to compute the length of the shortest chain of friends between A and B, I chose the BFS algorithm due to its simplicity and the fact that it guarantees to find a solution.  
I also considered using the Bellmand-Ford algorithm thinking that if the problem should change (the graph becomes weighted or directed or both) the BFS aproach won't provide a solution. However, I did not since the time complexity is larger (O(V*E) vs O(V+E)) and I think that while future possible problems should be taken into consideration, efficient solutions should be implemented for the current ones.

## Test cases <a name="ts"></a>

When testing the correctness of the provided solution, I considered the following cases:  

1. user A and B don't have any common friends - the length of the chain of friends should be 0    
2. there are multiple shortest paths between A and B - since it's a BFS algorithm, it should provide the first found solution  
3. A and B are the same node - the length should be 0  
4. a general case - to confirm whether the algorithm provides the correct solution or not  


