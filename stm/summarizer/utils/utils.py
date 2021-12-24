from pydub import AudioSegment
from moviepy.editor import VideoFileClip

def format_time(length: int) -> tuple:
    '''
    Converts time in seconds to (hours, mins and seconds)

    :param length (int): time in seconds
    :return (tuple): time in (hours, mins, seconds) format
    '''
    
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return hours, mins, seconds

def get_meeting_length_from_audio(audio_path: str) -> tuple:
    '''
    Finds the duration of an audio file (.mp3 or .wav)

    :param audio_path (str): path to the .mp3 or .wav file
    :return (tuple): length of audio file in (hours, mins, seconds) format
    '''

    audio = AudioSegment.from_file(audio_path)
    length = int(audio.duration_seconds)
    
    return format_time(length)

def get_meeting_length_from_text(text: str) -> tuple:
    '''
    Estimates the length of the meeting from the transcript text.

    :param text (str): text from transcript
    :return (tuple): estimated duration of the meeting in (hours, mins, seconds) format
    '''

    num_words = len(text.split())

    # Average person speaks at a speed of 100 to 130 words per minute
    # taking an average as 115 words per minute
    length = (num_words / 115) * 60 # length in seconds
    return format_time(length)


def video_to_audio(video_path: str, audio_path: str) -> None:
    '''
    Extracts audio from a video file. Converts mp4 file to wav file.
    Though the code can work for different video and audio file formats,
    it is suggested to use .wav audio format, other formats may cause unexpected results.

    :param video_path: path to the video file that is to be used
    :param audio_path: path to the audio file that is to be saved
    :return: None
    '''
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
