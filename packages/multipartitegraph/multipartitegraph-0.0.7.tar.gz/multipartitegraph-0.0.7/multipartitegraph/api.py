import copy
import string
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class myNode:
    def __init__(self, x, y, _id):
        self.x = x
        self.y = y
        self.id = _id
        self.label = _id
        self.next = []
        
    def plot(self, ax, boxstyle):
        ax.text(self.x, self.y, self.label, transform=ax.transAxes, fontsize=18, va='center', ha='center', bbox=dict(boxstyle=boxstyle, facecolor='wheat', alpha=1))
        
    def add_child(self, x):
        self.next.append(x)
        
    def remove_child(self, x):
        self.next.remove(x)


class Net:
    def __init__(self, arrays:list):
        if not isinstance(arrays, list):
            raise TypeError("The parameter arrays of object of class Net accepts only a regular Python list of pandas DataFrame. You try to supply %s instead. Please correct." % (type(arrays)))
        if not len(arrays):
            raise TypeError("You supply to the parameter arrays of object of class Net an empty Python list while it should contain pandas DataFrames. Please correct")
        self.notPandas = []
        self.zeroPandas = []
        self.mismatchPandas = []
        self.namesInPandas = []
        for i, array in enumerate(arrays):
            if not isinstance(array, pd.DataFrame):
                self.notPandas.append(str(i))
            if i:
                try:
                    np.dot(arrays[i-1].values, array.values)
                except:
                    self.mismatchPandas.append(str(i-1) + ' and ' + str(i))
                else:
                    if np.any(self.namesTest != array.index.values):
                        arrays[i-1].columns = array.index.values
                        self.namesInPandas.append(str(i))
            if array.shape[0] < 1 or array.shape[1] < 1:
                self.zeroPandas.append(str(i))
            self.namesTest = array.columns.values
        if len(self.notPandas):
            raise TypeError("The parameter arrays of object of class Net accepts only a list of pandas DataFrame. You try to supply a list where the elements %s are not pandas DataFrames. Please correct." % (', '.join(self.notPandas),))
        if len(self.zeroPandas):
            raise TypeError("The parameter arrays of object of class Net accepts only a list of non-empty pandas DataFrame. You try to supply a list where the elements %s look like empty pandas DataFrames. Please correct." % (', '.join(self.zeroPandas),))
        if len(self.mismatchPandas):
            raise ValueError("The dimentions of the matrices %s don't match each other" % (', '.join(self.mismatchPandas),))
        if len(self.namesInPandas):
            warnings.warn("The parameter arrays of object of class Net expects a list of pandas DataFrame, in which each next DataFrame has index names identical to the column names of the previous DataFrame. You try to supply a list where the DataFrames %s don't seem to have column names satisfying this condition. The script will use only the column names ingnoring the row names where they don't match. Please be warned and check whether the order of your DataFrames is correct in the list." % (', '.join(self.namesInPandas),))
        self.nodes = dict()
        self.arrays = copy.deepcopy(arrays)
        self.xdim = len(arrays) + 1
        self.ydim = np.zeros(self.xdim, dtype=np.int64)
        self.pivot = pd.DataFrame(columns=['source', 'target', 'linked'], dtype=('str', np.int64))
        self._ids = []
        self.labels = set()
        for i, array in enumerate(arrays):
            if i:
                self._ids.append(array.columns.values)
                self.labels.update(array.columns.values)
            else:
                self._ids.append(array.index.values)
                self._ids.append(array.columns.values)
                self.labels.update(array.index.values)
                self.labels.update(array.columns.values)
            self.ydim[i] = array.shape[0]
            self.pivot = pd.concat([self.pivot, array.reset_index().melt(id_vars='source', var_name='target', value_name='linked')])
        self.ydim[i+1] = array.shape[1]
        self.max_label = np.array(list(map(len, self.labels))).max()
        self.boxstyle = 'circle' if self.max_label < 3 else 'round'
        self.max_y = 0
        for i in range(self.xdim):
            self.max_y = max(self.max_y, self.ydim[i])
        self.odd = bool(self.max_y % 2)
        self.pivot = self.pivot.loc[self.pivot['linked']==1, ['source', 'target']].set_index('source')
        self.x_coord = np.linspace(0.05, 0.95, self.xdim)
        self.y_coords = []
        for x in range(self.xdim):
            if self.odd == bool(self.ydim[x] % 2):
                self.y_coords.append(np.linspace(0.1, 0.9, self.ydim[x]))
            else:
                self.y_coords.append(np.linspace(0.1, 0.9, self.ydim[x] * 2 + 1)[1::2])
            for y in range(self.ydim[x]):
                _id = self._ids[x][y]
                self.nodes[_id] = myNode(self.x_coord[x], self.y_coords[x][y], _id)
        for row in range(self.pivot.shape[0]):
            self.nodes[self.pivot.index[row]].add_child(self.nodes[self.pivot.iloc[row]['target']])
            
                
    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=(self.max_label * 0.2 + self.xdim * 1.1 + self.max_y * 0.1, self.max_y * 1.1))
        for i in self.nodes: 
            self.nodes[i].plot(self.ax, self.boxstyle)
            for nextNode in self.nodes[i].next:
                self.ax.plot([self.nodes[i].x, nextNode.x], [self.nodes[i].y, nextNode.y], 'k-', lw=2, transform=self.ax.transAxes)
        plt.axis('off')
        plt.show()