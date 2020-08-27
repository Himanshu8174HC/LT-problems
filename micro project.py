import os, shutil
dict_extensions= {
    "audio_extension" : ('.3gp','.mp3', '.m4a', '.wav', '.flac','.aiff','aiac','m4p','wma'),
    "video_extension" : ('MP4', 'mp4', 'm4a', 'm4v', 'f4v', 'f4a', 'm4b', 'm4r', 'f4b', '.MOV', '3GP', '3gp', '3gp2', '3g2', '3gpp', '3gpp2','AVI','.mkv', '.MKV', '.flv', '.mpeg'),
    "reader_extension" : ('.doc', '.pdf', '.txt','.DOC','.DOCX','.HTML','.HTM','.PPT','.PPTX'),
    "image_extension" : ('.JPG', '.PNG',)
}

folderpath=input("enter the folder path:")
def file_finder(folder_path, file_extensions):
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]
    
for extension_type,extension_tuple in dict_extensions.items():
    if len(file_finder(folderpath,extension_tuple)) > 0:
        folder_name = extension_type.split('_')[0] + ' Files'
        folder_path = os.path.join(folderpath, folder_name)
        os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)  
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)

