import pandas as pd

class Keyword_finding:
    def __init__(self, file):
        '''

        :param
        file: 분석을 원하는 파일을 입력한다.
        '''
        self.sentences = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line != '\n':
                    if line[-1] == '\n':
                        self.sentences.append(line[:-1])
                    else:
                        self.sentences.append(line)

        self.result = None

    def find_keyword(self, *args):
        '''

        :param
        args: 원하는 키워드를 문자열형태로 입력한다. 입력가능한 키워드 수에는 제한이 없다.
        :return: 해당 키워드가 포함된 문장과 해당 키워드가 등장하는 순서대로 담고있는 문자열을 리스트 형태로 갖는다.
        '''
        target_word_lst = args

        result = []
        for sentence in self.sentences:
            len_sentence = len(sentence)
            appear_word = []
            for i in range(len_sentence):
                for target_word in target_word_lst:
                    len_target_word = len(target_word)
                    if i + len_target_word >= len_sentence:
                        continue
                    if sentence[i:i + len_target_word] == target_word:
                        appear_word.append(target_word)

            if len(appear_word) != 0:
                result.append([sentence, ','.join(appear_word)])

        self.result = result
        return result


    def save_to_csv(self, file):
        '''

        :param
        file: 저장할 파일명을 입력한다.
        '''
        result_df = pd.DataFrame(self.result)
        result_df.to_csv(file, header=False, index=False)


