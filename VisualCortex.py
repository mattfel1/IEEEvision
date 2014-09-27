import numpy as np
from copy import deepcopy
import cv2


class VisualCortex:
	####################################
	#####  1. LIST OF PROPERTIES   #####
	####################################
	FullMap = None;
	Position = None;
	Rotation = None;
	CourseBounds = None;
	__mapFeatures = None;
	__viewFeatures = None;
	__transformedView = None;
	__perspectiveMatrix = None;


    ####################################
    #####      2. INITIALIZER      #####
    ####################################
    #initialization for integrating with GNC
	def __init__(self, viewCoordinates, mapCoordinates):
		#initialize the map and coordinates to be published to other nodes
		self.FullMap= 0;   #make this actually initialize to a black map...
		self.Position = [0 , 0];
		self.Rotation = 0;
		self.CourseBounds = [[ -1 , -1 , 1 ,  1 ]
							 [ -1 ,  1 , 1 , -1 ]]; #how should we initialize this?

		#get the transform matrix
		self.__perspectiveMatrix = getForwardMatrix(viewCoordinates , mapCoordinates);


	####################################
	#####     3. PUBLIC METHODS    #####
	####################################
	# Takes an image from the camera's video feed and transforms it into a bird's eye view
	def Transform_Image(self, imageorfeatures , _perspectiveMatrix): 
		return None;

	#Finds the features/corners of interest of an input image, which can be either the _transformedView, FullMap, or raw camera image
	def Feature_Detect(self, image , mask ):
		return None;

	#use SIFT/SURF/ORB/other for determining the Rotation and Position of the robot
	def Localize(self,  _viewFeatures, _mapFeatures):
		return None;

	#updates the FullMap based on new information discovered about the field, anchored at the position and rotation calculated by Localize
	def Stitch(self, Position, Rotation):
		return None;


	####################################
	#####    4. PRIVATE METHODS    #####
	####################################

	# Add any kind of private methods here that support the above public methods.
	# Be sure to include a detailed summary of what the method does


	#Calculate the transform matrix
	def getForwardMatrix(self, viewCoordinates , mapCoordinates):
		return None;














	####################################
	#####     5. DEBUG/TESTING     #####
	####################################

	# Put the main program here that uses the above class(es) to test

#calculate xform matrix
viewCoordinates = np.float32([[556,481],[509,457],[783,481],[669,457]])
#assuming square is 227px big
mapCoordinates = np.float32([[556,481],[556,254],[783,481],[783,254]])
VC = VisualCortex(viewCoordinates,mapCoordinates);

