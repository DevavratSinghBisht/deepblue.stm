from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage

from .utils import *
from .models import summarizer, asr

from pathlib import Path
import itertools
import os

def summary(request):
    
    if request.method == 'POST':
        file = request.FILES['meeting_file']

        doc_extensions = ['doc', 'docx']
        audio_extensions = ['mp3', 'wav']
        video_extensions = ['mp4']
        suported_extensions = list(itertools.chain(
                                                    doc_extensions,
                                                    audio_extensions,
                                                    video_extensions,
                                                   ))
        extension = file.name.split('.')[-1]
        
        if extension in suported_extensions:
            
            save_dir = f'summarizer/data/{extension}/'
            fs = FileSystemStorage(location=save_dir)
            f = fs.save(file.name, file)
            file_location = save_dir + f

            if extension in doc_extensions:
                meet = TeamsMeet.from_doc(file_location)
                summary = summarizer.summarize(meet.as_str())

            elif extension in audio_extensions:

                if extension == 'mp3':
                    Path('summarizer/data/wav/').mkdir(exist_ok=True, parents=True)
                    wav_file_path = 'summarizer/data/wav/' + os.path.splitext(f)[0] + '.wav'
                    mp3_to_wav(file_location, wav_file_path)
                
                elif extension == 'wav':
                    wav_file_path = file_location
                
                # print(asr.recognize(wav_file_path))
                summary = summarizer.summarize(asr.recognize(wav_file_path)[0])

            elif extension in video_extensions:
                Path('summarizer/data/wav/').mkdir(exist_ok=True, parents=True)
                wav_file_path = 'summarizer/data/wav/' + os.path.splitext(f)[0] + '.wav'
                video_to_audio(file_location, wav_file_path)
                summary = summarizer.summarize(asr.recognize(wav_file_path)[0])

            return render(request, 'index.html', {'summary': summary})

        else:
            data = f'File Extension not supported please uploat from {suported_extensions}'
            return render(request, 'index.html', {'summary': data})
    
    else: 
        return render(request, 'index.html')
