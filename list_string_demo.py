# _*_coding:utf-8_*_
if __name__ == "__main__":
    sentence = input("Please input sentence:")
    screen_width = 80
    text_width = len(sentence)
    box_width =  text_width
    left_margin = (screen_width - box_width) // 2

    print()
    print('' * left_margin + '+' + '-' * (box_width) + '+')
    print('' * left_margin + '|' + ' ' * text_width      + '|')
    print('' * left_margin + '|' + sentence              + '|')
    print('' * left_margin + '|' + ' ' * text_width      + '|')
    print('' * left_margin + '+' + '-' * (box_width) + '+')
    print()
