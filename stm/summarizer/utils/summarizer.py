from transformers import pipeline

def summarizer(article:str, max_length:int = 130, min_length:int = 30) -> str:
    '''
    Function for summarizing an article

    :param article: article to be summarized
    :param max_length: maximum length of the summary
    :param min_length: minimum length of the summary  
    :return: summary text
    '''
    summarizer = pipeline("summarization") # use model="facebook/bart-large-cnn"
    return summarizer(article, max_length=max_length, min_length=min_length, do_sample=False)