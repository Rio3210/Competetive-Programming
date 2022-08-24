class MyQueue(object):

    def __init__(self):
        self.Q=[]
        

    def push(self, x):
        self.Q.append(x)
        
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
      
        m=self.Q.pop(0)
        return m
        """
        :rtype: int
        """
        

    def peek(self):
        
        return self.Q[0]
        """
        :rtype: int
        """
        

    def empty(self):
        if self.Q==[]:
            return True
            
        
        """
        :rtype: bool
        """
        

