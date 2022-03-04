class Evaluator:
    @classmethod
    def check_value_input(cls, words, coefs):
        v_words = [f for f in words if type(f) is str]
        v_coefs = [f for f in coefs if type(f) in [int, float]]
        if len(v_coefs) != len(coefs) or len(v_words) != len(words):
            return False
        return True

    @classmethod
    def zip_evaluate(cls, words, coefs):
        total = 0
        if len(words) != len(coefs) or not words and not coefs or not \
                Evaluator.check_value_input(words, coefs):
            return -1
        for word, coef in zip(words, coefs):
            total += len(word) * coef
        return total

    @classmethod
    def enumerate_evaluate(cls, words, coefs):
        total = 0
        if len(words) != len(coefs):
            return -1
        for i, word in enumerate(words):
            total += len(word) * coefs[i]
        return total
