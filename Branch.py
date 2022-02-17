#coding:utf-8
import rhinoscriptsyntax as rs

class Branch:
     
    def __init__(
        self,
        parentEPt,
        parentLength,
        parentAxises,
        angleXY,
        scale
        ):
            
        self.parentEPt = parentEPt
        self.parentLength = parentLength
        self.parentAxises = parentAxises
        self.angle = angle
        self.scale = scale
         
        # setChild Axises
        self.childAxises = []
        self.setAxises()
        
        # setChildPts
        self.childSPt = []
        self.childEPt = []
        self.setChildAxises()

    def setChildAxises(self):   
        for axis in self.parentAxises:
            newAxis = rs.VectorRotate(axis,self.angleXY,self.parentAxises[2])
            self.childAxises.append(newAxis)
    
    def setChildEpt():
        vec = self.childAxises[1]
        vec = rs.VectorUnitize(vec)
        vec = rs.VectorScale(vec, self.parentLength*self.scale)
       
        self.childSPt = self.parentEPt
        self.childEPt = rs.VectorAdd(ePt, vec)
    
    def draw(self):
        obj = rs.AddLine(self.sPt, self.ePt)
        return obj