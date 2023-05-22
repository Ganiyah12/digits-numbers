#!/usr/bin/env python
# coding: utf-8

# In[14]:



def letters_digits(sentence):
    digit = 0
    alpha = 0
    for character in sentence:
        if character.isdigit():
            digit += 1
        elif character.isalpha():
            alpha+=1

        else:
            pass

    print(f'LETTERS {alpha}')
    print(f'DIGITS {digit}')


# In[15]:


letters_digits('hello world! 123')


# In[ ]:




