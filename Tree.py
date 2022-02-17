#coding:utf-8
from Branch import Branch
import random
import rhinoscriptsyntax as rs
import scriptcontext

class Tree:
     
    def __init__(self):
        self.branches = []
         
        # parent branch
        ePt = [0,0,0]
        length = 1800
        axises = [
            [300,0,0],
            [0,300,0],
            [0,0,300]
        ]
        
        # child paremeter
        angleXY = 45
        scale = 1
        
        # child brnch
#        newAxises = []
#        for axis in axises:
#            newAxis = rs.VectorRotate(axis,angleXY,axises[2])
#            newAxises.append(newAxis)
#           
#        vec = newAxises[1]
#       vec = rs.VectorUnitize(vec)
#        vec = rs.VectorScale(vec,length*scale)
#       
#        newsPt = ePt
#        newePt = rs.VectorAdd(ePt, vec)

        branch = Branch(
            parentEPt,
            parentLength,
            parentAxises,
            angleXY,
            scale
        )
        
        self.branches.append(branch)
         
#       self.makeChildBranch(branch, 0)
         
    def makeChildBranch(self,branch, n):
        # end condition
        if (scriptcontext.escape_test(False)):
            print "TimeConsumingTask cancelled."
            return
        if (n>=6):
            return
        
        # left branch
        vec = rs.VectorSubtract(branch.ePt, branch.sPt)
        vec = rs.VectorUnitize(vec)
        dis = rs.Distance(branch.ePt, branch.sPt)
        scale = random.uniform(0.8, 0.9)
        vec = rs.VectorScale(vec, dis*scale)
        angle = random.uniform(10, 45)
        vec = rs.VectorRotate(vec, angle, [0,0,1])
         
        newSpt = branch.ePt
        newEpt = rs.VectorAdd(branch.ePt, vec)
        childbranchL = Branch(newSpt,newEpt)
        self.branches.append(childbranchL)
        
        self.makeChildBranch(childbranchL,n+1)
         
        # right branch
        vec = rs.VectorSubtract(branch.ePt, branch.sPt)
        vec = rs.VectorUnitize(vec)
        dis = rs.Distance(branch.ePt, branch.sPt)
        scale = random.uniform(0.8, 0.9)
        vec = rs.VectorScale(vec, dis*scale)
        angle = -random.uniform(10, 45)
        vec = rs.VectorRotate(vec, angle, [0,0,1])
         
        newSpt = branch.ePt
        newEpt = rs.VectorAdd(branch.ePt, vec)
        childbranchR = Branch(newSpt,newEpt)
        self.branches.append(childbranchR)
        
        self.makeChildBranch(childbranchR,n+1)