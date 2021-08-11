class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
hello = SpecialString("Hello world!")
spam = SpecialString("spam")

print(hello/spam)
