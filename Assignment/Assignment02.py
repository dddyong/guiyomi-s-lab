#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# # 1. 함수 정의
# $y=f(x)=x^3$

# # 2. 도메인 정의
# - $(-10,10): -10<=x<=10$
# - $-∞<y<∞$

# In[37]:


x = [a for a in range(-10,10)] # x의 범위


# In[41]:


y = [b*b*b for b in range(-10,10)] # 함수에 x의 범위 지정


# ### 3. 함수 그리기

# In[39]:


plt.plot(x,y)


# # 4. 도메인 내의 점 선택
# - $(2,8)$
# - scatter를 이용하여 그래프 위에 점을 찍을 수 있음

# # 5. 선택한 점 표시

# In[43]:


plt.plot(x,y) # 3번
plt.scatter(2,8) # 4번, 5번


# # 6. (2,8)에서의 1차 테일러 근사 
# - $y'=3x^2$
# - $D=f'(2)(x-2)+8=12(x-2)+8=12x-16$

# # 7. 원래 함수에 테일러 근사 그리기

# In[45]:


plt.plot(x,y)
d = [12*b-16 for b in range(-10,10)]
plt.plot(x,d)
plt.scatter(2,8)


# In[ ]:




