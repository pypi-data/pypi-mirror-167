#/*
# * Copyright 2018 Marwan Kilani
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *    http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# */

from pathlib import Path

class Reader :
    @staticmethod
    def  readFile( fileName_str) :

        fileName = Path(fileName_str)
        text = ""
        # The name of the file to open.
        # This will reference one line at a time
        line = None
        try :
            # FileReader reads text files in the default encoding.
            f = open(fileName, "r")
            lines = f.readlines()
            for line in lines:
                text = text + line #+ "\n"
            # Always close files.

        except FileNotFoundError:
            print("Unable to open file - File not found \'" + str(fileName) + "\'")
        else :
            empty = 0
            #print ("File read")
            #print("Error reading file \'" + str(fileName) + "\'")
        return text