// inefficient processing exists. becuase I use vector space x2

#include<vector>

using namespace std;

class MinStack {
public:
    vector<int> _stack;
    vector<int> _val_stack;
    int _top;
        
    MinStack() {
        vector<int> tmp;
        _stack.swap(tmp);
        _top = 0;
    }
    
    void push(int val) {
        if(_top<=0)
        {
            _stack.push_back(val);
        }else
        {
            if(_stack[_top-1] < val)
            {
                _stack.push_back(_stack[_top-1]);
            }else
            {
                _stack.push_back(val);
            }
        }
        _val_stack.push_back(val);
        _top++;
    }
    
    void pop() {
        _stack.pop_back();
        _val_stack.pop_back();
        _top--;
    }
    
    int top() {
        return _val_stack[_top-1];
    }
    
    int getMin() {
        return _stack[_top-1];
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
