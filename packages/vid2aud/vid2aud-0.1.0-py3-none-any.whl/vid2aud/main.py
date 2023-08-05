import ffmpeg
import numpy as np
import subprocess
from soundscape_IR.soundscape_viewer  import lts_maker
import os

class vid2aud:
  def __init__(self, path = None, folder_id = None, file_format = '.mp4'):  
    if(folder_id):
      LTS_run=lts_maker()
      LTS_run.collect_Gdrive(folder_id, file_extension = file_format)
      temp=LTS_run.Gdrive.file_list      
      self.filelist = []
      for i in range(len(temp)):
        self.filelist.append(temp[i]['title'])
      self.gdrive = LTS_run
    
    if(path):
      allfiles = os.listdir(path)
      self.filelist = [ fname for fname in allfiles if fname.endswith('.mp4')]
      self.path = path

    if(len(self.filelist) == 0):
      print('Identified no file')   
    else:
      for i in range(0,len(self.filelist)):
        print('File No.'+str(i+1)+': '+str(self.filelist[i]))
  
  def metadata(self):
    vid = ffmpeg.probe(self.dir)
    self.bit_rate = str(int(np.ceil(int(vid['streams'][1]['bit_rate'])/1024)))
    self.sampleing_rate = str(vid['streams'][1]['sample_rate'])
    self.channels = str(vid['streams'][1]['channels'])
    print('Video filename = ' + self.filename)
    print('Audio filename = ' + self.audio_name+self.audio_format)
    print('Audio channels = ' + self.channels)
    print('Audio sampleing rate = ' + self.sampleing_rate)

  def convert(self, file_no = 0, audio_name = 'audio', audio_format = '.wav'):
    self.audio_name = audio_name
    self.audio_format = audio_format

    if(hasattr(self, 'gdrive')):
      temp=self.gdrive.Gdrive.file_list[file_no-1]
      temp.GetContentFile(temp['title'])
      self.filename = temp['title']
      self.dir = './'+self.filename
      
    else:
      self.filename = self.filelist[file_no-1]
      self.dir = self.path+'/'+self.filename
    
    self.metadata()    
    command = 'ffmpeg -i '+self.dir+' -ab '+self.bit_rate+'k -ac '+self.channels+' -ar '+self.sampleing_rate+' -vn '+self.audio_name+self.audio_format
    subprocess.call(command, shell=True)