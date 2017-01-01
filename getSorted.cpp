/*

Problem:
Implement a service which keeps it's element in a data structure defined by you and on each query gives an element greater than previous.
So on i_th query number returned should be smaller than (i+1)_th query

Assumptions taken for quick and ease of implementation :
Implemented with BST. Not balanced binary search tree.
Could have used Red Black BST for better time complexity.

Data is assumed to be int. Also for ease of implementation it is assumed that all data values are unique.
Could use template class for generalisation. 

All class declaration definition everything is put together in same file for submission.
Using header file and distributing classes over other file will result in many file submissions.

For easy and fast implementation many assumptions has taken. Like returning MIN_INT in case where
exception should be thrown.

*/

#include <iostream>
#include <cstddef>
#include <climits>
#include <exception>

//For verbose comment out below 
//#define DEBUG


//Node declaration 
class Node{
	public:
	Node(int);
	int data;
	Node* left;
	Node* right;
	Node* parent;
};

Node::Node(int data){
	this->data = data;
	left = NULL;
	right = NULL;
	parent = NULL;
}

class BSTree{
	private:
	void insert(int data, Node* t);
	
	public:
	BSTree();
	void insert(int data);
	Node* succsessor(Node* t);
	
	Node* root;
};

BSTree::BSTree(){
	root = NULL;
}

Node* BSTree::succsessor(Node* t){
	if(t->right != NULL){
		//get left most of right child
		Node* temp = t->right;
		while(temp){
			if(temp->left == NULL){
				return temp;
			}
			temp = temp->left;
		}
	}
	else{
		//succsessor will be in parents while taking first right turn
		Node* temp = t;
		while(temp->parent){
			if(temp->parent->left == temp){
				return temp->parent;
			}
			else{
				temp = temp->parent;
			}
		}
		//no succsessor
		return NULL;
	}
};

void BSTree::insert(int data){
	if(root == NULL){
		root = new Node(data);
	}
	else{
		insert(data, root);
	}
}

void BSTree::insert(int data, Node* t){
	if(t->data < data){
		if(t->right == NULL){
			t->right = new Node(data);
			t->right->parent = t;
#ifdef DEBUG
			std::cout<<"inserted at root: "<<t->data<<" right data: "<<t->right->data<<std::endl;
#endif
		}
		else
			insert(data,t->right);
	}
	else{
		if(t->left == NULL){
			t->left = new Node(data);
			t->left->parent = t;
#ifdef DEBUG
			std::cout<<"inserted at root: "<<t->data<<" left data: "<<t->left->data<<std::endl;
#endif
		}
		else
			insert(data,t->left);
	}
}

//this class implements the interface to get the numbers in sorted order

class GetSorted{
	private:
	Node* lastOutputNode;
	BSTree bst;
	
	public:
	GetSorted();
	//Function to be called from outside to get the elements in sorted order
	int getsorted();
	void insert(int);
	
};
GetSorted::GetSorted(){
	lastOutputNode = NULL;
}

void GetSorted::insert(int data){
	bst.insert(data);
}


int GetSorted::getsorted(){
	if(lastOutputNode){
		Node* t = bst.succsessor(lastOutputNode);
		if(t){
			lastOutputNode = t;
			return t->data;
		}
		else{
			//throw exception
			throw -1;
			return INT_MIN;
		}
	}
	else{
		//start from root get most child
		if(bst.root == NULL){
			//throw exception
			throw -1;
			return INT_MIN;
		}
		Node* t = bst.root;
		while(t->left != NULL){
			t = t->left;
		}
		lastOutputNode = t;
		return t->data;
	}
}

//Sample driver program to test

int main(){
	GetSorted gsrt;
	//insert some numbers
	gsrt.insert(1);
	gsrt.insert(2);
	gsrt.insert(5);
	gsrt.insert(12);
	gsrt.insert(4);
	
	std::cout<<"output: "<<gsrt.getsorted()<<std::endl;;
	std::cout<<"output: "<<gsrt.getsorted()<<std::endl;
	std::cout<<"output: "<<gsrt.getsorted()<<std::endl;
	
	gsrt.insert(3);
	std::cout<<"output: "<<gsrt.getsorted()<<std::endl;
	gsrt.insert(6);
	std::cout<<"output: "<<gsrt.getsorted()<<std::endl;
}
