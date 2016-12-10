import itertools
import collections

def bar(s): print(s)

class City:
  def __init__(self,id,score):
    self.id=id; self.score=score; self.parent=self
    self.children=[]
  def set_parent(self,parent):
    if self.parent!=self: self.parent.set_parent(self)
    self.parent=parent
  def add_child(self,child): self.children.append(child)
  def get_bott_high(self,top_low):
    self.top_low=top_low
    top_low=min(top_low,self.score)
    self.bott_high=max(
      (node.get_bott_high(top_low) for node in self.children),
      default=self.score
    )
    self.type=''
    if self.top_low  <self.score: self.type+='L'
    if self.bott_high>self.score: self.type+='H'
    return self.bott_high

  def show(self):
    print(
      # self.score,
      self.type,
      self.id,
      # self.parent.id,
      '=>',
      ':'.join(str(x.id) for x in self.children)
    )

def result(k,low,high): print('result:',low,high)
def top_score_results(items):
  pass
def solution(k,scores,parents):
  nodes=prepare_input(scores,parents)
  root=nodes[-1]
  root.get_bott_high(root.score)
  grey=nodes[0].score
  count=len(nodes)
  for score,iter in itertools.groupby(nodes,lambda x:x.score):
    print('--score:', score)
    items=list(iter)
    count-=len(items)
    if score==root.score: return top_score_results(items)
    if score>=grey:
      cc=collections.Counter(x.type for x in items)
      result(k,count+cc['H'],count+cc['H']+cc[''])
    grey=max((x.bott_high for x in items),default=grey)
  return 0

def prepare_input(scores,parents):
  nodes_by_id=[City(id,score) for id,score in enumerate(scores)]
  for id,parent_id in enumerate(parents):
    nodes_by_id[id].set_parent(nodes_by_id[parent_id])
  nodes=sorted(nodes_by_id,key=lambda x:x.score)

  top_node=nodes[-1]; top_score=top_node.score
  top_node.set_parent(top_node)

  for node in nodes:
    if node.parent != node:
      node.parent.add_child(node)

  return nodes;

scores=[6,2,7,5,6,5,2]
parents=[1,3,0,3,2,4,4]
print(solution(4,scores,parents))

"""
__init__(self,args...)
enumerate
scope: read enclosing write local (or global explicitly)
exceptions; with
sorted(list, key=lambda x:f(x))
"""

