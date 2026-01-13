
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# path = 'C:/Windows/Fonts/malgun.ttf'

# if platform.system() == "Darwin":
#     print("MAC")
# elif platform.system() == "Windows":    
#     font_name = font_manager.FontProperties(fname=path).get_name()
#     print('한글 굿')
#     rc('font', family=font_name)
# else:
#     print("sorry")
    
# plt.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
 
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
