class MinStack {
public:
    int _min;
    vector<int> _stack;
    int top;
        
    MinStack() {
        vector<int> tmp;
        _stack.swap(tmp);
        top = 0;
    }
    
    void push(int val) {
        if(val < _min)
        {
            _stack.push_back(val);
        }
        top++;
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
