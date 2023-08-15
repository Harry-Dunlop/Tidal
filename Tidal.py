import os, sys, time
PROJECT_DIRECTORY = "C://Users//harry//PROGRAMMING//Python Game Engine"
src = "C://Users//harry//PROGRAMMING//Python Game Engine"
def ToString(list: list):
    return ''.join(list)


class globals:
    import KeyCodes
    collidableTags = []
    triggerTags = []

    
    all_tags = []
    

    object_positions = {}
    IGNORE_CHAR = "x"
    KEY_ASSIGNED_FUNCTIONS = [None] * len(KeyCodes.KEYS.values())

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"
    
    def AsTuple(self):
        return (self.x, self.y)

    def magnitude(self):
        from math import sqrt
        return sqrt(self.x * self.x + self.y * self.y)

    def up():
        return Vector2(0, 1)

    def down():
        return Vector2(0, -1)

    def right():
        return Vector2(1, 0)

    def left():
        return Vector2(-1, 0)

    def zero():
        return Vector2(0, 0)

    def distance(pointA, pointB):
        x = pointB.x - pointA.x
        y = pointB.y - pointA.y
        import math
        return math.sqrt(y ** 2 + x ** 2)

    def Equal(vectorA, vectorB):
        if vectorA.x == vectorB.x and vectorA.y == vectorB.y:
            return True
        else:
            return False

    def Add(vectorA, vectorB):

        return Vector2(vectorA.x + vectorB.x, vectorA.y + vectorB.y)

    def Multiply(vectorA, vectorB):
        return Vector2(vectorA.x * vectorB.x, vectorA.y * vectorB.y)


class Color:
    RED = 1
    YELLOW = 3
    GREEN = 2
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    BLACK = 0


class Vector3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
    def AsTuple(self):
        return (self.x, self.y,self.z)
    
    def Distance(pointA, pointB):
        width = pointB.x - pointA.x
        depth = pointB.z - pointB.z
        from math import sqrt
        diag = sqrt((width ** 2 + depth ** 2))

        height = pointB.y - pointA.y

        distance = sqrt((diag ** 2 + height ** 2))

        return distance

class ImageManipulation:
    """for each y from top to bottom do
    for each x from left to right do
        oldpixel := pixels[x][y]
        newpixel := find_closest_palette_color(oldpixel)
        pixels[x][y] := newpixel
        quant_error := oldpixel - newpixel
        pixels[x + 1][y    ] := pixels[x + 1][y    ] + quant_error × 7 / 16
        pixels[x - 1][y + 1] := pixels[x - 1][y + 1] + quant_error × 3 / 16
        pixels[x    ][y + 1] := pixels[x    ][y + 1] + quant_error × 5 / 16
        pixels[x + 1][y + 1] := pixels[x + 1][y + 1] + quant_error × 1 / 16"""
    


class Mathf:
 
    pi_file = open("pi.dat", "r")
    PI = float(pi_file.readlines()[0])

    class Matrix2D:
        def __init__(self, width, height):
            self.width = width
            self.height = height

            self.matrix = [[None] * self.width for _ in range(self.height)]
            print(len(self.matrix))

        def __repr__(self):
            return self.matrix

        def __len__(self):
            return len(self.matrix)

        def Reverse(self):

            for i in range(len (self.matrix) ):
                self.matrix[i].reverse()


        def Transpose(matrix):

            transposed_matrix = []
            _matrix = matrix.matrix
            for counter in range(matrix.width):
                """
                JAVA CODE I TRANSLATED FOR THIS FUNCTION
                for(int row = 0; row < numRows; row++)
                {
                    colArray[row] = m2Darray[row][columnOfInterest];
                }
                """
                vert_column = [row[counter] for row in _matrix]
                transposed_matrix.append(vert_column)

            matrix.matrix = transposed_matrix
            print("V matrix V")
            print(matrix.matrix)
            new_matrix = Mathf.Matrix2D(len(matrix.matrix[0]),len(matrix.matrix))
            new_matrix.matrix = matrix.matrix
            return new_matrix
        
        def GetItem(self, pos: Vector2):
            return self.matrix[pos.y][pos.x]
        def Equal(Matrix1, Matrix2):
            if Matrix1.matrix == Matrix2.matrix:
                return True
            else:
                return False

    def lerp(a, x, b):
        return a + x * (b - a)


    def Get2DLinePoints(pointA: Vector2, pointB: Vector2):
        pointsArray = []

        x1 = pointA.x
        x2 = pointB.x

        y1 = pointA.y
        y2 = pointB.y
        try:
            gradient = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            gradient = 0
        point = Vector2(x1, y1)

        current_x = int()

        length = x2 - x1
        height = y2 - y1
        print(f"height: {height}")
        negative = False
        if length < 0:
            negative = True
            length *= -1
        print("prerun")
        print(length)
        if length == 0:
            print("RUN RUN RUN RUN RUN RUN RUN RUN")
            height = y2-y1
            for h in range(height):
                point = Vector2(x1,h)
                pointsArray.append(point)
        if height == 0:
            print("rab")
            for h in range(length):
                point = Vector2(h,y1)
                pointsArray.append(point)
        
        if negative:
            current_x = 7

        while point.x != pointB.x and point.y != pointB.y:
            point = Vector2(x1 + current_x, (current_x * gradient)+pointA.y)

            # print(current_x)

            if negative == True:
                current_x -= 1
            else:
                current_x += 1

            if negative:
                pointsArray.append(Vector2(round(point.x) - length, round(point.y)))
            else:
                pointsArray.append(Vector2(round(point.x), round(point.y)))

            if current_x > length:
                print("failed")

        return pointsArray

    def Get3DLinePoints(pointA: Vector3, pointB: Vector3):
        pointsArray = []
        
        #print(pointA.AsTuple())
        #print(pointB.AsTuple())
        x1 = pointA.x
        x2 = pointB.x

        y1 = pointA.y
        y2 = pointB.y

        z1 = pointA.z
        z2 = pointB.z
        #print(y1)

        height =  y2-y1

        #print("ALL POINTS")
        #print(f"x1: {pointA.x}")
        #print(f"x2: {pointB.x}")

        #print(f"y1: {pointA.y}")
        #print(f"y2: {pointB.y}")

        #print(f"z1: {pointA.z}")
        #print(f"z2 {pointB.z}")
        # get first z triangle thing
        p1 = Vector2(x1,z1) 
        p2 = Vector2(x2,z2)
        
        #print(p1)
        #print(p2)
        z_line_points = Mathf.Get2DLinePoints(p1, p2)
        #print(z_line_points)
        p1 = Vector2(x1,y1)
        p2 = Vector2(x2,y2)
        pointsArray = Mathf.Get2DLinePoints(p1, p2)
        #print(pointsArray)
        
        for i, item in enumerate(pointsArray):
            pointsArray[i] = Vector3( item.x, item.y, z_line_points[i].y )
        
    
        return pointsArray
    
    # adapted from https://www.geeksforgeeks.org/draw-circle-without-floating-point-arithmetic-unpublished/?ref=lbp
    def GetCirclePoints(centre, radius):
        

        points = []
        # Consider a rectangle of size N*N 
        N = 2*radius+ 1
        
        # Draw a square of size N*N. 
        for i in range(N) :    
            for j in range(N) :
            
                # Start from the left most corner point 
                x = i - radius 
                y = j - radius
    
                # If this point is inside the circle, save its position
                if (x * x + y * y <= radius * radius + 1 ) :
                    points.append(Vector2(i+centre.x,j+centre.y))
                else :# If outside the circle, ignore
                    
                    continue

        return points  
             

        





        return
    
    def DegToRads(deg):
        return deg * (Mathf.PI / 180)
    
    def RadToDeg(rad):
        return  rad * (180 / Mathf.PI)
    
    # print("MATHS")
    def FS_Dither(image,desc= "Floyd–Steinberg dithering for greyscale images"):
        import PIL
        image_matrix = []
        width, height = image.size

        def find_closest_palette_color(oldpixel):
            return round(oldpixel / 255)
        print(image.size)
        pixels = image.getdata()
        # CREATE IMAGE MATRIX
        y = 0
        x = 0
        
        img_matrix = Mathf.Matrix2D(width,height+1)
        for count, pixel in enumerate(pixels):
            # is divisble
            x+=1
            print(f"x:{x} y:{y}")
            if count % width == 0:
                y+=1
                x=0
            img_matrix.matrix[y][x] = pixel
        
        #print(img_matrix.matrix)
        """
        
        PSUEDO CODE FROM THE FLOYD-STEINBERG DITHERING PAGE
        
        for each y from top to bottom do
            for each x from left to right do
                oldpixel := pixels[x][y]
                newpixel := find_closest_palette_color(oldpixel)
                pixels[x][y] := newpixel
                quant_error := oldpixel - newpixel
                pixels[x + 1][y    ] := pixels[x + 1][y    ] + quant_error × 7 / 16
                pixels[x - 1][y + 1] := pixels[x - 1][y + 1] + quant_error × 3 / 16
                pixels[x    ][y + 1] := pixels[x    ][y + 1] + quant_error × 5 / 16
                pixels[x + 1][y + 1] := pixels[x + 1][y + 1] + quant_error × 1 / 16"""
        
        pixels = img_matrix.matrix
        pixels.pop(0)
        #print("FART")
        print(pixels)
        print(len(pixels))
        for y in range(len(pixels)):
            for x in range(len(pixels[y])-1):
                print(len(pixels[y]))
                print(f"x:{x} y:{y}")
                oldpixel = pixels[y][x]
                newpixel = find_closest_palette_color(oldpixel)
                pixels[y][x] = newpixel

                quant_error = oldpixel - newpixel

                pixels[x + 1][ y ] = pixels[x + 1][ y ] + quant_error * 7 / 16
                pixels[x - 1][y + 1] = pixels[x - 1][y + 1] + quant_error * 3 / 16
                pixels[  x  ][y + 1] = pixels[ x ][y + 1] + quant_error * 5 / 16
                pixels[x + 1][y + 1] = pixels[x + 1][y + 1] + quant_error * 1 / 16
        
        
        #print(pixels)
        img_matrix.matrix = pixels
        img_matrix_1D = Utils.MatrixObjectTo1DList(img_matrix.matrix)
        DITHERED_IMAGE = PIL.Image.fromarray(img_matrix_1D)

        return DITHERED_IMAGE
    



class Mixer:
    
    def PlayMelody(melody_string):
        
        import sounds
        print(sounds.sound_dict)
        soundArray = melody_string.split(",")
        melodyToPlay = Mixer.AudioClip()
        for sound in soundArray:
            print(sounds.sound_dict[sound])
            current_sound = Mixer.Sound(sounds.sound_dict[sound], 500)
            melodyToPlay.AppendSound(current_sound)
        print(melodyToPlay.soundArray)
        melodyToPlay.Play()
        print("played")
    
    class Sound:
        def __init__(self, hz, time_ms):
            self.HZ = hz
            self.time_ms = time_ms
        
        def Play(self):
            import winsound
            winsound.Beep(self.HZ , self.time_ms)
    
   
# an array of sound objects, with a tempo
    class AudioClip:
        def __init__(self):
            self.tempo = 0
            self.soundArray = []
            
            import threading, time

            self.play_thread = threading.Thread(target=self.play_audio_clip)
            self.play_thread.daemon = True
        
        def play_audio_clip(self):
                import time
                print(self.soundArray)
                for sound in self.soundArray:
                    print("play")
                    if type(sound) is str and sound == "/":
                        time.sleep(0.25)
                        print("a")
                    else:
                        sound.Play()
                        print("ran")
        
        def AppendSound(self,sound):
            self.soundArray.append(sound)
        
        def AddSound(self, sound, index):
            #shift array up one
            temp_shifted_array = [None] * ( len(self.soundArray) + 1 )
            #shift every list item up if it is less than the index given and not zero
            for x in range(len(self.soundArray)):
                if x >= index:
                    temp_shifted_array[x+1] = self.soundArray[x]
                else:
                    temp_shifted_array[x] = self.soundArray[x]
            
            
            # set freed item to the sounds hz
            #print(temp_shifted_array)
            if sound == "/":
                temp_shifted_array[index] = "/"
            else:
                try:
                    temp_shifted_array[index] = sound
                except TypeError:
                    print("Error: for pauses, use '/'")

            
            # set the audioclips array to the shifted, and updated one
            self.soundArray = temp_shifted_array

            #print(temp_shifted_array)
        
        def ReplaceSound(self, sound, index):
            self.soundArray[index] = sound
        
        def DeleteSound(self,index):
            temp_shifted_array = [None] * ( len(self.soundArray) - 1 )
            #shift every list item down if it is less than the index given and not zero
            for x in range(len(self.soundArray)):
                if x > index and x != 0:
                    temp_shifted_array[x-1] = self.soundArray[x]
                else:
                    temp_shifted_array[x] = self.soundArray[x]
            
            # set freed item to the sounds hz
            # set the audioclips array to the shifted, and updated one
            self.soundArray = temp_shifted_array

            print(temp_shifted_array)

        
        def Play(self):
            #play_thread = threading.Thread(target=play_audio_clip)
            #play_thread.daemon = True
            import threading
            self.play_thread.start()
        
        def Stop(self):
            self.play_thread.join()

        def PlayOnce(self):
            self.play_thread.start()
            self.play_thread.join()
    

        
        

class RigidBody2D:
    def __init__(self):
        self.isActive = False
        self.gravitationForce = 1

        self.drag = 0
        self.mass = 1

        self.x_velocity = 0
        self.y_velocity = 0

    def AddForce(self, forceVector: Vector2):
        self.x_velocity += (forceVector.x / self.mass)
        self.y_velocity += (forceVector.y / self.mass)


# Make These A Thing ✔
class Collider2D:
    
    def __init__(self, parentObject):

        self.isActive = False
        self.parentObject = parentObject
        self.colliderPositions = []
        self.isTrigger = False

        self.touched = False
        #self.screen = parentObject.sprite.screen
    
    def CheckForCollision(self,stepsF,stepsU):
        start = time.perf_counter()
        positions_dict = globals.object_positions.items()
        positionsToCheckForCollision = []
        parentObjPositions = []
        
        for item in positions_dict:
            tag = item[0]
            pos_array = item[1]
            if tag != self.parentObject.tag and globals.collidableTags:
                positionsToCheckForCollision.append(pos_array)

        positionsToCheckForCollisionsList = Utils.MatrixTo1DList(positionsToCheckForCollision)
        print("OLD OBJ POS V")
        print( [ v2.AsTuple() for v2 in globals.object_positions[self.parentObject.tag] ] )
        positionsToCheckForCollisionsList = [v2.AsTuple() for v2 in positionsToCheckForCollisionsList]
        for pos in self.parentObject.positions:
            parentObjPositions.append( (pos.x+stepsF, pos.y+stepsU) )
            #parentObjPositions.append( (pos.x, pos.y) )
        
        print("NEW OBJ POS V")
        print(parentObjPositions)

        print("OTHER POS V")
        print(positionsToCheckForCollisionsList)
        for obj_pos in parentObjPositions:
            if obj_pos in positionsToCheckForCollisionsList:
                end = time.perf_counter()
                print(end-start)
                return {"hit": True, "type": "collider"}
            
        else:
            end = time.perf_counter()
            print(end-start)
            return {"hit": False, "type": "None"}
        

            
        



class Utils:
    def Coinflip():
        from random import randint
        num = randint(0,1)
        if num == 1:
            return True
        return False
    def ListToMatrix(array, width, height):
        newMatrix = Mathf.Matrix2D(width, height)
        
        for y in range(height):
            current = y
            newMatrix.matrix[y] = array[ current*width : (current*width)+width ]
        
        return newMatrix.matrix     
    
    def RetrieveDictKeyAtIndex(_dict, index):
        return list(_dict.keys() )[index]
    
    def ChangeDictValueIndex(value, _dict, index):
        key = list( _dict.keys() )[index]
        _dict[key] = value
        return _dict

    def RandomString(length):
        string = str()

        allChars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@;:~#/?><-_=+`¬¦|!'$()%^&")
        from random import choice
        for add_chars_into_string in range(length):
            string += choice(allChars)
        return string
    
    def FileToMatrix(filename):
        arrayToReturn = []
        f = open(filename, "r", encoding="utf-8")
        dat = f.readlines()
        print(f"filename: {filename}")
        print(f"dat len {len(dat)}")
        newDat = dat[0].strip("\n")

        width = len(newDat)
        f.close()

        for line in dat:
            newline = line.strip("\n")
            arrayToReturn.append(list(newline))

        Matrix_To_Return = Mathf.Matrix2D(width, len(dat))

        Matrix_To_Return.matrix = arrayToReturn

        return Matrix_To_Return

    def layer_index(e):
        return e["layer_index"]

    # Basically legacy, and really really bad, however, since the entire library runs on it, it is staying.
    
    def ReplaceStringItemInMatrixArray(_list, newValue, index):
        new_string = str().join(_list)
        new_str = new_string[:index] + newValue + new_string[index + 1:]
        return list(new_str)

    def ReplaceStringItemInMatrixArrayButForTagMap(_list, newValue, index):
        new_string = ",".join(_list)
        new_str = new_string[:index] + newValue + new_string[index + 1:]
        return list(new_str)

    def CreateUniqueFilename(filename):
        import os
        num = 0
        name = filename
        while os.path.exists(filename + ".sprite"):
            num += 1
            filename = f"{name}({num})"
        return filename + ".sprite"
    
    def MatrixObjectTo1DList(mtrx: Mathf.Matrix2D):
        two_dim = mtrx.matrix
        one_dim_list = [n for one_dim in two_dim for n in one_dim]
        return one_dim_list

    def MatrixTo1DList(two_dim):
        one_dim_list = [n for one_dim in two_dim for n in one_dim]
        return one_dim_list


class InputHandler:

    def Listen():
        import keyboard, KeyCodes, time
        while True:
            if keyboard.read_key() in KeyCodes.KEYS.values():
                KEY = keyboard.read_key()
                #print(f"you pressed a valid key: '{KEY}'")

                # Parraallel Arrays, so if key is valid, run function
                # check if exists
                key_values = list(KeyCodes.KEYS.values())
                key_index = key_values.index(KEY)

                try:
                    # if exists run function
                    #print(globals.KEY_ASSIGNED_FUNCTIONS)
                    globals.KEY_ASSIGNED_FUNCTIONS[key_index]()
                    continue
                except TypeError:
                    #print("nuh uh")
                    #if not, redo loop
                    continue
    def WaitForKeyPress():
        import keyboard
        while True:
            KEY = keyboard.read_key()
            if KEY:
                return KEY 


    def AssignFunctionToKey(key, fn):
        import KeyCodes
        #print("ran")
        key_array = list(KeyCodes.KEYS.values())  # .index(key)
        key_index = key_array.index(key)
        if key in KeyCodes.KEYS.keys() or key in KeyCodes.KEYS.values():
            #print("in keys")
            globals.KEY_ASSIGNED_FUNCTIONS[key_index] = fn


class UI:
    class Text:
        def __init__(self,layer):
            self.text = "Text Here"
            self.bold = bool()
            self.underline = bool()
            self.color = []
            self.blink = bool()
            text_len = len(self.text)
            
            self.Text_Obj = _2D.Sprite("sprite_placeholderFORBADCODE.txt",self.layer)
            self.Text_Obj.spriteMatrix = Mathf.Matrix2D(text_len, 0)
        

    
    class Button:
        print("button")

class SceneManager:
    
    sceneBuildIndex = []
    print("cool")
    def LoadScene(sceneBuildIndex):
        return

class Scene:
    def __init__(self, sceneName: str, buildIndex: int):
        import os
        self.sceneName = sceneName
        self.buildIndex = buildIndex
        self.sceneWorldSpace = _2D.WorldSpace()
        
        self.sceneObjects = {}
        
        self.SCENE_DIR = f"{PROJECT_DIRECTORY}/{self.sceneName}"
        
        if not os.path.exists(self.SCENE_DIR):

            # make the scene directory

            os.mkdir(self.SCENE_DIR)
            # make the 'objdat' file for storing all objects data
            os.mkdir(self.SCENE_DIR + "/objdat")
            os.mkdir(self.SCENE_DIR + "/core")
            #shutil.copy("")
            return

# only supports 2d

class _2D:
    class Camera2D:
        # TODO: probably implement this for 3D 
        def __init__(self, position, scene):
            
            self.position_x = position.x
            self.position_y = position.y
            
            self.scene = scene
            
            self.world_space = scene.sceneWorldSpace
            
            self.width = 70
            self.height = 20


            self.BG_CHAR = "x"
            self.BG_COLOR = "0"
        def MoveSteps(self, steps_forward, steps_up):
            self.position_x += steps_forward
            self.position_y += steps_up
        
        def GetScreenPositions(self):
            
            ScreenDataPostitionsToAcquire = []
            ScreenDataMirror = []
            for y in range(self.height):
                for x in range(self.width):
                    ScreenDataPostitionsToAcquire.append( Vector2(   self.position_x+x    ,    self.position_y+y    ) )
                    ScreenDataMirror.append( Vector2(x,y) )

            
            #print([(v.x, v.y) for v in ScreenDataPostitionsToAcquire])
            
            return Vector2(ScreenDataPostitionsToAcquire, ScreenDataMirror)

        
        def GetCameraData(self):
            ScreenDataPostitionsToAcquire = self.GetScreenPositions().x
            ScreenDataMirror = self.GetScreenPositions().y
            # sort layers, and keep indexes
            
            layer_indexs = [   x["layer_index"] for x in self.world_space.LAYER_DATA   ]


            layer_dict = []

            for count, layer in enumerate(self.world_space.LAYERS):
                layer_dict.append( {"layerObj": layer,"layerIndex": self.world_space.LAYER_DATA[count]["layer_index"]} )
            #print(layer_indexs)
            

            layerSortOrderDict = sorted(layer_dict, key=lambda d: d['layerIndex']) 

            layerSortOrder = [x["layerObj"] for x in layerSortOrderDict]
            charMap = Mathf.Matrix2D(self.width,self.height)
            colorMap = Mathf.Matrix2D(self.width,self.height)
            print("RUN")
            print("layers V")
            print(self.world_space.LAYERS)
            #FIXME 🟨🟨🟨🟨🟨
            # FLAGGED ISSUE: LayerSortOrder is empty for some reason
            # need to define the world space in worldspace
            # still something to do with layers
            print(layer_dict)
            for currentLayerIndex, layer in enumerate(layerSortOrder):
                #print("iter")
                worldLayerCharMatrix = layer.layerCharMatrix
                worldColorMatrix = layer.layerColorMatrix
                worldTagMap = layer.layerTagMatrix

                
                tagMap = Mathf.Matrix2D(self.width, self.height)
                

                # Get Tag map in cameras view
                for count, pos in enumerate(ScreenDataPostitionsToAcquire):
                    tagMap.matrix[ScreenDataMirror[count].y][ScreenDataMirror[count].x] = worldTagMap[pos.y][pos.x]
                
                #print(tagMap.matrix)
                for y in range(tagMap.height):
                    #print(f"tagMap.height")
                    for x in range(tagMap.width):
                        position = ScreenDataMirror[count]
                        WorldPosition = ScreenDataPostitionsToAcquire[count]
                        tag = tagMap.matrix[y][x]
                        if tag == "bg":
                            
                            #print("BG, IGNORE")
                            #print("True")
                            if currentLayerIndex == 0:
                                #print("alsoTrue")
                                charMap.matrix[y][x] = self.BG_CHAR
                                colorMap.matrix[y][x] = self.BG_COLOR

                            
                            else:
                                continue
                        else:
                            #print("CHANGE")
                            #print(f"x: {x} y: {y}")
                            charMap.matrix[y][x] = worldLayerCharMatrix[y+self.position_y][x+self.position_x]
                            colorMap.matrix[y][x] = worldColorMatrix[y+self.position_y][x+self.position_x]

                    #print(charMap.matrix)
            #print(colorMap.matrix)
            #print(charMap.matrix)
            return {"charMap": charMap, "colorMap": colorMap}

        def CameraDatToFile(self):
            CameraData = self.GetCameraData()
            char_file = open("camera.scrn","w",encoding="utf-8")
            color_file = open("camera.cDAT","w")
            
            char_mtrx = CameraData["charMap"].matrix
            color_mtrx = CameraData["colorMap"].matrix
            for y in range(len(char_mtrx)):
                char_file.write(char_mtrx[y]+"\n")
                color_file.write(color_mtrx[y]+"\n")
            char_mtrx.close()
            color_file.close()


        def Display(self):
            from termcolor import cprint
            import colorama

            colorama.just_fix_windows_console()
            CameraData = self.GetCameraData()
            charMatrix = CameraData["charMap"].matrix

            #print(charMatrix)
            colorMatrix = CameraData["colorMap"].matrix
            #print(colorMatrix)
            for y in range(len(charMatrix)):
                for x in range(len(charMatrix[y])):
                    
                    color_code = colorMatrix[y][x]
                    
                    #print(colorMatrix[y][x])

                    color_code_as_int = int(color_code)
                    #print("a",end="")
                    print(f"\033[38;5;{color_code_as_int}m{charMatrix[y][x]}\033", end="")
                
                print("")
            print(f"\033[38;5;{1}m\033", end="")

            return

    
    class WorldSpace:
        def __init__(self):
            self.WorldSpaceMatrix = Mathf.Matrix2D(3000,3000)
            
            self.LAYERS = []
            self.LAYER_DATA = []

    class Layer:
        def __init__(self, layerIndex: int, layerName: str, parent_scene):
            self.layerIndex = layerIndex
            self.layerName = layerName

            self.parent_scene = parent_scene
            self.parent_world_space = parent_scene.sceneWorldSpace
            width, height = self.parent_world_space.WorldSpaceMatrix.width, self.parent_world_space.WorldSpaceMatrix.height
            
            self.layerCharMatrix = [[" "] * width for _ in range(height)]
            self.layerColorMatrix = [["0"] * width for _ in range(height)]
            self.layerTagMatrix = [["bg"] * width for _ in range(height)]
            
            self.Create_Layer()
       
        def Create_Layer(self):
            
            self.parent_world_space.LAYER_DATA.append(  
            {"layer_index": self.layerIndex, "layer_file": self.layerName}  
            )
            
            self.parent_world_space.LAYERS.append(self)
            print("Create_Layer() debug stuff V")
            print(self.parent_world_space)
            print(self.parent_world_space.LAYERS)
            print(self.layerName)
            print("--------------------")
         
    
    class Line:
        def __init__(self,pointA: Vector2,pointB:Vector2):
            
            self.pointA = pointA
            self.pointB = pointB
            
            self.points = Mathf.Get2DLinePoints(pointA, pointB)
            self.length = len(self.points)
            
            
            self.minX = min([pointA.x, pointB.x])
            self.minY = min([pointA.y, pointB.y])

            self.maxX = max([pointA.x, pointB.x])
            self.maxY = max([pointA.y, pointB.y]) 
            
            self.width = self.maxX - self.minX 
            self.height = self.maxY - self.minY

           

    
            
    class Pixel:

        def __init__(self, char: str, color: str, layer):
            self.char = char
            self.color = color

            #self.screen = screen
            self.layer = layer

        def __str__(self):
            return self.char

        def Stamp(self, position):
            
            self.x = position.x
            self.y = position.y

            self.previousChar  = self.layer.layerCharMatrix[self.y][self.x]
            self.previousColor = self.layer.layerColorMatrix[self.y][self.x]
            self.previousTag = self.layer.layerTagMatrix[self.y][self.x]

            
            #print(self.layer.layerTagMatrix)
            """if os.path.exists(self.layer.layerName + ".txt") is False:
                print("Layer does not exist")
                sys.exit()
            else:"""
                
            # 🟨 i think the bug is resulting from either the movesteps func, the addtolayer func or the object stamp func
            # FIXME: this
            if self.char != globals.IGNORE_CHAR or self.char != "x":
                
                self.layer.layerCharMatrix[self.y][self.x] = self.char
                
                self.layer.layerColorMatrix[self.y][self.x] = self.color
                
                self.layer.layerTagMatrix[self.y][self.x] = "_"
                
                '''temp = self.layer.layerTagMap[self.y]
                temp[self.x] = "_"'''
            
            else:
                print("EXITS") 
                print(self.previousChar)
                print(self.previousColor)
                # delete the object and replace it with whatever was there before
                # update
                print("it should update, and has updated, howerver it is overwritten at some point")
                
                self.layer.layerCharMatrix[self.y][self.x] = self.previousChar
                self.layer.layerColorMatrix[self.y][self.x] = self.previousColor
                self.layer.layerTagMatrix[self.y][self.x] = self.previousTag
                # check if char is the ignore character, if so, then give it the "bg" tag
                #if self.char != globals.IGNORE_CHAR and self.char != self.screen.BG_CHAR:

                # print(self.layer.layerTagMap)

                # print(self.layer.layerTagMap)
                #self.layer.AddToLayer()

    class Sprite(object):
        def __init__(self, sprite_file: None, layer):
            
            self.sprite_file = sprite_file
            self.layer = layer

            self.spriteMatrix = Utils.FileToMatrix(sprite_file)

            print(type(self.spriteMatrix))
            file_name = sprite_file.split(".")[0]
            self.spriteColorMatrix = Mathf.Matrix2D(self.spriteMatrix.width, self.spriteMatrix.height)

            temp_matrix = []
            cf = open(file_name+".cDAT","r",encoding="utf-8") 
            dat = cf.readlines()
            for i in range(len(dat)):
                
                strippedRow = dat[i].strip("\n")
                temp_matrix.append( strippedRow.split(",") )

            self.spriteColorMatrix.matrix = temp_matrix
            #fart.append(dat.split(","))
            cf.close()
            print(temp_matrix)

            self.flippedX = False
            self.flippedY =  False
            self.x = 0
            self.y = 0

            self.previousCharMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )
            self.previousColorMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )
            self.previousTagMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )

        def Image(src_file, WIDTH,HEIGHT, layer, screen, dither: bool):
            name = src_file.split(".")[0]
            import PIL.Image
            sprite_image = PIL.Image.open(src_file).convert('L')
            width, height = sprite_image.size
            detailed = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,'.")
            print(detailed)
            simple = list("@%#*+=-:.")


            #sprite_image.show()

            ratio = height / width
            new_height = HEIGHT

            resized_image = sprite_image.resize((WIDTH, new_height))

            pixels = resized_image.getdata()
            characters = "".join([detailed[pixel//25] for pixel in pixels])

            pixel_count = len(characters)
            new_width = WIDTH
            ascii_image = "\n".join(characters[i:(i+new_width)] for i in range(0, pixel_count, new_width))
            print(ascii_image)

            with open(name+".sprite","w",encoding="utf-8") as img:
                img.write(ascii_image)

            img.close()
            with open(name+".cDAT","w",encoding="utf-8") as c_img:
                for i in range(HEIGHT):
                    c_img.write( ("w"*WIDTH) + "\n")

            c_img.close()



            return _2D.Sprite(name+".sprite", layer=layer)


        def Rect(_char, color, width, height, layer):
            file_name = Utils.CreateUniqueFilename("Square")
            sq_f = open(file_name, "w")
            sq_matrix = Mathf.Matrix2D(width, height)
            sq_color = open(file_name.split(".")[0] + ".cDAT", "w")
            for line in range(len(sq_matrix.matrix)):
                sq_f.write(_char * width + "\n")
                sq_color.write( (color+",") * width + "\n")

            sq_f.close()
            sq_color.close()

            print("written")

            return _2D.Sprite(sprite_file=file_name, layer=layer)

        # FIXED THIOS 😀
        def Line(_char: str,color, pointA: Vector2, pointB: Vector2, layer, screen):

            line_obj = _2D.Line(pointA,pointB)

            lineMatrix = Mathf.Matrix2D(line_obj.width+1, line_obj.height+1)
            lineColorMatrix = Mathf.Matrix2D(line_obj.width+1, line_obj.height+1)
            print(f"width: {line_obj.width}, height: {line_obj.height}")
            print(line_obj.points)
            
            # fill in the matrix (chars)
            for line in lineMatrix.matrix:
                for i in range(len(line)):
                    line[i] = screen.BG_CHAR
            
            for colored_line in lineColorMatrix.matrix:
                for i in range(len(colored_line)):
                    colored_line[i] = screen.BG_CHAR
            
            for index, current_point in enumerate(line_obj.points):

                print("A")
                print(current_point)
                print(f"to change: {pointA.x},{pointA.y}")
                print("adjusted")
                print(current_point.y-pointA.y)
                print(current_point.x-pointA.x)
                

                lineMatrix.matrix[current_point.y-pointA.y][current_point.x-pointA.x] = _char
                lineColorMatrix.matrix[current_point.y-pointA.y][current_point.x-pointA.x] = color

                
            
            f = open("aDJhkvnfwf.sprite","w")
            c = open("aDJhkvnfwf.cDAT","w")
            for y in range(line_obj.height):
                f.write("." * line_obj.width + "\n")
                c.write("w"* line_obj.width + "\n")
            f.close(); c.close()
            
            line_sprite = _2D.Sprite("aDJhkvnfwf.sprite",layer,screen)
            
            line_sprite.spriteMatrix.matrix = lineMatrix.matrix
            line_sprite.spriteColorMatrix.matrix = lineColorMatrix.matrix

            return line_sprite
        

        
        def FlipX(self):
            if self.flippedX is False:
                for y in range(len(self.spriteMatrix.matrix)):
                    lineAsArray = list(self.spriteMatrix.matrix[y])
                    lineAsArray.reverse()
                    colorLinesAsArray = list(self.spriteColorMatrix.matrix[y])
                    colorLinesAsArray.reverse()
                    self.spriteMatrix.matrix[y] = ''.join(lineAsArray)
                    self.spriteColorMatrix.matrix[y] = ''.join(colorLinesAsArray)
                print("change")
                self.flippedX = True

        def FlipY(self):
            if self.flippedY is False:
                self.spriteMatrix.matrix.reverse()
                self.spriteColorMatrix.matrix.reverse()
                self.flippedY = True

        # finish this for colors

        def Rotate(self):
            # transpose matrix
            rot = Mathf.Matrix2D(self.spriteMatrix.height, self.spriteMatrix.width)
            rot = Mathf.Matrix2D.Transpose(self.spriteMatrix)

            colorRot = Mathf.Matrix2D(self.spriteColorMatrix.height, self.spriteColorMatrix.width)
            colorRot = Mathf.Matrix2D.Transpose(self.spriteColorMatrix)
            # reverse the matrix
            rot.Reverse()
            colorRot.Reverse()

            rotMatrix = rot.matrix
            colorRotMatrix = colorRot.matrix

            print("rot matrix")
            for line in rot.matrix:
                print(''.join(line))
            #set sprites data to the new rotated data
            self.spriteMatrix.matrix = rotMatrix
            self.spriteColorMatrix.matrix = colorRotMatrix

            # adjust sprite matrixs size to prevent errors
            self.spriteMatrix.width = len(rotMatrix[0])
            self.spriteMatrix.height = len(rotMatrix)

            self.spriteColorMatrix.width = len(colorRotMatrix[0])
            self.spriteColorMatrix.height = len(colorRotMatrix)
            

            self.previousCharMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )
            self.previousColorMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )
            self.previousTagMatrix = Mathf.Matrix2D( self.spriteColorMatrix.width, self.spriteColorMatrix.height )
            #self.FlipX()


            

        def Stamp(self, position: Vector2):
            self.x = position.x
            self.y = position.y
            # rrrrr
            #print(self.spriteMatrix.matrix)
            #print(type(self.spriteColorMatrix))

            if len(self.spriteMatrix.matrix) != len(self.spriteColorMatrix.matrix):
                print("sprite size does not match the color data")
            for y in range(len(self.spriteMatrix.matrix)):
                # print(len(self.spriteMatrix.matrix))
                #print(len(self.spriteMatrix.matrix))
                #print(f"{len(self.spriteColorMatrix.matrix)}")
                for x in range(len(self.spriteMatrix.matrix[y])):
                    
                    #try:r
                    if self.spriteMatrix.matrix [y][x] != globals.IGNORE_CHAR:
                        #print(f"iter {x}")
                        #print("char V")
                        #print(self.spriteMatrix.matrix [y][x])
                        new_pixel = _2D.Pixel(
                            self.spriteMatrix.matrix[y][x], 
                            self.spriteColorMatrix.matrix[y][x],
                            self.layer
                        )
                        new_pixel.Stamp(Vector2(self.x + x, self.y + y))
                    else:
                        print("great")
                    """self.previousCharMatrix.matrix[y][x] = new_pixel.previousChar
                    self.previousColorMatrix.matrix[y][x] = new_pixel.previousColor
                    self.previousTagMatrix.matrix[y][x] = new_pixel.previousTag"""
                    
                    """except:
                       print(len(self.spriteMatrix.matrix))
                        print(len(self.spriteMatrix.matrix[y]))
                        print(f"x: {x}, y: {y}")
                        print("unable to stamp")"""

    class Animation:
        
        def __init__(self,parentObject):
            import threading
            self.parentObject = parentObject
            
            self.frames = []
            self.time_between_frames = 0.3
            
            self.hasCondition = bool()
            self.conditionalBool = bool()

            self.animThread =  threading.Thread(target=self.Frames())
        def Frames(self):
            frameCharFiles = []
            frameColorFiles = []
            for frameName in self.frames:
                frameCharFiles.append(frameName+".sprite")
                frameColorFiles.append(frameName+".cDAT")
            
            for frame_index in range(len(frameCharFiles)):
                self.parentObject.Destroy()
                currentFrameCharMatrix = Utils.FileToMatrix(frameCharFiles[frame_index])
                currentFrameColorMatrix = Utils.FileToMatrix(frameColorFiles[frame_index])
                
                self.parentObject.sprite.spriteMatrix.matrix = currentFrameCharMatrix.matrix
                self.parentObject.sprite.spriteColorMatrix.matrix = currentFrameColorMatrix.matrix
                
                self.parentObject.Stamp()
                #self.parentObject.sprite.screen.OrderLayersToDisplay()
                show()
        
        def Play(self):
            self.animThread.daemon = True
            self.animThread.start()

        def Stop(self):
            self.animThread.join()
            


    class Object(object):
        def __init__(self, sprite, tag, position: Vector2):
            self.sprite = sprite
            self.tag = tag
            self.position = position
            self.id = Utils.RandomString(8)
            self.RigidBody2D = RigidBody2D()
            self.Collider = Collider2D(self)

            self.layer = self.sprite.layer
         
            self.tagMatrix = [ [ [None] * len(self.sprite.spriteMatrix.matrix[0]) for _ in range(len(self.sprite.spriteMatrix.matrix))] ]
            self.positions = []

            self.Rotation = 0
            self.enabled = True

            if self.Collider.isActive and self.Collider.isTrigger is False:
                globals.collidableTags.append(self.tag)
            #print("type")
            #print( type(self.sprite) )
            globals.all_tags.append(self.tag)
            #print("_PREFAB" in self.tag)
            if "_PREFAB" not in self.tag:
                self.Update()
        def Update(self):
            import json
            # updayte the objects json file
            dat_dict = {
                "pos": (self.position.x, self.position.y), 
                "tag": self.tag,
                "layer_index": self.layer.layerIndex, 
                "sprite_chars": self.sprite.spriteMatrix.matrix,
                "sprite_colors": self.sprite.spriteColorMatrix.matrix,
                "has_collider": self.Collider.isActive,
                "enabled": self.enabled
            }
            #print(dat_dict)

            with open("objdata/"+ self.tag+"_OBJ"+".json", "w") as fp:
                json_string = json.dump(dat_dict, fp) 
                #fp.write(json_string)
            return
        
        def Stamp(self):
            
            #print(self.Collider.isActive)
            
            globals.collidableTags.append(self.tag)
            self.sprite.FlipY()
            if self.Collider.isActive:
                #print("TRUE")
                if self.Collider.isTrigger is False:
                    if self.tag not in globals.collidableTags:
                        globals.collidableTags.append(self.tag)

            self.sprite.Stamp(self.position)

            for y in range(len(self.sprite.spriteMatrix.matrix)):
                for x in range(len(self.sprite.spriteMatrix.matrix[y])):
                    #fix this, so it completely works //  🟩 FIXED 😁 LETS GOOOOOOOOOOOOOOOOOOOOO
                    
                    if self.layer.layerTagMatrix[ self.position.y + y ][ self.position.x + x ] != "bg":
                        self.positions.append(Vector2(self.position.x + x, self.position.y + y))
                    
                    
                    pixel = self.sprite.spriteMatrix.matrix[y][x]
                    if pixel == globals.IGNORE_CHAR:
                        
                        # set it to itself, hope this works
                        self.sprite.layer.layerTagMatrix[self.position.y + y][self.position.x + x] = self.sprite.layer.layerTagMatrix[self.position.y + y][self.position.x + x]

                    else:
                        self.sprite.layer.layerTagMatrix[self.position.y + y][self.position.x + x] = self.tag

            #print(globals.collidableTags)
            #print(globals.triggerTags)

            globals.object_positions[self.tag] = self.positions
            #self.sprite.layer.AddToLayer()
        def Rotate(self):
            self.Rotation += 90
            self.Destroy()
            self.sprite.Rotate()
            

        def MoveSteps(self, stepsForward, stepsUp):
            self.old_pos = self.position
            new_pos = Vector2(self.position.x + stepsForward, self.position.y + stepsUp)
            
            print(self.Collider.isActive)
            if self.Collider.isActive == True:
                print("collider on")
                from time import perf_counter
                if self.Collider.CheckForCollision(stepsForward, stepsUp).get("hit") == True:
                    print("HIT")
                    return

                else:
                    print(new_pos)
                    self.position = new_pos
                    print("Destrpy")
                    self.Destroy()
                    self.Stamp()
                    
                    print("V EXEC TIME V")
                    
                    #print(execution_time)

            else:
                self.position = new_pos
                self.Destroy() 
                self.Stamp()

        
        def SetPosition(self, new_pos: Vector2):
            if self.Collider.isActive == True:
                if self.Collider.CheckForCollision(new_pos):
                    return
                elif self.Collider.CheckForCollisionn(new_pos) == "Trigger":
                    # do something with triggers
                    print("trigger activated")
            
            self.position = new_pos
            self.Destroy()
            self.Stamp()
        def FlipY(self):
            self.sprite.FlipY()
            self.tagMatrix.reverse()
        
        # Fix This
        def Destroy(self):
            self.layer = self.sprite.layer
            globals.collidableTags.remove(self.tag)
            print("positions being destroyed")
            print(len(self.positions))
            

            #NOTE: basically, it needs to catch up, and is destroying objects at a position where
            #FIXME
            for pos in self.positions:
                if self.layer.layerTagMatrix[pos.y][pos.x-1] != self.tag:
                    #print("RAN")
                    print(pos.AsTuple())
                    print("EPIC")
                    print(self.layer.layerTagMatrix[pos.y][pos.x])
                    if self.layer.layerTagMatrix[pos.y][pos.x] != self.tag:
                        continue
                    else:
                        self.layer.layerCharMatrix[pos.y][pos.x] = "x"
                        self.layer.layerColorMatrix[pos.y][pos.x] = 0
                        self.layer.layerTagMatrix[pos.y][pos.x] = "bg"
                
                                                                                                                              
            self.positions.clear()
    class Prefab(Object):
    
        def __init__(self, obj):
            self.object = obj
            # inherit EVERYTHING from object
            
            super().__init__(self.object.sprite, self.object.tag, self.object.position)
            new_tag = self.tag+"_PREFAB_"+Utils.RandomString(5)
            self.tag = new_tag
            
        def Instantiate(self, position):
            import random
            
            self.object.position = position
            instantiated_object = _2D.Object(self.sprite, self.tag ,position)
            instantiated_object.Stamp()

    class Ray:
        def __init__(self, origin: Vector2, direction_degrees: int, scene):
            import math
            self.layer = ""
            self.length = 60
            self.maxRayLength = 60

            self.scene = scene

            self.world_space = scene.sceneWorldSpace
            
            self.origin = origin
            self.direction = Mathf.DegToRads(direction_degrees)
            #last_angle = (180 - self.direction + 90)
            
            if direction_degrees == 0 or direction_degrees == 360:
                print("0 degs")
                self.endPoint = Vector2(origin.x+self.length, origin.y)
            
            elif direction_degrees == 180:
                self.endPoint = Vector2(origin.x-self.length, origin.y)

            elif direction_degrees == 90:
                self.endPoint = Vector2(origin.x, origin.y+self.length)
            
            elif direction_degrees == 270:
                self.endPoint = Vector2(origin.x, origin.y-self.length)
            
            else:
                self.endPoint = Vector2(
                int(origin.x + self.length * math.cos(self.direction)), 
                int(origin.y + self.length * math.sin(self.direction))
                )


            print(f"ENDPOINT X: {self.endPoint.x}ENDPOINT Y: {self.endPoint.y}")
            
            self.rayPoints = Mathf.Get2DLinePoints(self.origin, self.endPoint)

            self.layerMask = "_"
            print("sin check")
            print(math.sin(45))
        def HasLayerMask(self):
            if self.layerMask != "_" or self.layerMask != "bg":
                return True
            else:
                return False
        
        def HitCheck(self):
            # REWRITE THIS
            # loop through all layer tag maps
            #note positions of tags that are not bg
            #check if any ray positions are in the tagPositions
            # if so return a dictionary with the data e.g
            # return {"wasHit": True, "tag": "test", "hitPos": pos }

            #hit = ray.HitCheck()
            #if hit.get("wasHit") == True and hit.get( "tag" ) == "test":
            ray_positions = []
            rayPosTuple = []
            
            
            
            for point in self.rayPoints:
                ray_positions.append( Vector2(point.x, point.y) )
            
            for pos in ray_positions:
                rayPosTuple.append( (pos.x, pos.y) )
            
            positions_dict = globals.object_positions.items()
            collision_dict = [x for x in positions_dict if x[0] in globals.collidableTags]

            collisions = [pos[1] for pos in positions_dict]

            coll1DList = Utils.MatrixTo1DList(collisions)
            coll1DTuple = []
            for pos in coll1DList:
                coll1DTuple.append( (pos.x, pos.y) )

            print(rayPosTuple)
            print(coll1DTuple)
            for pos in rayPosTuple:
                if pos in coll1DTuple:
                    # hit
                    return {"hit": True, "hit_pos": Vector2(pos[0],pos[1])}
            
            #miss
            
            return {"hit": False, "hit_pos": None}

            
class _3D:

    foo = ""


def show():
    print("RAN")
    screen = open("screenData.txt", "r")
    dat = screen.readlines()
    dat.reverse()
    print("=" * 60)
    for line in dat:
        newline = line.strip("\n")
        print(newline)

# EXAMPLE CODE
if __name__ == "__main__":
    
    
    SampleScene = Scene("SampleScene", 0)
    SampleScene.sceneWorldSpace = _2D.WorldSpace()
    
    
    Mixer.PlayMelody("A2,B2,C2")
    import winsound
    #winsound.Beep(600,50)
    SampleLayer = _2D.Layer(6, "SampleLayer", SampleScene)
    spr = _2D.Sprite("man.txt",SampleLayer)
    my_obj = _2D.Object(spr, "OBJ_1",Vector2(0,0))
    
    #print(my_obj.__dict__)
    print()
    
    
    
    
    BackLayer = _2D.Layer(3,"BG_LAYER", SampleScene)
    BackLayer.Create_Layer()
    SampleLayer.Create_Layer()
    
    Camera = _2D.Camera2D(Vector2(1,0), SampleScene)

    Camera.BG_CHAR = " "
    Camera.height = 50

    

    pixel = _2D.Pixel("@",7,BackLayer)
    print("aaaaaaaaaaaaaaaaaaaaaaaaa")
    sprite = _2D.Sprite("Square.sprite",SampleLayer)
    pixel.Stamp(Vector2(20,10))


    #sprite.Stamp(Vector2(10,3) )
    square2 = _2D.Object(sprite,"fart", Vector2(10,0) )
    
    tetris_block = _2D.Sprite("water.sprite",SampleLayer)
    square2.Collider.isActive = True
    square2.Stamp()
    silly_object = _2D.Object(tetris_block,"man", Vector2(0,2) )
    silly_object.Collider.isActive = True
    silly_object.Stamp()
    
    myRay = _2D.Ray(Vector2(7,0),33, SampleScene)
    myRay.HitCheck()
    print(myRay.HitCheck())

    #Camera.Display()
    #silly_object.MoveSteps(1,0)
    #print("RAN")
    #Camera.Display()
    import time
    def Tidal_EXIT():
        import sys
        print("ended")
        sys.exit()
    def MoveR():
        start = time.perf_counter()
        silly_object.MoveSteps(1,0)
        end = time.perf_counter()
        print(end-start)
        Camera.Display()
        
    def MoveL():
        silly_object.MoveSteps(-1,0)
        Camera.Display()
    def MoveU():
        silly_object.MoveSteps(0,-1)
        Camera.Display()
    def MoveD():
        silly_object.MoveSteps(0,1)
        Camera.Display()
    
    def Rotate():
        silly_object.Rotate()
        silly_object.Stamp()
        Camera.Display()

    import KeyCodes
    InputHandler.AssignFunctionToKey(KeyCodes.RIGHT, MoveR)
    InputHandler.AssignFunctionToKey(KeyCodes.LEFT, MoveL)
    InputHandler.AssignFunctionToKey(KeyCodes.UP, MoveU)
    InputHandler.AssignFunctionToKey(KeyCodes.DOWN, MoveD)
    
    InputHandler.AssignFunctionToKey(KeyCodes.ESC, Tidal_EXIT)
    
    InputHandler.AssignFunctionToKey(KeyCodes.R, Rotate)
    InputHandler.Listen()