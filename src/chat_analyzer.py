from pathlib import Path
import re
from typing import Union
class Chat_Analyser:
    def __init__(chat_file):
        # TODO Add execption when file is not passed
        self.chat_file = Path(chat_file)
        #TODO Add exception when person name and group name is not provided
        self.name,self.group_name = self.chat_file.stem.split("_")
        # Reading WhatsApp data files
        with open('chat.txt', 'r') as handle:
            self.group_data  = handle.readlines()

        @staticmethod
        def handel_void_outputs(Data_extractor_output:str = "")-> Union[list,None]:
            """this function returns a none value if list is empty"""
            if type(Data_extractor_output) == type(re.match('','')):
                # This is to handel name or mobile number in person name feild
                if Data_extractor_output.groups()[0] != None:
                    return Data_extractor_output.groups()[0]
                else :
                    return Data_extractor_output.groups()[1]
            elif Data_extractor_output is None:
                return None
                # This is to handel meessages,date and time
            elif  len(Data_extractor_output) == 0:
                return None
            else:
                return(Data_extractor_output[0])
        
        def data_extractor(self.group_data:str = "")-> dict: 
            """this function extracts date,time,name,messages"""
            # this is to extract dates from data
            date = self.handel_void_outputs(re.findall('\d{2}\/\d{2}\/\d{2}',self.group_data))
            # This is to extract time from data
            time = self.handel_void_outputs(re.findall('\d{2}\:\d{2}',self.group_data))
            # This is to extract name or mobile number from the data
            name = self.handel_void_outputs(re.search('-\s([\w\s@\-_@\!\*\#]+)|-\s(\+\d{2}\s\d{5}\s\d{5})',self.group_data))
            # this is to extract messages from the data 
            messages = self.handel_void_outputs(re.findall(':\s[\w\s@\-_\$\@\!\*\#\.\(\)\[\]\>\<\+\&]*.*',self.group_data))
            return({'Date':date,'Time':time,'Name_or_number':name,'Messages':messages,})


        
        def create_chat_data_frame(self):
            """here we are mapping Data_extractor function with self.group_datas"""
            data_frame_whatsapp_chat = pd.DataFrame(map(data_extractor,self.group_data))
            # this is to remove te none values from the data frame
            data_frame_whatsapp_chat_without_null_values = data_frame_whatsapp_chat.dropna()
            return data_frame_whatsapp_chat_without_null_values

        def most_active_member_in_group()
        