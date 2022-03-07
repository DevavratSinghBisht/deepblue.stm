from transformers import pipeline

class Summarizer:

    def __init__(self) -> None:
        self.summarizer = pipeline("summarization")

    def summarize(self, article:str, max_length:float = 0.70, min_length:float = 0.30) -> str:
        '''
        Function for summarizing an article
        :param article: article to be summarized
        :param max_length: maximum percentage of length of the summary
        :param min_length: minimum percentage of length of the summary  
        :return: summary text
        '''
        article_list = article.split(' ')
        summary = ''
        for i in range(0, len(article_list), 512):
            a_list = article_list[i:i+512]
            a = ' '.join(a_list)
            s = self.summarizer(a, max_length=int(len(a_list)*max_length), min_length=int(len(a_list)*min_length), do_sample=False)
            summary += s[0]['summary_text']
        return summary
